from payfacsdk import communication
import unittest
import payfacsdk
from payfacsdk import payfac_legalEntity
from payfacsdk import payfac_agreement
from payfacsdk import payfac_submerchant
from payfacsdk import payfac_principal
from payfacsdk import payfac_mcc

def test_get_retrieval_request():

        # agreementPostRequest = '<legalEntityAgreementCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><legalEntityAgreement><legalEntityAgreementType>MERCHANT_AGREEMENT</legalEntityAgreementType><agreementVersion>agreementVersion1</agreementVersion><userFullName>userFullName</userFullName><userSystemName>systemUserName</userSystemName><userIPAddress>196.198.100.100</userIPAddress><manuallyEntered>false</manuallyEntered><acceptanceDateTime>2017-02-11T12:00:00-06:00</acceptanceDateTime></legalEntityAgreement></legalEntityAgreementCreateRequest>'
        # print payfac_agreement.post_by_legalEntityId("21003", agreementPostRequest)

        # print payfac_agreement.get_by_legalEntityId("1000293")

        # legalEntityPostRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><legalEntityCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><legalEntityName>Legal Entity Name</legalEntityName><legalEntityType>CORPORATION</legalEntityType><legalEntityOwnershipType>PUBLIC</legalEntityOwnershipType><doingBusinessAs>Alternate Business Name</doingBusinessAs><taxId>123456789</taxId><contactPhone>7817659800</contactPhone><annualCreditCardSalesVolume>80000000</annualCreditCardSalesVolume><hasAcceptedCreditCards>true</hasAcceptedCreditCards><address><streetAddress1>Street Address 1</streetAddress1><streetAddress2>Street Address 2</streetAddress2><city>City</city><stateProvince>MA</stateProvince><postalCode>01730</postalCode><countryCode>USA</countryCode></address><principal><title>Chief Financial Officer</title><firstName>p first</firstName><lastName>p last</lastName><emailAddress>emailAddress</emailAddress><ssn>123459876</ssn><contactPhone>7817659800</contactPhone><dateOfBirth>1980-10-12</dateOfBirth><driversLicense>892327409832</driversLicense><driversLicenseState>MA</driversLicenseState><address><streetAddress1>p street address 1</streetAddress1><streetAddress2>p street address 2</streetAddress2><city>Boston</city><stateProvince>MA</stateProvince><postalCode>01890</postalCode><countryCode>USA</countryCode></address><stakePercent>33</stakePercent></principal><yearsInBusiness>12</yearsInBusiness></legalEntityCreateRequest>'
        # print payfac_legalEntity.post_by_legalEntity(legalEntityPostRequest)

        # legalEntityPutRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><legalEntityUpdateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><address><streetAddress1>LE Street Address 1</streetAddress1><streetAddress2>LE Street Address 2</streetAddress2><city>LE City</city><stateProvince>MA</stateProvince><postalCode>01730</postalCode><countryCode>USA</countryCode></address><contactPhone>9785550101</contactPhone><doingBusinessAs>Other Name Co.</doingBusinessAs><annualCreditCardSalesVolume>10000000</annualCreditCardSalesVolume><hasAcceptedCreditCards>true</hasAcceptedCreditCards><principal><principalId>9</principalId><title>CEO</title><emailAddress>jdoe@mail.net</emailAddress><contactPhone>9785551234</contactPhone><address><streetAddress1>p street address 1</streetAddress1><streetAddress2>p street address 2</streetAddress2><city>Boston</city><stateProvince>MA</stateProvince><postalCode>01890</postalCode><countryCode>USA</countryCode></address><backgroundCheckFields><firstName>p first</firstName><lastName>p last</lastName><ssn>123459876</ssn><dateOfBirth>1980-10-12</dateOfBirth><driversLicense>892327409832</driversLicense><driversLicenseState>MA</driversLicenseState></backgroundCheckFields></principal><backgroundCheckFields><legalEntityName>Company Name</legalEntityName><legalEntityType>INDIVIDUAL_SOLE_PROPRIETORSHIP</legalEntityType><taxId>123456789</taxId></backgroundCheckFields><legalEntityOwnershipType>PUBLIC</legalEntityOwnershipType><yearsInBusiness>10</yearsInBusiness></legalEntityUpdateRequest>'
        # print payfac_legalEntity.put_by_legalEntityId("1000293",legalEntityPutRequest)

        payfac_legalEntity.get_by_legalEntityId("1000293")

        # principalPostRequest = '<legalEntityPrincipalCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><principal><title>Mr.</title><firstName>First</firstName><lastName>Last</lastName><emailAddress>abc@gmail.com</emailAddress><ssn>123450015</ssn><dateOfBirth>1980-10-12</dateOfBirth><address><streetAddress1>p2 street address 1</streetAddress1><streetAddress2>p2 street address 2</streetAddress2><city>Boston2</city><stateProvince>MA</stateProvince><postalCode>01892</postalCode><countryCode>USA</countryCode></address><stakePercent>31</stakePercent></principal></legalEntityPrincipalCreateRequest>'
        # print payfac_principal.post_by_legalEntity("2018",principalPostRequest)

        # payfac_principal.delete_by_legalEntityId("2018","9")

        # submerchantPostRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><subMerchantCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><merchantName>Merchant Name</merchantName><amexMid>1234567890</amexMid><discoverConveyedMid>123456789012345</discoverConveyedMid><url>http://merchantUrl</url><customerServiceNumber>8407809000</customerServiceNumber><hardCodedBillingDescriptor>billing Descriptor</hardCodedBillingDescriptor><maxTransactionAmount>8400</maxTransactionAmount><purchaseCurrency>USD</purchaseCurrency><merchantCategoryCode>5964</merchantCategoryCode><bankRoutingNumber>840123124</bankRoutingNumber><bankAccountNumber>84012312415</bankAccountNumber><pspMerchantId>123456</pspMerchantId><fraud enabled="true"></fraud><amexAcquired enabled="false"></amexAcquired><address><streetAddress1>Street Address 1</streetAddress1><streetAddress2>Street Address 2</streetAddress2><city>City</city><stateProvince>MA</stateProvince><postalCode>01970</postalCode><countryCode>USA</countryCode></address><primaryContact><firstName>John</firstName><lastName>Doe</lastName><emailAddress>John.Doe@company.com</emailAddress><phone>9785552222</phone></primaryContact><createCredentials>true</createCredentials><eCheck enabled="true"><eCheckCompanyName>Company Name</eCheckCompanyName><eCheckBillingDescriptor>9785552222</eCheckBillingDescriptor></eCheck><subMerchantFunding enabled="false"></subMerchantFunding><settlementCurrency>USD</settlementCurrency></subMerchantCreateRequest>'
        # payfac_submerchant.post_by_legalEntity("2018",submerchantPostRequest)

        # submerchantPutRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><subMerchantUpdateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><amexMid>1234567890</amexMid><discoverConveyedMid>123456789012345</discoverConveyedMid><url>http://merchantUrl</url><customerServiceNumber>8407809000</customerServiceNumber><hardCodedBillingDescriptor>Descriptor</hardCodedBillingDescriptor><maxTransactionAmount>8400</maxTransactionAmount><bankRoutingNumber>840123124</bankRoutingNumber><bankAccountNumber>84012312415</bankAccountNumber><pspMerchantId>785412365</pspMerchantId><purchaseCurrency>USD</purchaseCurrency><address><streetAddress1>Street Address 1</streetAddress1><streetAddress2>Street Address 2</streetAddress2><city>City</city><stateProvince>MA</stateProvince><postalCode>01970</postalCode></address><primaryContact><firstName>John</firstName><lastName>Doe</lastName><phone>9785552222</phone></primaryContact><fraud enabled="true"></fraud><amexAcquired enabled="true"></amexAcquired><eCheck enabled="true"><eCheckBillingDescriptor>9785552222</eCheckBillingDescriptor></eCheck></subMerchantUpdateRequest>'
        # payfac_submerchant.put_by_subMerchantId("2018","123456",submerchantPutRequest)

        # payfac_submerchant.get_by_subMerchantId("2018","123456")

        payfac_mcc.get_mcc()





test_get_retrieval_request()