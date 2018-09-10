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


    @mock.patch('payfacsdk.communication.http_post_request')
    def test_post_by_legalEntity(self,mock_request):
        principalPostRequest = '<legalEntityPrincipalCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><principal><title>Mr.</title><firstName>First</firstName><lastName>Last</lastName><emailAddress>abc@gmail.com</emailAddress><ssn>123450015</ssn><dateOfBirth>1980-10-12</dateOfBirth><address><streetAddress1>p2 street address 1</streetAddress1><streetAddress2>p2 street address 2</streetAddress2><city>Boston2</city><stateProvince>MA</stateProvince><postalCode>01892</postalCode><countryCode>USA</countryCode></address><stakePercent>31</stakePercent></principal></legalEntityPrincipalCreateRequest>'
        mock_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'), (u'legalEntityId', u'2018'), (
            u'principal', OrderedDict(
                [(u'principalId', u'6'), (u'firstName', u'First'), (u'lastName', u'Last'), (u'responseCode', u'10'),
                 (u'responseDescription', u'Approved')])), (u'transactionId', u'8944566037')])

        response = payfac_principal.post_by_legalEntity("2018",principalPostRequest)
        expected_url_suffix = '/legalentity/2018/principal'
        mock_request.assert_called_with(expected_url_suffix,principalPostRequest,mock.ANY)
        self.assertEquals("2018",response['legalEntityId'])
        self.assertEquals("6",response["principal"]["principalId"])
        self.assertEquals("10",response['principal']['responseCode'])
        self.assertEquals("Approved", response['principal']['responseDescription'])

