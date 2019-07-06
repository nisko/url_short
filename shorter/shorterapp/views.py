from rest_framework.decorators import api_view
from rest_framework.response import Response
from shorter.shorterapp import dbworker


@api_view()
def get_short(request):
    if 'longurl' in request.query_params.keys():
        longurl = request.query_params['longurl']
        shorturl = dbworker.get_short(longurl)
        dict_res = {'longurl': longurl, 'shorturl': shorturl}
        return Response(dict_res)
    return Response({"Give me longurl"})


@api_view()
def get_long(request):
    if 'shorturl' in request.query_params.keys():
        shorturl = request.query_params['shorturl']
        longurl = dbworker.get_long(shorturl)
        dict_res = {'longurl': longurl, 'shorturl': shorturl}
        return Response(dict_res)
    return Response({"Give me shorturl"})
