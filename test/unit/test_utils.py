import unittest
from payfacMPSdk import utils






class TestLegalEntity(unittest.TestCase):
    conf = utils.Configuration()

    def test_convert_to_dict(self):
        http_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><approvedMccResponse xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><transactionId>99010</transactionId><approvedMccs><approvedMcc>5967</approvedMcc><approvedMcc>5970</approvedMcc></approvedMccs></approvedMccResponse>'
        dict = utils.convert_to_dict(http_response)
        expect_dict = {'@xmlns': 'http://payfac.vantivcnp.com/api/merchant/onboard', u'transactionId': 99010, u'approvedMccs': {u'approvedMcc': [u'5967', u'5970']}}

        self.assertEquals(expect_dict,dict)
        http_response_without_xmlns = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><approvedMccResponse xmlns=""><transactionId>99010</transactionId><approvedMccs><approvedMcc>5967</approvedMcc><approvedMcc>5970</approvedMcc></approvedMccs></approvedMccResponse>'
        self.assertRaises(utils.PayfacSchemaError, utils.convert_to_dict, http_response_without_xmlns)







