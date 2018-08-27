#
from __future__ import absolute_import, print_function, unicode_literals

import mimetypes
import re

import requests
from requests.auth import HTTPBasicAuth

from payfacsdk import (utils)

conf = utils.Configuration()

PAYFAC_CONTENT_TYPE = "application/com.vantivcnp.payfac-v13+xml"

CHARGEBACK_API_HEADERS = {"Accept": PAYFAC_CONTENT_TYPE,
                          "Content-Type": PAYFAC_CONTENT_TYPE}

HTTP_ERROR_MESSAGE = "Error with Https Request, Please Check Proxy and Url configuration"


def http_get_retrieval_request(url_suffix, config=conf):
    request_url = config.url + url_suffix

    try:
        http_response = requests.get(request_url, headers=CHARGEBACK_API_HEADERS,
                                     auth=HTTPBasicAuth(config.username, config.password))

    except requests.RequestException:
        raise utils.ChargebackError(HTTP_ERROR_MESSAGE)

    print_to_console("\nGET request to:", request_url, config)
    validate_response(http_response)
    print_to_console("\nResponse :", http_response.text, config)
    return utils.generate_retrieval_response(http_response)




def _generate_error_data(error_response):
    error_list = error_response['errors']['error']
    error_message = ""
    prefix = ""
    for error in error_list:
        print(error)
        error_message += prefix + error
        prefix = "\n"
    return error_list, error_message

def validate_response(http_response, config=conf):
    """check the status code of the response
    :param http_response: http response generated
    :return: raises an exception
    """
    # Check empty response
    if http_response is None:
        raise utils.ChargebackError("There was an exception while fetching the response")

    content_type = http_response.headers._store['content-type'][1]

    if http_response.status_code != 200:
        if PAYFAC_CONTENT_TYPE in content_type:
            error_response = utils.generate_error_response(http_response)
            print_to_console("\nResponse :", http_response.text, config)
            error_list, error_message = _generate_error_data(error_response)
            raise utils.ChargebackWebError(error_message, str(http_response.status_code), error_list)
        raise utils.ChargebackWebError(http_response, str(http_response.status_code))





def neuter_xml(xml_string):
    xml_string = re.sub(r"<token>.*</token>", "<token>****</token>", xml_string)
    xml_string = re.sub(r"<cardNumberLast4>.*</cardNumberLast4>", "<cardNumberLast4>****</cardNumberLast4>", xml_string)
    return xml_string

def print_to_console(prefix_message, xml_string, config=conf):
    if config.print_xml:
        if config.neuter_xml:
            xml_string = neuter_xml(xml_string)
        print(prefix_message, xml_string)