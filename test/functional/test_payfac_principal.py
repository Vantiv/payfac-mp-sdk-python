import unittest
from payfacsdk import payfac_principal


class TestPrincipal(unittest.TestCase):

    def test_post_by_legalEntity(self):
        principalPostRequest = '<legalEntityPrincipalCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><principal><title>Mr.</title><firstName>First</firstName><lastName>Last</lastName><emailAddress>abc@gmail.com</emailAddress><ssn>123450015</ssn><dateOfBirth>1980-10-12</dateOfBirth><address><streetAddress1>p2 street address 1</streetAddress1><streetAddress2>p2 street address 2</streetAddress2><city>Boston2</city><stateProvince>MA</stateProvince><postalCode>01892</postalCode><countryCode>USA</countryCode></address><stakePercent>31</stakePercent></principal></legalEntityPrincipalCreateRequest>'
        response = payfac_principal.post_by_legalEntity("21003",principalPostRequest)
        self.assertIsNotNone(response['transactionId'])
        self.assertEquals("21003",response["legalEntityId"])

    def test_delete_by_legalEntityId(self):
        response = payfac_principal.delete_by_legalEntityId("21003","9")
        self.assertIsNotNone(response['transactionId'])
        self.assertEquals("21003",response["legalEntityId"])
        self.assertEquals("9",response["principalId"])
        self.assertEquals("Legal Entity Principal successfully deleted",response["responseDescription"])