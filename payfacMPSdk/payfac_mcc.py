from __future__ import absolute_import, print_function, unicode_literals

from payfacMPSdk import communication

SERVICE_ROUTE = "/mcc"

"""
/////////////////////////////////////////////////////
            mcc APIs:
/////////////////////////////////////////////////////
"""


def get_mcc():
    return communication.http_get_retrieval_request(SERVICE_ROUTE)