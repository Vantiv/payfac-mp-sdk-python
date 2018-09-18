import unittest
from payfacMPSdk import payfac_agreement, generatedClass, utils
from dateutil.parser import parse

class TestAgreement(unittest.TestCase):

    def test_get_by_legalEntityId(self):
        response = payfac_agreement.get_by_legalEntityId("1000293")
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertIsNotNone(response["transactionId"])

    def test_post_by_legalEntity(self):
        legalEntityAgreementCreateRequest = generatedClass.legalEntityAgreementCreateRequest.factory()
        legalEntityAgreement = generatedClass.legalEntityAgreement.factory()
        legalEntityAgreement.set_legalEntityAgreementType("MERCHANT_AGREEMENT")
        legalEntityAgreement.set_agreementVersion("agreementVersion1")
        legalEntityAgreement.set_userFullName("userFullName")
        legalEntityAgreement.set_userSystemName("systemUserName")
        legalEntityAgreement.set_userIPAddress("196.198.100.100")
        legalEntityAgreement.set_manuallyEntered("false")
        legalEntityAgreement.set_acceptanceDateTime(parse("2017-02-11T12:00:00-06:00"))
        legalEntityAgreementCreateRequest.set_legalEntityAgreement(legalEntityAgreement)


        response = payfac_agreement.post_by_legalEntityId("21003",legalEntityAgreementCreateRequest)
        self.assertIsNotNone(response['transactionId'])

        legalEntityAgreement2 = generatedClass.legalEntityAgreement.factory()
        legalEntityAgreement.set_agreementVersion("agreementVersion1")
        legalEntityAgreement.set_userFullName("userFullName")
        legalEntityAgreement.set_userSystemName("systemUserName")
        legalEntityAgreement.set_userIPAddress("196.198.100.100")
        legalEntityAgreement.set_manuallyEntered("false")
        legalEntityAgreement.set_acceptanceDateTime(parse("2017-02-11T12:00:00-06:00"))
        legalEntityAgreementCreateRequest.set_legalEntityAgreement(legalEntityAgreement2)
        self.assertRaises(utils.PayfacSchemaError, payfac_agreement.post_by_legalEntityId, "21003",legalEntityAgreementCreateRequest)