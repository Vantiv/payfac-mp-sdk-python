from __future__ import absolute_import, print_function, unicode_literals

from payfacsdk import communication

SERVICE_ROUTE1 = "/legalentity/"

SERVICE_ROUTE2 = "/principal"

"""
/////////////////////////////////////////////////////
            principal APIs:
/////////////////////////////////////////////////////
"""


def post_by_legalEntity(legalEntityId, request):
    url_suffix = SERVICE_ROUTE1 + legalEntityId + SERVICE_ROUTE2
    return communication.http_post_request(url_suffix, request, "principalCreateResponse")


def delete_by_legalEntityId(legalEntityId, principalId):
    url_suffix = SERVICE_ROUTE1 + legalEntityId + SERVICE_ROUTE2 + "/" + principalId
    return communication.http_delete_request(url_suffix, "principalDeleteResponse")
