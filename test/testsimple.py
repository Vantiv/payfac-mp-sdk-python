from payfacsdk import communication
import unittest


def test_get_retrieval_request():
        suffix = '/legalentity/1000293'
        communication.http_get_retrieval_request(suffix)

test_get_retrieval_request()