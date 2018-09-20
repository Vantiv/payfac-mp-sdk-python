from __future__ import absolute_import, print_function, unicode_literals

import xmlschema
import os
import sys

from payfacMPSdk import communication, utils

SERVICE_ROUTE1 = "/legalentity/"

SERVICE_ROUTE2 = "/submerchant"
"""
/////////////////////////////////////////////////////
            subMerchantRetrievalResponse APIs:
/////////////////////////////////////////////////////
"""
package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)
version = utils.Configuration().VERSION
xsd_name = 'merchant-onboard-api-v%s.xsd' % version
xsd_abs_path = os.path.join(package_root, "schema", xsd_name)
my_schema = xmlschema.XMLSchema(xsd_abs_path)
xml_path =  os.path.join(package_root, "payfacMPSdk")

def get_by_subMerchantId(legalEntityId, subMerchantId):
    url_suffix = SERVICE_ROUTE1  + legalEntityId + SERVICE_ROUTE2 +"/"+ subMerchantId
    return communication.http_get_retrieval_request(url_suffix)

def post_by_legalEntity(legalEntityId,subMerchantCreateRequest):

    xmlFile = open(xml_path + "/testXML", "w+")
    xmlFile.truncate(0)
    subMerchantCreateRequest.export(xmlFile, 0)
    xmlFile.close()
    xmlFile = open(xml_path + "/testXML", "r")
    request = xmlFile.read()
    xmlFile.close()
    request = request.replace("tns:", "")
    request = request.replace(":tns", "")
    if my_schema.is_valid(request):
        request = request.replace("tns:", "")
        request = request.replace(":tns", "")
        url_suffix = (SERVICE_ROUTE1 + legalEntityId + SERVICE_ROUTE2).encode('utf-8')
        return communication.http_post_request(url_suffix, request.encode('utf-8'))
    else:
        raise utils.PayfacSchemaError("Input is not compatible with schema")

def put_by_subMerchantId(legalEntityId,subMerchantId, subMerchantUpdateRequest):

    xmlFile = open(xml_path + "/testXML", "w+")
    xmlFile.truncate(0)
    subMerchantUpdateRequest.export(xmlFile, 0)
    xmlFile.close()
    xmlFile = open(xml_path + "/testXML", "r")
    request = xmlFile.read()
    xmlFile.close()
    if my_schema.is_valid(request):
        request = request.replace("tns:", "")
        request = request.replace(":tns", "")
        url_suffix = (SERVICE_ROUTE1 + legalEntityId + SERVICE_ROUTE2 + "/" + subMerchantId).encode('utf-8')
        return communication.http_put_request(url_suffix, request.encode('utf-8'))
    else:
        raise utils.PayfacSchemaError("Input is not compatible with schema")