from __future__ import absolute_import, print_function, unicode_literals

import xmlschema
import os
import sys

from payfacMPSdk import communication, utils

SERVICE_ROUTE1 = "/legalentity/"

SERVICE_ROUTE2 = "/principal"

"""
/////////////////////////////////////////////////////
            principal APIs:
/////////////////////////////////////////////////////
"""
package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)
version = utils.Configuration().VERSION
xsd_name = 'merchant-onboard-api-v%s.xsd' % version
xsd_abs_path = os.path.join(package_root, "schema", xsd_name)
my_schema = xmlschema.XMLSchema(xsd_abs_path)
xml_path =  os.path.join(package_root, "payfacMPSdk")

def post_by_legalEntity(legalEntityId, legalEntityPrincipalCreateRequest):

    xmlFile = open(xml_path + "/testXML", "w+")
    xmlFile.truncate(0)
    legalEntityPrincipalCreateRequest.export(xmlFile, 0)
    xmlFile.close()
    xmlFile = open(xml_path + "/testXML", "r")
    request = xmlFile.read()
    xmlFile.close()
    if my_schema.is_valid(request):
        request = request.replace("tns:", "")
        request = request.replace(":tns", "")
        url_suffix = (SERVICE_ROUTE1 + legalEntityId + SERVICE_ROUTE2).encode('utf-8')
        return communication.http_post_request(url_suffix, request.encode('utf-8'))
    else:
        raise utils.PayfacSchemaError("Input is not compatible with schema")


def delete_by_legalEntityId(legalEntityId, principalId):
    url_suffix = SERVICE_ROUTE1 + legalEntityId + SERVICE_ROUTE2 + "/" + principalId
    return communication.http_delete_request(url_suffix)
