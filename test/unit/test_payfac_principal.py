import unittest
import mock
from collections import OrderedDict
from payfacsdk import payfac_principal


class TestPrincipal(unittest.TestCase):

    @mock.patch('payfacsdk.communication.http_delete_request')
    def test_delete_by_legalEntityId(self, mock_http_delete_request):
        mock_http_delete_request.return_value = \
            OrderedDict([(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'),
                         (u'transactionId', u'6192205869'),
                         (u'legalEntityId', u'2018'),
                         (u'principalId', u'9'),
                         (u'responseDescription', u'Legal Entity Principal successfully deleted')])
        response = payfac_principal.delete_by_legalEntityId("2018", "9")
        expected_url_suffix = "/legalentity/2018/principal/9"
        mock_http_delete_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertEquals("2018", response["legalEntityId"])
        self.assertEquals("9", response["principalId"])
        self.assertEquals("Legal Entity Principal successfully deleted", response["responseDescription"])
