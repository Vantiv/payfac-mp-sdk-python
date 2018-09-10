import unittest
import mock
from collections import OrderedDict
from payfacsdk import payfac_mcc


class TestMCC(unittest.TestCase):

    @mock.patch('payfacsdk.communication.http_get_retrieval_request')
    def test_get_mcc(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.return_value = \
            OrderedDict([(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'),
                         (u'transactionId', u'6192205869'),
                         (u'approvedMccs', OrderedDict([(u'approvedMcc', ['5967', '5970'])]))])
        response = payfac_mcc.get_mcc()
        expected_url_suffix = "/mcc"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertEquals("5967", response["approvedMccs"]["approvedMcc"][0])
        self.assertEquals("5970", response["approvedMccs"]["approvedMcc"][1])