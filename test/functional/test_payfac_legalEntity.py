import unittest
from payfacMPSdk import payfac_legalEntity, generatedClass, utils
from dateutil.parser import parse

class TestLegalEntity(unittest.TestCase):

    def test_get_by_legalEntityId(self):
        response = payfac_legalEntity.get_by_legalEntityId("1000293")
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertEquals("123456789",response["taxId"])
        self.assertIsNotNone(response["transactionId"])


    def test_put_by_legalEntityId(self):
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

        response = payfac_legalEntity.put_by_legalEntityId("1000293", legalEntityUpdateRequest)

        self.assertEquals("1000293", response["legalEntityId"])
        self.assertIsNotNone(response["transactionId"])
        self.assertEquals(10, response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])

        principal2 = generatedClass.legalEntityPrincipalUpdatable.factory()
        principal2.set_title("CEO")
        principal2.set_emailAddress("jdoe@mail.net")
        principal2.set_contactPhone("9785551234")
        principal2.set_address(address)

        legalEntityUpdateRequest.set_principal(principal2)
        self.assertRaises(utils.PayfacSchemaError, payfac_legalEntity.put_by_legalEntityId, "1000293",legalEntityUpdateRequest)


    def test_post_by_legalEntity(self):
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

        response = payfac_legalEntity.post_by_legalEntity(legalEntityCreateRequest)
        self.assertIsNotNone(response["legalEntityId"])
        self.assertIsNotNone(response["transactionId"])
        self.assertEquals(10, response["responseCode"])
        self.assertEquals("Approved", response["responseDescription"])

        address2 = generatedClass.address.factory()
        address.set_streetAddress1("Street Address 1")
        address.set_streetAddress2("Street Address 2")
        legalEntityCreateRequest.set_address(address2)
        self.assertRaises(utils.PayfacSchemaError, payfac_legalEntity.post_by_legalEntity, legalEntityCreateRequest)