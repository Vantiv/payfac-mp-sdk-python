import unittest
import mock
from collections import OrderedDict
from payfacMPSdk import payfac_legalEntity


class TestLegalEntity(unittest.TestCase):

    @mock.patch('payfacMPSdk.communication.http_get_retrieval_request')
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

    @mock.patch('payfacMPSdk.communication.http_put_request')
    def test_put_by_legalEntityId(self, mock_http_put_request):
        legalEntityPutRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><legalEntityUpdateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><address><streetAddress1>LE Street Address 1</streetAddress1><streetAddress2>LE Street Address 2</streetAddress2><city>LE City</city><stateProvince>MA</stateProvince><postalCode>01730</postalCode><countryCode>USA</countryCode></address><contactPhone>9785550101</contactPhone><doingBusinessAs>Other Name Co.</doingBusinessAs><annualCreditCardSalesVolume>10000000</annualCreditCardSalesVolume><hasAcceptedCreditCards>true</hasAcceptedCreditCards><principal><principalId>9</principalId><title>CEO</title><emailAddress>jdoe@mail.net</emailAddress><contactPhone>9785551234</contactPhone><address><streetAddress1>p street address 1</streetAddress1><streetAddress2>p street address 2</streetAddress2><city>Boston</city><stateProvince>MA</stateProvince><postalCode>01890</postalCode><countryCode>USA</countryCode></address><backgroundCheckFields><firstName>p first</firstName><lastName>p last</lastName><ssn>123459876</ssn><dateOfBirth>1980-10-12</dateOfBirth><driversLicense>892327409832</driversLicense><driversLicenseState>MA</driversLicenseState></backgroundCheckFields></principal><backgroundCheckFields><legalEntityName>Company Name</legalEntityName><legalEntityType>INDIVIDUAL_SOLE_PROPRIETORSHIP</legalEntityType><taxId>123456789</taxId></backgroundCheckFields><legalEntityOwnershipType>PUBLIC</legalEntityOwnershipType><yearsInBusiness>10</yearsInBusiness></legalEntityUpdateRequest>'

        mock_http_put_request.return_value = \
            OrderedDict(
                [(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'), (u'transactionId', u'3885139362'),
                 (u'legalEntityId', u'1000293'), (u'responseCode', u'10'), (u'responseDescription', u'Approved')])

        response = payfac_legalEntity.put_by_legalEntityId("1000293", legalEntityPutRequest)
        expected_url_suffix = "/legalentity/1000293"
        mock_http_put_request.assert_called_with(expected_url_suffix, legalEntityPutRequest, mock.ANY)
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertEquals("3885139362", response["transactionId"])
        self.assertEquals("10", response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])

    @mock.patch('payfacMPSdk.communication.http_post_request')
    def test_post_by_legalEntity(self, mock_http_post_request):
        legalEntityPostRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><legalEntityCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><legalEntityName>Legal Entity Name</legalEntityName><legalEntityType>CORPORATION</legalEntityType><legalEntityOwnershipType>PUBLIC</legalEntityOwnershipType><doingBusinessAs>Alternate Business Name</doingBusinessAs><taxId>123456789</taxId><contactPhone>7817659800</contactPhone><annualCreditCardSalesVolume>80000000</annualCreditCardSalesVolume><hasAcceptedCreditCards>true</hasAcceptedCreditCards><address><streetAddress1>Street Address 1</streetAddress1><streetAddress2>Street Address 2</streetAddress2><city>City</city><stateProvince>MA</stateProvince><postalCode>01730</postalCode><countryCode>USA</countryCode></address><principal><title>Chief Financial Officer</title><firstName>p first</firstName><lastName>p last</lastName><emailAddress>emailAddress</emailAddress><ssn>123459876</ssn><contactPhone>7817659800</contactPhone><dateOfBirth>1980-10-12</dateOfBirth><driversLicense>892327409832</driversLicense><driversLicenseState>MA</driversLicenseState><address><streetAddress1>p street address 1</streetAddress1><streetAddress2>p street address 2</streetAddress2><city>Boston</city><stateProvince>MA</stateProvince><postalCode>01890</postalCode><countryCode>USA</countryCode></address><stakePercent>33</stakePercent></principal><yearsInBusiness>12</yearsInBusiness></legalEntityCreateRequest>'

        mock_http_post_request.return_value = \
            OrderedDict([(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'),
                         (u'transactionId', u'7631456377'), (u'legalEntityId', u'41183'),
                         (u'responseCode', u'10'), (u'responseDescription', u'Approved'),
                         (u'backgroundCheckResults',
                          OrderedDict([(u'business',
                                        OrderedDict([(u'verificationResult',
                                                      OrderedDict([(u'overallScore',
                                                                    OrderedDict([(u'score', u'40'),
                                                                                 (u'description',
                                                                                  u'Business identity is confirmed at the input address')])),
                                                                   (u'nameAddressTaxIdAssociation',
                                                                    OrderedDict([(u'code', u'NAME_ADDRESS_TAX_ID'),
                                                                                 (u'description',
                                                                                  u'Name, address, and Tax Id verified.')])),
                                                                   (u'nameAddressPhoneAssociation',
                                                                    OrderedDict([(u'code', u'NAME_ADDRESS_PHONE'),
                                                                                 (u'description',
                                                                                  u'Name, address, and phone verified.')])),
                                                                   (u'verificationIndicators',
                                                                    OrderedDict([(u'nameVerified', u'true'),
                                                                                 (u'addressVerified', u'true'),
                                                                                 (u'cityVerified', u'true'),
                                                                                 (u'stateVerified', u'true'),
                                                                                 (u'zipVerified', u'true'),
                                                                                 (u'phoneVerified', u'true'),
                                                                                 (u'taxIdVerified', u'true')])), (
                                                                       u'riskIndicators',
                                                                       OrderedDict([(u'riskIndicator', [
                                                                           OrderedDict(
                                                                               [(u'code', u'PHONE_NUMBER_MOBILE'), (
                                                                                   u'description',
                                                                                   u'The submitted phone number is a mobile number.')]),
                                                                           OrderedDict(
                                                                               [(u'code', u'PHONE_NUMBER_MOBILE'), (
                                                                                   u'description',
                                                                                   u'The submitted phone number is a mobile number.')])])]))]))])),
                                       (u'principal', OrderedDict([(u'verificationResult', OrderedDict([(
                                           u'overallScore',
                                           OrderedDict([(
                                               u'score',
                                               u'50'),
                                               (
                                                   u'description',
                                                   u'Full name, address, phone, and SSN verified.')])),
                                           (
                                               u'nameAddressSsnAssociation',
                                               OrderedDict([(
                                                   u'code',
                                                   u'FIRST_LAST_ADDRESS_SSN'),
                                                   (
                                                       u'description',
                                                       u'First name, last name, address, and SSN verified.')])),
                                           (
                                               u'nameAddressPhoneAssociation',
                                               OrderedDict([(
                                                   u'code',
                                                   u'LAST_ADDRESS_PHONE'),
                                                   (
                                                       u'description',
                                                       u'Last name, address, and phone number verified.')])),
                                           (
                                               u'verificationIndicators',
                                               OrderedDict([(
                                                   u'nameVerified',
                                                   u'true'),
                                                   (
                                                       u'addressVerified',
                                                       u'true'),
                                                   (
                                                       u'phoneVerified',
                                                       u'true'),
                                                   (
                                                       u'ssnVerified',
                                                       u'true'),
                                                   (
                                                       u'dobVerified',
                                                       u'true')])),
                                           (
                                               u'riskIndicators',
                                               OrderedDict([(
                                                   u'riskIndicator',
                                                   [
                                                       OrderedDict(
                                                           [
                                                               (
                                                                   u'code',
                                                                   u'PHONE_NUMBER_MOBILE'),
                                                               (
                                                                   u'description',
                                                                   u'The submitted phone number is a mobile number.')]),
                                                       OrderedDict(
                                                           [
                                                               (
                                                                   u'code',
                                                                   u'PHONE_NUMBER_MOBILE'),
                                                               (
                                                                   u'description',
                                                                   u'The submitted phone number is a mobile number.')])])]))]))])),
                                       (u'businessToPrincipalAssociation', OrderedDict([(u'score', u'20'), (
                                           u'description',
                                           u'Principal\xe2\x80\x99s verified address matches input Business address.')])),
                                       (u'backgroundCheckDecisionNotes', u'TZwNvYvgXPolSx8g5kSx'), (u'bankruptcyData',
                                                                                                    OrderedDict([(
                                                                                                        u'bankruptcyType',
                                                                                                        u'3j1Vs'),
                                                                                                        (
                                                                                                            u'bankruptcyCount',
                                                                                                            u'3'),
                                                                                                        (
                                                                                                            u'companyName',
                                                                                                            u'Company Name'),
                                                                                                        (
                                                                                                            u'streetAddress1',
                                                                                                            u'100 Main Street'),
                                                                                                        (
                                                                                                            u'streetAddress2',
                                                                                                            u'Suite 2'),
                                                                                                        (
                                                                                                            u'city',
                                                                                                            u'Boston'),
                                                                                                        (
                                                                                                            u'state',
                                                                                                            u'MA'),
                                                                                                        (
                                                                                                            u'zip',
                                                                                                            u'01150'),
                                                                                                        (
                                                                                                            u'zip4',
                                                                                                            u'2202'),
                                                                                                        (
                                                                                                            u'filingDate',
                                                                                                            u'2018-09-10')])),
                                       (u'lienResult', OrderedDict(
                                           [(u'lienType', u'VmXehYQZN4pMesb'), (u'releasedCount', u'6'),
                                            (u'unreleasedCount', u'6'), (u'companyName', u'Company Name'),
                                            (u'streetAddress1', u'100 Main Street'), (u'streetAddress2', u'Suite 2'),
                                            (u'city', u'Boston'), (u'state', u'MA'), (u'zip', u'01150'),
                                            (u'zip4', u'2202'), (u'filingDate', u'2018-09-10')]))])), (u'principal',
                                                                                                       OrderedDict([(
                                                                                                           u'principalId',
                                                                                                           u'74832'),
                                                                                                           (
                                                                                                               u'firstName',
                                                                                                               u'p_first'),
                                                                                                           (
                                                                                                               u'lastName',
                                                                                                               u'p_last')]))])

        response = payfac_legalEntity.post_by_legalEntity(legalEntityPostRequest)
        expected_url_suffix = "/legalentity"
        mock_http_post_request.assert_called_with(expected_url_suffix, legalEntityPostRequest, mock.ANY)
        self.assertEquals("41183", response["legalEntityId"])
        self.assertEquals("7631456377", response["transactionId"])
        self.assertEquals("10", response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])
