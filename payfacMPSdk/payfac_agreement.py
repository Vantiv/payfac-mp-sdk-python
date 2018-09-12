from __future__ import absolute_import, print_function, unicode_literals

from payfacMPSdk import  communication

SERVICE_ROUTE1 = "/legalentity/"

SERVICE_ROUTE2 = "/agreement"
"""
/////////////////////////////////////////////////////
            legalEntityAgreement APIs:
/////////////////////////////////////////////////////
"""


def get_by_legalEntityId(legalEntityId):
    url_suffix = SERVICE_ROUTE1  + legalEntityId + SERVICE_ROUTE2
    return communication.http_get_retrieval_request(url_suffix, "legalEntityAgreementRetrievalResponse")


def post_by_legalEntityId(legalEntityId,request):
    url_suffix = SERVICE_ROUTE1 + legalEntityId + SERVICE_ROUTE2
    return communication.http_post_request(url_suffix, request, "legalEntityAgreementCreateResponse")