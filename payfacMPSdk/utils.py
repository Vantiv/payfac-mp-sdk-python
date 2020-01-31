import os
import json
import xmlschema
import sys

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)
version = u'13'
xsd_name = 'merchant-onboard-api-v%s.xsd' % version
xsd_abs_path = os.path.join(package_root, "schema", xsd_name)
my_schema = xmlschema.XMLSchema(xsd_abs_path)

class Configuration(object):
    """Setup Configuration variables.

    Attributes:
        user (Str): authentication.user
        password (Str): authentication.password
        merchant_id (Str): The unique string to identify the merchant within the system.
        url (Str): Url for server.
        proxy (Str): Https proxy server address. Must start with "https://"
        print_xml (Str): Whether print request and response xml
    """
    VERSION = version
    if 'PAYFAC_MP_SDK_CONFIG' in os.environ:
        _CONFIG_FILE_PATH = os.path.join(os.environ['PAYFAC_MP_SDK_CONFIG'])
    else:
        _CONFIG_FILE_PATH = os.path.join(os.path.expanduser("~"), ".payfac_mp_sdk.conf")

    def __init__(self, conf_dict=dict()):

        # print("config file path -> "+self._CONFIG_FILE_PATH)

        attr_dict = {
            'merchant_id': '',
            'neuterXml': False,
            'password': '',
            'printXml': False,
            'proxy': '',
            'url': '',
            'username': ''
        }

        # set default values
        for k in attr_dict:
            setattr(self, k, attr_dict[k])

        # override values by loading saved conf
        try:
            with open(self._CONFIG_FILE_PATH, 'r') as config_file:
                config_json = json.load(config_file)
                # print ("overriding config values here \n")
                for ke in attr_dict:
                    if ke in config_json and config_json[ke]:
                        # print(ke + "\t" + config_json[ke])
                        setattr(self, ke, config_json[ke])
        except:
            # If get any exception just pass.
            pass

        # override values by args
        if conf_dict:
            for key in conf_dict:
                if key in attr_dict:
                    setattr(self, key, conf_dict[key])
                # else:
                #     raise payfacError('"%s" is NOT an attribute of conf' % k)

    def save(self):
        """Save Class Attributes to .payfac_mp_sdk.conf

        Returns:
            full path for configuration file.

        Raises:
            IOError: An error occurred
        """
        with open(self._CONFIG_FILE_PATH, 'w') as config_file:
            json.dump(vars(self), config_file)
        return self._CONFIG_FILE_PATH


def generate_response(http_response):
    return convert_to_dict(http_response.text)


def convert_to_dict(xml_response):
    if(not (my_schema.is_valid(xml_response.encode('utf-8')))): raise PayfacSchemaError("Input is not compatible with schema")
    response_dict = my_schema.to_dict(xml_response.encode('utf-8'))
    if response_dict['@xmlns'] != "":
        _create_lists(response_dict)
        return response_dict
    else:
        raise PayfacError("Invalid Format")


def _create_lists(response_dict):
    if "payfacCase" in response_dict:
        _create_list("payfacCase", response_dict)

        for case in response_dict["payfacCase"]:
            if "activity" in case:
                _create_list("activity", case)

    if "errors" in response_dict:
        _create_list("error", response_dict["errors"])


# if there is only one element for the given key in container, create a list for it
def _create_list(element_key, container):
    element_value = container[element_key]
    if element_value != "" and not isinstance(element_value, list):
        container[element_key] = [element_value]


def generate_error_response(http_response, return_format='dict'):
    return convert_to_dict(http_response.text)

class PayfacError(Exception):

    def __init__(self, message):
        self.message = message

class PayfacWebError(Exception):

    def __init__(self, message, code, error_list=None):
        self.message = message
        self.code = code
        self.error_list = error_list

class PayfacSchemaError(Exception):
    def __init__(self,message):
        self.message = message
