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



    @mock.patch('payfacsdk.communication.http_put_request')
    def test_put_by_legalEntityId(self, mock_http_get_retrieval_request):
        legalEntityPutRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><legalEntityUpdateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><address><streetAddress1>LE Street Address 1</streetAddress1><streetAddress2>LE Street Address 2</streetAddress2><city>LE City</city><stateProvince>MA</stateProvince><postalCode>01730</postalCode><countryCode>USA</countryCode></address><contactPhone>9785550101</contactPhone><doingBusinessAs>Other Name Co.</doingBusinessAs><annualCreditCardSalesVolume>10000000</annualCreditCardSalesVolume><hasAcceptedCreditCards>true</hasAcceptedCreditCards><principal><principalId>9</principalId><title>CEO</title><emailAddress>jdoe@mail.net</emailAddress><contactPhone>9785551234</contactPhone><address><streetAddress1>p street address 1</streetAddress1><streetAddress2>p street address 2</streetAddress2><city>Boston</city><stateProvince>MA</stateProvince><postalCode>01890</postalCode><countryCode>USA</countryCode></address><backgroundCheckFields><firstName>p first</firstName><lastName>p last</lastName><ssn>123459876</ssn><dateOfBirth>1980-10-12</dateOfBirth><driversLicense>892327409832</driversLicense><driversLicenseState>MA</driversLicenseState></backgroundCheckFields></principal><backgroundCheckFields><legalEntityName>Company Name</legalEntityName><legalEntityType>INDIVIDUAL_SOLE_PROPRIETORSHIP</legalEntityType><taxId>123456789</taxId></backgroundCheckFields><legalEntityOwnershipType>PUBLIC</legalEntityOwnershipType><yearsInBusiness>10</yearsInBusiness></legalEntityUpdateRequest>'

        mock_http_get_retrieval_request.return_value = \
            OrderedDict(
                [(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'), (u'transactionId', u'3885139362'),
                 (u'legalEntityId', u'1000293'), (u'responseCode', u'10'), (u'responseDescription', u'Approved')])

        response = payfac_legalEntity.put_by_legalEntityId("1000293",legalEntityPutRequest)
        expected_url_suffix = "/legalentity/1000293"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, legalEntityPutRequest, mock.ANY)
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertEquals("3885139362", response["transactionId"])
        self.assertEquals("10", response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])


