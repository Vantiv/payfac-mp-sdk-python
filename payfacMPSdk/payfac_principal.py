from __future__ import absolute_import, print_function, unicode_literals

import xmlschema
import os
import sys
import pkg_resources

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

from payfacMPSdk import communication, utils, version as SdkVersion

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
xsd_path = pkg_resources.resource_filename('payfacMPSdk', 'schema/' + xsd_name)
my_schema = xmlschema.XMLSchema(xsd_path)

def post_by_legalEntity(legalEntityId, legalEntityPrincipalCreateRequest):
    legalEntityPrincipalCreateRequest.set_sdkVersion(SdkVersion.RELEASE)
    legalEntityPrincipalCreateRequest.set_language(SdkVersion.LANGUAGE)
    stringIO = StringIO()
    legalEntityPrincipalCreateRequest.export(stringIO, 0, pretty_print=False)
    request = stringIO.getvalue()
    request = request.replace("tns:", "")
    request = request.replace(":tns", "")
    if my_schema.is_valid(request):
        url_suffix = (SERVICE_ROUTE1 + legalEntityId + SERVICE_ROUTE2).encode('utf-8')
        return communication.http_post_request(url_suffix, request.encode('utf-8'))
    else:
        raise utils.PayfacSchemaError("Input is not compatible with schema")


def delete_by_legalEntityId(legalEntityId, principalId):
    url_suffix = SERVICE_ROUTE1 + legalEntityId + SERVICE_ROUTE2 + "/" + principalId
    return communication.http_delete_request(url_suffix)
