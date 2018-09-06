from __future__ import absolute_import, print_function, unicode_literals

from payfacsdk import communication


SERVICE_ROUTE = "/legalentity"

"""
/////////////////////////////////////////////////////
            legalEntity APIs:
/////////////////////////////////////////////////////
"""


def get_by_legalEntityId(legalEntityId):
    url_suffix = SERVICE_ROUTE + "/" + legalEntityId
    return communication.http_get_retrieval_request(url_suffix, "legalEntityRetrievalResponse")


def post_by_legalEntity(request):
    url_suffix = SERVICE_ROUTE
    return communication.http_post_request(url_suffix, request,"legalEntityCreateResponse")

def put_by_legalEntityId(legalEntityId,request):
    url_suffix = SERVICE_ROUTE + "/" + legalEntityId
    return communication.http_put_request(url_suffix, request, "legalEntityResponse")