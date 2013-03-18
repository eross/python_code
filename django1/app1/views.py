from django.shortcuts import render_to_response
from app1.forms import WorkForm
from django.http import HttpResponseRedirect
from subprocess import Popen
from django.http import HttpResponse
import urlparse
from StringIO import StringIO
import xmlrpclib


from django1 import rpc_handler

workers={}
# rpc funcs
def multiply(a, b):
    """
    Multiplication is fun!
    Takes two arguments, which are multiplied together.
    Returns the result of the multiplication!
    """
    return a*b

def register(name, addr):
    """
    Used by workers to register their address
    """
    global workers
    workers[name]=addr
    return True


rpc = rpc_handler.RpcHandler()

# you have to manually register all functions that are xml-rpc-able with the dispatcher
# the dispatcher then maps the args down.
# The first argument is the actual method, the second is what to call it from the XML-RPC side...

print rpc.dispatcher()
rpc.dispatcher().register_function(multiply, 'multiply')
rpc.dispatcher().register_function(register, 'register')
rpc.dispatcher().register_introspection_functions()


def work(request):
    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print "Do something with "+cd['worker']
            u = urlparse.urlparse(request.build_absolute_uri())
            pid = Popen(["python","worker/worker.py",cd['worker'],u.scheme+"://"+u.netloc+"/rpc/"]).pid

            return HttpResponseRedirect('/work/')
    else:
        form = WorkForm()
    return render_to_response('work.html',{'form': form})

def callback(request):
    print "called back "
    if request.method == "POST":
        return HttpResponse(request.POST['foo'])
    else:
        return HttpResponse('GET not supported.')


def rpc_handler(request):
    response = rpc.rpc_handler(request)
    return response


def listWorkers(request):
    s = StringIO()
    s.write("<br>Workers currently running:  \n")
    s.write("<table>\n")
    for name, address in workers.items():
        s.write('<tr><td>'+name+'</td><td>'+str(address)+'</td></tr>\n')
    s.write('</table>\n')
    contents = s.getvalue()
    s.close()
    return HttpResponse(contents)

def shutdown(request):
    s = StringIO()
    s.write('<br>Shutting down:</br>')
    for name, url in workers.items():
        s.write('<br>'+name+'</br>')
        # TBD:  exception handling for rpc
        rpc_srv = xmlrpclib.ServerProxy(url)
        rpc_srv.shutdown()
    content = s.getvalue()
    s.close()
    return HttpResponse(content)

def login_status(request):
    if request.user.is_authenticated():
        return HttpResponse('<p> You are authenticated as %s </p>' % request.user.username)
    else:
        return HttpResponse("<p> I don't know you </p>")