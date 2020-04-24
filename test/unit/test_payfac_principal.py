import unittest
import mock
from collections import OrderedDict
from payfacMPSdk import payfac_principal,generatedClass
from dateutil.parser import parse

class TestPrincipal(unittest.TestCase):

    @mock.patch('payfacMPSdk.communication.http_delete_request')
    def test_delete_by_legalEntityId(self, mock_http_delete_request):
        mock_http_delete_request.return_value = \
            OrderedDict([(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'),
                         (u'transactionId', u'6192205869'),
                         (u'legalEntityId', u'2018'),
                         (u'principalId', u'9'),
                         (u'responseDescription', u'Legal Entity Principal successfully deleted')])
        response = payfac_principal.delete_by_legalEntityId("2018", "9")
        expected_url_suffix = "/legalentity/2018/principal/9"
        mock_http_delete_request.assert_called_with(expected_url_suffix)
        self.assertEquals("2018", response["legalEntityId"])
        self.assertEquals("9", response["principalId"])
        self.assertEquals("Legal Entity Principal successfully deleted", response["responseDescription"])


    @mock.patch('payfacMPSdk.communication.http_post_request')
    def test_post_by_legalEntity(self,mock_request):
        legalEntityPrincipalCreateRequest = generatedClass.legalEntityPrincipalCreateRequest.factory()
        principal = generatedClass.legalEntityPrincipal.factory()
        principal.set_title("Mr.")
        principal.set_firstName("First")
        principal.set_lastName("Last")
        principal.set_emailAddress("abc@gamil.com")
        principal.set_ssn("123450015")
        principal.set_dateOfBirth(parse("1980-10-12T12:00:00-06:00"))
        address = generatedClass.principalAddress.factory()
        address.set_streetAddress1("p2 street address 1")
        address.set_streetAddress2("p2 street address 2")
        address.set_city("Boston2")
        address.set_stateProvince("MA")
        address.set_postalCode("01892")
        address.set_countryCode("USA")
        principal.set_address(address)
        principal.set_stakePercent(31)
        legalEntityPrincipalCreateRequest.set_principal(principal)

        expected_request = u'<legalEntityPrincipalCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><principal><title>Mr.</title><firstName>First</firstName><lastName>Last</lastName><emailAddress>abc@gamil.com</emailAddress><ssn>123450015</ssn><dateOfBirth>1980-10-12-06:00</dateOfBirth><address><streetAddress1>p2 street address 1</streetAddress1><streetAddress2>p2 street address 2</streetAddress2><city>Boston2</city><stateProvince>MA</stateProvince><postalCode>01892</postalCode><countryCode>USA</countryCode></address><stakePercent>31</stakePercent></principal><sdkVersion>13.1.0</sdkVersion><language>python</language></legalEntityPrincipalCreateRequest>'

        mock_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'),
             (u'legalEntityId', u'2018'),
             (u'principal', OrderedDict(
                    [(u'principalId', u'6'), (u'firstName', u'First'), (u'lastName', u'Last'), (u'responseCode', u'10'),
                     (u'responseDescription', u'Approved')])), (u'transactionId', u'8944566037')])

        response = payfac_principal.post_by_legalEntity("2018",legalEntityPrincipalCreateRequest)
        expected_url_suffix = '/legalentity/2018/principal'.encode('utf-8')
        mock_request.assert_called_with(expected_url_suffix, expected_request)
        self.assertEquals("2018",response['legalEntityId'])
        self.assertEquals("6",response["principal"]["principalId"])
        self.assertEquals("10",response['principal']['responseCode'])
        self.assertEquals("Approved", response['principal']['responseDescription'])

