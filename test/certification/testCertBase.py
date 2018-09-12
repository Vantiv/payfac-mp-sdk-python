import random
import unittest
from payfacsdk import communication, utils


class TestCertification(unittest.TestCase):

    conf = utils.Configuration()
    conf.__setattr__("url", "https://payfac.vantivprelive.com")
    conf.__setattr__("username", "")
    conf.__setattr__("password","")


    legalEntityPostRequest1 = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' \
                              '<legalEntityCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard">' \
                              '<legalEntityName>Legal Entity Name</legalEntityName>' \
                              '<legalEntityType>'
    legalEntityPostRequest2 = '</legalEntityType>' \
                              '<legalEntityOwnershipType>PRIVATE</legalEntityOwnershipType>' \
                              '<doingBusinessAs>Alternate Business Name</doingBusinessAs>' \
                              '<taxId>'
    legalEntityPostRequest3 = '</taxId>' \
                              '<contactPhone>7817659800</contactPhone>' \
                              '<annualCreditCardSalesVolume>80000000</annualCreditCardSalesVolume>' \
                              '<hasAcceptedCreditCards>true</hasAcceptedCreditCards>' \
                              '<address>' \
                               '<streetAddress1>'
    legalEntityPostRequest4 =  '</streetAddress1>' \
                                    '<streetAddress2>Street Address 2</streetAddress2>' \
                                    '<city>City</city>' \
                                    '<stateProvince>MA</stateProvince>' \
                                    '<postalCode>01730</postalCode>' \
                                    '<countryCode>USA</countryCode>' \
                                 '</address>' \
                                 '<principal>' \
                                    '<title>Chief Financial Officer</title>' \
                                    '<firstName>p first</firstName>' \
                                    '<lastName>p last</lastName>' \
                                    '<emailAddress>emailAddress</emailAddress>' \
                                    '<ssn>123459876</ssn>' \
                                    '<contactPhone>7817659800</contactPhone>' \
                                    '<dateOfBirth>1980-10-12</dateOfBirth>' \
                                    '<driversLicense>892327409832</driversLicense>' \
                                    '<driversLicenseState>MA</driversLicenseState>' \
                                    '<address>' \
                                        '<streetAddress1>p street address 1</streetAddress1>' \
                                        '<streetAddress2>p street address 2</streetAddress2>' \
                                        '<city>Boston</city>' \
                                        '<stateProvince>MA</stateProvince>' \
                                        '<postalCode>01890</postalCode>' \
                                        '<countryCode>USA</countryCode>' \
                                    '</address>' \
                                    '<stakePercent>100</stakePercent>' \
                                 '</principal>' \
                                 '<yearsInBusiness>12</yearsInBusiness>' \
                                 '</legalEntityCreateRequest>'

    legalEntityPutRequest1 = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' \
                            '<legalEntityUpdateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard">' \
                            '<address>' \
                                '<streetAddress1>Street Address 1</streetAddress1>' \
                                 '<streetAddress2>Street Address 2</streetAddress2>' \
                                '<city>City</city>' \
                                '<stateProvince>MA</stateProvince>' \
                                '<postalCode>01730</postalCode>' \
                                '<countryCode>USA</countryCode>' \
                            '</address>' \
                            '<contactPhone>776498</contactPhone>' \
                            '<doingBusinessAs>Alternate Business Name</doingBusinessAs>' \
                            '<annualCreditCardSalesVolume>100000000</annualCreditCardSalesVolume>' \
                            '<hasAcceptedCreditCards>true</hasAcceptedCreditCards>' \
                            '<principal>' \
                                '<principalId>1</principalId>' \
                                '<title>CEO</title>' \
                                '<emailAddress>4894@mail.net</emailAddress>' \
                                '<contactPhone>118484</contactPhone>' \
                                '<address>' \
                                    '<streetAddress1>p street address 1</streetAddress1>' \
                                    '<streetAddress2>p street address 2</streetAddress2>' \
                                    '<city>Boston</city>' \
                                    '<stateProvince>MA</stateProvince>' \
                                    '<postalCode>01890</postalCode>' \
                                    '<countryCode>USA</countryCode>' \
                                '</address>' \
                                '<backgroundCheckFields>' \
                                    '<firstName>p first</firstName>' \
                                    '<lastName>p last</lastName>' \
                                    '<ssn>123459876</ssn>' \
                                    '<dateOfBirth>1980-10-12</dateOfBirth>' \
                                    '<driversLicense>892327409832</driversLicense>' \
                                    '<driversLicenseState>MA</driversLicenseState>' \
                                '</backgroundCheckFields>' \
                            '</principal>' \
                            '<backgroundCheckFields>' \
                                '<legalEntityName>Company Name2</legalEntityName>' \
                                '<legalEntityType>INDIVIDUAL_SOLE_PROPRIETORSHIP</legalEntityType>' \
                                '<taxId>'
    legalEntityPutRequest2 = '</taxId>' \
                            '</backgroundCheckFields>' \
                            '<legalEntityOwnershipType>PRIVATE</legalEntityOwnershipType>' \
                            '<yearsInBusiness>10</yearsInBusiness>' \
                            '</legalEntityUpdateRequest>'

    submerchant_post_request1 = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' \
                               '<subMerchantCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard">' \
                               '<merchantName>Merchant Name</merchantName>' \
                               '<amexMid>1234567890</amexMid>' \
                               '<url>URL</url>' \
                               '<customerServiceNumber>1234567894</customerServiceNumber>' \
                               '<hardCodedBillingDescriptor>SDK*</hardCodedBillingDescriptor>' \
                               '<maxTransactionAmount>123</maxTransactionAmount>' \
                               '<merchantCategoryCode>5137</merchantCategoryCode>' \
                               '<bankRoutingNumber>211370545</bankRoutingNumber>' \
                               '<bankAccountNumber>84012312415</bankAccountNumber>' \
                               '<pspMerchantId>'

    submerchant_post_request2 = '</pspMerchantId>' \
                               '<fraud enabled="false"></fraud>' \
                               '<amexAcquired enabled="false"></amexAcquired>' \
                               '<address>' \
                                    '<streetAddress1>Street Address 1</streetAddress1>' \
                                    '<streetAddress2>Street Address 2</streetAddress2>' \
                                    '<city>City</city>' \
                                    '<stateProvince>MA</stateProvince>' \
                                    '<postalCode>01970</postalCode>' \
                                    '<countryCode>USA</countryCode>' \
                               '</address>' \
                               '<primaryContact>' \
                                    '<firstName>John</firstName>' \
                                    '<lastName>Doe</lastName>' \
                                    '<emailAddress>John.Doe@company.com</emailAddress>' \
                                    '<phone>9785552222</phone>' \
                               '</primaryContact>' \
                               '<createCredentials>true</createCredentials>' \
                               '<eCheck enabled="true">' \
                                    '<eCheckCompanyName>Company Name</eCheckCompanyName>' \
                                    '<eCheckBillingDescriptor>9785552222</eCheckBillingDescriptor>' \
                               '</eCheck>' \
                               '<subMerchantFunding enabled="true">' \
                                    '<fundingSubmerchantId>AUTO_GENERATE</fundingSubmerchantId>'\
                               '</subMerchantFunding>' \
                               '<settlementCurrency>USD</settlementCurrency>' \
                               '</subMerchantCreateRequest>'

    submerchant_put_request1 = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' \
                              '<subMerchantUpdateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard">' \
                              '<amexMid>1234567890</amexMid>' \
                              '<discoverConveyedMid>123456789012345</discoverConveyedMid>' \
                              '<url>http://merchantUrl</url>' \
                              '<customerServiceNumber>8407809000</customerServiceNumber>' \
                              '<hardCodedBillingDescriptor>SDK*</hardCodedBillingDescriptor>' \
                              '<maxTransactionAmount>8400</maxTransactionAmount>' \
                              '<bankRoutingNumber>211370545</bankRoutingNumber>' \
                              '<bankAccountNumber>84012312415</bankAccountNumber>' \
                              '<pspMerchantId>'
    submerchant_put_request2 = '</pspMerchantId>' \
                              '<purchaseCurrency>USD</purchaseCurrency>' \
                              '<address>' \
                                    '<streetAddress1>Street Address 1</streetAddress1>' \
                                    '<streetAddress2>Street Address 2</streetAddress2>' \
                                    '<city>City</city>' \
                                    '<stateProvince>MA</stateProvince>' \
                                    '<postalCode>01970</postalCode>' \
                                    '<countryCode>USA</countryCode>' \
                              '</address>' \
                              '<primaryContact>' \
                                    '<firstName>John</firstName>' \
                                    '<lastName>Doe</lastName>' \
                                    '<phone>9785552222</phone>' \
                              '</primaryContact>' \
                              '</subMerchantUpdateRequest>'





    #==========================================================================================
    #                             Legalentity certification Tests
    #==========================================================================================


    def test1(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)
        self.assertEquals("10",response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])


    def test2(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "912 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)
        self.assertEquals("20",response["responseCode"])


    # wait a minimum of two hours after submitting test #2
    def test2and2a(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest2 = response["legalEntityId"]
        expected_url_suffix2 = expected_url_suffix + "/" + legalEntityIdFromTest2
        response2 = communication.http_get_retrieval_request(expected_url_suffix2,"legalEntityRetrievalResponse",self.conf)


    # wait a minimum of two hours after submitting test #2
    def test2and2a(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest2 = response["legalEntityId"]
        expected_url_suffix2 = expected_url_suffix + "/" + legalEntityIdFromTest2
        response2 = communication.http_get_retrieval_request(expected_url_suffix2,"legalEntityRetrievalResponse",self.conf)

        self.assertEquals("10",response2["responseCode"])
        self.assertEquals("Approved",response2["responseDescription"])


    def test3(self):
        legalEntityType = "LIMITED_LIABILITY_COMPANY"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "914 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)
        self.assertEquals("10",response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])

    def test1and4(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest1 = response["legalEntityId"]
        expected_url_suffix2 = expected_url_suffix + "/" + legalEntityIdFromTest1
        taxId = random.randint(100000000, 999999999)
        legalEntityPutRequest = self.legalEntityPutRequest1 +str(taxId) + self.legalEntityPutRequest2
        response2 = communication.http_put_request(expected_url_suffix2,legalEntityPutRequest,"legalEntityResponse",self.conf)

        self.assertEquals("10",response2["responseCode"])
        self.assertEquals("Approved", response2["responseDescription"])


    def test5(self):
        expected_url_suffix = "/legalentity/0"
        taxId = random.randint(100000000, 999999999)
        legalEntityPutRequest = self.legalEntityPutRequest1 +str(taxId) + self.legalEntityPutRequest2
        self.assertRaises(utils.PayfacWebError,communication.http_put_request,expected_url_suffix,legalEntityPutRequest,"legalEntityResponse",self.conf)


    def test2and6(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "912 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest2 = response["legalEntityId"]
        expected_url_suffix2 = expected_url_suffix + "/" + legalEntityIdFromTest2
        response2 = communication.http_get_retrieval_request(expected_url_suffix2,"legalEntityRetrievalResponse",self.conf)
        self.assertEquals("20",response2["responseCode"])


    def test7(self):
        expected_url_suffix = "/legalentity/0"
        self.assertRaises(utils.PayfacWebError,communication.http_get_retrieval_request,expected_url_suffix,"legalEntityRetrievalResponse",self.conf)


    #==========================================================================================
    #                             Submerchant certification Tests
    #==========================================================================================


    def test1and8(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest1 = response["legalEntityId"]

        pspMerchantId = random.randint(100,999)
        submerchant_post_request = self.submerchant_post_request1 + str(pspMerchantId) + self.submerchant_post_request2
        expected_url_suffix2 = expected_url_suffix + "/" + legalEntityIdFromTest1 + "/submerchant"
        response2 = communication.http_post_request(expected_url_suffix2, submerchant_post_request ,"subMerchantCreateResponse",self.conf)


    def test9(self):
        pspMerchantId = random.randint(100, 999)
        submerchant_post_request = self.submerchant_post_request1 + str(pspMerchantId) + self.submerchant_post_request2
        expected_url_suffix = "/legalentity/0/submerchant"
        self.assertRaises(utils.PayfacWebError,communication.http_post_request,expected_url_suffix, submerchant_post_request ,"subMerchantCreateResponse",self.conf)

    def test2and10(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "912 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest2 = response["legalEntityId"]
        pspMerchantId = random.randint(100, 999)
        submerchant_post_request = self.submerchant_post_request1 + str(pspMerchantId) + self.submerchant_post_request2
        expected_url_suffix = "/legalentity/"+legalEntityIdFromTest2+ "/submerchant"
        self.assertRaises(utils.PayfacWebError,communication.http_post_request,expected_url_suffix, submerchant_post_request ,"subMerchantCreateResponse",self.conf)

    def test1and8and11(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest1 = response["legalEntityId"]

        pspMerchantId = random.randint(100,999)
        submerchant_post_request = self.submerchant_post_request1 + str(pspMerchantId) + self.submerchant_post_request2
        expected_url_suffix2 = expected_url_suffix + "/" + legalEntityIdFromTest1 + "/submerchant"
        response2 = communication.http_post_request(expected_url_suffix2, submerchant_post_request ,"subMerchantCreateResponse",self.conf)

        merchantIdFromTest8 = response2["subMerchantId"]
        pspMerchantId = random.randint(100, 999)
        submerchant_put_request = self.submerchant_put_request1 + str(pspMerchantId) + self.submerchant_put_request2
        expected_url_suffix3 = "/legalentity/" + legalEntityIdFromTest1 + "/submerchant/" + merchantIdFromTest8
        response3 = communication.http_put_request(expected_url_suffix3,submerchant_put_request,"response",self.conf)



    def test1and8and12(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest1 = response["legalEntityId"]

        pspMerchantId = random.randint(100,999)
        submerchant_post_request = self.submerchant_post_request1 + str(pspMerchantId) + self.submerchant_post_request2
        expected_url_suffix2 = expected_url_suffix + "/" + legalEntityIdFromTest1 + "/submerchant"
        response2 = communication.http_post_request(expected_url_suffix2, submerchant_post_request ,"subMerchantCreateResponse",self.conf)

        merchantIdFromTest8 = response2["subMerchantId"]
        pspMerchantId = random.randint(100, 999)
        submerchant_put_request = self.submerchant_put_request1 + str(pspMerchantId) + self.submerchant_put_request2
        expected_url_suffix3 = "/legalentity/0/submerchant/" + merchantIdFromTest8
        self.assertRaises(utils.PayfacWebError,communication.http_put_request,expected_url_suffix3,submerchant_put_request,"response",self.conf)


    def test1adn13(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest1 = response["legalEntityId"]

        pspMerchantId = random.randint(100, 999)
        submerchant_put_request = self.submerchant_put_request1 + str(pspMerchantId) + self.submerchant_put_request2
        expected_url_suffix3 = "/legalentity/"+legalEntityIdFromTest1+"/submerchant/0"
        self.assertRaises(utils.PayfacWebError,communication.http_put_request,expected_url_suffix3,submerchant_put_request,"response",self.conf)



    def test1and8and14(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest1 = response["legalEntityId"]

        pspMerchantId = random.randint(100,999)
        submerchant_post_request = self.submerchant_post_request1 + str(pspMerchantId) + self.submerchant_post_request2
        expected_url_suffix2 = expected_url_suffix + "/" + legalEntityIdFromTest1 + "/submerchant"
        response2 = communication.http_post_request(expected_url_suffix2, submerchant_post_request ,"subMerchantCreateResponse",self.conf)

        subMerchantId = response2["subMerchantId"]
        expected_url_suffix3 = expected_url_suffix2 + "/" + subMerchantId
        response3 = communication.http_get_retrieval_request(expected_url_suffix3,"subMerchantRetrievalResponse",self.conf)


    def test1and8and15(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest1 = response["legalEntityId"]

        pspMerchantId = random.randint(100,999)
        submerchant_post_request = self.submerchant_post_request1 + str(pspMerchantId) + self.submerchant_post_request2
        expected_url_suffix2 = expected_url_suffix + "/" + legalEntityIdFromTest1 + "/submerchant"
        response2 = communication.http_post_request(expected_url_suffix2, submerchant_post_request ,"subMerchantCreateResponse",self.conf)

        subMerchantId = response2["subMerchantId"]
        expected_url_suffix3 ="/legalentity/0/submerchant/"+ subMerchantId
        self.assertRaises(utils.PayfacWebError, communication.http_get_retrieval_request, expected_url_suffix3, "subMerchantRetrievalResponse", self.conf)


    def test1and8and16(self):
        legalEntityType = "INDIVIDUAL_SOLE_PROPRIETORSHIP"
        taxId = random.randint(100000000,999999999)
        streetAddress1 = "900 Chelmsford St"
        legalEntityPostRequest = self.legalEntityPostRequest1 + legalEntityType + self.legalEntityPostRequest2 + str(taxId) + self.legalEntityPostRequest3 + streetAddress1 + self.legalEntityPostRequest4
        expected_url_suffix = "/legalentity"
        response = communication.http_post_request(expected_url_suffix,legalEntityPostRequest,"legalEntityCreateResponse",self.conf)

        legalEntityIdFromTest1 = response["legalEntityId"]

        pspMerchantId = random.randint(100,999)
        submerchant_post_request = self.submerchant_post_request1 + str(pspMerchantId) + self.submerchant_post_request2
        expected_url_suffix2 = expected_url_suffix + "/" + legalEntityIdFromTest1 + "/submerchant"
        response2 = communication.http_post_request(expected_url_suffix2, submerchant_post_request ,"subMerchantCreateResponse",self.conf)

        subMerchantId = response2["subMerchantId"]
        expected_url_suffix3 = expected_url_suffix2 + "/0"
        self.assertRaises(utils.PayfacWebError, communication.http_get_retrieval_request, expected_url_suffix3, "subMerchantRetrievalResponse", self.conf)