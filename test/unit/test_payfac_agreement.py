import unittest
import mock
from collections import OrderedDict
from payfacMPSdk import payfac_agreement


class TestAgreement(unittest.TestCase):

    @mock.patch('payfacMPSdk.communication.http_get_retrieval_request')
    def test_get_by_legalEntityId(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'), (u'legalEntityId', u'1000293'),
             (u'transactionId', u'5163993725'), (u'agreements', OrderedDict([(u'legalEntityAgreement', OrderedDict(
                [(u'legalEntityAgreementType', u'MERCHANT_AGREEMENT'), (u'agreementVersion', u'agreementVersion1'),
                 (u'userFullName', u'userFullName1'), (u'userSystemName', u'userSystemName1'),
                 (u'userIPAddress', u'196.198.100.100'), (u'manuallyEntered', u'false'),
                 (u'acceptanceDateTime', u'2017-06-11T13:00:00-05:00')]))]))])

        response = payfac_agreement.get_by_legalEntityId("1000293")
        expected_url_suffix = "/legalentity/1000293/agreement"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertEquals("5163993725", response["transactionId"])

    @mock.patch('payfacMPSdk.communication.http_post_request')
    def test_post_by_legalEntity(self, mock_http_post_request):
        agreementPostRequest = '<legalEntityAgreementCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><legalEntityAgreement><legalEntityAgreementType>MERCHANT_AGREEMENT</legalEntityAgreementType><agreementVersion>agreementVersion1</agreementVersion><userFullName>userFullName</userFullName><userSystemName>systemUserName</userSystemName><userIPAddress>196.198.100.100</userIPAddress><manuallyEntered>false</manuallyEntered><acceptanceDateTime>2017-02-11T12:00:00-06:00</acceptanceDateTime></legalEntityAgreement></legalEntityAgreementCreateRequest>'
        mock_http_post_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'), (u'transactionId', u'4978173558')])

        response = payfac_agreement.post_by_legalEntityId("21003",agreementPostRequest)
        expected_url_suffix = "/legalentity/21003/agreement"
        mock_http_post_request.assert_called_with(expected_url_suffix,agreementPostRequest,mock.ANY)
        self.assertEquals("4978173558",response['transactionId'])
