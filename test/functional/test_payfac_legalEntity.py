import unittest
from payfacMPSdk import payfac_legalEntity


class TestLegalEntity(unittest.TestCase):

    def test_get_by_legalEntityId(self):
        response = payfac_legalEntity.get_by_legalEntityId("1000293")
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertEquals("123456789",response["taxId"])
        self.assertIsNotNone(response["transactionId"])

    def test_put_by_legalEntityId(self):
        legalEntityPutRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><legalEntityUpdateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><address><streetAddress1>LE Street Address 1</streetAddress1><streetAddress2>LE Street Address 2</streetAddress2><city>LE City</city><stateProvince>MA</stateProvince><postalCode>01730</postalCode><countryCode>USA</countryCode></address><contactPhone>9785550101</contactPhone><doingBusinessAs>Other Name Co.</doingBusinessAs><annualCreditCardSalesVolume>10000000</annualCreditCardSalesVolume><hasAcceptedCreditCards>true</hasAcceptedCreditCards><principal><principalId>9</principalId><title>CEO</title><emailAddress>jdoe@mail.net</emailAddress><contactPhone>9785551234</contactPhone><address><streetAddress1>p street address 1</streetAddress1><streetAddress2>p street address 2</streetAddress2><city>Boston</city><stateProvince>MA</stateProvince><postalCode>01890</postalCode><countryCode>USA</countryCode></address><backgroundCheckFields><firstName>p first</firstName><lastName>p last</lastName><ssn>123459876</ssn><dateOfBirth>1980-10-12</dateOfBirth><driversLicense>892327409832</driversLicense><driversLicenseState>MA</driversLicenseState></backgroundCheckFields></principal><backgroundCheckFields><legalEntityName>Company Name</legalEntityName><legalEntityType>INDIVIDUAL_SOLE_PROPRIETORSHIP</legalEntityType><taxId>123456789</taxId></backgroundCheckFields><legalEntityOwnershipType>PUBLIC</legalEntityOwnershipType><yearsInBusiness>10</yearsInBusiness></legalEntityUpdateRequest>'
        response = payfac_legalEntity.put_by_legalEntityId("1000293", legalEntityPutRequest)
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertIsNotNone(response["transactionId"])
        self.assertEquals("10", response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])

    def test_post_by_legalEntity(self):
        legalEntityPostRequest = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><legalEntityCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><legalEntityName>Legal Entity Name</legalEntityName><legalEntityType>CORPORATION</legalEntityType><legalEntityOwnershipType>PUBLIC</legalEntityOwnershipType><doingBusinessAs>Alternate Business Name</doingBusinessAs><taxId>123456789</taxId><contactPhone>7817659800</contactPhone><annualCreditCardSalesVolume>80000000</annualCreditCardSalesVolume><hasAcceptedCreditCards>true</hasAcceptedCreditCards><address><streetAddress1>Street Address 1</streetAddress1><streetAddress2>Street Address 2</streetAddress2><city>City</city><stateProvince>MA</stateProvince><postalCode>01730</postalCode><countryCode>USA</countryCode></address><principal><title>Chief Financial Officer</title><firstName>p first</firstName><lastName>p last</lastName><emailAddress>emailAddress</emailAddress><ssn>123459876</ssn><contactPhone>7817659800</contactPhone><dateOfBirth>1980-10-12</dateOfBirth><driversLicense>892327409832</driversLicense><driversLicenseState>MA</driversLicenseState><address><streetAddress1>p street address 1</streetAddress1><streetAddress2>p street address 2</streetAddress2><city>Boston</city><stateProvince>MA</stateProvince><postalCode>01890</postalCode><countryCode>USA</countryCode></address><stakePercent>33</stakePercent></principal><yearsInBusiness>12</yearsInBusiness></legalEntityCreateRequest>'
        response = payfac_legalEntity.post_by_legalEntity(legalEntityPostRequest)
        self.assertIsNotNone(response["legalEntityId"])
        self.assertIsNotNone(response["transactionId"])
        self.assertEquals("10", response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])
