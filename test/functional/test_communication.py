
import unittest
from payfacMPSdk import communication, utils

class TestCommunication(unittest.TestCase):

    def test_http_get_retrieval_request(self):
        response = communication.http_get_retrieval_request("/legalentity/1000293")
        self.assertIsNotNone(response["transactionId"])
        self.assertEquals("1000293",response["legalEntityId"])

    def test_http_get_retrieval_request_with_PayfacError(self):
        new_conf = utils.Configuration()
        new_conf.__setattr__("url","https://")
        self.assertRaises(utils.PayfacError, communication.http_get_retrieval_request, "/legalentity/1000293",new_conf)

    def test_http_post_request(self):
        agreementPostRequest = '<legalEntityAgreementCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><legalEntityAgreement><legalEntityAgreementType>MERCHANT_AGREEMENT</legalEntityAgreementType><agreementVersion>agreementVersion1</agreementVersion><userFullName>userFullName</userFullName><userSystemName>systemUserName</userSystemName><userIPAddress>196.198.100.100</userIPAddress><manuallyEntered>false</manuallyEntered><acceptanceDateTime>2017-02-11T12:00:00-06:00</acceptanceDateTime></legalEntityAgreement></legalEntityAgreementCreateRequest>'
        response = communication.http_post_request("/legalentity/21003/agreement",agreementPostRequest)
        self.assertIsNotNone(response["transactionId"])

    def test_http_post_request_with_PayfacError(self):
        agreementPostRequest = '<legalEntityAgreementCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><legalEntityAgreement><legalEntityAgreementType>MERCHANT_AGREEMENT</legalEntityAgreementType><agreementVersion>agreementVersion1</agreementVersion><userFullName>userFullName</userFullName><userSystemName>systemUserName</userSystemName><userIPAddress>196.198.100.100</userIPAddress><manuallyEntered>false</manuallyEntered><acceptanceDateTime>2017-02-11T12:00:00-06:00</acceptanceDateTime></legalEntityAgreement></legalEntityAgreementCreateRequest>'
        new_conf = utils.Configuration()
        new_conf.__setattr__("url","https://")
        self.assertRaises(utils.PayfacError, communication.http_post_request, "/legalentity/21003/agreement", agreementPostRequest,new_conf)

    def test_http_put_request(self):
        legalEntityPutRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><legalEntityUpdateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><address><streetAddress1>LE Street Address 1</streetAddress1><streetAddress2>LE Street Address 2</streetAddress2><city>LE City</city><stateProvince>MA</stateProvince><postalCode>01730</postalCode><countryCode>USA</countryCode></address><contactPhone>9785550101</contactPhone><doingBusinessAs>Other Name Co.</doingBusinessAs><annualCreditCardSalesVolume>10000000</annualCreditCardSalesVolume><hasAcceptedCreditCards>true</hasAcceptedCreditCards><principal><principalId>9</principalId><title>CEO</title><emailAddress>jdoe@mail.net</emailAddress><contactPhone>9785551234</contactPhone><address><streetAddress1>p street address 1</streetAddress1><streetAddress2>p street address 2</streetAddress2><city>Boston</city><stateProvince>MA</stateProvince><postalCode>01890</postalCode><countryCode>USA</countryCode></address><backgroundCheckFields><firstName>p first</firstName><lastName>p last</lastName><ssn>123459876</ssn><dateOfBirth>1980-10-12</dateOfBirth><driversLicense>892327409832</driversLicense><driversLicenseState>MA</driversLicenseState></backgroundCheckFields></principal><backgroundCheckFields><legalEntityName>Company Name</legalEntityName><legalEntityType>INDIVIDUAL_SOLE_PROPRIETORSHIP</legalEntityType><taxId>123456789</taxId></backgroundCheckFields><legalEntityOwnershipType>PUBLIC</legalEntityOwnershipType><yearsInBusiness>10</yearsInBusiness></legalEntityUpdateRequest>'
        response = communication.http_put_request("/legalentity/1000293",legalEntityPutRequest)
        self.assertIsNotNone(response["transactionId"])
        self.assertEquals("1000293",response["legalEntityId"])
        self.assertEquals(10,response["responseCode"])
        self.assertEquals("Approved",response["responseDescription"])

    def test_http_put_request_with_PayfacError(self):
        legalEntityPutRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><legalEntityUpdateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><address><streetAddress1>LE Street Address 1</streetAddress1><streetAddress2>LE Street Address 2</streetAddress2><city>LE City</city><stateProvince>MA</stateProvince><postalCode>01730</postalCode><countryCode>USA</countryCode></address><contactPhone>9785550101</contactPhone><doingBusinessAs>Other Name Co.</doingBusinessAs><annualCreditCardSalesVolume>10000000</annualCreditCardSalesVolume><hasAcceptedCreditCards>true</hasAcceptedCreditCards><principal><principalId>9</principalId><title>CEO</title><emailAddress>jdoe@mail.net</emailAddress><contactPhone>9785551234</contactPhone><address><streetAddress1>p street address 1</streetAddress1><streetAddress2>p street address 2</streetAddress2><city>Boston</city><stateProvince>MA</stateProvince><postalCode>01890</postalCode><countryCode>USA</countryCode></address><backgroundCheckFields><firstName>p first</firstName><lastName>p last</lastName><ssn>123459876</ssn><dateOfBirth>1980-10-12</dateOfBirth><driversLicense>892327409832</driversLicense><driversLicenseState>MA</driversLicenseState></backgroundCheckFields></principal><backgroundCheckFields><legalEntityName>Company Name</legalEntityName><legalEntityType>INDIVIDUAL_SOLE_PROPRIETORSHIP</legalEntityType><taxId>123456789</taxId></backgroundCheckFields><legalEntityOwnershipType>PUBLIC</legalEntityOwnershipType><yearsInBusiness>10</yearsInBusiness></legalEntityUpdateRequest>'
        new_conf = utils.Configuration()
        new_conf.__setattr__("url","https://")
        self.assertRaises(utils.PayfacError, communication.http_put_request, "/legalentity/1000293", legalEntityPutRequest,new_conf)

    def test_http_delete_request(self):
        response = communication.http_delete_request("/legalentity/2018/principal/9")
        self.assertIsNotNone(response["transactionId"])
        self.assertEquals("2018",response["legalEntityId"])
        self.assertEquals(9,response["principalId"])
        self.assertEquals("Legal Entity Principal successfully deleted",response["responseDescription"])

    def test_http_delete_request_with_PayfacError(self):
        new_conf = utils.Configuration()
        new_conf.__setattr__("url", "https://")
        self.assertRaises(utils.PayfacError, communication.http_delete_request, "/legalentity/2018/principal/9", new_conf)

    def test_validate_response_with_PayfacWebError(self):
        self.assertRaises(utils.PayfacWebError, communication.http_get_retrieval_request, "/legalentity")

    def test_validate_response_with_PayfacWebError_generateErrorResponse(self):
        self.assertRaises(utils.PayfacWebError, communication.http_get_retrieval_request, "/legalentity/10002930000000000000000000000000000")


    def test_validate_response_with_PayfacError(self):
        self.assertRaises(utils.PayfacError, communication.validate_response, None)

