#
# import unittest
# import mock
# from collections import OrderedDict
# from payfacsdk import communication
# from requests.auth import HTTPBasicAuth
# import requests
#
# class TestCommunication(unittest.TestCase):
#     PAYFAC_CONTENT_TYPE = "application/com.vantivcnp.payfac-v13+xml"
#
#     PAYFAC_API_HEADERS = {"Accept": PAYFAC_CONTENT_TYPE,
#                           "Content-Type": PAYFAC_CONTENT_TYPE}
#
#     @mock.patch(['payfacsdk.utils.generate_response','requests.get'])
#     def test_http_get_retrieval_request(self, mock1, mock2):
#         expect_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><approvedMccResponse xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><transactionId>9901030109</transactionId><approvedMccs><approvedMcc>5967</approvedMcc><approvedMcc>5970</approvedMcc></approvedMccs></approvedMccResponse>'
#         mock1.return_value = expect_response
#         mock2.return_value = OrderedDict([(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'),
#                          (u'transactionId', u'6192205869'),
#                          (u'approvedMccs', OrderedDict([(u'approvedMcc', ['5967', '5970'])]))])
#
#         expected_url_suffix = "/mcc"
#
#         mock2.assert_called_with(expected_url_suffix, mock.ANY)
#         response = communication.http_get_retrieval_request("1000293","legalEntityRetrievalResponse")
#         expected_url_suffix = "/legalentity/1000293"
#         mock_http_get_retrieval_request[0].assert_called_with(expected_url_suffix, mock.ANY)
#         self.assertEquals("1000293", response["legalEntityId"])
#         self.assertEquals("6192205869", response["transactionId"])