import unittest
import mock
from payfacMPSdk import payfac_submerchant,generatedClass

class TestSubmerchant(unittest.TestCase):

    @mock.patch('payfacMPSdk.communication.http_get_retrieval_request')
    def test_get_by_subMerchantId(self, mock_http_get_retrieval_request):
        payfac_submerchant.get_by_subMerchantId("2018", "123456")
        expected_url_suffix = "/legalentity/2018/submerchant/123456"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix)


    @mock.patch('payfacMPSdk.communication.http_post_request')
    def test_post_by_legalEntity(self, mock_http_post_request):
        subMerchantCreateRequest = generatedClass.subMerchantCreateRequest.factory()
        subMerchantCreateRequest.set_merchantName("Merchant Name")
        subMerchantCreateRequest.set_amexMid("1234567890")
        subMerchantCreateRequest.set_discoverConveyedMid("12345678901235")
        subMerchantCreateRequest.set_url("http://merchantUrl")
        subMerchantCreateRequest.set_customerServiceNumber("8407809000")
        subMerchantCreateRequest.set_hardCodedBillingDescriptor("billing Descriptor")
        subMerchantCreateRequest.set_maxTransactionAmount(8400)
        subMerchantCreateRequest.set_purchaseCurrency("USD")
        subMerchantCreateRequest.set_merchantCategoryCode("5964")
        subMerchantCreateRequest.set_bankRoutingNumber("840123124")
        subMerchantCreateRequest.set_bankAccountNumber("84012312415")
        subMerchantCreateRequest.set_pspMerchantId("123456")
        fraud = generatedClass.subMerchantFraudFeature.factory()
        fraud.set_enabled("true")
        subMerchantCreateRequest.set_fraud(fraud)

        amexAcquired = generatedClass.subMerchantAmexAcquiredFeature.factory()
        amexAcquired.set_enabled("false")
        subMerchantCreateRequest.set_amexAcquired(amexAcquired)

        address = generatedClass.address.factory()
        address.set_streetAddress1("Street Address 1")
        address.set_streetAddress2("Street Address 2")
        address.set_city("City")
        address.set_stateProvince("MA")
        address.set_postalCode("01970")
        address.set_countryCode("USA")
        subMerchantCreateRequest.set_address(address)

        primaryContact = generatedClass.subMerchantPrimaryContact.factory()
        primaryContact.set_firstName("John")
        primaryContact.set_lastName("Doe")
        primaryContact.set_emailAddress("John.Doe@company.com")
        primaryContact.set_phone("978555222")
        subMerchantCreateRequest.set_primaryContact(primaryContact)

        subMerchantCreateRequest.set_createCredentials("true")

        eCheck = generatedClass.subMerchantECheckFeature.factory()
        eCheck.set_eCheckCompanyName("Company Name")
        eCheck.set_eCheckBillingDescriptor("978555222")
        eCheck.set_enabled("true")
        subMerchantCreateRequest.set_eCheck(eCheck)

        submerchantFunding = generatedClass.subMerchantFunding.factory()
        submerchantFunding.set_enabled("false")
        subMerchantCreateRequest.set_subMerchantFunding(submerchantFunding)

        subMerchantCreateRequest.set_settlementCurrency("USD")

        expected_request = '<subMerchantCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><merchantName>Merchant Name</merchantName><amexMid>1234567890</amexMid><discoverConveyedMid>12345678901235</discoverConveyedMid><url>http://merchantUrl</url><customerServiceNumber>8407809000</customerServiceNumber><hardCodedBillingDescriptor>billing Descriptor</hardCodedBillingDescriptor><maxTransactionAmount>8400</maxTransactionAmount><purchaseCurrency>USD</purchaseCurrency><merchantCategoryCode>5964</merchantCategoryCode><bankRoutingNumber>840123124</bankRoutingNumber><bankAccountNumber>84012312415</bankAccountNumber><pspMerchantId>123456</pspMerchantId><fraud enabled="true"/><amexAcquired enabled="false"/><address><streetAddress1>Street Address 1</streetAddress1><streetAddress2>Street Address 2</streetAddress2><city>City</city><stateProvince>MA</stateProvince><postalCode>01970</postalCode><countryCode>USA</countryCode></address><primaryContact><firstName>John</firstName><lastName>Doe</lastName><emailAddress>John.Doe@company.com</emailAddress><phone>978555222</phone></primaryContact><createCredentials>true</createCredentials><eCheck enabled="true"><eCheckCompanyName>Company Name</eCheckCompanyName><eCheckBillingDescriptor>978555222</eCheckBillingDescriptor></eCheck><subMerchantFunding enabled="false"/><settlementCurrency>USD</settlementCurrency><sdkVersion>13.1.0</sdkVersion><language>python</language></subMerchantCreateRequest>'

        payfac_submerchant.post_by_legalEntity("2018", subMerchantCreateRequest)
        expected_url_suffix = "/legalentity/2018/submerchant".encode('utf-8')
        mock_http_post_request.assert_called_with(expected_url_suffix, expected_request)

    @mock.patch('payfacMPSdk.communication.http_put_request')
    def test_put_by_subMerchantId(self, mock_http_put_request):
        subMerchantUpdateRequest = generatedClass.subMerchantUpdateRequest.factory()
        subMerchantUpdateRequest.set_amexMid("1234567890")
        subMerchantUpdateRequest.set_discoverConveyedMid("123456789012345")
        subMerchantUpdateRequest.set_url("http://merchantUrl")
        subMerchantUpdateRequest.set_customerServiceNumber("8407809000")
        subMerchantUpdateRequest.set_hardCodedBillingDescriptor("Descriptor")
        subMerchantUpdateRequest.set_maxTransactionAmount(8400)
        subMerchantUpdateRequest.set_bankRoutingNumber("840123124")
        subMerchantUpdateRequest.set_bankAccountNumber("84012312415")
        subMerchantUpdateRequest.set_pspMerchantId("785412365")
        subMerchantUpdateRequest.set_purchaseCurrency("USD")
        address = generatedClass.addressUpdatable.factory()
        address.set_streetAddress1("Street Address 1")
        address.set_streetAddress2("Street Address 2")
        address.set_city("City")
        address.set_stateProvince("MA")
        address.set_postalCode("01970")
        subMerchantUpdateRequest.set_address(address)
        primaryContact = generatedClass.subMerchantPrimaryContactUpdatable.factory()
        primaryContact.set_firstName("John")
        primaryContact.set_lastName("Doe")
        primaryContact.set_phone("978555222")
        subMerchantUpdateRequest.set_primaryContact(primaryContact)
        fraud = generatedClass.subMerchantFraudFeature.factory()
        fraud.set_enabled("true")
        subMerchantUpdateRequest.set_fraud(fraud)
        amexAcquired = generatedClass.subMerchantAmexAcquiredFeature.factory()
        amexAcquired.set_enabled("true")
        subMerchantUpdateRequest.set_amexAcquired(amexAcquired)
        eCheck = generatedClass.subMerchantECheckFeature.factory()
        eCheck.set_eCheckBillingDescriptor("978555222")
        eCheck.set_enabled("true")
        subMerchantUpdateRequest.set_eCheck(eCheck)

        payfac_submerchant.put_by_subMerchantId("2018", "123456", subMerchantUpdateRequest)
        expected_url_suffix = "/legalentity/2018/submerchant/123456".encode('utf-8')
        mock_http_put_request.assert_called_with(expected_url_suffix, mock.ANY)
