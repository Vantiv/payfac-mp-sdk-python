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
xsd_path = pkg_resources.resource_filename('payfacMPSdk', 'schema/' + xsd_name)
my_schema = xmlschema.XMLSchema(xsd_path)


def get_by_legalEntityId(legalEntityId):
    url_suffix = SERVICE_ROUTE + "/" + legalEntityId
    return communication.http_get_retrieval_request(url_suffix)


def post_by_legalEntity(legalEntityCreateRequest):
    legalEntityCreateRequest.set_sdkVersion(SdkVersion.RELEASE)
    legalEntityCreateRequest.set_language(SdkVersion.LANGUAGE)
    stringIO = StringIO()
    legalEntityCreateRequest.export(stringIO, 0, pretty_print=False)
    request = stringIO.getvalue()
    request = request.replace("tns:", "")
    request = request.replace(":tns", "")
    if my_schema.is_valid(request):
        url_suffix = SERVICE_ROUTE.encode('utf-8')
        return communication.http_post_request(url_suffix, request.encode('utf-8'))
    else:
        raise utils.PayfacSchemaError("Input is not compatible with schema")

def put_by_legalEntityId(legalEntityId,legalEntityUpdateRequest):
    url_suffix = (SERVICE_ROUTE + "/" + legalEntityId).encode('utf-8')

    stringIO = StringIO()
    legalEntityUpdateRequest.export(stringIO, 0)
    request = stringIO.getvalue()
    request = request.replace("tns:", "")
    request = request.replace(":tns", "")
    if my_schema.is_valid(request):
        request = request.replace("tns:", "")
        request = request.replace(":tns", "")
        return communication.http_put_request(url_suffix, request.encode('utf-8'))
    else:
        raise utils.PayfacSchemaError("Input is not compatible with schema")
