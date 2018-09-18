import unittest
from payfacMPSdk import payfac_principal, generatedClass, utils
from dateutil.parser import parse

class TestPrincipal(unittest.TestCase):

    def test_post_by_legalEntity(self):
        legalEntityPrincipalCreateRequest = generatedClass.legalEntityPrincipalCreateRequest.factory()
        principal = generatedClass.legalEntityPrincipal.factory()
        principal.set_title("Mr.")
        principal.set_firstName("First")
        principal.set_lastName("Last")
        principal.set_emailAddress("abc@gamil.com")
        principal.set_ssn("123450015")
        principal.set_dateOfBirth(parse("1980-10-12T12:00:00-06:00"))
        address = generatedClass.principalAddress.factory()
        address.set_streetAddress1("p2 street address 1")
        address.set_streetAddress2("p2 street address 2")
        address.set_city("Boston2")
        address.set_stateProvince("MA")
        address.set_postalCode("01892")
        address.set_countryCode("USA")
        principal.set_address(address)
        principal.set_stakePercent(31)
        legalEntityPrincipalCreateRequest.set_principal(principal)

        response = payfac_principal.post_by_legalEntity("21003", legalEntityPrincipalCreateRequest)
        self.assertIsNotNone(response['transactionId'])
        self.assertEquals("21003", response["legalEntityId"])

        principal2 = generatedClass.legalEntityPrincipal.factory()
        principal2.set_title("Mr.")
        principal2.set_firstName("First")
        principal2.set_lastName("Last")
        principal2.set_emailAddress("abc@gamil.com")
        principal2.set_ssn("123450015")
        principal2.set_dateOfBirth(parse("1980-10-12T12:00:00-06:00"))
        legalEntityPrincipalCreateRequest.set_principal(principal2)
        self.assertRaises(utils.PayfacSchemaError, payfac_principal.post_by_legalEntity, "21003", legalEntityPrincipalCreateRequest)

    def test_delete_by_legalEntityId(self):
        response = payfac_principal.delete_by_legalEntityId("21003", "9")
        self.assertIsNotNone(response['transactionId'])
        self.assertEquals("21003", response["legalEntityId"])
        self.assertEquals(9, response["principalId"])
        self.assertEquals("Legal Entity Principal successfully deleted", response["responseDescription"])
