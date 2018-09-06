from __future__ import absolute_import, print_function, unicode_literals

from payfacsdk import communication

SERVICE_ROUTE1 = "/legalentity/"

SERVICE_ROUTE2 = "/submerchant"
"""
/////////////////////////////////////////////////////
            subMerchantRetrievalResponse APIs:
/////////////////////////////////////////////////////
"""


def get_by_subMerchantId(legalEntityId, subMerchantId):
    url_suffix = SERVICE_ROUTE1  + legalEntityId + SERVICE_ROUTE2 +"/"+ subMerchantId
    return communication.http_get_retrieval_request(url_suffix, "subMerchantRetrievalResponse", config)