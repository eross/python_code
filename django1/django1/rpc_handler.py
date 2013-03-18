from django.http import HttpResponse
from SimpleXMLRPCServer import SimpleXMLRPCDispatcher


class RpcHandler:
    def __init__(self):
        self.__dispatcher = SimpleXMLRPCDispatcher(allow_none=False, encoding=None)


    def dispatcher(self):
        return self.__dispatcher

    def rpc_handler(self,request):
        """
        the actual handler:
        if you setup your urls.py properly, all calls to the xml-rpc service
        should be routed through here.
        If post data is defined, it assumes it's XML-RPC and tries to process as such
        Empty post assumes you're viewing from a browser and tells you about the service.
        """

        if len(request.POST):
            response = HttpResponse(mimetype="application/xml")
            response.write(self.__dispatcher._marshaled_dispatch(request.raw_post_data))
        else:
            response = HttpResponse()
            response.write("<b>This is an XML-RPC Service.</b><br>")
            response.write("You need to invoke it using an XML-RPC Client!<br>")
            response.write("The following methods are available:<ul>")
            methods = self.__dispatcher.system_listMethods()

            for method in methods:
                # right now, my version of SimpleXMLRPCDispatcher always
                # returns "signatures not supported"... :(
                # but, in an ideal world it will tell users what args are expected
                sig = self.__dispatcher.system_methodSignature(method)

                # this just reads your docblock, so fill it in!
                help =  self.__dispatcher.system_methodHelp(method)

                response.write("<li><b>%s</b>: [%s] %s" % (method, sig, help))

            response.write("</ul>")

        #        response['Content-length'] = str(len(response.content))
        return response
