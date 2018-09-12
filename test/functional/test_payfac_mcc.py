import unittest
from payfacsdk import payfac_mcc


class TestMcc(unittest.TestCase):

    def test_get_mcc(self):
        response = payfac_mcc.get_mcc()
        self.assertEquals("5967", response["approvedMccs"]["approvedMcc"][0])
        self.assertEquals("5970", response["approvedMccs"]["approvedMcc"][1])
        self.assertIsNotNone(response["transactionId"])