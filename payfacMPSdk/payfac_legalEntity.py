from __future__ import absolute_import, print_function, unicode_literals
import xmlschema
import os
import sys
from payfacMPSdk import communication, utils

SERVICE_ROUTE = "/legalentity"

"""
/////////////////////////////////////////////////////
            legalEntity APIs:
/////////////////////////////////////////////////////
"""

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)
version = utils.Configuration().VERSION
xsd_name = 'merchant-onboard-api-v%s.xsd' % version
xsd_abs_path = os.path.join(package_root, "schema", xsd_name)
my_schema = xmlschema.XMLSchema(xsd_abs_path)
xml_path =  os.path.join(package_root, "payfacMPSdk")


def get_by_legalEntityId(legalEntityId):
    url_suffix = SERVICE_ROUTE + "/" + legalEntityId
    return communication.http_get_retrieval_request(url_suffix)


def post_by_legalEntity(legalEntityCreateRequest):

    xmlFile = open(xml_path+"/testXML", "w+")
    xmlFile.truncate(0)
    legalEntityCreateRequest.export(xmlFile, 0)
    xmlFile.close()
    xmlFile = open(xml_path+"/testXML", "r")
    request = xmlFile.read()
    xmlFile.close()
    if my_schema.is_valid(request):
        request = request.replace("tns:", "")
        request = request.replace(":tns", "")
        url_suffix = SERVICE_ROUTE.encode('utf-8')
        return communication.http_post_request(url_suffix, request.encode('utf-8'))
    else:
        raise utils.PayfacSchemaError("Input is not compatible with schema")

def put_by_legalEntityId(legalEntityId,legalEntityUpdateRequest):
    url_suffix = (SERVICE_ROUTE + "/" + legalEntityId).encode('utf-8')

    xmlFile = open(xml_path+"/testXML", "w+")
    xmlFile.truncate(0)
    legalEntityUpdateRequest.export(xmlFile, 0)
    xmlFile.close()
    xmlFile = open(xml_path+"/testXML", "r")
    request = xmlFile.read()
    xmlFile.close()

    if my_schema.is_valid(request):
        request = request.replace("tns:", "")
        request = request.replace(":tns", "")
        return communication.http_put_request(url_suffix, request.encode('utf-8'))
    else:
        raise utils.PayfacSchemaError("Input is not compatible with schema")