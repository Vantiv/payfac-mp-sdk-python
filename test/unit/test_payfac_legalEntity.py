import unittest
import mock
from collections import OrderedDict
from payfacsdk import payfac_legalEntity


class TestLegalEntity(unittest.TestCase):

    @mock.patch('payfacsdk.communication.http_get_retrieval_request')
    def test_get_by_legalEntityId(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.return_value = \
            OrderedDict([(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'),
                         (u'legalEntityId', u'1000293'),
                         (u'transactionId', u'6192205869'),
                         (u'agreements', OrderedDict([(u'legalEntityAgreement', OrderedDict(
                             [(u'legalEntityAgreementType', u'MERCHANT_AGREEMENT'),
                              (u'agreementVersion', u'agreementVersion1'),
                              (u'userFullName', u'userFullName1'),
                              (u'userSystemName', u'userSystemName1'),
                              (u'userIPAddress', u'196.198.100.100'),
                              (u'manuallyEntered', u'false'),
                              (u'acceptanceDateTime', u'2017-06-11T13:00:00-05:00')]))]))])
        response = payfac_legalEntity.get_by_legalEntityId("1000293")
        expected_url_suffix = "/legalentity/1000293"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertEquals("6192205869", response["transactionId"])

