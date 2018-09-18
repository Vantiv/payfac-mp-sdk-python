import unittest
from payfacMPSdk import payfac_submerchant, generatedClass, utils


class TestSubMerchant(unittest.TestCase):

    def test_get_by_subMerchantId(self):
        response = payfac_submerchant.get_by_subMerchantId("2018","123456")
        self.assertEquals("123456", response["subMerchantId"])
        self.assertEquals("123456",response["pspMerchantId"])
        self.assertIsNotNone(response["transactionId"])

    def test_put_by_subMerchantId(self):
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

        response = payfac_submerchant.put_by_subMerchantId("2018","123456", subMerchantUpdateRequest)
        self.assertIsNotNone(response["transactionId"])


    def test_post_by_legalEntity(self):
        subMerchantCreateRequest = generatedClass.subMerchantCreateRequest.factory()
        subMerchantCreateRequest.set_merchantName("Merchant Name")
        subMerchantCreateRequest.set_amexMid("1234567890")
        subMerchantCreateRequest.set_discoverConveyedMid("12345678901235")
        subMerchantCreateRequest.set_url("http://merchantUrl")
        subMerchantCreateRequest.set_customerServiceNumber("8407809000")
        subMerchantCreateRequest.set_hardCodedBillingDescriptor("billing Descriptor")
        subMerchantCreateRequest.set_maxTransactionAmount(840000l)
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

        response = payfac_submerchant.post_by_legalEntity("2018",subMerchantCreateRequest)
        self.assertIsNotNone(response["subMerchantId"])
        self.assertIsNotNone(response["transactionId"])
        self.assertIsNotNone(response["merchantIdentString"])

        subMerchantCreateRequest2 = generatedClass.subMerchantCreateRequest.factory()
        self.assertRaises(utils.PayfacSchemaError, payfac_submerchant.post_by_legalEntity, "2018", subMerchantCreateRequest2)