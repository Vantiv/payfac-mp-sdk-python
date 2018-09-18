import unittest
import mock
from collections import OrderedDict
from payfacMPSdk import payfac_legalEntity,generatedClass
from dateutil.parser import parse

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
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix)
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertEquals("6192205869", response["transactionId"])

    @mock.patch('payfacMPSdk.communication.http_put_request')
    def test_put_by_legalEntityId(self, mock_http_put_request):
        legalEntityUpdateRequest = generatedClass.legalEntityUpdateRequest.factory()
        address = generatedClass.address.factory()
        address.set_streetAddress1("LE Street Address 1")
        address.set_streetAddress2("LE Street Address 2")
        address.set_city("LE City")
        address.set_stateProvince("MA")
        address.set_postalCode("01730")
        address.set_countryCode("USA")

        legalEntityUpdateRequest.set_address(address)
        legalEntityUpdateRequest.set_contactPhone("9785550101")
        legalEntityUpdateRequest.set_doingBusinessAs("Other Name Co.")
        legalEntityUpdateRequest.set_annualCreditCardSalesVolume(10000000)
        legalEntityUpdateRequest.set_hasAcceptedCreditCards("true")

        principal = generatedClass.legalEntityPrincipalUpdatable.factory()
        principal.set_principalId(9)
        principal.set_title("CEO")
        principal.set_emailAddress("jdoe@mail.net")
        principal.set_contactPhone("9785551234")
        principal.set_address(address)

        backgroundCheckField = generatedClass.principalBackgroundCheckFields.factory()
        backgroundCheckField.set_firstName("p first")
        backgroundCheckField.set_lastName("p last")
        backgroundCheckField.set_ssn("123459876")
        backgroundCheckField.set_dateOfBirth(parse("1980-10-12T12:00:00-06:00"))
        backgroundCheckField.set_driversLicense("892327409832")
        backgroundCheckField.set_driversLicenseState("MA")
        principal.set_backgroundCheckFields(backgroundCheckField)

        legalEntityUpdateRequest.set_principal(principal)

        backgroundCheckFields = generatedClass.legalEntityBackgroundCheckFields.factory()
        backgroundCheckFields.set_legalEntityName("Company Name")
        backgroundCheckFields.set_legalEntityType("INDIVIDUAL_SOLE_PROPRIETORSHIP")
        backgroundCheckFields.set_taxId("123456789")
        legalEntityUpdateRequest.set_backgroundCheckFields(backgroundCheckFields)
        legalEntityUpdateRequest.set_legalEntityOwnershipType("PUBLIC")
        legalEntityUpdateRequest.set_yearsInBusiness("10")

        mock_http_put_request.return_value = \
            OrderedDict(
                [(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'), (u'transactionId', u'3885139362'),
                 (u'legalEntityId', u'1000293'), (u'responseCode', u'10'), (u'responseDescription', u'Approved')])

        response = payfac_legalEntity.put_by_legalEntityId("1000293", legalEntityUpdateRequest)
        expected_url_suffix = "/legalentity/1000293"
        mock_http_put_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertEquals("3885139362", response["transactionId"])
        self.assertEquals("10", response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])


    @mock.patch('payfacMPSdk.communication.http_post_request')
    def test_post_by_legalEntity(self, mock_http_post_request):
        legalEntityCreateRequest = generatedClass.legalEntityCreateRequest.factory()

        legalEntityCreateRequest.set_legalEntityName("Legal Entity Name")
        legalEntityCreateRequest.set_legalEntityType("CORPORATION")
        legalEntityCreateRequest.set_legalEntityOwnershipType("PUBLIC")
        legalEntityCreateRequest.set_doingBusinessAs("Alternate Business Name")
        legalEntityCreateRequest.set_taxId("123456789")
        legalEntityCreateRequest.set_contactPhone("7817659800")
        legalEntityCreateRequest.set_annualCreditCardSalesVolume("80000000")
        legalEntityCreateRequest.set_hasAcceptedCreditCards("true")
        address = generatedClass.address.factory()
        address.set_streetAddress1("Street Address 1")
        address.set_streetAddress2("Street Address 2")
        address.set_city("City")
        address.set_stateProvince("MA")
        address.set_postalCode("01730")
        address.set_countryCode("USA")
        legalEntityCreateRequest.set_address(address)
        principal = generatedClass.legalEntityPrincipal.factory()
        principal.set_title("Chief Financial Officer")
        principal.set_firstName("p first")
        principal.set_lastName("p last")
        principal.set_emailAddress("emailAddress")
        principal.set_ssn("123459876")
        principal.set_contactPhone("7817659800")
        principal.set_dateOfBirth(parse("1980-10-11T12:00:00-06:00"))
        principal.set_driversLicense("892327409832")
        principal.set_driversLicenseState("MA")
        principal.set_address(address)
        principal.set_stakePercent(33)
        legalEntityCreateRequest.set_principal(principal)
        legalEntityCreateRequest.set_yearsInBusiness("12")
        mock_http_post_request.return_value = {'@xmlns': 'http://payfac.vantivcnp.com/api/merchant/onboard', u'legalEntityId': u'19924', u'backgroundCheckResults': {u'lienResult': {u'streetAddress2': u'Suite 2', u'streetAddress1': u'100 Main Street', u'releasedCount': 7, u'filingDate': u'2018-09-17', u'zip': u'01150', u'companyName': u'Company Name', u'unreleasedCount': 8, u'state': u'MA', u'lienType': u'4mFY0F0uiOnERSZ', u'city': u'Boston', u'zip4': u'2202'}, u'bankruptcyData': {u'streetAddress2': u'Suite 2', u'streetAddress1': u'100 Main Street', u'bankruptcyType': u'HJuBu', u'filingDate': u'2018-09-17', u'zip': u'01150', u'city': u'Boston', u'companyName': u'Company Name', u'state': u'MA', u'bankruptcyCount': 4, u'zip4': u'2202'}, u'business': {u'verificationResult': {u'nameAddressTaxIdAssociation': {u'code': u'NAME_ADDRESS_TAX_ID', u'description': u'Name, address, and Tax Id verified.'}, u'verificationIndicators': {u'nameVerified': True, u'stateVerified': True, u'cityVerified': True, u'addressVerified': True, u'phoneVerified': True, u'taxIdVerified': True, u'zipVerified': True}, u'riskIndicators': {u'riskIndicator': [{u'code': u'PHONE_NUMBER_MOBILE', u'description': u'The submitted phone number is a mobile number.'}, {u'code': u'PHONE_NUMBER_MOBILE', u'description': u'The submitted phone number is a mobile number.'}]}, u'nameAddressPhoneAssociation': {u'code': u'NAME_ADDRESS_PHONE', u'description': u'Name, address, and phone verified.'}, u'overallScore': {u'score': 40, u'description': u'Business identity is confirmed at the input address'}}}, u'backgroundCheckDecisionNotes': u'T5tAwny8nhngwxkYmo0a', u'businessToPrincipalAssociation': {u'score': 20, u'description': u'Principal\xe2\x80\x99s verified address matches input Business address.'}, u'principal': {u'verificationResult': {u'nameAddressPhoneAssociation': {u'code': u'LAST_ADDRESS_PHONE', u'description': u'Last name, address, and phone number verified.'}, u'nameAddressSsnAssociation': {u'code': u'FIRST_LAST_ADDRESS_SSN', u'description': u'First name, last name, address, and SSN verified.'}, u'riskIndicators': {u'riskIndicator': [{u'code': u'PHONE_NUMBER_MOBILE', u'description': u'The submitted phone number is a mobile number.'}, {u'code': u'PHONE_NUMBER_MOBILE', u'description': u'The submitted phone number is a mobile number.'}]}, u'verificationIndicators': {u'dobVerified': True, u'nameVerified': True, u'addressVerified': True, u'phoneVerified': True, u'ssnVerified': True}, u'overallScore': {u'score': 50, u'description': u'Full name, address, phone, and SSN verified.'}}}}, u'responseDescription': u'Approved', u'responseCode': 10, u'transactionId': 5018599851L, u'principal': {u'lastName': u'p_last', u'firstName': u'p_first', u'principalId': 79452}}

        response = payfac_legalEntity.post_by_legalEntity(legalEntityCreateRequest)
        expected_url_suffix = "/legalentity"
        mock_http_post_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertEquals("19924", response["legalEntityId"])
        self.assertEquals(5018599851L, response["transactionId"])
        self.assertEquals(10, response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])
