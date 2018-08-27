# import os
# import json
# import pyxb
# import xmltodict
#
# class Configuration(object):
#     """Setup Configuration variables.
#
#     Attributes:
#         user (Str): authentication.user
#         password (Str): authentication.password
#         merchant_id (Str): The unique string to identify the merchant within the system.
#         url (Str): Url for server.
#         proxy (Str): Https proxy server address. Must start with "https://"
#         print_xml (Str): Whether print request and response xml
#     """
#
#     _CONFIG_FILE_PATH = os.path.join(os.environ['PAYFAC_MP_SDK_CONFIG'], ".payfac_mp_sdk.conf") \
#         if 'PAYFAC_MP_SDK_CONFIG' in os.environ else os.path.join(os.path.expanduser("~"), ".payfac_mp_sdk.conf")
#
#     def __init__(self, conf_dict=dict()):
#         attr_dict = {
#             'username': '',
#             'password': '',
#             'merchant_id': '',
#             'url': '',
#             'proxy': '',
#             'print_xml': False,
#             'neuter_xml': False,
#         }
#
#         # set default values
#         for k in attr_dict:
#             setattr(self, k, attr_dict[k])
#
#         # override values by loading saved conf
#         try:
#             with open(self._CONFIG_FILE_PATH, 'r') as config_file:
#                 config_json = json.load(config_file)
#                 for k in attr_dict:
#                     if k in config_json and config_json[k]:
#                         setattr(self, k, config_json[k])
#         except:
#             # If get any exception just pass.
#             pass
#
#         # override values by args
#         if conf_dict:
#             for k in conf_dict:
#                 if k in attr_dict:
#                     setattr(self, k, conf_dict[k])
#                 # else:
#                 #     raise ChargebackError('"%s" is NOT an attribute of conf' % k)
#
#     def save(self):
#         """Save Class Attributes to .payfac_mp_sdk.conf
#
#         Returns:
#             full path for configuration file.
#
#         Raises:
#             IOError: An error occurred
#         """
#         with open(self._CONFIG_FILE_PATH, 'w') as config_file:
#             json.dump(vars(self), config_file)
#         return self._CONFIG_FILE_PATH
#
# def obj_to_xml(obj):
#     """Convert object to xml string without namespaces
#
#     Args:
#         obj: Object
#
#     Returns:
#         Xml string
#
#     Raises:
#         pyxb.ValidationError
#     """
#     # TODO convert object to xml without default namespace gracefully.
#     try:
#
#         xml = obj.toxml('utf-8')
#     except pyxb.ValidationError as e:
#         raise ChargebackError(e.details())
#     xml = xml.replace(b'ns1:', b'')
#     xml = xml.replace(b':ns1', b'')
#     return xml
#
# def generate_retrieval_response(http_response, return_format='dict'):
#     return convert_to_format(http_response.text, "chargebackRetrievalResponse", return_format)
#
#
#
#
#
# def convert_to_format(http_response, response_type, return_format='dict'):
#     return_format = return_format.lower()
#     if return_format == 'xml':
#         response_xml = http_response.text
#         return response_xml
#     # elif return_format == 'object':
#     #     return convert_to_obj(http_response.text)
#     else:
#         return convert_to_dict(http_response, response_type)
#
#
# # def convert_to_obj(xml_response):
# #     return fields_chargeback.CreateFromDocument(xml_response)
#
#
# def convert_to_dict(xml_response, response_type):
#     response_dict = xmltodict.parse(xml_response)[response_type]
#     if response_dict['@xmlns'] != "":
#         _create_lists(response_dict)
#         return response_dict
#     else:
#         raise ChargebackError("Invalid Format")
#
#
#
#
# def _create_lists(response_dict):
#     if "chargebackCase" in response_dict:
#         _create_list("chargebackCase", response_dict)
#
#         for case in response_dict["chargebackCase"]:
#             if "activity" in case:
#                 _create_list("activity", case)
#
#     if "errors" in response_dict:
#         _create_list("error", response_dict["errors"])
#
#
# # if there is only one element for the given key in container, create a list for it
# def _create_list(element_key, container):
#     element_value = container[element_key]
#     if element_value != "" and not isinstance(element_value, list):
#         container[element_key] = [element_value]
#
#
#
#
#
#
#
#
#
#
#
#
#
# class ChargebackError(Exception):
#
#     def __init__(self, message):
#         self.message = message
