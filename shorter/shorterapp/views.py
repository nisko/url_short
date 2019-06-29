from rest_framework.decorators import api_view
from rest_framework.response import Response
from shorter.shorterapp import dbworker


@api_view()
def hello_world(request):
    if 'longurl' in request.query_params.keys():
        longurl = request.query_params['longurl']
        short = dbworker.url_handle(longurl)
        dict_res = {'longurl': longurl, 'shorturl': short}
        return Response(dict_res)
    return Response({"Give me longurl"})
