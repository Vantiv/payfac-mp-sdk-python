import unittest
from payfacsdk import payfac_submerchant


class TestSubMerchant(unittest.TestCase):

    def test_get_by_subMerchantId(self):
        response = payfac_submerchant.get_by_subMerchantId("2018","123456")
        self.assertEquals("123456", response["subMerchantId"])
        self.assertEquals("123456",response["pspMerchantId"])
        self.assertIsNotNone(response["transactionId"])

    def test_put_by_subMerchantId(self):
        submerchantPutRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><subMerchantUpdateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><amexMid>1234567890</amexMid><discoverConveyedMid>123456789012345</discoverConveyedMid><url>http://merchantUrl</url><customerServiceNumber>8407809000</customerServiceNumber><hardCodedBillingDescriptor>Descriptor</hardCodedBillingDescriptor><maxTransactionAmount>8400</maxTransactionAmount><bankRoutingNumber>840123124</bankRoutingNumber><bankAccountNumber>84012312415</bankAccountNumber><pspMerchantId>785412365</pspMerchantId><purchaseCurrency>USD</purchaseCurrency><address><streetAddress1>Street Address 1</streetAddress1><streetAddress2>Street Address 2</streetAddress2><city>City</city><stateProvince>MA</stateProvince><postalCode>01970</postalCode></address><primaryContact><firstName>John</firstName><lastName>Doe</lastName><phone>9785552222</phone></primaryContact><fraud enabled="true"></fraud><amexAcquired enabled="true"></amexAcquired><eCheck enabled="true"><eCheckBillingDescriptor>9785552222</eCheckBillingDescriptor></eCheck></subMerchantUpdateRequest>'
        response = payfac_submerchant.put_by_subMerchantId("2018","123456", submerchantPutRequest)
        self.assertIsNotNone(response["transactionId"])

    def test_post_by_legalEntity(self):
        submerchantPostRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><subMerchantCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><merchantName>Merchant Name</merchantName><amexMid>1234567890</amexMid><discoverConveyedMid>123456789012345</discoverConveyedMid><url>http://merchantUrl</url><customerServiceNumber>8407809000</customerServiceNumber><hardCodedBillingDescriptor>billing Descriptor</hardCodedBillingDescriptor><maxTransactionAmount>8400</maxTransactionAmount><purchaseCurrency>USD</purchaseCurrency><merchantCategoryCode>5964</merchantCategoryCode><bankRoutingNumber>840123124</bankRoutingNumber><bankAccountNumber>84012312415</bankAccountNumber><pspMerchantId>123456</pspMerchantId><fraud enabled="true"></fraud><amexAcquired enabled="false"></amexAcquired><address><streetAddress1>Street Address 1</streetAddress1><streetAddress2>Street Address 2</streetAddress2><city>City</city><stateProvince>MA</stateProvince><postalCode>01970</postalCode><countryCode>USA</countryCode></address><primaryContact><firstName>John</firstName><lastName>Doe</lastName><emailAddress>John.Doe@company.com</emailAddress><phone>9785552222</phone></primaryContact><createCredentials>true</createCredentials><eCheck enabled="true"><eCheckCompanyName>Company Name</eCheckCompanyName><eCheckBillingDescriptor>9785552222</eCheckBillingDescriptor></eCheck><subMerchantFunding enabled="false"></subMerchantFunding><settlementCurrency>USD</settlementCurrency></subMerchantCreateRequest>'
        response = payfac_submerchant.post_by_legalEntity("2018",submerchantPostRequest)
        self.assertIsNotNone(response["subMerchantId"])
        self.assertIsNotNone(response["transactionId"])
        self.assertIsNotNone(response["merchantIdentString"])
