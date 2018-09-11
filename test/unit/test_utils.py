import unittest
import mock
from collections import OrderedDict
from payfacsdk import utils






class TestLegalEntity(unittest.TestCase):
    conf = utils.Configuration()

    def test_convert_to_dict(self):
        http_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><approvedMccResponse xmlns="http://payfac.vantivcnp.com/api/merchant/onboard"><transactionId>9901030109</transactionId><approvedMccs><approvedMcc>5967</approvedMcc><approvedMcc>5970</approvedMcc></approvedMccs></approvedMccResponse>'
        dict = utils.convert_to_dict(http_response,"approvedMccResponse")
        expect_dict = OrderedDict([(u'@xmlns', u'http://payfac.vantivcnp.com/api/merchant/onboard'),
                         (u'transactionId', u'9901030109'),
                         (u'approvedMccs', OrderedDict([(u'approvedMcc', ['5967', '5970'])]))])
        self.assertEquals(expect_dict,dict)

        http_response_without_xmlns = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><approvedMccResponse xmlns=""><transactionId>9901030109</transactionId><approvedMccs><approvedMcc>5967</approvedMcc><approvedMcc>5970</approvedMcc></approvedMccs></approvedMccResponse>'

        self.assertRaises(utils.PayfacError, utils.convert_to_dict, http_response_without_xmlns, "approvedMccResponse")






