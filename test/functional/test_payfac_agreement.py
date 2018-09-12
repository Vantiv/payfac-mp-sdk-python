import unittest
from payfacMPSdk import payfac_agreement


class TestAgreement(unittest.TestCase):

    def test_get_by_legalEntityId(self):
        response = payfac_agreement.get_by_legalEntityId("1000293")
        self.assertEquals("1000293", response["legalEntityId"])
        self.assertIsNotNone(response["transactionId"])

    def test_post_by_legalEntity(self):
        agreementPostRequest = '<legalEntityAgreementCreateRequest xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><legalEntityAgreement><legalEntityAgreementType>MERCHANT_AGREEMENT</legalEntityAgreementType><agreementVersion>agreementVersion1</agreementVersion><userFullName>userFullName</userFullName><userSystemName>systemUserName</userSystemName><userIPAddress>196.198.100.100</userIPAddress><manuallyEntered>false</manuallyEntered><acceptanceDateTime>2017-02-11T12:00:00-06:00</acceptanceDateTime></legalEntityAgreement></legalEntityAgreementCreateRequest>'
        response = payfac_agreement.post_by_legalEntityId("21003",agreementPostRequest)
        self.assertIsNotNone(response['transactionId'])
