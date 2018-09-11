# ./fields_payfac.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:9608c9518b2c1add1a25370ac040759fdf43082e
# Generated 2018-09-11 11:44:24.700777 by PyXB version 1.2.5 using Python 2.7.14.final.0
# Namespace http://payfac.vantivcnp.com/api/merchant/onboard

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:8ea69070-b5d9-11e8-8a19-001a4a0106a3')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://payfac.vantivcnp.com/api/merchant/onboard', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityType
class legalEntityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 4, 4)
    _Documentation = None
legalEntityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=legalEntityType, enum_prefix=None)
legalEntityType.INDIVIDUAL_SOLE_PROPRIETORSHIP = legalEntityType._CF_enumeration.addEnumeration(unicode_value='INDIVIDUAL_SOLE_PROPRIETORSHIP', tag='INDIVIDUAL_SOLE_PROPRIETORSHIP')
legalEntityType.CORPORATION = legalEntityType._CF_enumeration.addEnumeration(unicode_value='CORPORATION', tag='CORPORATION')
legalEntityType.LIMITED_LIABILITY_COMPANY = legalEntityType._CF_enumeration.addEnumeration(unicode_value='LIMITED_LIABILITY_COMPANY', tag='LIMITED_LIABILITY_COMPANY')
legalEntityType.PARTNERSHIP = legalEntityType._CF_enumeration.addEnumeration(unicode_value='PARTNERSHIP', tag='PARTNERSHIP')
legalEntityType.LIMITED_PARTNERSHIP = legalEntityType._CF_enumeration.addEnumeration(unicode_value='LIMITED_PARTNERSHIP', tag='LIMITED_PARTNERSHIP')
legalEntityType.GENERAL_PARTNERSHIP = legalEntityType._CF_enumeration.addEnumeration(unicode_value='GENERAL_PARTNERSHIP', tag='GENERAL_PARTNERSHIP')
legalEntityType.TAX_EXEMPT_ORGANIZATION = legalEntityType._CF_enumeration.addEnumeration(unicode_value='TAX_EXEMPT_ORGANIZATION', tag='TAX_EXEMPT_ORGANIZATION')
legalEntityType.GOVERNMENT_AGENCY = legalEntityType._CF_enumeration.addEnumeration(unicode_value='GOVERNMENT_AGENCY', tag='GOVERNMENT_AGENCY')
legalEntityType._InitializeFacetMap(legalEntityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'legalEntityType', legalEntityType)
_module_typeBindings.legalEntityType = legalEntityType

# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}businessOverallScore
class businessOverallScore (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'businessOverallScore')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 17, 4)
    _Documentation = None
businessOverallScore._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=businessOverallScore, enum_prefix=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value='0', tag=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value='10', tag=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value='20', tag=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value='30', tag=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value='40', tag=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value='50', tag=None)
businessOverallScore._InitializeFacetMap(businessOverallScore._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'businessOverallScore', businessOverallScore)
_module_typeBindings.businessOverallScore = businessOverallScore

# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}nameAddressTaxIdAssociationCode
class nameAddressTaxIdAssociationCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameAddressTaxIdAssociationCode')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 28, 4)
    _Documentation = None
nameAddressTaxIdAssociationCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nameAddressTaxIdAssociationCode, enum_prefix=None)
nameAddressTaxIdAssociationCode.NOT_VERIFIED = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value='NOT_VERIFIED', tag='NOT_VERIFIED')
nameAddressTaxIdAssociationCode.WRONG_TAX_ID = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value='WRONG_TAX_ID', tag='WRONG_TAX_ID')
nameAddressTaxIdAssociationCode.NAME_OR_ADDRESS = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value='NAME_OR_ADDRESS', tag='NAME_OR_ADDRESS')
nameAddressTaxIdAssociationCode.BAD_NAME = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value='BAD_NAME', tag='BAD_NAME')
nameAddressTaxIdAssociationCode.BAD_ADDRESS = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value='BAD_ADDRESS', tag='BAD_ADDRESS')
nameAddressTaxIdAssociationCode.MISSING_ADDRESS = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value='MISSING_ADDRESS', tag='MISSING_ADDRESS')
nameAddressTaxIdAssociationCode.NAME_AND_ADDRESS_BAD_TAX_ID = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value='NAME_AND_ADDRESS_BAD_TAX_ID', tag='NAME_AND_ADDRESS_BAD_TAX_ID')
nameAddressTaxIdAssociationCode.NAME_AND_ADDRESS_NO_TAX_ID = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value='NAME_AND_ADDRESS_NO_TAX_ID', tag='NAME_AND_ADDRESS_NO_TAX_ID')
nameAddressTaxIdAssociationCode.NAME_ADDRESS_TAX_ID = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value='NAME_ADDRESS_TAX_ID', tag='NAME_ADDRESS_TAX_ID')
nameAddressTaxIdAssociationCode._InitializeFacetMap(nameAddressTaxIdAssociationCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'nameAddressTaxIdAssociationCode', nameAddressTaxIdAssociationCode)
_module_typeBindings.nameAddressTaxIdAssociationCode = nameAddressTaxIdAssociationCode

# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}businessNameAddressPhoneAssociationCode
class businessNameAddressPhoneAssociationCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'businessNameAddressPhoneAssociationCode')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 42, 4)
    _Documentation = None
businessNameAddressPhoneAssociationCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=businessNameAddressPhoneAssociationCode, enum_prefix=None)
businessNameAddressPhoneAssociationCode.NOT_VERIFIED = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='NOT_VERIFIED', tag='NOT_VERIFIED')
businessNameAddressPhoneAssociationCode.WRONG_PHONE = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='WRONG_PHONE', tag='WRONG_PHONE')
businessNameAddressPhoneAssociationCode.NAME_OR_ADDRESS = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='NAME_OR_ADDRESS', tag='NAME_OR_ADDRESS')
businessNameAddressPhoneAssociationCode.BAD_NAME = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='BAD_NAME', tag='BAD_NAME')
businessNameAddressPhoneAssociationCode.BAD_ADDRESS = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='BAD_ADDRESS', tag='BAD_ADDRESS')
businessNameAddressPhoneAssociationCode.MISSING_ADDRESS = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='MISSING_ADDRESS', tag='MISSING_ADDRESS')
businessNameAddressPhoneAssociationCode.NAME_AND_ADDRESS_BAD_PHONE = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='NAME_AND_ADDRESS_BAD_PHONE', tag='NAME_AND_ADDRESS_BAD_PHONE')
businessNameAddressPhoneAssociationCode.NAME_AND_ADDRESS_NO_PHONE = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='NAME_AND_ADDRESS_NO_PHONE', tag='NAME_AND_ADDRESS_NO_PHONE')
businessNameAddressPhoneAssociationCode.NAME_ADDRESS_PHONE = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='NAME_ADDRESS_PHONE', tag='NAME_ADDRESS_PHONE')
businessNameAddressPhoneAssociationCode._InitializeFacetMap(businessNameAddressPhoneAssociationCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'businessNameAddressPhoneAssociationCode', businessNameAddressPhoneAssociationCode)
_module_typeBindings.businessNameAddressPhoneAssociationCode = businessNameAddressPhoneAssociationCode

# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}riskIndicatorCode
class riskIndicatorCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'riskIndicatorCode')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 56, 4)
    _Documentation = None
riskIndicatorCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=riskIndicatorCode, enum_prefix=None)
riskIndicatorCode.UNKNOWN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='UNKNOWN', tag='UNKNOWN')
riskIndicatorCode.SSN_DECEASED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_DECEASED', tag='SSN_DECEASED')
riskIndicatorCode.SSN_PRIOR_TO_DOB = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_PRIOR_TO_DOB', tag='SSN_PRIOR_TO_DOB')
riskIndicatorCode.SSN_ADDRESS_PHONE_NOT_MATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_ADDRESS_PHONE_NOT_MATCH', tag='SSN_ADDRESS_PHONE_NOT_MATCH')
riskIndicatorCode.SSN_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_INVALID', tag='SSN_INVALID')
riskIndicatorCode.PHONE_NUMBER_DISCONNECTED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_NUMBER_DISCONNECTED', tag='PHONE_NUMBER_DISCONNECTED')
riskIndicatorCode.PHONE_NUMBER_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_NUMBER_INVALID', tag='PHONE_NUMBER_INVALID')
riskIndicatorCode.PHONE_NUMBER_PAGER = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_NUMBER_PAGER', tag='PHONE_NUMBER_PAGER')
riskIndicatorCode.PHONE_NUMBER_MOBILE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_NUMBER_MOBILE', tag='PHONE_NUMBER_MOBILE')
riskIndicatorCode.ADDRESS_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_INVALID', tag='ADDRESS_INVALID')
riskIndicatorCode.ZIP_BELONGS_POST_OFFICE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ZIP_BELONGS_POST_OFFICE', tag='ZIP_BELONGS_POST_OFFICE')
riskIndicatorCode.ADDRESS_INVALID_APARTMENT_DESIGNATION = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_INVALID_APARTMENT_DESIGNATION', tag='ADDRESS_INVALID_APARTMENT_DESIGNATION')
riskIndicatorCode.ADDRESS_COMMERCIAL = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_COMMERCIAL', tag='ADDRESS_COMMERCIAL')
riskIndicatorCode.PHONE_NUMBER_COMMERCIAL = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_NUMBER_COMMERCIAL', tag='PHONE_NUMBER_COMMERCIAL')
riskIndicatorCode.PHONE_NUMBER_ZIP_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_NUMBER_ZIP_INVALID', tag='PHONE_NUMBER_ZIP_INVALID')
riskIndicatorCode.UNABLE_TO_VERIFY_NAS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='UNABLE_TO_VERIFY_NAS', tag='UNABLE_TO_VERIFY_NAS')
riskIndicatorCode.UNABLE_TO_VERIFY_ADDRESS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='UNABLE_TO_VERIFY_ADDRESS', tag='UNABLE_TO_VERIFY_ADDRESS')
riskIndicatorCode.UNABLE_TO_VERIFY_SSN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='UNABLE_TO_VERIFY_SSN', tag='UNABLE_TO_VERIFY_SSN')
riskIndicatorCode.UNABLE_TO_VERIFY_PHONE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='UNABLE_TO_VERIFY_PHONE', tag='UNABLE_TO_VERIFY_PHONE')
riskIndicatorCode.UNABLE_TO_VERIFY_DOB = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='UNABLE_TO_VERIFY_DOB', tag='UNABLE_TO_VERIFY_DOB')
riskIndicatorCode.SSN_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_MISKEYED', tag='SSN_MISKEYED')
riskIndicatorCode.ADDRESS_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_MISKEYED', tag='ADDRESS_MISKEYED')
riskIndicatorCode.PHONE_NUMBER_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_NUMBER_MISKEYED', tag='PHONE_NUMBER_MISKEYED')
riskIndicatorCode.NAME_MATCHES_OFAC = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='NAME_MATCHES_OFAC', tag='NAME_MATCHES_OFAC')
riskIndicatorCode.UNABLE_TO_VERIFY_NAME = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='UNABLE_TO_VERIFY_NAME', tag='UNABLE_TO_VERIFY_NAME')
riskIndicatorCode.SSN_MATCHES_MULTI_NAMES = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_MATCHES_MULTI_NAMES', tag='SSN_MATCHES_MULTI_NAMES')
riskIndicatorCode.SSN_RECENTLY_ISSUED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_RECENTLY_ISSUED', tag='SSN_RECENTLY_ISSUED')
riskIndicatorCode.ZIP_CORPORATE_MILITARY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ZIP_CORPORATE_MILITARY', tag='ZIP_CORPORATE_MILITARY')
riskIndicatorCode.DLL_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='DLL_INVALID', tag='DLL_INVALID')
riskIndicatorCode.NAME_ADDRESS_MATCH_BANKRUPTCY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='NAME_ADDRESS_MATCH_BANKRUPTCY', tag='NAME_ADDRESS_MATCH_BANKRUPTCY')
riskIndicatorCode.PHONE_AREA_CODE_CHANGING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_AREA_CODE_CHANGING', tag='PHONE_AREA_CODE_CHANGING')
riskIndicatorCode.WORK_PHONE_PAGER = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='WORK_PHONE_PAGER', tag='WORK_PHONE_PAGER')
riskIndicatorCode.UNABLE_TO_VERIFY_FIRST_NAME = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='UNABLE_TO_VERIFY_FIRST_NAME', tag='UNABLE_TO_VERIFY_FIRST_NAME')
riskIndicatorCode.PHONE_ADDRESS_DISTANT = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_ADDRESS_DISTANT', tag='PHONE_ADDRESS_DISTANT')
riskIndicatorCode.ADDRESS_MATCHES_PRISON = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_MATCHES_PRISON', tag='ADDRESS_MATCHES_PRISON')
riskIndicatorCode.SSN_LAST_NAME_NO_MATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_LAST_NAME_NO_MATCH', tag='SSN_LAST_NAME_NO_MATCH')
riskIndicatorCode.SSN_FIRST_NAME_NO_MATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_FIRST_NAME_NO_MATCH', tag='SSN_FIRST_NAME_NO_MATCH')
riskIndicatorCode.WORK_HOME_PHONE_DISTANT = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='WORK_HOME_PHONE_DISTANT', tag='WORK_HOME_PHONE_DISTANT')
riskIndicatorCode.NAME_ADDRESS_TIN_MISMATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='NAME_ADDRESS_TIN_MISMATCH', tag='NAME_ADDRESS_TIN_MISMATCH')
riskIndicatorCode.WORK_PHONE_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='WORK_PHONE_INVALID', tag='WORK_PHONE_INVALID')
riskIndicatorCode.WORK_PHONE_DISCONNECTED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='WORK_PHONE_DISCONNECTED', tag='WORK_PHONE_DISCONNECTED')
riskIndicatorCode.WORK_PHONE_MOBILE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='WORK_PHONE_MOBILE', tag='WORK_PHONE_MOBILE')
riskIndicatorCode.ADDRESS_RETURNS_DIFF_PHONE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_RETURNS_DIFF_PHONE', tag='ADDRESS_RETURNS_DIFF_PHONE')
riskIndicatorCode.SSN_LNAME_NOT_MATCHED_FNAME_MATCHED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_LNAME_NOT_MATCHED_FNAME_MATCHED', tag='SSN_LNAME_NOT_MATCHED_FNAME_MATCHED')
riskIndicatorCode.PHONE_RESIDENTIAL_LISTING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_RESIDENTIAL_LISTING', tag='PHONE_RESIDENTIAL_LISTING')
riskIndicatorCode.SINGLE_FAMILY_DWELLING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SINGLE_FAMILY_DWELLING', tag='SINGLE_FAMILY_DWELLING')
riskIndicatorCode.SSN_NOT_FOUND = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_NOT_FOUND', tag='SSN_NOT_FOUND')
riskIndicatorCode.SSN_BELONGS_TO_DIFF_NAME_ADDRESS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_BELONGS_TO_DIFF_NAME_ADDRESS', tag='SSN_BELONGS_TO_DIFF_NAME_ADDRESS')
riskIndicatorCode.PHONE_BELONGS_TO_DIFF_NAME_ADDRESS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_BELONGS_TO_DIFF_NAME_ADDRESS', tag='PHONE_BELONGS_TO_DIFF_NAME_ADDRESS')
riskIndicatorCode.NAME_ADDRESS_UNLISTED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='NAME_ADDRESS_UNLISTED', tag='NAME_ADDRESS_UNLISTED')
riskIndicatorCode.NAME_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='NAME_MISKEYED', tag='NAME_MISKEYED')
riskIndicatorCode.NAME_MISSING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='NAME_MISSING', tag='NAME_MISSING')
riskIndicatorCode.ADDRESS_MISSING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_MISSING', tag='ADDRESS_MISSING')
riskIndicatorCode.SSN_MISSING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_MISSING', tag='SSN_MISSING')
riskIndicatorCode.PHONE_NUMBER_MISSING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='PHONE_NUMBER_MISSING', tag='PHONE_NUMBER_MISSING')
riskIndicatorCode.DOB_MISSING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='DOB_MISSING', tag='DOB_MISSING')
riskIndicatorCode.NAME_ADDRESS_RETURN_DIFF_PHONE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='NAME_ADDRESS_RETURN_DIFF_PHONE', tag='NAME_ADDRESS_RETURN_DIFF_PHONE')
riskIndicatorCode.DOB_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='DOB_MISKEYED', tag='DOB_MISKEYED')
riskIndicatorCode.SSN_NON_US_CITIZEN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_NON_US_CITIZEN', tag='SSN_NON_US_CITIZEN')
riskIndicatorCode.ALTERNATE_BUSINESS_NAME_FOUND = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ALTERNATE_BUSINESS_NAME_FOUND', tag='ALTERNATE_BUSINESS_NAME_FOUND')
riskIndicatorCode.DBA_MATCH_PUBLIC_RECORDS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='DBA_MATCH_PUBLIC_RECORDS', tag='DBA_MATCH_PUBLIC_RECORDS')
riskIndicatorCode.SSN_RECENT = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_RECENT', tag='SSN_RECENT')
riskIndicatorCode.SSN_TOO_OLD = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_TOO_OLD', tag='SSN_TOO_OLD')
riskIndicatorCode.TIN_NAME_ADDRESS_MISMATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='TIN_NAME_ADDRESS_MISMATCH', tag='TIN_NAME_ADDRESS_MISMATCH')
riskIndicatorCode.BUSINESS_NOT_IN_GOOD_STANDING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='BUSINESS_NOT_IN_GOOD_STANDING', tag='BUSINESS_NOT_IN_GOOD_STANDING')
riskIndicatorCode.NAME_ADDRESS_MATCH_JUDGMENT = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='NAME_ADDRESS_MATCH_JUDGMENT', tag='NAME_ADDRESS_MATCH_JUDGMENT')
riskIndicatorCode.BUSINESS_INACTIVE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='BUSINESS_INACTIVE', tag='BUSINESS_INACTIVE')
riskIndicatorCode.NO_UPDATE_IN_LAST_THREE_YEARS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='NO_UPDATE_IN_LAST_THREE_YEARS', tag='NO_UPDATE_IN_LAST_THREE_YEARS')
riskIndicatorCode.SSN_NOT_PRIMARY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_NOT_PRIMARY', tag='SSN_NOT_PRIMARY')
riskIndicatorCode.ZIP_CORP_ONLY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ZIP_CORP_ONLY', tag='ZIP_CORP_ONLY')
riskIndicatorCode.ADDRESS_MISMATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_MISMATCH', tag='ADDRESS_MISMATCH')
riskIndicatorCode.DL_DIFFERENT = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='DL_DIFFERENT', tag='DL_DIFFERENT')
riskIndicatorCode.DL_NOT_FOUND = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='DL_NOT_FOUND', tag='DL_NOT_FOUND')
riskIndicatorCode.DL_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='DL_MISKEYED', tag='DL_MISKEYED')
riskIndicatorCode.UNABLE_TO_VERIFY_DL = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='UNABLE_TO_VERIFY_DL', tag='UNABLE_TO_VERIFY_DL')
riskIndicatorCode.SSN_INVALID_SSA = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_INVALID_SSA', tag='SSN_INVALID_SSA')
riskIndicatorCode.SSN_IS_ITIN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_IS_ITIN', tag='SSN_IS_ITIN')
riskIndicatorCode.SSN_MULTI_IDENTITY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_MULTI_IDENTITY', tag='SSN_MULTI_IDENTITY')
riskIndicatorCode.ZIP_MILITARY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ZIP_MILITARY', tag='ZIP_MILITARY')
riskIndicatorCode.MULTIPLE_SSN_FOUND = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='MULTIPLE_SSN_FOUND', tag='MULTIPLE_SSN_FOUND')
riskIndicatorCode.ADDRESS_DISCREPANCY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_DISCREPANCY', tag='ADDRESS_DISCREPANCY')
riskIndicatorCode.ADDRESS_PO_BOX = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_PO_BOX', tag='ADDRESS_PO_BOX')
riskIndicatorCode.SSN_RANDOM_SSA = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='SSN_RANDOM_SSA', tag='SSN_RANDOM_SSA')
riskIndicatorCode.ADDRESS_MISMATCH_SECONDARY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_MISMATCH_SECONDARY', tag='ADDRESS_MISMATCH_SECONDARY')
riskIndicatorCode.NAME_MATCHES_NON_OFAC = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='NAME_MATCHES_NON_OFAC', tag='NAME_MATCHES_NON_OFAC')
riskIndicatorCode.UNABLE_TO_VERIFY_ZIP_CODE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='UNABLE_TO_VERIFY_ZIP_CODE', tag='UNABLE_TO_VERIFY_ZIP_CODE')
riskIndicatorCode.IP_ADDRESS_UNKNOWN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='IP_ADDRESS_UNKNOWN', tag='IP_ADDRESS_UNKNOWN')
riskIndicatorCode.IP_ADDRESS_DIFFERENT_STATE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='IP_ADDRESS_DIFFERENT_STATE', tag='IP_ADDRESS_DIFFERENT_STATE')
riskIndicatorCode.IP_ADDRESS_DIFFERENT_ZIP = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='IP_ADDRESS_DIFFERENT_ZIP', tag='IP_ADDRESS_DIFFERENT_ZIP')
riskIndicatorCode.IP_ADDRESS_DIFFERENT_PHONE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='IP_ADDRESS_DIFFERENT_PHONE', tag='IP_ADDRESS_DIFFERENT_PHONE')
riskIndicatorCode.IP_ADDRESS_DOMAIN_UNKNOWN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='IP_ADDRESS_DOMAIN_UNKNOWN', tag='IP_ADDRESS_DOMAIN_UNKNOWN')
riskIndicatorCode.IP_ADDRESS_NOT_ASSIGNED_TO_USA = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='IP_ADDRESS_NOT_ASSIGNED_TO_USA', tag='IP_ADDRESS_NOT_ASSIGNED_TO_USA')
riskIndicatorCode.IP_ADDRESS_NON_ROUTABLE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value='IP_ADDRESS_NON_ROUTABLE', tag='IP_ADDRESS_NON_ROUTABLE')
riskIndicatorCode._InitializeFacetMap(riskIndicatorCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'riskIndicatorCode', riskIndicatorCode)
_module_typeBindings.riskIndicatorCode = riskIndicatorCode

# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}principalOverallScore
class principalOverallScore (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalOverallScore')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 154, 4)
    _Documentation = None
principalOverallScore._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=principalOverallScore, enum_prefix=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value='0', tag=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value='10', tag=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value='20', tag=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value='30', tag=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value='40', tag=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value='50', tag=None)
principalOverallScore._InitializeFacetMap(principalOverallScore._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'principalOverallScore', principalOverallScore)
_module_typeBindings.principalOverallScore = principalOverallScore

# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}nameAddressSsnAssociationCode
class nameAddressSsnAssociationCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameAddressSsnAssociationCode')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 165, 4)
    _Documentation = None
nameAddressSsnAssociationCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nameAddressSsnAssociationCode, enum_prefix=None)
nameAddressSsnAssociationCode.NOTHING = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='NOTHING', tag='NOTHING')
nameAddressSsnAssociationCode.WRONG_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='WRONG_SSN', tag='WRONG_SSN')
nameAddressSsnAssociationCode.FIRST_LAST = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_LAST', tag='FIRST_LAST')
nameAddressSsnAssociationCode.FIRST_ADDRESS = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_ADDRESS', tag='FIRST_ADDRESS')
nameAddressSsnAssociationCode.FIRST_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_SSN', tag='FIRST_SSN')
nameAddressSsnAssociationCode.LAST_ADDRESS = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='LAST_ADDRESS', tag='LAST_ADDRESS')
nameAddressSsnAssociationCode.ADDRESS_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_SSN', tag='ADDRESS_SSN')
nameAddressSsnAssociationCode.LAST_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='LAST_SSN', tag='LAST_SSN')
nameAddressSsnAssociationCode.FIRST_LAST_ADDRESS = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_LAST_ADDRESS', tag='FIRST_LAST_ADDRESS')
nameAddressSsnAssociationCode.FIRST_LAST_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_LAST_SSN', tag='FIRST_LAST_SSN')
nameAddressSsnAssociationCode.FIRST_ADDRESS_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_ADDRESS_SSN', tag='FIRST_ADDRESS_SSN')
nameAddressSsnAssociationCode.LAST_ADDRESS_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='LAST_ADDRESS_SSN', tag='LAST_ADDRESS_SSN')
nameAddressSsnAssociationCode.FIRST_LAST_ADDRESS_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_LAST_ADDRESS_SSN', tag='FIRST_LAST_ADDRESS_SSN')
nameAddressSsnAssociationCode._InitializeFacetMap(nameAddressSsnAssociationCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'nameAddressSsnAssociationCode', nameAddressSsnAssociationCode)
_module_typeBindings.nameAddressSsnAssociationCode = nameAddressSsnAssociationCode

# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}principalNameAddressPhoneAssociationCode
class principalNameAddressPhoneAssociationCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalNameAddressPhoneAssociationCode')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 183, 4)
    _Documentation = None
principalNameAddressPhoneAssociationCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=principalNameAddressPhoneAssociationCode, enum_prefix=None)
principalNameAddressPhoneAssociationCode.NOTHING = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='NOTHING', tag='NOTHING')
principalNameAddressPhoneAssociationCode.WRONG_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='WRONG_PHONE', tag='WRONG_PHONE')
principalNameAddressPhoneAssociationCode.FIRST_LAST = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_LAST', tag='FIRST_LAST')
principalNameAddressPhoneAssociationCode.FIRST_ADDRESS = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_ADDRESS', tag='FIRST_ADDRESS')
principalNameAddressPhoneAssociationCode.FIRST_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_PHONE', tag='FIRST_PHONE')
principalNameAddressPhoneAssociationCode.LAST_ADDRESS = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='LAST_ADDRESS', tag='LAST_ADDRESS')
principalNameAddressPhoneAssociationCode.ADDRESS_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='ADDRESS_PHONE', tag='ADDRESS_PHONE')
principalNameAddressPhoneAssociationCode.LAST_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='LAST_PHONE', tag='LAST_PHONE')
principalNameAddressPhoneAssociationCode.FIRST_LAST_ADDRESS = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_LAST_ADDRESS', tag='FIRST_LAST_ADDRESS')
principalNameAddressPhoneAssociationCode.FIRST_LAST_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_LAST_PHONE', tag='FIRST_LAST_PHONE')
principalNameAddressPhoneAssociationCode.FIRST_ADDRESS_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_ADDRESS_PHONE', tag='FIRST_ADDRESS_PHONE')
principalNameAddressPhoneAssociationCode.LAST_ADDRESS_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='LAST_ADDRESS_PHONE', tag='LAST_ADDRESS_PHONE')
principalNameAddressPhoneAssociationCode.FIRST_LAST_ADDRESS_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value='FIRST_LAST_ADDRESS_PHONE', tag='FIRST_LAST_ADDRESS_PHONE')
principalNameAddressPhoneAssociationCode._InitializeFacetMap(principalNameAddressPhoneAssociationCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'principalNameAddressPhoneAssociationCode', principalNameAddressPhoneAssociationCode)
_module_typeBindings.principalNameAddressPhoneAssociationCode = principalNameAddressPhoneAssociationCode

# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}businessToPrincipalScore
class businessToPrincipalScore (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'businessToPrincipalScore')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 201, 4)
    _Documentation = None
businessToPrincipalScore._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=businessToPrincipalScore, enum_prefix=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value='0', tag=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value='10', tag=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value='20', tag=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value='30', tag=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value='40', tag=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value='50', tag=None)
businessToPrincipalScore._InitializeFacetMap(businessToPrincipalScore._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'businessToPrincipalScore', businessToPrincipalScore)
_module_typeBindings.businessToPrincipalScore = businessToPrincipalScore

# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreementType
class legalEntityAgreementType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreementType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 212, 4)
    _Documentation = None
legalEntityAgreementType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=legalEntityAgreementType, enum_prefix=None)
legalEntityAgreementType.MERCHANT_AGREEMENT = legalEntityAgreementType._CF_enumeration.addEnumeration(unicode_value='MERCHANT_AGREEMENT', tag='MERCHANT_AGREEMENT')
legalEntityAgreementType._InitializeFacetMap(legalEntityAgreementType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'legalEntityAgreementType', legalEntityAgreementType)
_module_typeBindings.legalEntityAgreementType = legalEntityAgreementType

# Atomic simple type: {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityOwnershipType
class legalEntityOwnershipType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityOwnershipType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 218, 4)
    _Documentation = None
legalEntityOwnershipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=legalEntityOwnershipType, enum_prefix=None)
legalEntityOwnershipType.PUBLIC = legalEntityOwnershipType._CF_enumeration.addEnumeration(unicode_value='PUBLIC', tag='PUBLIC')
legalEntityOwnershipType.PRIVATE = legalEntityOwnershipType._CF_enumeration.addEnumeration(unicode_value='PRIVATE', tag='PRIVATE')
legalEntityOwnershipType._InitializeFacetMap(legalEntityOwnershipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'legalEntityOwnershipType', legalEntityOwnershipType)
_module_typeBindings.legalEntityOwnershipType = legalEntityOwnershipType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 281, 16)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern='\\p{IsBasicLatin}*')
STD_ANON._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern,
   STD_ANON._CF_maxLength,
   STD_ANON._CF_minLength)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 292, 16)
    _Documentation = None
STD_ANON_._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_maxLength,
   STD_ANON_._CF_minLength)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 300, 16)
    _Documentation = None
STD_ANON_2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25))
STD_ANON_2._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_maxLength,
   STD_ANON_2._CF_minLength)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 308, 16)
    _Documentation = None
STD_ANON_3._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
STD_ANON_3._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_maxLength,
   STD_ANON_3._CF_minLength)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 320, 16)
    _Documentation = None
STD_ANON_4._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_4._CF_pattern.addPattern(pattern='[0-9]{0,3}')
STD_ANON_4._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_4._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_pattern,
   STD_ANON_4._CF_maxLength,
   STD_ANON_4._CF_minLength)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 336, 16)
    _Documentation = None
STD_ANON_5._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_5._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_maxLength,
   STD_ANON_5._CF_minLength)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 344, 16)
    _Documentation = None
STD_ANON_6._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_6._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_maxLength,
   STD_ANON_6._CF_minLength)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 352, 16)
    _Documentation = None
STD_ANON_7._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_7._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_maxLength,
   STD_ANON_7._CF_minLength)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 360, 16)
    _Documentation = None
STD_ANON_8._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_8._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_maxLength,
   STD_ANON_8._CF_minLength)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 368, 16)
    _Documentation = None
STD_ANON_9._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(7))
STD_ANON_9._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_maxLength,
   STD_ANON_9._CF_minLength)
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 376, 16)
    _Documentation = None
STD_ANON_10._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_10._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_maxLength,
   STD_ANON_10._CF_minLength)
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 390, 16)
    _Documentation = None
STD_ANON_11._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_11._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_maxLength,
   STD_ANON_11._CF_minLength)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 398, 16)
    _Documentation = None
STD_ANON_12._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_12._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_maxLength,
   STD_ANON_12._CF_minLength)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 406, 16)
    _Documentation = None
STD_ANON_13._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_13._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_maxLength,
   STD_ANON_13._CF_minLength)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 414, 16)
    _Documentation = None
STD_ANON_14._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_14._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_maxLength,
   STD_ANON_14._CF_minLength)
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 422, 16)
    _Documentation = None
STD_ANON_15._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25))
STD_ANON_15._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_maxLength,
   STD_ANON_15._CF_minLength)
_module_typeBindings.STD_ANON_15 = STD_ANON_15

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 430, 16)
    _Documentation = None
STD_ANON_16._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
STD_ANON_16._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_maxLength,
   STD_ANON_16._CF_minLength)
_module_typeBindings.STD_ANON_16 = STD_ANON_16

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 439, 16)
    _Documentation = None
STD_ANON_17._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25))
STD_ANON_17._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_maxLength,
   STD_ANON_17._CF_minLength)
_module_typeBindings.STD_ANON_17 = STD_ANON_17

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 447, 16)
    _Documentation = None
STD_ANON_18._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_18._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_maxLength,
   STD_ANON_18._CF_minLength)
_module_typeBindings.STD_ANON_18 = STD_ANON_18

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 456, 16)
    _Documentation = None
STD_ANON_19._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_19, value=pyxb.binding.datatypes.int(0))
STD_ANON_19._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_19, value=pyxb.binding.datatypes.int(100))
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_minInclusive,
   STD_ANON_19._CF_maxInclusive)
_module_typeBindings.STD_ANON_19 = STD_ANON_19

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 470, 16)
    _Documentation = None
STD_ANON_20._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_20._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_maxLength,
   STD_ANON_20._CF_minLength)
_module_typeBindings.STD_ANON_20 = STD_ANON_20

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 478, 16)
    _Documentation = None
STD_ANON_21._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_21._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_21._InitializeFacetMap(STD_ANON_21._CF_maxLength,
   STD_ANON_21._CF_minLength)
_module_typeBindings.STD_ANON_21 = STD_ANON_21

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 486, 16)
    _Documentation = None
STD_ANON_22._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_22._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_maxLength,
   STD_ANON_22._CF_minLength)
_module_typeBindings.STD_ANON_22 = STD_ANON_22

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 494, 16)
    _Documentation = None
STD_ANON_23._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_23._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_maxLength,
   STD_ANON_23._CF_minLength)
_module_typeBindings.STD_ANON_23 = STD_ANON_23

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 502, 16)
    _Documentation = None
STD_ANON_24._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(7))
STD_ANON_24._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_maxLength,
   STD_ANON_24._CF_minLength)
_module_typeBindings.STD_ANON_24 = STD_ANON_24

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 510, 16)
    _Documentation = None
STD_ANON_25._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_25._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_maxLength,
   STD_ANON_25._CF_minLength)
_module_typeBindings.STD_ANON_25 = STD_ANON_25

# Atomic simple type: [anonymous]
class STD_ANON_26 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 537, 24)
    _Documentation = None
STD_ANON_26._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_26._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_26._InitializeFacetMap(STD_ANON_26._CF_maxLength,
   STD_ANON_26._CF_minLength)
_module_typeBindings.STD_ANON_26 = STD_ANON_26

# Atomic simple type: [anonymous]
class STD_ANON_27 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 546, 24)
    _Documentation = None
STD_ANON_27._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_27._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_27._InitializeFacetMap(STD_ANON_27._CF_maxLength,
   STD_ANON_27._CF_minLength)
_module_typeBindings.STD_ANON_27 = STD_ANON_27

# Atomic simple type: [anonymous]
class STD_ANON_28 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 554, 24)
    _Documentation = None
STD_ANON_28._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_28._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_maxLength,
   STD_ANON_28._CF_minLength)
_module_typeBindings.STD_ANON_28 = STD_ANON_28

# Atomic simple type: [anonymous]
class STD_ANON_29 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 562, 24)
    _Documentation = None
STD_ANON_29._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_29._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_29._InitializeFacetMap(STD_ANON_29._CF_maxLength,
   STD_ANON_29._CF_minLength)
_module_typeBindings.STD_ANON_29 = STD_ANON_29

# Atomic simple type: [anonymous]
class STD_ANON_30 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 597, 24)
    _Documentation = None
STD_ANON_30._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_30._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_30._InitializeFacetMap(STD_ANON_30._CF_maxLength,
   STD_ANON_30._CF_minLength)
_module_typeBindings.STD_ANON_30 = STD_ANON_30

# Atomic simple type: [anonymous]
class STD_ANON_31 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 605, 24)
    _Documentation = None
STD_ANON_31._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_31._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_31._InitializeFacetMap(STD_ANON_31._CF_maxLength,
   STD_ANON_31._CF_minLength)
_module_typeBindings.STD_ANON_31 = STD_ANON_31

# Atomic simple type: [anonymous]
class STD_ANON_32 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 623, 24)
    _Documentation = None
STD_ANON_32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_32._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_32._InitializeFacetMap(STD_ANON_32._CF_maxLength,
   STD_ANON_32._CF_minLength)
_module_typeBindings.STD_ANON_32 = STD_ANON_32

# Atomic simple type: [anonymous]
class STD_ANON_33 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 632, 24)
    _Documentation = None
STD_ANON_33._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_33._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_33._InitializeFacetMap(STD_ANON_33._CF_maxLength,
   STD_ANON_33._CF_minLength)
_module_typeBindings.STD_ANON_33 = STD_ANON_33

# Atomic simple type: [anonymous]
class STD_ANON_34 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 641, 24)
    _Documentation = None
STD_ANON_34._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_34._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_34._InitializeFacetMap(STD_ANON_34._CF_maxLength,
   STD_ANON_34._CF_minLength)
_module_typeBindings.STD_ANON_34 = STD_ANON_34

# Atomic simple type: [anonymous]
class STD_ANON_35 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 651, 24)
    _Documentation = None
STD_ANON_35._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_35._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_35._InitializeFacetMap(STD_ANON_35._CF_maxLength,
   STD_ANON_35._CF_minLength)
_module_typeBindings.STD_ANON_35 = STD_ANON_35

# Atomic simple type: [anonymous]
class STD_ANON_36 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 661, 20)
    _Documentation = None
STD_ANON_36._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_36._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_36._InitializeFacetMap(STD_ANON_36._CF_maxLength,
   STD_ANON_36._CF_minLength)
_module_typeBindings.STD_ANON_36 = STD_ANON_36

# Atomic simple type: [anonymous]
class STD_ANON_37 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 678, 16)
    _Documentation = None
STD_ANON_37._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2000))
STD_ANON_37._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_37._InitializeFacetMap(STD_ANON_37._CF_maxLength,
   STD_ANON_37._CF_minLength)
_module_typeBindings.STD_ANON_37 = STD_ANON_37

# Atomic simple type: [anonymous]
class STD_ANON_38 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 716, 16)
    _Documentation = None
STD_ANON_38._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(110))
STD_ANON_38._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_38._InitializeFacetMap(STD_ANON_38._CF_maxLength,
   STD_ANON_38._CF_minLength)
_module_typeBindings.STD_ANON_38 = STD_ANON_38

# Atomic simple type: [anonymous]
class STD_ANON_39 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 730, 16)
    _Documentation = None
STD_ANON_39._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120))
STD_ANON_39._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_39._InitializeFacetMap(STD_ANON_39._CF_maxLength,
   STD_ANON_39._CF_minLength)
_module_typeBindings.STD_ANON_39 = STD_ANON_39

# Atomic simple type: [anonymous]
class STD_ANON_40 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 744, 16)
    _Documentation = None
STD_ANON_40._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120))
STD_ANON_40._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_40._InitializeFacetMap(STD_ANON_40._CF_maxLength,
   STD_ANON_40._CF_minLength)
_module_typeBindings.STD_ANON_40 = STD_ANON_40

# Atomic simple type: [anonymous]
class STD_ANON_41 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 770, 16)
    _Documentation = None
STD_ANON_41._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120))
STD_ANON_41._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_41._InitializeFacetMap(STD_ANON_41._CF_maxLength,
   STD_ANON_41._CF_minLength)
_module_typeBindings.STD_ANON_41 = STD_ANON_41

# Atomic simple type: [anonymous]
class STD_ANON_42 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 784, 16)
    _Documentation = None
STD_ANON_42._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2000))
STD_ANON_42._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_42._InitializeFacetMap(STD_ANON_42._CF_maxLength,
   STD_ANON_42._CF_minLength)
_module_typeBindings.STD_ANON_42 = STD_ANON_42

# Atomic simple type: [anonymous]
class STD_ANON_43 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 814, 16)
    _Documentation = None
STD_ANON_43._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(200))
STD_ANON_43._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_43._InitializeFacetMap(STD_ANON_43._CF_maxLength,
   STD_ANON_43._CF_minLength)
_module_typeBindings.STD_ANON_43 = STD_ANON_43

# Atomic simple type: [anonymous]
class STD_ANON_44 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 828, 16)
    _Documentation = None
STD_ANON_44._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_44._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_44._InitializeFacetMap(STD_ANON_44._CF_maxLength,
   STD_ANON_44._CF_minLength)
_module_typeBindings.STD_ANON_44 = STD_ANON_44

# Atomic simple type: [anonymous]
class STD_ANON_45 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 842, 16)
    _Documentation = None
STD_ANON_45._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_45._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_45._InitializeFacetMap(STD_ANON_45._CF_maxLength,
   STD_ANON_45._CF_minLength)
_module_typeBindings.STD_ANON_45 = STD_ANON_45

# Atomic simple type: [anonymous]
class STD_ANON_46 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 866, 16)
    _Documentation = None
STD_ANON_46._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(95))
STD_ANON_46._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_46._InitializeFacetMap(STD_ANON_46._CF_maxLength,
   STD_ANON_46._CF_minLength)
_module_typeBindings.STD_ANON_46 = STD_ANON_46

# Atomic simple type: [anonymous]
class STD_ANON_47 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 879, 16)
    _Documentation = None
STD_ANON_47._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
STD_ANON_47._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_47._InitializeFacetMap(STD_ANON_47._CF_maxLength,
   STD_ANON_47._CF_minLength)
_module_typeBindings.STD_ANON_47 = STD_ANON_47

# Atomic simple type: [anonymous]
class STD_ANON_48 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 888, 16)
    _Documentation = None
STD_ANON_48._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120))
STD_ANON_48._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_48._InitializeFacetMap(STD_ANON_48._CF_maxLength,
   STD_ANON_48._CF_minLength)
_module_typeBindings.STD_ANON_48 = STD_ANON_48

# Atomic simple type: [anonymous]
class STD_ANON_49 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 896, 16)
    _Documentation = None
STD_ANON_49._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_49._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_49._InitializeFacetMap(STD_ANON_49._CF_maxLength,
   STD_ANON_49._CF_minLength)
_module_typeBindings.STD_ANON_49 = STD_ANON_49

# Atomic simple type: [anonymous]
class STD_ANON_50 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 904, 16)
    _Documentation = None
STD_ANON_50._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_50._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_50._InitializeFacetMap(STD_ANON_50._CF_maxLength,
   STD_ANON_50._CF_minLength)
_module_typeBindings.STD_ANON_50 = STD_ANON_50

# Atomic simple type: [anonymous]
class STD_ANON_51 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 912, 16)
    _Documentation = None
STD_ANON_51._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
STD_ANON_51._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_51._InitializeFacetMap(STD_ANON_51._CF_maxLength,
   STD_ANON_51._CF_minLength)
_module_typeBindings.STD_ANON_51 = STD_ANON_51

# Atomic simple type: [anonymous]
class STD_ANON_52 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 920, 16)
    _Documentation = None
STD_ANON_52._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_52._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_52._InitializeFacetMap(STD_ANON_52._CF_maxLength,
   STD_ANON_52._CF_minLength)
_module_typeBindings.STD_ANON_52 = STD_ANON_52

# Atomic simple type: [anonymous]
class STD_ANON_53 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 928, 16)
    _Documentation = None
STD_ANON_53._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
STD_ANON_53._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_53._InitializeFacetMap(STD_ANON_53._CF_maxLength,
   STD_ANON_53._CF_minLength)
_module_typeBindings.STD_ANON_53 = STD_ANON_53

# Atomic simple type: [anonymous]
class STD_ANON_54 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 936, 16)
    _Documentation = None
STD_ANON_54._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_54._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_54._InitializeFacetMap(STD_ANON_54._CF_maxLength,
   STD_ANON_54._CF_minLength)
_module_typeBindings.STD_ANON_54 = STD_ANON_54

# Atomic simple type: [anonymous]
class STD_ANON_55 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 950, 16)
    _Documentation = None
STD_ANON_55._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_55._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_55._InitializeFacetMap(STD_ANON_55._CF_maxLength,
   STD_ANON_55._CF_minLength)
_module_typeBindings.STD_ANON_55 = STD_ANON_55

# Atomic simple type: [anonymous]
class STD_ANON_56 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 960, 16)
    _Documentation = None
STD_ANON_56._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120))
STD_ANON_56._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_56._InitializeFacetMap(STD_ANON_56._CF_maxLength,
   STD_ANON_56._CF_minLength)
_module_typeBindings.STD_ANON_56 = STD_ANON_56

# Atomic simple type: [anonymous]
class STD_ANON_57 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 968, 16)
    _Documentation = None
STD_ANON_57._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_57._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_57._InitializeFacetMap(STD_ANON_57._CF_maxLength,
   STD_ANON_57._CF_minLength)
_module_typeBindings.STD_ANON_57 = STD_ANON_57

# Atomic simple type: [anonymous]
class STD_ANON_58 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 976, 16)
    _Documentation = None
STD_ANON_58._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_58._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_58._InitializeFacetMap(STD_ANON_58._CF_maxLength,
   STD_ANON_58._CF_minLength)
_module_typeBindings.STD_ANON_58 = STD_ANON_58

# Atomic simple type: [anonymous]
class STD_ANON_59 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 984, 16)
    _Documentation = None
STD_ANON_59._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
STD_ANON_59._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_59._InitializeFacetMap(STD_ANON_59._CF_maxLength,
   STD_ANON_59._CF_minLength)
_module_typeBindings.STD_ANON_59 = STD_ANON_59

# Atomic simple type: [anonymous]
class STD_ANON_60 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 992, 16)
    _Documentation = None
STD_ANON_60._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_60._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_60._InitializeFacetMap(STD_ANON_60._CF_maxLength,
   STD_ANON_60._CF_minLength)
_module_typeBindings.STD_ANON_60 = STD_ANON_60

# Atomic simple type: [anonymous]
class STD_ANON_61 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1000, 16)
    _Documentation = None
STD_ANON_61._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
STD_ANON_61._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_61._InitializeFacetMap(STD_ANON_61._CF_maxLength,
   STD_ANON_61._CF_minLength)
_module_typeBindings.STD_ANON_61 = STD_ANON_61

# Atomic simple type: [anonymous]
class STD_ANON_62 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1008, 16)
    _Documentation = None
STD_ANON_62._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_62._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_62._InitializeFacetMap(STD_ANON_62._CF_maxLength,
   STD_ANON_62._CF_minLength)
_module_typeBindings.STD_ANON_62 = STD_ANON_62

# Atomic simple type: [anonymous]
class STD_ANON_63 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1023, 16)
    _Documentation = None
STD_ANON_63._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
STD_ANON_63._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_63._InitializeFacetMap(STD_ANON_63._CF_maxLength,
   STD_ANON_63._CF_minLength)
_module_typeBindings.STD_ANON_63 = STD_ANON_63

# Atomic simple type: [anonymous]
class STD_ANON_64 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1031, 16)
    _Documentation = None
STD_ANON_64._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_64._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_64._InitializeFacetMap(STD_ANON_64._CF_maxLength,
   STD_ANON_64._CF_minLength)
_module_typeBindings.STD_ANON_64 = STD_ANON_64

# Atomic simple type: [anonymous]
class STD_ANON_65 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1044, 16)
    _Documentation = None
STD_ANON_65._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_65._CF_pattern.addPattern(pattern='[0-9]{0,3}')
STD_ANON_65._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_65._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
STD_ANON_65._InitializeFacetMap(STD_ANON_65._CF_pattern,
   STD_ANON_65._CF_maxLength,
   STD_ANON_65._CF_minLength)
_module_typeBindings.STD_ANON_65 = STD_ANON_65

# Atomic simple type: [anonymous]
class STD_ANON_66 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1058, 16)
    _Documentation = None
STD_ANON_66._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_66._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_66._InitializeFacetMap(STD_ANON_66._CF_maxLength,
   STD_ANON_66._CF_minLength)
_module_typeBindings.STD_ANON_66 = STD_ANON_66

# Atomic simple type: [anonymous]
class STD_ANON_67 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1066, 16)
    _Documentation = None
STD_ANON_67._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_67._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_67._InitializeFacetMap(STD_ANON_67._CF_maxLength,
   STD_ANON_67._CF_minLength)
_module_typeBindings.STD_ANON_67 = STD_ANON_67

# Atomic simple type: [anonymous]
class STD_ANON_68 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1074, 16)
    _Documentation = None
STD_ANON_68._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_68._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_68._InitializeFacetMap(STD_ANON_68._CF_maxLength,
   STD_ANON_68._CF_minLength)
_module_typeBindings.STD_ANON_68 = STD_ANON_68

# Atomic simple type: [anonymous]
class STD_ANON_69 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1082, 16)
    _Documentation = None
STD_ANON_69._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_69._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_69._InitializeFacetMap(STD_ANON_69._CF_maxLength,
   STD_ANON_69._CF_minLength)
_module_typeBindings.STD_ANON_69 = STD_ANON_69

# Atomic simple type: [anonymous]
class STD_ANON_70 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1090, 16)
    _Documentation = None
STD_ANON_70._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(7))
STD_ANON_70._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_70._InitializeFacetMap(STD_ANON_70._CF_maxLength,
   STD_ANON_70._CF_minLength)
_module_typeBindings.STD_ANON_70 = STD_ANON_70

# Atomic simple type: [anonymous]
class STD_ANON_71 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1098, 16)
    _Documentation = None
STD_ANON_71._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_71._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_71._InitializeFacetMap(STD_ANON_71._CF_maxLength,
   STD_ANON_71._CF_minLength)
_module_typeBindings.STD_ANON_71 = STD_ANON_71

# Atomic simple type: [anonymous]
class STD_ANON_72 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1112, 16)
    _Documentation = None
STD_ANON_72._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_72._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
STD_ANON_72._InitializeFacetMap(STD_ANON_72._CF_maxLength,
   STD_ANON_72._CF_minLength)
_module_typeBindings.STD_ANON_72 = STD_ANON_72

# Atomic simple type: [anonymous]
class STD_ANON_73 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1120, 16)
    _Documentation = None
STD_ANON_73._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_73._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_73._InitializeFacetMap(STD_ANON_73._CF_maxLength,
   STD_ANON_73._CF_minLength)
_module_typeBindings.STD_ANON_73 = STD_ANON_73

# Atomic simple type: [anonymous]
class STD_ANON_74 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1128, 16)
    _Documentation = None
STD_ANON_74._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13))
STD_ANON_74._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_74._InitializeFacetMap(STD_ANON_74._CF_maxLength,
   STD_ANON_74._CF_minLength)
_module_typeBindings.STD_ANON_74 = STD_ANON_74

# Atomic simple type: [anonymous]
class STD_ANON_75 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1137, 16)
    _Documentation = None
STD_ANON_75._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_75, value=pyxb.binding.datatypes.int(0))
STD_ANON_75._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_75, value=pyxb.binding.datatypes.int(100))
STD_ANON_75._InitializeFacetMap(STD_ANON_75._CF_minInclusive,
   STD_ANON_75._CF_maxInclusive)
_module_typeBindings.STD_ANON_75 = STD_ANON_75

# Atomic simple type: [anonymous]
class STD_ANON_76 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1151, 16)
    _Documentation = None
STD_ANON_76._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_76._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_76._InitializeFacetMap(STD_ANON_76._CF_maxLength,
   STD_ANON_76._CF_minLength)
_module_typeBindings.STD_ANON_76 = STD_ANON_76

# Atomic simple type: [anonymous]
class STD_ANON_77 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1159, 16)
    _Documentation = None
STD_ANON_77._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_77._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_77._InitializeFacetMap(STD_ANON_77._CF_maxLength,
   STD_ANON_77._CF_minLength)
_module_typeBindings.STD_ANON_77 = STD_ANON_77

# Atomic simple type: [anonymous]
class STD_ANON_78 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1167, 16)
    _Documentation = None
STD_ANON_78._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25))
STD_ANON_78._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
STD_ANON_78._InitializeFacetMap(STD_ANON_78._CF_maxLength,
   STD_ANON_78._CF_minLength)
_module_typeBindings.STD_ANON_78 = STD_ANON_78

# Atomic simple type: [anonymous]
class STD_ANON_79 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1176, 16)
    _Documentation = None
STD_ANON_79._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25))
STD_ANON_79._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_79._InitializeFacetMap(STD_ANON_79._CF_maxLength,
   STD_ANON_79._CF_minLength)
_module_typeBindings.STD_ANON_79 = STD_ANON_79

# Atomic simple type: [anonymous]
class STD_ANON_80 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1184, 16)
    _Documentation = None
STD_ANON_80._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
STD_ANON_80._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_80._InitializeFacetMap(STD_ANON_80._CF_maxLength,
   STD_ANON_80._CF_minLength)
_module_typeBindings.STD_ANON_80 = STD_ANON_80

# Atomic simple type: [anonymous]
class STD_ANON_81 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1197, 16)
    _Documentation = None
STD_ANON_81._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_81._CF_pattern.addPattern(pattern='\\p{IsBasicLatin}*')
STD_ANON_81._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
STD_ANON_81._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_81._InitializeFacetMap(STD_ANON_81._CF_pattern,
   STD_ANON_81._CF_maxLength,
   STD_ANON_81._CF_minLength)
_module_typeBindings.STD_ANON_81 = STD_ANON_81

# Atomic simple type: [anonymous]
class STD_ANON_82 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1207, 16)
    _Documentation = None
STD_ANON_82._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25))
STD_ANON_82._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
STD_ANON_82._InitializeFacetMap(STD_ANON_82._CF_maxLength,
   STD_ANON_82._CF_minLength)
_module_typeBindings.STD_ANON_82 = STD_ANON_82

# Atomic simple type: [anonymous]
class STD_ANON_83 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1220, 16)
    _Documentation = None
STD_ANON_83._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_83._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_83._InitializeFacetMap(STD_ANON_83._CF_maxLength,
   STD_ANON_83._CF_minLength)
_module_typeBindings.STD_ANON_83 = STD_ANON_83

# Atomic simple type: [anonymous]
class STD_ANON_84 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1228, 16)
    _Documentation = None
STD_ANON_84._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
STD_ANON_84._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_84._InitializeFacetMap(STD_ANON_84._CF_maxLength,
   STD_ANON_84._CF_minLength)
_module_typeBindings.STD_ANON_84 = STD_ANON_84

# Atomic simple type: [anonymous]
class STD_ANON_85 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1236, 16)
    _Documentation = None
STD_ANON_85._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
STD_ANON_85._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_85._InitializeFacetMap(STD_ANON_85._CF_maxLength,
   STD_ANON_85._CF_minLength)
_module_typeBindings.STD_ANON_85 = STD_ANON_85

# Atomic simple type: [anonymous]
class STD_ANON_86 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1244, 16)
    _Documentation = None
STD_ANON_86._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120))
STD_ANON_86._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_86._InitializeFacetMap(STD_ANON_86._CF_maxLength,
   STD_ANON_86._CF_minLength)
_module_typeBindings.STD_ANON_86 = STD_ANON_86

# Atomic simple type: [anonymous]
class STD_ANON_87 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1252, 16)
    _Documentation = None
STD_ANON_87._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13))
STD_ANON_87._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_87._InitializeFacetMap(STD_ANON_87._CF_maxLength,
   STD_ANON_87._CF_minLength)
_module_typeBindings.STD_ANON_87 = STD_ANON_87

# Atomic simple type: [anonymous]
class STD_ANON_88 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1260, 16)
    _Documentation = None
STD_ANON_88._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25))
STD_ANON_88._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_88._InitializeFacetMap(STD_ANON_88._CF_maxLength,
   STD_ANON_88._CF_minLength)
_module_typeBindings.STD_ANON_88 = STD_ANON_88

# Atomic simple type: [anonymous]
class STD_ANON_89 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1268, 16)
    _Documentation = None
STD_ANON_89._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12))
STD_ANON_89._InitializeFacetMap(STD_ANON_89._CF_totalDigits)
_module_typeBindings.STD_ANON_89 = STD_ANON_89

# Atomic simple type: [anonymous]
class STD_ANON_90 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1275, 16)
    _Documentation = None
STD_ANON_90._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_90._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_90._InitializeFacetMap(STD_ANON_90._CF_maxLength,
   STD_ANON_90._CF_minLength)
_module_typeBindings.STD_ANON_90 = STD_ANON_90

# Atomic simple type: [anonymous]
class STD_ANON_91 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1283, 16)
    _Documentation = None
STD_ANON_91._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
STD_ANON_91._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_91._InitializeFacetMap(STD_ANON_91._CF_maxLength,
   STD_ANON_91._CF_minLength)
_module_typeBindings.STD_ANON_91 = STD_ANON_91

# Atomic simple type: [anonymous]
class STD_ANON_92 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1293, 16)
    _Documentation = None
STD_ANON_92._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_92._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_92._InitializeFacetMap(STD_ANON_92._CF_maxLength,
   STD_ANON_92._CF_minLength)
_module_typeBindings.STD_ANON_92 = STD_ANON_92

# Atomic simple type: [anonymous]
class STD_ANON_93 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1301, 16)
    _Documentation = None
STD_ANON_93._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_93._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_93._InitializeFacetMap(STD_ANON_93._CF_maxLength,
   STD_ANON_93._CF_minLength)
_module_typeBindings.STD_ANON_93 = STD_ANON_93

# Atomic simple type: [anonymous]
class STD_ANON_94 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1309, 16)
    _Documentation = None
STD_ANON_94._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
STD_ANON_94._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_94._InitializeFacetMap(STD_ANON_94._CF_maxLength,
   STD_ANON_94._CF_minLength)
_module_typeBindings.STD_ANON_94 = STD_ANON_94

# Atomic simple type: [anonymous]
class STD_ANON_95 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1324, 16)
    _Documentation = None
STD_ANON_95._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_95._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_95._InitializeFacetMap(STD_ANON_95._CF_maxLength,
   STD_ANON_95._CF_minLength)
_module_typeBindings.STD_ANON_95 = STD_ANON_95

# Atomic simple type: [anonymous]
class STD_ANON_96 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1347, 16)
    _Documentation = None
STD_ANON_96._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_96._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_96._InitializeFacetMap(STD_ANON_96._CF_maxLength,
   STD_ANON_96._CF_minLength)
_module_typeBindings.STD_ANON_96 = STD_ANON_96

# Atomic simple type: [anonymous]
class STD_ANON_97 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1355, 16)
    _Documentation = None
STD_ANON_97._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_97._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_97._InitializeFacetMap(STD_ANON_97._CF_maxLength,
   STD_ANON_97._CF_minLength)
_module_typeBindings.STD_ANON_97 = STD_ANON_97

# Atomic simple type: [anonymous]
class STD_ANON_98 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1363, 16)
    _Documentation = None
STD_ANON_98._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_98._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_98._InitializeFacetMap(STD_ANON_98._CF_maxLength,
   STD_ANON_98._CF_minLength)
_module_typeBindings.STD_ANON_98 = STD_ANON_98

# Atomic simple type: [anonymous]
class STD_ANON_99 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1371, 16)
    _Documentation = None
STD_ANON_99._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13))
STD_ANON_99._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_99._InitializeFacetMap(STD_ANON_99._CF_maxLength,
   STD_ANON_99._CF_minLength)
_module_typeBindings.STD_ANON_99 = STD_ANON_99

# Atomic simple type: [anonymous]
class STD_ANON_100 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1384, 16)
    _Documentation = None
STD_ANON_100._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
STD_ANON_100._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_100._InitializeFacetMap(STD_ANON_100._CF_maxLength,
   STD_ANON_100._CF_minLength)
_module_typeBindings.STD_ANON_100 = STD_ANON_100

# Atomic simple type: [anonymous]
class STD_ANON_101 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1392, 16)
    _Documentation = None
STD_ANON_101._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
STD_ANON_101._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_101._InitializeFacetMap(STD_ANON_101._CF_maxLength,
   STD_ANON_101._CF_minLength)
_module_typeBindings.STD_ANON_101 = STD_ANON_101

# Atomic simple type: [anonymous]
class STD_ANON_102 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1406, 16)
    _Documentation = None
STD_ANON_102._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
STD_ANON_102._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_102._InitializeFacetMap(STD_ANON_102._CF_maxLength,
   STD_ANON_102._CF_minLength)
_module_typeBindings.STD_ANON_102 = STD_ANON_102

# Atomic simple type: [anonymous]
class STD_ANON_103 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1414, 16)
    _Documentation = None
STD_ANON_103._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
STD_ANON_103._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_103._InitializeFacetMap(STD_ANON_103._CF_maxLength,
   STD_ANON_103._CF_minLength)
_module_typeBindings.STD_ANON_103 = STD_ANON_103

# Atomic simple type: [anonymous]
class STD_ANON_104 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1430, 24)
    _Documentation = None
STD_ANON_104._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_104._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_104._InitializeFacetMap(STD_ANON_104._CF_maxLength,
   STD_ANON_104._CF_minLength)
_module_typeBindings.STD_ANON_104 = STD_ANON_104

# Atomic simple type: [anonymous]
class STD_ANON_105 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1438, 24)
    _Documentation = None
STD_ANON_105._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_105._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_105._InitializeFacetMap(STD_ANON_105._CF_maxLength,
   STD_ANON_105._CF_minLength)
_module_typeBindings.STD_ANON_105 = STD_ANON_105

# Atomic simple type: [anonymous]
class STD_ANON_106 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1455, 24)
    _Documentation = None
STD_ANON_106._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
STD_ANON_106._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_106._InitializeFacetMap(STD_ANON_106._CF_maxLength,
   STD_ANON_106._CF_minLength)
_module_typeBindings.STD_ANON_106 = STD_ANON_106

# Atomic simple type: [anonymous]
class STD_ANON_107 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1473, 24)
    _Documentation = None
STD_ANON_107._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_107._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_107._InitializeFacetMap(STD_ANON_107._CF_maxLength,
   STD_ANON_107._CF_minLength)
_module_typeBindings.STD_ANON_107 = STD_ANON_107

# Atomic simple type: [anonymous]
class STD_ANON_108 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1481, 24)
    _Documentation = None
STD_ANON_108._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
STD_ANON_108._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_108._InitializeFacetMap(STD_ANON_108._CF_maxLength,
   STD_ANON_108._CF_minLength)
_module_typeBindings.STD_ANON_108 = STD_ANON_108

# Atomic simple type: [anonymous]
class STD_ANON_109 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1490, 24)
    _Documentation = None
STD_ANON_109._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_109._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_109._InitializeFacetMap(STD_ANON_109._CF_maxLength,
   STD_ANON_109._CF_minLength)
_module_typeBindings.STD_ANON_109 = STD_ANON_109

# Atomic simple type: [anonymous]
class STD_ANON_110 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1498, 24)
    _Documentation = None
STD_ANON_110._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_110._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_110._InitializeFacetMap(STD_ANON_110._CF_maxLength,
   STD_ANON_110._CF_minLength)
_module_typeBindings.STD_ANON_110 = STD_ANON_110

# Atomic simple type: [anonymous]
class STD_ANON_111 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1522, 16)
    _Documentation = None
STD_ANON_111._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(72))
STD_ANON_111._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_111._InitializeFacetMap(STD_ANON_111._CF_maxLength,
   STD_ANON_111._CF_minLength)
_module_typeBindings.STD_ANON_111 = STD_ANON_111

# Atomic simple type: [anonymous]
class STD_ANON_112 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1530, 16)
    _Documentation = None
STD_ANON_112._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(72))
STD_ANON_112._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_112._InitializeFacetMap(STD_ANON_112._CF_maxLength,
   STD_ANON_112._CF_minLength)
_module_typeBindings.STD_ANON_112 = STD_ANON_112

# Atomic simple type: [anonymous]
class STD_ANON_113 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1544, 16)
    _Documentation = None
STD_ANON_113._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(72))
STD_ANON_113._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_113._InitializeFacetMap(STD_ANON_113._CF_maxLength,
   STD_ANON_113._CF_minLength)
_module_typeBindings.STD_ANON_113 = STD_ANON_113

# Atomic simple type: [anonymous]
class STD_ANON_114 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1552, 16)
    _Documentation = None
STD_ANON_114._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_114._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_114._InitializeFacetMap(STD_ANON_114._CF_maxLength,
   STD_ANON_114._CF_minLength)
_module_typeBindings.STD_ANON_114 = STD_ANON_114

# Atomic simple type: [anonymous]
class STD_ANON_115 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1565, 16)
    _Documentation = None
STD_ANON_115._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_115._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_115._InitializeFacetMap(STD_ANON_115._CF_maxLength,
   STD_ANON_115._CF_minLength)
_module_typeBindings.STD_ANON_115 = STD_ANON_115

# Atomic simple type: [anonymous]
class STD_ANON_116 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1573, 16)
    _Documentation = None
STD_ANON_116._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
STD_ANON_116._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_116._InitializeFacetMap(STD_ANON_116._CF_maxLength,
   STD_ANON_116._CF_minLength)
_module_typeBindings.STD_ANON_116 = STD_ANON_116

# Atomic simple type: [anonymous]
class STD_ANON_117 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1581, 16)
    _Documentation = None
STD_ANON_117._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
STD_ANON_117._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_117._InitializeFacetMap(STD_ANON_117._CF_maxLength,
   STD_ANON_117._CF_minLength)
_module_typeBindings.STD_ANON_117 = STD_ANON_117

# Atomic simple type: [anonymous]
class STD_ANON_118 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1589, 16)
    _Documentation = None
STD_ANON_118._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120))
STD_ANON_118._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_118._InitializeFacetMap(STD_ANON_118._CF_maxLength,
   STD_ANON_118._CF_minLength)
_module_typeBindings.STD_ANON_118 = STD_ANON_118

# Atomic simple type: [anonymous]
class STD_ANON_119 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1597, 16)
    _Documentation = None
STD_ANON_119._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13))
STD_ANON_119._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_119._InitializeFacetMap(STD_ANON_119._CF_maxLength,
   STD_ANON_119._CF_minLength)
_module_typeBindings.STD_ANON_119 = STD_ANON_119

# Atomic simple type: [anonymous]
class STD_ANON_120 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1605, 16)
    _Documentation = None
STD_ANON_120._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25))
STD_ANON_120._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_120._InitializeFacetMap(STD_ANON_120._CF_maxLength,
   STD_ANON_120._CF_minLength)
_module_typeBindings.STD_ANON_120 = STD_ANON_120

# Atomic simple type: [anonymous]
class STD_ANON_121 (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1613, 16)
    _Documentation = None
STD_ANON_121._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(12))
STD_ANON_121._InitializeFacetMap(STD_ANON_121._CF_totalDigits)
_module_typeBindings.STD_ANON_121 = STD_ANON_121

# Atomic simple type: [anonymous]
class STD_ANON_122 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1620, 16)
    _Documentation = None
STD_ANON_122._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_122._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_122._InitializeFacetMap(STD_ANON_122._CF_maxLength,
   STD_ANON_122._CF_minLength)
_module_typeBindings.STD_ANON_122 = STD_ANON_122

# Atomic simple type: [anonymous]
class STD_ANON_123 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1628, 16)
    _Documentation = None
STD_ANON_123._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_123._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_123._InitializeFacetMap(STD_ANON_123._CF_maxLength,
   STD_ANON_123._CF_minLength)
_module_typeBindings.STD_ANON_123 = STD_ANON_123

# Atomic simple type: [anonymous]
class STD_ANON_124 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1636, 16)
    _Documentation = None
STD_ANON_124._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32))
STD_ANON_124._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_124._InitializeFacetMap(STD_ANON_124._CF_maxLength,
   STD_ANON_124._CF_minLength)
_module_typeBindings.STD_ANON_124 = STD_ANON_124

# Atomic simple type: [anonymous]
class STD_ANON_125 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1644, 16)
    _Documentation = None
STD_ANON_125._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_125._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
STD_ANON_125._InitializeFacetMap(STD_ANON_125._CF_maxLength,
   STD_ANON_125._CF_minLength)
_module_typeBindings.STD_ANON_125 = STD_ANON_125

# Atomic simple type: [anonymous]
class STD_ANON_126 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1666, 16)
    _Documentation = None
STD_ANON_126._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_126._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_126._InitializeFacetMap(STD_ANON_126._CF_maxLength,
   STD_ANON_126._CF_minLength)
_module_typeBindings.STD_ANON_126 = STD_ANON_126

# Atomic simple type: [anonymous]
class STD_ANON_127 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1674, 16)
    _Documentation = None
STD_ANON_127._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_127._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_127._InitializeFacetMap(STD_ANON_127._CF_maxLength,
   STD_ANON_127._CF_minLength)
_module_typeBindings.STD_ANON_127 = STD_ANON_127

# Atomic simple type: [anonymous]
class STD_ANON_128 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1682, 16)
    _Documentation = None
STD_ANON_128._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_128._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_128._InitializeFacetMap(STD_ANON_128._CF_maxLength,
   STD_ANON_128._CF_minLength)
_module_typeBindings.STD_ANON_128 = STD_ANON_128

# Atomic simple type: [anonymous]
class STD_ANON_129 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1690, 16)
    _Documentation = None
STD_ANON_129._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13))
STD_ANON_129._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_129._InitializeFacetMap(STD_ANON_129._CF_maxLength,
   STD_ANON_129._CF_minLength)
_module_typeBindings.STD_ANON_129 = STD_ANON_129

# Atomic simple type: [anonymous]
class STD_ANON_130 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1743, 16)
    _Documentation = None
STD_ANON_130._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_130._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_130._InitializeFacetMap(STD_ANON_130._CF_maxLength,
   STD_ANON_130._CF_minLength)
_module_typeBindings.STD_ANON_130 = STD_ANON_130

# Atomic simple type: [anonymous]
class STD_ANON_131 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1751, 16)
    _Documentation = None
STD_ANON_131._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_131._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_131._InitializeFacetMap(STD_ANON_131._CF_maxLength,
   STD_ANON_131._CF_minLength)
_module_typeBindings.STD_ANON_131 = STD_ANON_131

# Atomic simple type: [anonymous]
class STD_ANON_132 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1759, 16)
    _Documentation = None
STD_ANON_132._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
STD_ANON_132._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_132._InitializeFacetMap(STD_ANON_132._CF_maxLength,
   STD_ANON_132._CF_minLength)
_module_typeBindings.STD_ANON_132 = STD_ANON_132

# Atomic simple type: [anonymous]
class STD_ANON_133 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1767, 16)
    _Documentation = None
STD_ANON_133._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_133._CF_pattern.addPattern(pattern='([a-zA-Z0-9.:])*')
STD_ANON_133._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
STD_ANON_133._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_133._InitializeFacetMap(STD_ANON_133._CF_pattern,
   STD_ANON_133._CF_maxLength,
   STD_ANON_133._CF_minLength)
_module_typeBindings.STD_ANON_133 = STD_ANON_133

# Atomic simple type: [anonymous]
class STD_ANON_134 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1791, 16)
    _Documentation = None
STD_ANON_134._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_134._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_134._InitializeFacetMap(STD_ANON_134._CF_maxLength,
   STD_ANON_134._CF_minLength)
_module_typeBindings.STD_ANON_134 = STD_ANON_134

# Atomic simple type: [anonymous]
class STD_ANON_135 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1815, 24)
    _Documentation = None
STD_ANON_135._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_135._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_135._InitializeFacetMap(STD_ANON_135._CF_maxLength,
   STD_ANON_135._CF_minLength)
_module_typeBindings.STD_ANON_135 = STD_ANON_135

# Atomic simple type: [anonymous]
class STD_ANON_136 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1824, 24)
    _Documentation = None
STD_ANON_136._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_136._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_136._InitializeFacetMap(STD_ANON_136._CF_maxLength,
   STD_ANON_136._CF_minLength)
_module_typeBindings.STD_ANON_136 = STD_ANON_136

# Atomic simple type: [anonymous]
class STD_ANON_137 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1842, 16)
    _Documentation = None
STD_ANON_137._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_137._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_137._InitializeFacetMap(STD_ANON_137._CF_maxLength,
   STD_ANON_137._CF_minLength)
_module_typeBindings.STD_ANON_137 = STD_ANON_137

# Atomic simple type: [anonymous]
class STD_ANON_138 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1850, 16)
    _Documentation = None
STD_ANON_138._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
STD_ANON_138._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_138._InitializeFacetMap(STD_ANON_138._CF_maxLength,
   STD_ANON_138._CF_minLength)
_module_typeBindings.STD_ANON_138 = STD_ANON_138

# Atomic simple type: [anonymous]
class STD_ANON_139 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1859, 16)
    _Documentation = None
STD_ANON_139._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_139._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_139._InitializeFacetMap(STD_ANON_139._CF_maxLength,
   STD_ANON_139._CF_minLength)
_module_typeBindings.STD_ANON_139 = STD_ANON_139

# Atomic simple type: [anonymous]
class STD_ANON_140 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1873, 16)
    _Documentation = None
STD_ANON_140._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_140._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_140._InitializeFacetMap(STD_ANON_140._CF_maxLength,
   STD_ANON_140._CF_minLength)
_module_typeBindings.STD_ANON_140 = STD_ANON_140

# Atomic simple type: [anonymous]
class STD_ANON_141 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1891, 16)
    _Documentation = None
STD_ANON_141._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(19))
STD_ANON_141._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_141._InitializeFacetMap(STD_ANON_141._CF_maxLength,
   STD_ANON_141._CF_minLength)
_module_typeBindings.STD_ANON_141 = STD_ANON_141

# Atomic simple type: [anonymous]
class STD_ANON_142 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1900, 16)
    _Documentation = None
STD_ANON_142._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
STD_ANON_142._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON_142._InitializeFacetMap(STD_ANON_142._CF_maxLength,
   STD_ANON_142._CF_minLength)
_module_typeBindings.STD_ANON_142 = STD_ANON_142

# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest with content type ELEMENT_ONLY
class legalEntityCreateRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityCreateRequest')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 278, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityName uses Python identifier legalEntityName
    __legalEntityName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityName'), 'legalEntityName', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboardlegalEntityName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 280, 12), )

    
    legalEntityName = property(__legalEntityName.value, __legalEntityName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityType uses Python identifier legalEntityType
    __legalEntityType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityType'), 'legalEntityType', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboardlegalEntityType', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 289, 12), )

    
    legalEntityType = property(__legalEntityType.value, __legalEntityType.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityOwnershipType uses Python identifier legalEntityOwnershipType
    __legalEntityOwnershipType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityOwnershipType'), 'legalEntityOwnershipType', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboardlegalEntityOwnershipType', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 290, 12), )

    
    legalEntityOwnershipType = property(__legalEntityOwnershipType.value, __legalEntityOwnershipType.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}doingBusinessAs uses Python identifier doingBusinessAs
    __doingBusinessAs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'doingBusinessAs'), 'doingBusinessAs', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboarddoingBusinessAs', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 291, 12), )

    
    doingBusinessAs = property(__doingBusinessAs.value, __doingBusinessAs.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}taxId uses Python identifier taxId
    __taxId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxId'), 'taxId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboardtaxId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 299, 12), )

    
    taxId = property(__taxId.value, __taxId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}contactPhone uses Python identifier contactPhone
    __contactPhone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contactPhone'), 'contactPhone', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboardcontactPhone', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 307, 12), )

    
    contactPhone = property(__contactPhone.value, __contactPhone.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}annualCreditCardSalesVolume uses Python identifier annualCreditCardSalesVolume
    __annualCreditCardSalesVolume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annualCreditCardSalesVolume'), 'annualCreditCardSalesVolume', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboardannualCreditCardSalesVolume', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 315, 12), )

    
    annualCreditCardSalesVolume = property(__annualCreditCardSalesVolume.value, __annualCreditCardSalesVolume.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}hasAcceptedCreditCards uses Python identifier hasAcceptedCreditCards
    __hasAcceptedCreditCards = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasAcceptedCreditCards'), 'hasAcceptedCreditCards', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboardhasAcceptedCreditCards', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 316, 12), )

    
    hasAcceptedCreditCards = property(__hasAcceptedCreditCards.value, __hasAcceptedCreditCards.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address'), 'address', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboardaddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 317, 12), )

    
    address = property(__address.value, __address.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principal'), 'principal', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboardprincipal', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 318, 12), )

    
    principal = property(__principal.value, __principal.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}yearsInBusiness uses Python identifier yearsInBusiness
    __yearsInBusiness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yearsInBusiness'), 'yearsInBusiness', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateRequest__httppayfac_vantivcnp_comapimerchantonboardyearsInBusiness', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 319, 12), )

    
    yearsInBusiness = property(__yearsInBusiness.value, __yearsInBusiness.set, None, None)

    _ElementMap.update({
        __legalEntityName.name() : __legalEntityName,
        __legalEntityType.name() : __legalEntityType,
        __legalEntityOwnershipType.name() : __legalEntityOwnershipType,
        __doingBusinessAs.name() : __doingBusinessAs,
        __taxId.name() : __taxId,
        __contactPhone.name() : __contactPhone,
        __annualCreditCardSalesVolume.name() : __annualCreditCardSalesVolume,
        __hasAcceptedCreditCards.name() : __hasAcceptedCreditCards,
        __address.name() : __address,
        __principal.name() : __principal,
        __yearsInBusiness.name() : __yearsInBusiness
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityCreateRequest_ = legalEntityCreateRequest_
Namespace.addCategoryObject('typeBinding', 'legalEntityCreateRequest', legalEntityCreateRequest_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}address with content type ELEMENT_ONLY
class address (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}address with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'address')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 333, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}streetAddress1 uses Python identifier streetAddress1
    __streetAddress1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1'), 'streetAddress1', '__httppayfac_vantivcnp_comapimerchantonboard_address_httppayfac_vantivcnp_comapimerchantonboardstreetAddress1', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 335, 12), )

    
    streetAddress1 = property(__streetAddress1.value, __streetAddress1.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}streetAddress2 uses Python identifier streetAddress2
    __streetAddress2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2'), 'streetAddress2', '__httppayfac_vantivcnp_comapimerchantonboard_address_httppayfac_vantivcnp_comapimerchantonboardstreetAddress2', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 343, 12), )

    
    streetAddress2 = property(__streetAddress2.value, __streetAddress2.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httppayfac_vantivcnp_comapimerchantonboard_address_httppayfac_vantivcnp_comapimerchantonboardcity', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 351, 12), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}stateProvince uses Python identifier stateProvince
    __stateProvince = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stateProvince'), 'stateProvince', '__httppayfac_vantivcnp_comapimerchantonboard_address_httppayfac_vantivcnp_comapimerchantonboardstateProvince', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 359, 12), )

    
    stateProvince = property(__stateProvince.value, __stateProvince.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), 'postalCode', '__httppayfac_vantivcnp_comapimerchantonboard_address_httppayfac_vantivcnp_comapimerchantonboardpostalCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 367, 12), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), 'countryCode', '__httppayfac_vantivcnp_comapimerchantonboard_address_httppayfac_vantivcnp_comapimerchantonboardcountryCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 375, 12), )

    
    countryCode = property(__countryCode.value, __countryCode.set, None, None)

    _ElementMap.update({
        __streetAddress1.name() : __streetAddress1,
        __streetAddress2.name() : __streetAddress2,
        __city.name() : __city,
        __stateProvince.name() : __stateProvince,
        __postalCode.name() : __postalCode,
        __countryCode.name() : __countryCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.address = address
Namespace.addCategoryObject('typeBinding', 'address', address)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipal with content type ELEMENT_ONLY
class legalEntityPrincipal (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipal with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipal')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 386, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principalId uses Python identifier principalId
    __principalId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principalId'), 'principalId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboardprincipalId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 388, 12), )

    
    principalId = property(__principalId.value, __principalId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboardtitle', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 389, 12), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstName'), 'firstName', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboardfirstName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 397, 12), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastName'), 'lastName', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboardlastName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 405, 12), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), 'emailAddress', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboardemailAddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 413, 12), )

    
    emailAddress = property(__emailAddress.value, __emailAddress.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}ssn uses Python identifier ssn
    __ssn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ssn'), 'ssn', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboardssn', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 421, 12), )

    
    ssn = property(__ssn.value, __ssn.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}contactPhone uses Python identifier contactPhone
    __contactPhone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contactPhone'), 'contactPhone', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboardcontactPhone', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 429, 12), )

    
    contactPhone = property(__contactPhone.value, __contactPhone.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}dateOfBirth uses Python identifier dateOfBirth
    __dateOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dateOfBirth'), 'dateOfBirth', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboarddateOfBirth', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 437, 12), )

    
    dateOfBirth = property(__dateOfBirth.value, __dateOfBirth.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}driversLicense uses Python identifier driversLicense
    __driversLicense = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'driversLicense'), 'driversLicense', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboarddriversLicense', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 438, 12), )

    
    driversLicense = property(__driversLicense.value, __driversLicense.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}driversLicenseState uses Python identifier driversLicenseState
    __driversLicenseState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'driversLicenseState'), 'driversLicenseState', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboarddriversLicenseState', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 446, 12), )

    
    driversLicenseState = property(__driversLicenseState.value, __driversLicenseState.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address'), 'address', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboardaddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 454, 12), )

    
    address = property(__address.value, __address.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}stakePercent uses Python identifier stakePercent
    __stakePercent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stakePercent'), 'stakePercent', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboardstakePercent', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 455, 12), )

    
    stakePercent = property(__stakePercent.value, __stakePercent.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principal'), 'principal', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipal_httppayfac_vantivcnp_comapimerchantonboardprincipal', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 463, 12), )

    
    principal = property(__principal.value, __principal.set, None, None)

    _ElementMap.update({
        __principalId.name() : __principalId,
        __title.name() : __title,
        __firstName.name() : __firstName,
        __lastName.name() : __lastName,
        __emailAddress.name() : __emailAddress,
        __ssn.name() : __ssn,
        __contactPhone.name() : __contactPhone,
        __dateOfBirth.name() : __dateOfBirth,
        __driversLicense.name() : __driversLicense,
        __driversLicenseState.name() : __driversLicenseState,
        __address.name() : __address,
        __stakePercent.name() : __stakePercent,
        __principal.name() : __principal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityPrincipal = legalEntityPrincipal
Namespace.addCategoryObject('typeBinding', 'legalEntityPrincipal', legalEntityPrincipal)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalAddress with content type ELEMENT_ONLY
class principalAddress (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalAddress with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalAddress')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 467, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}streetAddress1 uses Python identifier streetAddress1
    __streetAddress1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1'), 'streetAddress1', '__httppayfac_vantivcnp_comapimerchantonboard_principalAddress_httppayfac_vantivcnp_comapimerchantonboardstreetAddress1', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 469, 12), )

    
    streetAddress1 = property(__streetAddress1.value, __streetAddress1.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}streetAddress2 uses Python identifier streetAddress2
    __streetAddress2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2'), 'streetAddress2', '__httppayfac_vantivcnp_comapimerchantonboard_principalAddress_httppayfac_vantivcnp_comapimerchantonboardstreetAddress2', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 477, 12), )

    
    streetAddress2 = property(__streetAddress2.value, __streetAddress2.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httppayfac_vantivcnp_comapimerchantonboard_principalAddress_httppayfac_vantivcnp_comapimerchantonboardcity', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 485, 12), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}stateProvince uses Python identifier stateProvince
    __stateProvince = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stateProvince'), 'stateProvince', '__httppayfac_vantivcnp_comapimerchantonboard_principalAddress_httppayfac_vantivcnp_comapimerchantonboardstateProvince', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 493, 12), )

    
    stateProvince = property(__stateProvince.value, __stateProvince.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), 'postalCode', '__httppayfac_vantivcnp_comapimerchantonboard_principalAddress_httppayfac_vantivcnp_comapimerchantonboardpostalCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 501, 12), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), 'countryCode', '__httppayfac_vantivcnp_comapimerchantonboard_principalAddress_httppayfac_vantivcnp_comapimerchantonboardcountryCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 509, 12), )

    
    countryCode = property(__countryCode.value, __countryCode.set, None, None)

    _ElementMap.update({
        __streetAddress1.name() : __streetAddress1,
        __streetAddress2.name() : __streetAddress2,
        __city.name() : __city,
        __stateProvince.name() : __stateProvince,
        __postalCode.name() : __postalCode,
        __countryCode.name() : __countryCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.principalAddress = principalAddress
Namespace.addCategoryObject('typeBinding', 'principalAddress', principalAddress)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}response with content type ELEMENT_ONLY
class response_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}response with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'response')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 576, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httppayfac_vantivcnp_comapimerchantonboard_response__httppayfac_vantivcnp_comapimerchantonboardtransactionId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, None)

    _ElementMap.update({
        __transactionId.name() : __transactionId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.response_ = response_
Namespace.addCategoryObject('typeBinding', 'response', response_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipalCreateRequest with content type ELEMENT_ONLY
class legalEntityPrincipalCreateRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipalCreateRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipalCreateRequest')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 584, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principal'), 'principal', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalCreateRequest__httppayfac_vantivcnp_comapimerchantonboardprincipal', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 586, 12), )

    
    principal = property(__principal.value, __principal.set, None, None)

    _ElementMap.update({
        __principal.name() : __principal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityPrincipalCreateRequest_ = legalEntityPrincipalCreateRequest_
Namespace.addCategoryObject('typeBinding', 'legalEntityPrincipalCreateRequest', legalEntityPrincipalCreateRequest_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}backgroundCheckResults with content type ELEMENT_ONLY
class backgroundCheckResults_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}backgroundCheckResults with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckResults')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 672, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}business uses Python identifier business
    __business = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'business'), 'business', '__httppayfac_vantivcnp_comapimerchantonboard_backgroundCheckResults__httppayfac_vantivcnp_comapimerchantonboardbusiness', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 674, 12), )

    
    business = property(__business.value, __business.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principal'), 'principal', '__httppayfac_vantivcnp_comapimerchantonboard_backgroundCheckResults__httppayfac_vantivcnp_comapimerchantonboardprincipal', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 675, 12), )

    
    principal = property(__principal.value, __principal.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}businessToPrincipalAssociation uses Python identifier businessToPrincipalAssociation
    __businessToPrincipalAssociation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'businessToPrincipalAssociation'), 'businessToPrincipalAssociation', '__httppayfac_vantivcnp_comapimerchantonboard_backgroundCheckResults__httppayfac_vantivcnp_comapimerchantonboardbusinessToPrincipalAssociation', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 676, 12), )

    
    businessToPrincipalAssociation = property(__businessToPrincipalAssociation.value, __businessToPrincipalAssociation.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}backgroundCheckDecisionNotes uses Python identifier backgroundCheckDecisionNotes
    __backgroundCheckDecisionNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckDecisionNotes'), 'backgroundCheckDecisionNotes', '__httppayfac_vantivcnp_comapimerchantonboard_backgroundCheckResults__httppayfac_vantivcnp_comapimerchantonboardbackgroundCheckDecisionNotes', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 677, 12), )

    
    backgroundCheckDecisionNotes = property(__backgroundCheckDecisionNotes.value, __backgroundCheckDecisionNotes.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}bankruptcyData uses Python identifier bankruptcyData
    __bankruptcyData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bankruptcyData'), 'bankruptcyData', '__httppayfac_vantivcnp_comapimerchantonboard_backgroundCheckResults__httppayfac_vantivcnp_comapimerchantonboardbankruptcyData', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 685, 12), )

    
    bankruptcyData = property(__bankruptcyData.value, __bankruptcyData.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}lienResult uses Python identifier lienResult
    __lienResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lienResult'), 'lienResult', '__httppayfac_vantivcnp_comapimerchantonboard_backgroundCheckResults__httppayfac_vantivcnp_comapimerchantonboardlienResult', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 686, 12), )

    
    lienResult = property(__lienResult.value, __lienResult.set, None, None)

    _ElementMap.update({
        __business.name() : __business,
        __principal.name() : __principal,
        __businessToPrincipalAssociation.name() : __businessToPrincipalAssociation,
        __backgroundCheckDecisionNotes.name() : __backgroundCheckDecisionNotes,
        __bankruptcyData.name() : __bankruptcyData,
        __lienResult.name() : __lienResult
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.backgroundCheckResults_ = backgroundCheckResults_
Namespace.addCategoryObject('typeBinding', 'backgroundCheckResults', backgroundCheckResults_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessResult with content type ELEMENT_ONLY
class businessResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'businessResult')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 690, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}verificationResult uses Python identifier verificationResult
    __verificationResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verificationResult'), 'verificationResult', '__httppayfac_vantivcnp_comapimerchantonboard_businessResult_httppayfac_vantivcnp_comapimerchantonboardverificationResult', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 692, 12), )

    
    verificationResult = property(__verificationResult.value, __verificationResult.set, None, None)

    _ElementMap.update({
        __verificationResult.name() : __verificationResult
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.businessResult = businessResult
Namespace.addCategoryObject('typeBinding', 'businessResult', businessResult)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessVerificationResult with content type ELEMENT_ONLY
class businessVerificationResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessVerificationResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'businessVerificationResult')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 696, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}overallScore uses Python identifier overallScore
    __overallScore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'overallScore'), 'overallScore', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationResult_httppayfac_vantivcnp_comapimerchantonboardoverallScore', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 698, 12), )

    
    overallScore = property(__overallScore.value, __overallScore.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}nameAddressTaxIdAssociation uses Python identifier nameAddressTaxIdAssociation
    __nameAddressTaxIdAssociation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameAddressTaxIdAssociation'), 'nameAddressTaxIdAssociation', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationResult_httppayfac_vantivcnp_comapimerchantonboardnameAddressTaxIdAssociation', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 699, 12), )

    
    nameAddressTaxIdAssociation = property(__nameAddressTaxIdAssociation.value, __nameAddressTaxIdAssociation.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}nameAddressPhoneAssociation uses Python identifier nameAddressPhoneAssociation
    __nameAddressPhoneAssociation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameAddressPhoneAssociation'), 'nameAddressPhoneAssociation', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationResult_httppayfac_vantivcnp_comapimerchantonboardnameAddressPhoneAssociation', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 700, 12), )

    
    nameAddressPhoneAssociation = property(__nameAddressPhoneAssociation.value, __nameAddressPhoneAssociation.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}verificationIndicators uses Python identifier verificationIndicators
    __verificationIndicators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verificationIndicators'), 'verificationIndicators', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationResult_httppayfac_vantivcnp_comapimerchantonboardverificationIndicators', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 701, 12), )

    
    verificationIndicators = property(__verificationIndicators.value, __verificationIndicators.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}riskIndicators uses Python identifier riskIndicators
    __riskIndicators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'riskIndicators'), 'riskIndicators', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationResult_httppayfac_vantivcnp_comapimerchantonboardriskIndicators', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 702, 12), )

    
    riskIndicators = property(__riskIndicators.value, __riskIndicators.set, None, None)

    _ElementMap.update({
        __overallScore.name() : __overallScore,
        __nameAddressTaxIdAssociation.name() : __nameAddressTaxIdAssociation,
        __nameAddressPhoneAssociation.name() : __nameAddressPhoneAssociation,
        __verificationIndicators.name() : __verificationIndicators,
        __riskIndicators.name() : __riskIndicators
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.businessVerificationResult = businessVerificationResult
Namespace.addCategoryObject('typeBinding', 'businessVerificationResult', businessVerificationResult)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 703, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}riskIndicator uses Python identifier riskIndicator
    __riskIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'riskIndicator'), 'riskIndicator', '__httppayfac_vantivcnp_comapimerchantonboard_CTD_ANON_httppayfac_vantivcnp_comapimerchantonboardriskIndicator', True, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 705, 24), )

    
    riskIndicator = property(__riskIndicator.value, __riskIndicator.set, None, None)

    _ElementMap.update({
        __riskIndicator.name() : __riskIndicator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessScore with content type ELEMENT_ONLY
class businessScore (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessScore with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'businessScore')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 712, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}score uses Python identifier score
    __score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'score'), 'score', '__httppayfac_vantivcnp_comapimerchantonboard_businessScore_httppayfac_vantivcnp_comapimerchantonboardscore', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 714, 12), )

    
    score = property(__score.value, __score.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httppayfac_vantivcnp_comapimerchantonboard_businessScore_httppayfac_vantivcnp_comapimerchantonboarddescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 715, 12), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __score.name() : __score,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.businessScore = businessScore
Namespace.addCategoryObject('typeBinding', 'businessScore', businessScore)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}nameAddressTaxIdAssociation with content type ELEMENT_ONLY
class nameAddressTaxIdAssociation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}nameAddressTaxIdAssociation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameAddressTaxIdAssociation')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 726, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__httppayfac_vantivcnp_comapimerchantonboard_nameAddressTaxIdAssociation_httppayfac_vantivcnp_comapimerchantonboardcode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 728, 12), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httppayfac_vantivcnp_comapimerchantonboard_nameAddressTaxIdAssociation_httppayfac_vantivcnp_comapimerchantonboarddescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 729, 12), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __code.name() : __code,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.nameAddressTaxIdAssociation = nameAddressTaxIdAssociation
Namespace.addCategoryObject('typeBinding', 'nameAddressTaxIdAssociation', nameAddressTaxIdAssociation)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessNameAddressPhoneAssociation with content type ELEMENT_ONLY
class businessNameAddressPhoneAssociation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessNameAddressPhoneAssociation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'businessNameAddressPhoneAssociation')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 740, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__httppayfac_vantivcnp_comapimerchantonboard_businessNameAddressPhoneAssociation_httppayfac_vantivcnp_comapimerchantonboardcode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 742, 12), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httppayfac_vantivcnp_comapimerchantonboard_businessNameAddressPhoneAssociation_httppayfac_vantivcnp_comapimerchantonboarddescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 743, 12), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __code.name() : __code,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.businessNameAddressPhoneAssociation = businessNameAddressPhoneAssociation
Namespace.addCategoryObject('typeBinding', 'businessNameAddressPhoneAssociation', businessNameAddressPhoneAssociation)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessVerificationIndicators with content type ELEMENT_ONLY
class businessVerificationIndicators (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessVerificationIndicators with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'businessVerificationIndicators')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 754, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}nameVerified uses Python identifier nameVerified
    __nameVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameVerified'), 'nameVerified', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardnameVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 756, 12), )

    
    nameVerified = property(__nameVerified.value, __nameVerified.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}addressVerified uses Python identifier addressVerified
    __addressVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'addressVerified'), 'addressVerified', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardaddressVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 757, 12), )

    
    addressVerified = property(__addressVerified.value, __addressVerified.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}cityVerified uses Python identifier cityVerified
    __cityVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cityVerified'), 'cityVerified', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardcityVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 758, 12), )

    
    cityVerified = property(__cityVerified.value, __cityVerified.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}stateVerified uses Python identifier stateVerified
    __stateVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stateVerified'), 'stateVerified', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardstateVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 759, 12), )

    
    stateVerified = property(__stateVerified.value, __stateVerified.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}zipVerified uses Python identifier zipVerified
    __zipVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zipVerified'), 'zipVerified', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardzipVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 760, 12), )

    
    zipVerified = property(__zipVerified.value, __zipVerified.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}phoneVerified uses Python identifier phoneVerified
    __phoneVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phoneVerified'), 'phoneVerified', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardphoneVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 761, 12), )

    
    phoneVerified = property(__phoneVerified.value, __phoneVerified.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}taxIdVerified uses Python identifier taxIdVerified
    __taxIdVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxIdVerified'), 'taxIdVerified', '__httppayfac_vantivcnp_comapimerchantonboard_businessVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardtaxIdVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 762, 12), )

    
    taxIdVerified = property(__taxIdVerified.value, __taxIdVerified.set, None, None)

    _ElementMap.update({
        __nameVerified.name() : __nameVerified,
        __addressVerified.name() : __addressVerified,
        __cityVerified.name() : __cityVerified,
        __stateVerified.name() : __stateVerified,
        __zipVerified.name() : __zipVerified,
        __phoneVerified.name() : __phoneVerified,
        __taxIdVerified.name() : __taxIdVerified
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.businessVerificationIndicators = businessVerificationIndicators
Namespace.addCategoryObject('typeBinding', 'businessVerificationIndicators', businessVerificationIndicators)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}potentialRiskIndicator with content type ELEMENT_ONLY
class potentialRiskIndicator (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}potentialRiskIndicator with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'potentialRiskIndicator')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 766, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__httppayfac_vantivcnp_comapimerchantonboard_potentialRiskIndicator_httppayfac_vantivcnp_comapimerchantonboardcode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 768, 12), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httppayfac_vantivcnp_comapimerchantonboard_potentialRiskIndicator_httppayfac_vantivcnp_comapimerchantonboarddescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 769, 12), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __code.name() : __code,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.potentialRiskIndicator = potentialRiskIndicator
Namespace.addCategoryObject('typeBinding', 'potentialRiskIndicator', potentialRiskIndicator)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalResult with content type ELEMENT_ONLY
class principalResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalResult')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 780, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}verificationResult uses Python identifier verificationResult
    __verificationResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verificationResult'), 'verificationResult', '__httppayfac_vantivcnp_comapimerchantonboard_principalResult_httppayfac_vantivcnp_comapimerchantonboardverificationResult', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 782, 12), )

    
    verificationResult = property(__verificationResult.value, __verificationResult.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}backgroundCheckDecisionNotes uses Python identifier backgroundCheckDecisionNotes
    __backgroundCheckDecisionNotes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckDecisionNotes'), 'backgroundCheckDecisionNotes', '__httppayfac_vantivcnp_comapimerchantonboard_principalResult_httppayfac_vantivcnp_comapimerchantonboardbackgroundCheckDecisionNotes', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 783, 12), )

    
    backgroundCheckDecisionNotes = property(__backgroundCheckDecisionNotes.value, __backgroundCheckDecisionNotes.set, None, None)

    _ElementMap.update({
        __verificationResult.name() : __verificationResult,
        __backgroundCheckDecisionNotes.name() : __backgroundCheckDecisionNotes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.principalResult = principalResult
Namespace.addCategoryObject('typeBinding', 'principalResult', principalResult)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalVerificationResult with content type ELEMENT_ONLY
class principalVerificationResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalVerificationResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalVerificationResult')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 794, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}overallScore uses Python identifier overallScore
    __overallScore = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'overallScore'), 'overallScore', '__httppayfac_vantivcnp_comapimerchantonboard_principalVerificationResult_httppayfac_vantivcnp_comapimerchantonboardoverallScore', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 796, 12), )

    
    overallScore = property(__overallScore.value, __overallScore.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}nameAddressSsnAssociation uses Python identifier nameAddressSsnAssociation
    __nameAddressSsnAssociation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameAddressSsnAssociation'), 'nameAddressSsnAssociation', '__httppayfac_vantivcnp_comapimerchantonboard_principalVerificationResult_httppayfac_vantivcnp_comapimerchantonboardnameAddressSsnAssociation', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 797, 12), )

    
    nameAddressSsnAssociation = property(__nameAddressSsnAssociation.value, __nameAddressSsnAssociation.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}nameAddressPhoneAssociation uses Python identifier nameAddressPhoneAssociation
    __nameAddressPhoneAssociation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameAddressPhoneAssociation'), 'nameAddressPhoneAssociation', '__httppayfac_vantivcnp_comapimerchantonboard_principalVerificationResult_httppayfac_vantivcnp_comapimerchantonboardnameAddressPhoneAssociation', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 798, 12), )

    
    nameAddressPhoneAssociation = property(__nameAddressPhoneAssociation.value, __nameAddressPhoneAssociation.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}verificationIndicators uses Python identifier verificationIndicators
    __verificationIndicators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verificationIndicators'), 'verificationIndicators', '__httppayfac_vantivcnp_comapimerchantonboard_principalVerificationResult_httppayfac_vantivcnp_comapimerchantonboardverificationIndicators', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 799, 12), )

    
    verificationIndicators = property(__verificationIndicators.value, __verificationIndicators.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}riskIndicators uses Python identifier riskIndicators
    __riskIndicators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'riskIndicators'), 'riskIndicators', '__httppayfac_vantivcnp_comapimerchantonboard_principalVerificationResult_httppayfac_vantivcnp_comapimerchantonboardriskIndicators', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 800, 12), )

    
    riskIndicators = property(__riskIndicators.value, __riskIndicators.set, None, None)

    _ElementMap.update({
        __overallScore.name() : __overallScore,
        __nameAddressSsnAssociation.name() : __nameAddressSsnAssociation,
        __nameAddressPhoneAssociation.name() : __nameAddressPhoneAssociation,
        __verificationIndicators.name() : __verificationIndicators,
        __riskIndicators.name() : __riskIndicators
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.principalVerificationResult = principalVerificationResult
Namespace.addCategoryObject('typeBinding', 'principalVerificationResult', principalVerificationResult)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 801, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}riskIndicator uses Python identifier riskIndicator
    __riskIndicator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'riskIndicator'), 'riskIndicator', '__httppayfac_vantivcnp_comapimerchantonboard_CTD_ANON__httppayfac_vantivcnp_comapimerchantonboardriskIndicator', True, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 803, 24), )

    
    riskIndicator = property(__riskIndicator.value, __riskIndicator.set, None, None)

    _ElementMap.update({
        __riskIndicator.name() : __riskIndicator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalScore with content type ELEMENT_ONLY
class principalScore (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalScore with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalScore')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 810, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}score uses Python identifier score
    __score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'score'), 'score', '__httppayfac_vantivcnp_comapimerchantonboard_principalScore_httppayfac_vantivcnp_comapimerchantonboardscore', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 812, 12), )

    
    score = property(__score.value, __score.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httppayfac_vantivcnp_comapimerchantonboard_principalScore_httppayfac_vantivcnp_comapimerchantonboarddescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 813, 12), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __score.name() : __score,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.principalScore = principalScore
Namespace.addCategoryObject('typeBinding', 'principalScore', principalScore)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}nameAddressSsnAssociation with content type ELEMENT_ONLY
class nameAddressSsnAssociation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}nameAddressSsnAssociation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameAddressSsnAssociation')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 824, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__httppayfac_vantivcnp_comapimerchantonboard_nameAddressSsnAssociation_httppayfac_vantivcnp_comapimerchantonboardcode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 826, 12), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httppayfac_vantivcnp_comapimerchantonboard_nameAddressSsnAssociation_httppayfac_vantivcnp_comapimerchantonboarddescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 827, 12), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __code.name() : __code,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.nameAddressSsnAssociation = nameAddressSsnAssociation
Namespace.addCategoryObject('typeBinding', 'nameAddressSsnAssociation', nameAddressSsnAssociation)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalNameAddressPhoneAssociation with content type ELEMENT_ONLY
class principalNameAddressPhoneAssociation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalNameAddressPhoneAssociation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalNameAddressPhoneAssociation')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 838, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__httppayfac_vantivcnp_comapimerchantonboard_principalNameAddressPhoneAssociation_httppayfac_vantivcnp_comapimerchantonboardcode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 840, 12), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httppayfac_vantivcnp_comapimerchantonboard_principalNameAddressPhoneAssociation_httppayfac_vantivcnp_comapimerchantonboarddescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 841, 12), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __code.name() : __code,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.principalNameAddressPhoneAssociation = principalNameAddressPhoneAssociation
Namespace.addCategoryObject('typeBinding', 'principalNameAddressPhoneAssociation', principalNameAddressPhoneAssociation)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalVerificationIndicators with content type ELEMENT_ONLY
class principalVerificationIndicators (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalVerificationIndicators with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalVerificationIndicators')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 852, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}nameVerified uses Python identifier nameVerified
    __nameVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nameVerified'), 'nameVerified', '__httppayfac_vantivcnp_comapimerchantonboard_principalVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardnameVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 854, 12), )

    
    nameVerified = property(__nameVerified.value, __nameVerified.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}addressVerified uses Python identifier addressVerified
    __addressVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'addressVerified'), 'addressVerified', '__httppayfac_vantivcnp_comapimerchantonboard_principalVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardaddressVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 855, 12), )

    
    addressVerified = property(__addressVerified.value, __addressVerified.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}phoneVerified uses Python identifier phoneVerified
    __phoneVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phoneVerified'), 'phoneVerified', '__httppayfac_vantivcnp_comapimerchantonboard_principalVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardphoneVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 856, 12), )

    
    phoneVerified = property(__phoneVerified.value, __phoneVerified.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}ssnVerified uses Python identifier ssnVerified
    __ssnVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ssnVerified'), 'ssnVerified', '__httppayfac_vantivcnp_comapimerchantonboard_principalVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboardssnVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 857, 12), )

    
    ssnVerified = property(__ssnVerified.value, __ssnVerified.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}dobVerified uses Python identifier dobVerified
    __dobVerified = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dobVerified'), 'dobVerified', '__httppayfac_vantivcnp_comapimerchantonboard_principalVerificationIndicators_httppayfac_vantivcnp_comapimerchantonboarddobVerified', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 858, 12), )

    
    dobVerified = property(__dobVerified.value, __dobVerified.set, None, None)

    _ElementMap.update({
        __nameVerified.name() : __nameVerified,
        __addressVerified.name() : __addressVerified,
        __phoneVerified.name() : __phoneVerified,
        __ssnVerified.name() : __ssnVerified,
        __dobVerified.name() : __dobVerified
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.principalVerificationIndicators = principalVerificationIndicators
Namespace.addCategoryObject('typeBinding', 'principalVerificationIndicators', principalVerificationIndicators)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessToPrincipalAssociation with content type ELEMENT_ONLY
class businessToPrincipalAssociation (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}businessToPrincipalAssociation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'businessToPrincipalAssociation')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 862, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}score uses Python identifier score
    __score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'score'), 'score', '__httppayfac_vantivcnp_comapimerchantonboard_businessToPrincipalAssociation_httppayfac_vantivcnp_comapimerchantonboardscore', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 864, 12), )

    
    score = property(__score.value, __score.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'description'), 'description', '__httppayfac_vantivcnp_comapimerchantonboard_businessToPrincipalAssociation_httppayfac_vantivcnp_comapimerchantonboarddescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 865, 12), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __score.name() : __score,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.businessToPrincipalAssociation = businessToPrincipalAssociation
Namespace.addCategoryObject('typeBinding', 'businessToPrincipalAssociation', businessToPrincipalAssociation)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}bankruptcyResult with content type ELEMENT_ONLY
class bankruptcyResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}bankruptcyResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bankruptcyResult')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 876, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}bankruptcyType uses Python identifier bankruptcyType
    __bankruptcyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bankruptcyType'), 'bankruptcyType', '__httppayfac_vantivcnp_comapimerchantonboard_bankruptcyResult_httppayfac_vantivcnp_comapimerchantonboardbankruptcyType', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 878, 12), )

    
    bankruptcyType = property(__bankruptcyType.value, __bankruptcyType.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}bankruptcyCount uses Python identifier bankruptcyCount
    __bankruptcyCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bankruptcyCount'), 'bankruptcyCount', '__httppayfac_vantivcnp_comapimerchantonboard_bankruptcyResult_httppayfac_vantivcnp_comapimerchantonboardbankruptcyCount', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 886, 12), )

    
    bankruptcyCount = property(__bankruptcyCount.value, __bankruptcyCount.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}companyName uses Python identifier companyName
    __companyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'companyName'), 'companyName', '__httppayfac_vantivcnp_comapimerchantonboard_bankruptcyResult_httppayfac_vantivcnp_comapimerchantonboardcompanyName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 887, 12), )

    
    companyName = property(__companyName.value, __companyName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}streetAddress1 uses Python identifier streetAddress1
    __streetAddress1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1'), 'streetAddress1', '__httppayfac_vantivcnp_comapimerchantonboard_bankruptcyResult_httppayfac_vantivcnp_comapimerchantonboardstreetAddress1', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 895, 12), )

    
    streetAddress1 = property(__streetAddress1.value, __streetAddress1.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}streetAddress2 uses Python identifier streetAddress2
    __streetAddress2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2'), 'streetAddress2', '__httppayfac_vantivcnp_comapimerchantonboard_bankruptcyResult_httppayfac_vantivcnp_comapimerchantonboardstreetAddress2', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 903, 12), )

    
    streetAddress2 = property(__streetAddress2.value, __streetAddress2.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httppayfac_vantivcnp_comapimerchantonboard_bankruptcyResult_httppayfac_vantivcnp_comapimerchantonboardcity', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 911, 12), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'state'), 'state', '__httppayfac_vantivcnp_comapimerchantonboard_bankruptcyResult_httppayfac_vantivcnp_comapimerchantonboardstate', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 919, 12), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zip'), 'zip', '__httppayfac_vantivcnp_comapimerchantonboard_bankruptcyResult_httppayfac_vantivcnp_comapimerchantonboardzip', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 927, 12), )

    
    zip = property(__zip.value, __zip.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}zip4 uses Python identifier zip4
    __zip4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zip4'), 'zip4', '__httppayfac_vantivcnp_comapimerchantonboard_bankruptcyResult_httppayfac_vantivcnp_comapimerchantonboardzip4', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 935, 12), )

    
    zip4 = property(__zip4.value, __zip4.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}filingDate uses Python identifier filingDate
    __filingDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filingDate'), 'filingDate', '__httppayfac_vantivcnp_comapimerchantonboard_bankruptcyResult_httppayfac_vantivcnp_comapimerchantonboardfilingDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 943, 12), )

    
    filingDate = property(__filingDate.value, __filingDate.set, None, None)

    _ElementMap.update({
        __bankruptcyType.name() : __bankruptcyType,
        __bankruptcyCount.name() : __bankruptcyCount,
        __companyName.name() : __companyName,
        __streetAddress1.name() : __streetAddress1,
        __streetAddress2.name() : __streetAddress2,
        __city.name() : __city,
        __state.name() : __state,
        __zip.name() : __zip,
        __zip4.name() : __zip4,
        __filingDate.name() : __filingDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.bankruptcyResult = bankruptcyResult
Namespace.addCategoryObject('typeBinding', 'bankruptcyResult', bankruptcyResult)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}lienResult with content type ELEMENT_ONLY
class lienResult (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}lienResult with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lienResult')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 947, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}lienType uses Python identifier lienType
    __lienType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lienType'), 'lienType', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardlienType', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 949, 12), )

    
    lienType = property(__lienType.value, __lienType.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}releasedCount uses Python identifier releasedCount
    __releasedCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'releasedCount'), 'releasedCount', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardreleasedCount', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 957, 12), )

    
    releasedCount = property(__releasedCount.value, __releasedCount.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}unreleasedCount uses Python identifier unreleasedCount
    __unreleasedCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'unreleasedCount'), 'unreleasedCount', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardunreleasedCount', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 958, 12), )

    
    unreleasedCount = property(__unreleasedCount.value, __unreleasedCount.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}companyName uses Python identifier companyName
    __companyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'companyName'), 'companyName', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardcompanyName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 959, 12), )

    
    companyName = property(__companyName.value, __companyName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}streetAddress1 uses Python identifier streetAddress1
    __streetAddress1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1'), 'streetAddress1', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardstreetAddress1', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 967, 12), )

    
    streetAddress1 = property(__streetAddress1.value, __streetAddress1.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}streetAddress2 uses Python identifier streetAddress2
    __streetAddress2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2'), 'streetAddress2', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardstreetAddress2', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 975, 12), )

    
    streetAddress2 = property(__streetAddress2.value, __streetAddress2.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardcity', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 983, 12), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'state'), 'state', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardstate', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 991, 12), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zip'), 'zip', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardzip', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 999, 12), )

    
    zip = property(__zip.value, __zip.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}zip4 uses Python identifier zip4
    __zip4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'zip4'), 'zip4', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardzip4', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1007, 12), )

    
    zip4 = property(__zip4.value, __zip4.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}filingDate uses Python identifier filingDate
    __filingDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filingDate'), 'filingDate', '__httppayfac_vantivcnp_comapimerchantonboard_lienResult_httppayfac_vantivcnp_comapimerchantonboardfilingDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1015, 12), )

    
    filingDate = property(__filingDate.value, __filingDate.set, None, None)

    _ElementMap.update({
        __lienType.name() : __lienType,
        __releasedCount.name() : __releasedCount,
        __unreleasedCount.name() : __unreleasedCount,
        __companyName.name() : __companyName,
        __streetAddress1.name() : __streetAddress1,
        __streetAddress2.name() : __streetAddress2,
        __city.name() : __city,
        __state.name() : __state,
        __zip.name() : __zip,
        __zip4.name() : __zip4,
        __filingDate.name() : __filingDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.lienResult = lienResult
Namespace.addCategoryObject('typeBinding', 'lienResult', lienResult)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityUpdateRequest with content type ELEMENT_ONLY
class legalEntityUpdateRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityUpdateRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityUpdateRequest')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1019, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address'), 'address', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardaddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1021, 12), )

    
    address = property(__address.value, __address.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}contactPhone uses Python identifier contactPhone
    __contactPhone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contactPhone'), 'contactPhone', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardcontactPhone', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1022, 12), )

    
    contactPhone = property(__contactPhone.value, __contactPhone.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}doingBusinessAs uses Python identifier doingBusinessAs
    __doingBusinessAs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'doingBusinessAs'), 'doingBusinessAs', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityUpdateRequest__httppayfac_vantivcnp_comapimerchantonboarddoingBusinessAs', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1030, 12), )

    
    doingBusinessAs = property(__doingBusinessAs.value, __doingBusinessAs.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}annualCreditCardSalesVolume uses Python identifier annualCreditCardSalesVolume
    __annualCreditCardSalesVolume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'annualCreditCardSalesVolume'), 'annualCreditCardSalesVolume', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardannualCreditCardSalesVolume', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1038, 12), )

    
    annualCreditCardSalesVolume = property(__annualCreditCardSalesVolume.value, __annualCreditCardSalesVolume.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}hasAcceptedCreditCards uses Python identifier hasAcceptedCreditCards
    __hasAcceptedCreditCards = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hasAcceptedCreditCards'), 'hasAcceptedCreditCards', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardhasAcceptedCreditCards', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1039, 12), )

    
    hasAcceptedCreditCards = property(__hasAcceptedCreditCards.value, __hasAcceptedCreditCards.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principal'), 'principal', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardprincipal', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1040, 12), )

    
    principal = property(__principal.value, __principal.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}backgroundCheckFields uses Python identifier backgroundCheckFields
    __backgroundCheckFields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckFields'), 'backgroundCheckFields', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardbackgroundCheckFields', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1041, 12), )

    
    backgroundCheckFields = property(__backgroundCheckFields.value, __backgroundCheckFields.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityOwnershipType uses Python identifier legalEntityOwnershipType
    __legalEntityOwnershipType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityOwnershipType'), 'legalEntityOwnershipType', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardlegalEntityOwnershipType', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1042, 12), )

    
    legalEntityOwnershipType = property(__legalEntityOwnershipType.value, __legalEntityOwnershipType.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}yearsInBusiness uses Python identifier yearsInBusiness
    __yearsInBusiness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yearsInBusiness'), 'yearsInBusiness', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardyearsInBusiness', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1043, 12), )

    
    yearsInBusiness = property(__yearsInBusiness.value, __yearsInBusiness.set, None, None)

    _ElementMap.update({
        __address.name() : __address,
        __contactPhone.name() : __contactPhone,
        __doingBusinessAs.name() : __doingBusinessAs,
        __annualCreditCardSalesVolume.name() : __annualCreditCardSalesVolume,
        __hasAcceptedCreditCards.name() : __hasAcceptedCreditCards,
        __principal.name() : __principal,
        __backgroundCheckFields.name() : __backgroundCheckFields,
        __legalEntityOwnershipType.name() : __legalEntityOwnershipType,
        __yearsInBusiness.name() : __yearsInBusiness
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityUpdateRequest_ = legalEntityUpdateRequest_
Namespace.addCategoryObject('typeBinding', 'legalEntityUpdateRequest', legalEntityUpdateRequest_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}addressUpdatable with content type ELEMENT_ONLY
class addressUpdatable (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}addressUpdatable with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'addressUpdatable')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1055, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}streetAddress1 uses Python identifier streetAddress1
    __streetAddress1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1'), 'streetAddress1', '__httppayfac_vantivcnp_comapimerchantonboard_addressUpdatable_httppayfac_vantivcnp_comapimerchantonboardstreetAddress1', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1057, 12), )

    
    streetAddress1 = property(__streetAddress1.value, __streetAddress1.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}streetAddress2 uses Python identifier streetAddress2
    __streetAddress2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2'), 'streetAddress2', '__httppayfac_vantivcnp_comapimerchantonboard_addressUpdatable_httppayfac_vantivcnp_comapimerchantonboardstreetAddress2', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1065, 12), )

    
    streetAddress2 = property(__streetAddress2.value, __streetAddress2.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httppayfac_vantivcnp_comapimerchantonboard_addressUpdatable_httppayfac_vantivcnp_comapimerchantonboardcity', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1073, 12), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}stateProvince uses Python identifier stateProvince
    __stateProvince = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stateProvince'), 'stateProvince', '__httppayfac_vantivcnp_comapimerchantonboard_addressUpdatable_httppayfac_vantivcnp_comapimerchantonboardstateProvince', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1081, 12), )

    
    stateProvince = property(__stateProvince.value, __stateProvince.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), 'postalCode', '__httppayfac_vantivcnp_comapimerchantonboard_addressUpdatable_httppayfac_vantivcnp_comapimerchantonboardpostalCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1089, 12), )

    
    postalCode = property(__postalCode.value, __postalCode.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), 'countryCode', '__httppayfac_vantivcnp_comapimerchantonboard_addressUpdatable_httppayfac_vantivcnp_comapimerchantonboardcountryCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1097, 12), )

    
    countryCode = property(__countryCode.value, __countryCode.set, None, None)

    _ElementMap.update({
        __streetAddress1.name() : __streetAddress1,
        __streetAddress2.name() : __streetAddress2,
        __city.name() : __city,
        __stateProvince.name() : __stateProvince,
        __postalCode.name() : __postalCode,
        __countryCode.name() : __countryCode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.addressUpdatable = addressUpdatable
Namespace.addCategoryObject('typeBinding', 'addressUpdatable', addressUpdatable)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipalUpdatable with content type ELEMENT_ONLY
class legalEntityPrincipalUpdatable (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipalUpdatable with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipalUpdatable')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1108, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principalId uses Python identifier principalId
    __principalId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principalId'), 'principalId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalUpdatable_httppayfac_vantivcnp_comapimerchantonboardprincipalId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1110, 12), )

    
    principalId = property(__principalId.value, __principalId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'title'), 'title', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalUpdatable_httppayfac_vantivcnp_comapimerchantonboardtitle', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1111, 12), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), 'emailAddress', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalUpdatable_httppayfac_vantivcnp_comapimerchantonboardemailAddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1119, 12), )

    
    emailAddress = property(__emailAddress.value, __emailAddress.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}contactPhone uses Python identifier contactPhone
    __contactPhone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contactPhone'), 'contactPhone', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalUpdatable_httppayfac_vantivcnp_comapimerchantonboardcontactPhone', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1127, 12), )

    
    contactPhone = property(__contactPhone.value, __contactPhone.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address'), 'address', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalUpdatable_httppayfac_vantivcnp_comapimerchantonboardaddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1135, 12), )

    
    address = property(__address.value, __address.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}stakePercent uses Python identifier stakePercent
    __stakePercent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stakePercent'), 'stakePercent', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalUpdatable_httppayfac_vantivcnp_comapimerchantonboardstakePercent', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1136, 12), )

    
    stakePercent = property(__stakePercent.value, __stakePercent.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}backgroundCheckFields uses Python identifier backgroundCheckFields
    __backgroundCheckFields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckFields'), 'backgroundCheckFields', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalUpdatable_httppayfac_vantivcnp_comapimerchantonboardbackgroundCheckFields', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1144, 12), )

    
    backgroundCheckFields = property(__backgroundCheckFields.value, __backgroundCheckFields.set, None, None)

    _ElementMap.update({
        __principalId.name() : __principalId,
        __title.name() : __title,
        __emailAddress.name() : __emailAddress,
        __contactPhone.name() : __contactPhone,
        __address.name() : __address,
        __stakePercent.name() : __stakePercent,
        __backgroundCheckFields.name() : __backgroundCheckFields
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityPrincipalUpdatable = legalEntityPrincipalUpdatable
Namespace.addCategoryObject('typeBinding', 'legalEntityPrincipalUpdatable', legalEntityPrincipalUpdatable)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalBackgroundCheckFields with content type ELEMENT_ONLY
class principalBackgroundCheckFields (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalBackgroundCheckFields with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalBackgroundCheckFields')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1148, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstName'), 'firstName', '__httppayfac_vantivcnp_comapimerchantonboard_principalBackgroundCheckFields_httppayfac_vantivcnp_comapimerchantonboardfirstName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1150, 12), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastName'), 'lastName', '__httppayfac_vantivcnp_comapimerchantonboard_principalBackgroundCheckFields_httppayfac_vantivcnp_comapimerchantonboardlastName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1158, 12), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}ssn uses Python identifier ssn
    __ssn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ssn'), 'ssn', '__httppayfac_vantivcnp_comapimerchantonboard_principalBackgroundCheckFields_httppayfac_vantivcnp_comapimerchantonboardssn', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1166, 12), )

    
    ssn = property(__ssn.value, __ssn.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}dateOfBirth uses Python identifier dateOfBirth
    __dateOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dateOfBirth'), 'dateOfBirth', '__httppayfac_vantivcnp_comapimerchantonboard_principalBackgroundCheckFields_httppayfac_vantivcnp_comapimerchantonboarddateOfBirth', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1174, 12), )

    
    dateOfBirth = property(__dateOfBirth.value, __dateOfBirth.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}driversLicense uses Python identifier driversLicense
    __driversLicense = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'driversLicense'), 'driversLicense', '__httppayfac_vantivcnp_comapimerchantonboard_principalBackgroundCheckFields_httppayfac_vantivcnp_comapimerchantonboarddriversLicense', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1175, 12), )

    
    driversLicense = property(__driversLicense.value, __driversLicense.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}driversLicenseState uses Python identifier driversLicenseState
    __driversLicenseState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'driversLicenseState'), 'driversLicenseState', '__httppayfac_vantivcnp_comapimerchantonboard_principalBackgroundCheckFields_httppayfac_vantivcnp_comapimerchantonboarddriversLicenseState', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1183, 12), )

    
    driversLicenseState = property(__driversLicenseState.value, __driversLicenseState.set, None, None)

    _ElementMap.update({
        __firstName.name() : __firstName,
        __lastName.name() : __lastName,
        __ssn.name() : __ssn,
        __dateOfBirth.name() : __dateOfBirth,
        __driversLicense.name() : __driversLicense,
        __driversLicenseState.name() : __driversLicenseState
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.principalBackgroundCheckFields = principalBackgroundCheckFields
Namespace.addCategoryObject('typeBinding', 'principalBackgroundCheckFields', principalBackgroundCheckFields)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityBackgroundCheckFields with content type ELEMENT_ONLY
class legalEntityBackgroundCheckFields (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityBackgroundCheckFields with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityBackgroundCheckFields')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1194, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityName uses Python identifier legalEntityName
    __legalEntityName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityName'), 'legalEntityName', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityBackgroundCheckFields_httppayfac_vantivcnp_comapimerchantonboardlegalEntityName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1196, 12), )

    
    legalEntityName = property(__legalEntityName.value, __legalEntityName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityType uses Python identifier legalEntityType
    __legalEntityType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityType'), 'legalEntityType', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityBackgroundCheckFields_httppayfac_vantivcnp_comapimerchantonboardlegalEntityType', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1205, 12), )

    
    legalEntityType = property(__legalEntityType.value, __legalEntityType.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}taxId uses Python identifier taxId
    __taxId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxId'), 'taxId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityBackgroundCheckFields_httppayfac_vantivcnp_comapimerchantonboardtaxId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1206, 12), )

    
    taxId = property(__taxId.value, __taxId.set, None, None)

    _ElementMap.update({
        __legalEntityName.name() : __legalEntityName,
        __legalEntityType.name() : __legalEntityType,
        __taxId.name() : __taxId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityBackgroundCheckFields = legalEntityBackgroundCheckFields
Namespace.addCategoryObject('typeBinding', 'legalEntityBackgroundCheckFields', legalEntityBackgroundCheckFields)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest with content type ELEMENT_ONLY
class subMerchantCreateRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantCreateRequest')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1217, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}merchantName uses Python identifier merchantName
    __merchantName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'merchantName'), 'merchantName', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardmerchantName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1219, 12), )

    
    merchantName = property(__merchantName.value, __merchantName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}amexMid uses Python identifier amexMid
    __amexMid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amexMid'), 'amexMid', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardamexMid', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1227, 12), )

    
    amexMid = property(__amexMid.value, __amexMid.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}discoverConveyedMid uses Python identifier discoverConveyedMid
    __discoverConveyedMid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'discoverConveyedMid'), 'discoverConveyedMid', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboarddiscoverConveyedMid', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1235, 12), )

    
    discoverConveyedMid = property(__discoverConveyedMid.value, __discoverConveyedMid.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'url'), 'url', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardurl', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1243, 12), )

    
    url = property(__url.value, __url.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}customerServiceNumber uses Python identifier customerServiceNumber
    __customerServiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerServiceNumber'), 'customerServiceNumber', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardcustomerServiceNumber', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1251, 12), )

    
    customerServiceNumber = property(__customerServiceNumber.value, __customerServiceNumber.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}hardCodedBillingDescriptor uses Python identifier hardCodedBillingDescriptor
    __hardCodedBillingDescriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hardCodedBillingDescriptor'), 'hardCodedBillingDescriptor', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardhardCodedBillingDescriptor', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1259, 12), )

    
    hardCodedBillingDescriptor = property(__hardCodedBillingDescriptor.value, __hardCodedBillingDescriptor.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}maxTransactionAmount uses Python identifier maxTransactionAmount
    __maxTransactionAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxTransactionAmount'), 'maxTransactionAmount', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardmaxTransactionAmount', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1267, 12), )

    
    maxTransactionAmount = property(__maxTransactionAmount.value, __maxTransactionAmount.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}purchaseCurrency uses Python identifier purchaseCurrency
    __purchaseCurrency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'purchaseCurrency'), 'purchaseCurrency', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardpurchaseCurrency', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1274, 12), )

    
    purchaseCurrency = property(__purchaseCurrency.value, __purchaseCurrency.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}merchantCategoryCode uses Python identifier merchantCategoryCode
    __merchantCategoryCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'merchantCategoryCode'), 'merchantCategoryCode', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardmerchantCategoryCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1282, 12), )

    
    merchantCategoryCode = property(__merchantCategoryCode.value, __merchantCategoryCode.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}taxAuthority uses Python identifier taxAuthority
    __taxAuthority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxAuthority'), 'taxAuthority', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardtaxAuthority', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1290, 12), )

    
    taxAuthority = property(__taxAuthority.value, __taxAuthority.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}taxAuthorityState uses Python identifier taxAuthorityState
    __taxAuthorityState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxAuthorityState'), 'taxAuthorityState', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardtaxAuthorityState', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1291, 12), )

    
    taxAuthorityState = property(__taxAuthorityState.value, __taxAuthorityState.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}bankRoutingNumber uses Python identifier bankRoutingNumber
    __bankRoutingNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bankRoutingNumber'), 'bankRoutingNumber', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardbankRoutingNumber', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1292, 12), )

    
    bankRoutingNumber = property(__bankRoutingNumber.value, __bankRoutingNumber.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}bankAccountNumber uses Python identifier bankAccountNumber
    __bankAccountNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bankAccountNumber'), 'bankAccountNumber', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardbankAccountNumber', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1300, 12), )

    
    bankAccountNumber = property(__bankAccountNumber.value, __bankAccountNumber.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}pspMerchantId uses Python identifier pspMerchantId
    __pspMerchantId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pspMerchantId'), 'pspMerchantId', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardpspMerchantId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1308, 12), )

    
    pspMerchantId = property(__pspMerchantId.value, __pspMerchantId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}fraud uses Python identifier fraud
    __fraud = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fraud'), 'fraud', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardfraud', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1316, 12), )

    
    fraud = property(__fraud.value, __fraud.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}amexAcquired uses Python identifier amexAcquired
    __amexAcquired = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amexAcquired'), 'amexAcquired', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardamexAcquired', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1317, 12), )

    
    amexAcquired = property(__amexAcquired.value, __amexAcquired.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address'), 'address', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardaddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1318, 12), )

    
    address = property(__address.value, __address.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}primaryContact uses Python identifier primaryContact
    __primaryContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'primaryContact'), 'primaryContact', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardprimaryContact', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1319, 12), )

    
    primaryContact = property(__primaryContact.value, __primaryContact.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}createCredentials uses Python identifier createCredentials
    __createCredentials = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'createCredentials'), 'createCredentials', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardcreateCredentials', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1320, 12), )

    
    createCredentials = property(__createCredentials.value, __createCredentials.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}eCheck uses Python identifier eCheck
    __eCheck = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eCheck'), 'eCheck', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardeCheck', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1321, 12), )

    
    eCheck = property(__eCheck.value, __eCheck.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantFunding uses Python identifier subMerchantFunding
    __subMerchantFunding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subMerchantFunding'), 'subMerchantFunding', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardsubMerchantFunding', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1322, 12), )

    
    subMerchantFunding = property(__subMerchantFunding.value, __subMerchantFunding.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}settlementCurrency uses Python identifier settlementCurrency
    __settlementCurrency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'settlementCurrency'), 'settlementCurrency', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateRequest__httppayfac_vantivcnp_comapimerchantonboardsettlementCurrency', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1323, 12), )

    
    settlementCurrency = property(__settlementCurrency.value, __settlementCurrency.set, None, None)

    _ElementMap.update({
        __merchantName.name() : __merchantName,
        __amexMid.name() : __amexMid,
        __discoverConveyedMid.name() : __discoverConveyedMid,
        __url.name() : __url,
        __customerServiceNumber.name() : __customerServiceNumber,
        __hardCodedBillingDescriptor.name() : __hardCodedBillingDescriptor,
        __maxTransactionAmount.name() : __maxTransactionAmount,
        __purchaseCurrency.name() : __purchaseCurrency,
        __merchantCategoryCode.name() : __merchantCategoryCode,
        __taxAuthority.name() : __taxAuthority,
        __taxAuthorityState.name() : __taxAuthorityState,
        __bankRoutingNumber.name() : __bankRoutingNumber,
        __bankAccountNumber.name() : __bankAccountNumber,
        __pspMerchantId.name() : __pspMerchantId,
        __fraud.name() : __fraud,
        __amexAcquired.name() : __amexAcquired,
        __address.name() : __address,
        __primaryContact.name() : __primaryContact,
        __createCredentials.name() : __createCredentials,
        __eCheck.name() : __eCheck,
        __subMerchantFunding.name() : __subMerchantFunding,
        __settlementCurrency.name() : __settlementCurrency
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.subMerchantCreateRequest_ = subMerchantCreateRequest_
Namespace.addCategoryObject('typeBinding', 'subMerchantCreateRequest', subMerchantCreateRequest_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantFraudFeature with content type EMPTY
class subMerchantFraudFeature_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantFraudFeature with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantFraudFeature')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1334, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute enabled uses Python identifier enabled
    __enabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'enabled'), 'enabled', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantFraudFeature__enabled', pyxb.binding.datatypes.boolean)
    __enabled._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1336, 8)
    __enabled._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1336, 8)
    
    enabled = property(__enabled.value, __enabled.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __enabled.name() : __enabled
    })
_module_typeBindings.subMerchantFraudFeature_ = subMerchantFraudFeature_
Namespace.addCategoryObject('typeBinding', 'subMerchantFraudFeature', subMerchantFraudFeature_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantAmexAcquiredFeature with content type EMPTY
class subMerchantAmexAcquiredFeature_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantAmexAcquiredFeature with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantAmexAcquiredFeature')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1339, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute enabled uses Python identifier enabled
    __enabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'enabled'), 'enabled', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantAmexAcquiredFeature__enabled', pyxb.binding.datatypes.boolean)
    __enabled._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1341, 8)
    __enabled._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1341, 8)
    
    enabled = property(__enabled.value, __enabled.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __enabled.name() : __enabled
    })
_module_typeBindings.subMerchantAmexAcquiredFeature_ = subMerchantAmexAcquiredFeature_
Namespace.addCategoryObject('typeBinding', 'subMerchantAmexAcquiredFeature', subMerchantAmexAcquiredFeature_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantPrimaryContact with content type ELEMENT_ONLY
class subMerchantPrimaryContact (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantPrimaryContact with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantPrimaryContact')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1344, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstName'), 'firstName', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantPrimaryContact_httppayfac_vantivcnp_comapimerchantonboardfirstName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1346, 12), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastName'), 'lastName', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantPrimaryContact_httppayfac_vantivcnp_comapimerchantonboardlastName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1354, 12), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), 'emailAddress', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantPrimaryContact_httppayfac_vantivcnp_comapimerchantonboardemailAddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1362, 12), )

    
    emailAddress = property(__emailAddress.value, __emailAddress.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phone'), 'phone', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantPrimaryContact_httppayfac_vantivcnp_comapimerchantonboardphone', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1370, 12), )

    
    phone = property(__phone.value, __phone.set, None, None)

    _ElementMap.update({
        __firstName.name() : __firstName,
        __lastName.name() : __lastName,
        __emailAddress.name() : __emailAddress,
        __phone.name() : __phone
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.subMerchantPrimaryContact = subMerchantPrimaryContact
Namespace.addCategoryObject('typeBinding', 'subMerchantPrimaryContact', subMerchantPrimaryContact)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantECheckFeature with content type ELEMENT_ONLY
class subMerchantECheckFeature_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantECheckFeature with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantECheckFeature')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1381, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}eCheckCompanyName uses Python identifier eCheckCompanyName
    __eCheckCompanyName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eCheckCompanyName'), 'eCheckCompanyName', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantECheckFeature__httppayfac_vantivcnp_comapimerchantonboardeCheckCompanyName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1383, 12), )

    
    eCheckCompanyName = property(__eCheckCompanyName.value, __eCheckCompanyName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}eCheckBillingDescriptor uses Python identifier eCheckBillingDescriptor
    __eCheckBillingDescriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eCheckBillingDescriptor'), 'eCheckBillingDescriptor', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantECheckFeature__httppayfac_vantivcnp_comapimerchantonboardeCheckBillingDescriptor', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1391, 12), )

    
    eCheckBillingDescriptor = property(__eCheckBillingDescriptor.value, __eCheckBillingDescriptor.set, None, None)

    
    # Attribute enabled uses Python identifier enabled
    __enabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'enabled'), 'enabled', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantECheckFeature__enabled', pyxb.binding.datatypes.boolean)
    __enabled._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1400, 8)
    __enabled._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1400, 8)
    
    enabled = property(__enabled.value, __enabled.set, None, None)

    _ElementMap.update({
        __eCheckCompanyName.name() : __eCheckCompanyName,
        __eCheckBillingDescriptor.name() : __eCheckBillingDescriptor
    })
    _AttributeMap.update({
        __enabled.name() : __enabled
    })
_module_typeBindings.subMerchantECheckFeature_ = subMerchantECheckFeature_
Namespace.addCategoryObject('typeBinding', 'subMerchantECheckFeature', subMerchantECheckFeature_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantFunding with content type ELEMENT_ONLY
class subMerchantFunding (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantFunding with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantFunding')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1403, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}feeProfile uses Python identifier feeProfile
    __feeProfile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'feeProfile'), 'feeProfile', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantFunding_httppayfac_vantivcnp_comapimerchantonboardfeeProfile', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1405, 12), )

    
    feeProfile = property(__feeProfile.value, __feeProfile.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}fundingSubmerchantId uses Python identifier fundingSubmerchantId
    __fundingSubmerchantId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fundingSubmerchantId'), 'fundingSubmerchantId', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantFunding_httppayfac_vantivcnp_comapimerchantonboardfundingSubmerchantId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1413, 12), )

    
    fundingSubmerchantId = property(__fundingSubmerchantId.value, __fundingSubmerchantId.set, None, None)

    
    # Attribute enabled uses Python identifier enabled
    __enabled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'enabled'), 'enabled', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantFunding_enabled', pyxb.binding.datatypes.boolean, required=True)
    __enabled._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1422, 8)
    __enabled._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1422, 8)
    
    enabled = property(__enabled.value, __enabled.set, None, None)

    _ElementMap.update({
        __feeProfile.name() : __feeProfile,
        __fundingSubmerchantId.name() : __fundingSubmerchantId
    })
    _AttributeMap.update({
        __enabled.name() : __enabled
    })
_module_typeBindings.subMerchantFunding = subMerchantFunding
Namespace.addCategoryObject('typeBinding', 'subMerchantFunding', subMerchantFunding)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1448, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}paypageCredential uses Python identifier paypageCredential
    __paypageCredential = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paypageCredential'), 'paypageCredential', '__httppayfac_vantivcnp_comapimerchantonboard_CTD_ANON_2_httppayfac_vantivcnp_comapimerchantonboardpaypageCredential', True, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1450, 32), )

    
    paypageCredential = property(__paypageCredential.value, __paypageCredential.set, None, None)

    _ElementMap.update({
        __paypageCredential.name() : __paypageCredential
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1507, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}paypageCredential uses Python identifier paypageCredential
    __paypageCredential = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paypageCredential'), 'paypageCredential', '__httppayfac_vantivcnp_comapimerchantonboard_CTD_ANON_3_httppayfac_vantivcnp_comapimerchantonboardpaypageCredential', True, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1509, 32), )

    
    paypageCredential = property(__paypageCredential.value, __paypageCredential.set, None, None)

    _ElementMap.update({
        __paypageCredential.name() : __paypageCredential
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCredentials with content type ELEMENT_ONLY
class subMerchantCredentials (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCredentials with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantCredentials')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1519, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}username uses Python identifier username
    __username = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'username'), 'username', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCredentials_httppayfac_vantivcnp_comapimerchantonboardusername', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1521, 12), )

    
    username = property(__username.value, __username.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}password uses Python identifier password
    __password = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'password'), 'password', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCredentials_httppayfac_vantivcnp_comapimerchantonboardpassword', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1529, 12), )

    
    password = property(__password.value, __password.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}passwordExpirationDate uses Python identifier passwordExpirationDate
    __passwordExpirationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'passwordExpirationDate'), 'passwordExpirationDate', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCredentials_httppayfac_vantivcnp_comapimerchantonboardpasswordExpirationDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1537, 12), )

    
    passwordExpirationDate = property(__passwordExpirationDate.value, __passwordExpirationDate.set, None, None)

    _ElementMap.update({
        __username.name() : __username,
        __password.name() : __password,
        __passwordExpirationDate.name() : __passwordExpirationDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.subMerchantCredentials = subMerchantCredentials
Namespace.addCategoryObject('typeBinding', 'subMerchantCredentials', subMerchantCredentials)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}paypageCredential with content type ELEMENT_ONLY
class paypageCredential (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}paypageCredential with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'paypageCredential')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1541, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}username uses Python identifier username
    __username = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'username'), 'username', '__httppayfac_vantivcnp_comapimerchantonboard_paypageCredential_httppayfac_vantivcnp_comapimerchantonboardusername', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1543, 12), )

    
    username = property(__username.value, __username.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}paypageId uses Python identifier paypageId
    __paypageId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paypageId'), 'paypageId', '__httppayfac_vantivcnp_comapimerchantonboard_paypageCredential_httppayfac_vantivcnp_comapimerchantonboardpaypageId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1551, 12), )

    
    paypageId = property(__paypageId.value, __paypageId.set, None, None)

    _ElementMap.update({
        __username.name() : __username,
        __paypageId.name() : __paypageId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.paypageCredential = paypageCredential
Namespace.addCategoryObject('typeBinding', 'paypageCredential', paypageCredential)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantUpdateRequest with content type ELEMENT_ONLY
class subMerchantUpdateRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantUpdateRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantUpdateRequest')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1562, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}merchantName uses Python identifier merchantName
    __merchantName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'merchantName'), 'merchantName', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardmerchantName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1564, 12), )

    
    merchantName = property(__merchantName.value, __merchantName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}amexMid uses Python identifier amexMid
    __amexMid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amexMid'), 'amexMid', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardamexMid', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1572, 12), )

    
    amexMid = property(__amexMid.value, __amexMid.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}discoverConveyedMid uses Python identifier discoverConveyedMid
    __discoverConveyedMid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'discoverConveyedMid'), 'discoverConveyedMid', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboarddiscoverConveyedMid', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1580, 12), )

    
    discoverConveyedMid = property(__discoverConveyedMid.value, __discoverConveyedMid.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'url'), 'url', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardurl', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1588, 12), )

    
    url = property(__url.value, __url.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}customerServiceNumber uses Python identifier customerServiceNumber
    __customerServiceNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'customerServiceNumber'), 'customerServiceNumber', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardcustomerServiceNumber', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1596, 12), )

    
    customerServiceNumber = property(__customerServiceNumber.value, __customerServiceNumber.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}hardCodedBillingDescriptor uses Python identifier hardCodedBillingDescriptor
    __hardCodedBillingDescriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'hardCodedBillingDescriptor'), 'hardCodedBillingDescriptor', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardhardCodedBillingDescriptor', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1604, 12), )

    
    hardCodedBillingDescriptor = property(__hardCodedBillingDescriptor.value, __hardCodedBillingDescriptor.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}maxTransactionAmount uses Python identifier maxTransactionAmount
    __maxTransactionAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maxTransactionAmount'), 'maxTransactionAmount', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardmaxTransactionAmount', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1612, 12), )

    
    maxTransactionAmount = property(__maxTransactionAmount.value, __maxTransactionAmount.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}bankRoutingNumber uses Python identifier bankRoutingNumber
    __bankRoutingNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bankRoutingNumber'), 'bankRoutingNumber', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardbankRoutingNumber', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1619, 12), )

    
    bankRoutingNumber = property(__bankRoutingNumber.value, __bankRoutingNumber.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}bankAccountNumber uses Python identifier bankAccountNumber
    __bankAccountNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'bankAccountNumber'), 'bankAccountNumber', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardbankAccountNumber', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1627, 12), )

    
    bankAccountNumber = property(__bankAccountNumber.value, __bankAccountNumber.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}pspMerchantId uses Python identifier pspMerchantId
    __pspMerchantId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pspMerchantId'), 'pspMerchantId', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardpspMerchantId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1635, 12), )

    
    pspMerchantId = property(__pspMerchantId.value, __pspMerchantId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}purchaseCurrency uses Python identifier purchaseCurrency
    __purchaseCurrency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'purchaseCurrency'), 'purchaseCurrency', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardpurchaseCurrency', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1643, 12), )

    
    purchaseCurrency = property(__purchaseCurrency.value, __purchaseCurrency.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address'), 'address', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardaddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1651, 12), )

    
    address = property(__address.value, __address.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}primaryContact uses Python identifier primaryContact
    __primaryContact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'primaryContact'), 'primaryContact', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardprimaryContact', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1652, 12), )

    
    primaryContact = property(__primaryContact.value, __primaryContact.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}disable uses Python identifier disable
    __disable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'disable'), 'disable', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboarddisable', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1653, 12), )

    
    disable = property(__disable.value, __disable.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}fraud uses Python identifier fraud
    __fraud = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fraud'), 'fraud', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardfraud', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1654, 12), )

    
    fraud = property(__fraud.value, __fraud.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}amexAcquired uses Python identifier amexAcquired
    __amexAcquired = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amexAcquired'), 'amexAcquired', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardamexAcquired', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1655, 12), )

    
    amexAcquired = property(__amexAcquired.value, __amexAcquired.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}eCheck uses Python identifier eCheck
    __eCheck = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'eCheck'), 'eCheck', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardeCheck', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1656, 12), )

    
    eCheck = property(__eCheck.value, __eCheck.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantFunding uses Python identifier subMerchantFunding
    __subMerchantFunding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subMerchantFunding'), 'subMerchantFunding', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardsubMerchantFunding', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1657, 12), )

    
    subMerchantFunding = property(__subMerchantFunding.value, __subMerchantFunding.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}taxAuthority uses Python identifier taxAuthority
    __taxAuthority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxAuthority'), 'taxAuthority', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardtaxAuthority', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1658, 12), )

    
    taxAuthority = property(__taxAuthority.value, __taxAuthority.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}taxAuthorityState uses Python identifier taxAuthorityState
    __taxAuthorityState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'taxAuthorityState'), 'taxAuthorityState', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantUpdateRequest__httppayfac_vantivcnp_comapimerchantonboardtaxAuthorityState', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1659, 12), )

    
    taxAuthorityState = property(__taxAuthorityState.value, __taxAuthorityState.set, None, None)

    _ElementMap.update({
        __merchantName.name() : __merchantName,
        __amexMid.name() : __amexMid,
        __discoverConveyedMid.name() : __discoverConveyedMid,
        __url.name() : __url,
        __customerServiceNumber.name() : __customerServiceNumber,
        __hardCodedBillingDescriptor.name() : __hardCodedBillingDescriptor,
        __maxTransactionAmount.name() : __maxTransactionAmount,
        __bankRoutingNumber.name() : __bankRoutingNumber,
        __bankAccountNumber.name() : __bankAccountNumber,
        __pspMerchantId.name() : __pspMerchantId,
        __purchaseCurrency.name() : __purchaseCurrency,
        __address.name() : __address,
        __primaryContact.name() : __primaryContact,
        __disable.name() : __disable,
        __fraud.name() : __fraud,
        __amexAcquired.name() : __amexAcquired,
        __eCheck.name() : __eCheck,
        __subMerchantFunding.name() : __subMerchantFunding,
        __taxAuthority.name() : __taxAuthority,
        __taxAuthorityState.name() : __taxAuthorityState
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.subMerchantUpdateRequest_ = subMerchantUpdateRequest_
Namespace.addCategoryObject('typeBinding', 'subMerchantUpdateRequest', subMerchantUpdateRequest_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantPrimaryContactUpdatable with content type ELEMENT_ONLY
class subMerchantPrimaryContactUpdatable (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantPrimaryContactUpdatable with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantPrimaryContactUpdatable')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1663, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstName'), 'firstName', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantPrimaryContactUpdatable_httppayfac_vantivcnp_comapimerchantonboardfirstName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1665, 12), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastName'), 'lastName', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantPrimaryContactUpdatable_httppayfac_vantivcnp_comapimerchantonboardlastName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1673, 12), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), 'emailAddress', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantPrimaryContactUpdatable_httppayfac_vantivcnp_comapimerchantonboardemailAddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1681, 12), )

    
    emailAddress = property(__emailAddress.value, __emailAddress.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phone'), 'phone', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantPrimaryContactUpdatable_httppayfac_vantivcnp_comapimerchantonboardphone', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1689, 12), )

    
    phone = property(__phone.value, __phone.set, None, None)

    _ElementMap.update({
        __firstName.name() : __firstName,
        __lastName.name() : __lastName,
        __emailAddress.name() : __emailAddress,
        __phone.name() : __phone
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.subMerchantPrimaryContactUpdatable = subMerchantPrimaryContactUpdatable
Namespace.addCategoryObject('typeBinding', 'subMerchantPrimaryContactUpdatable', subMerchantPrimaryContactUpdatable)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1705, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}error uses Python identifier error
    __error = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'error'), 'error', '__httppayfac_vantivcnp_comapimerchantonboard_CTD_ANON_4_httppayfac_vantivcnp_comapimerchantonboarderror', True, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1707, 32), )

    
    error = property(__error.value, __error.set, None, None)

    _ElementMap.update({
        __error.name() : __error
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1721, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}approvedMcc uses Python identifier approvedMcc
    __approvedMcc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'approvedMcc'), 'approvedMcc', '__httppayfac_vantivcnp_comapimerchantonboard_CTD_ANON_5_httppayfac_vantivcnp_comapimerchantonboardapprovedMcc', True, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1723, 32), )

    
    approvedMcc = property(__approvedMcc.value, __approvedMcc.set, None, None)

    _ElementMap.update({
        __approvedMcc.name() : __approvedMcc
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreementCreateRequest with content type ELEMENT_ONLY
class legalEntityAgreementCreateRequest_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreementCreateRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreementCreateRequest')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1732, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreement uses Python identifier legalEntityAgreement
    __legalEntityAgreement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreement'), 'legalEntityAgreement', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreementCreateRequest__httppayfac_vantivcnp_comapimerchantonboardlegalEntityAgreement', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1734, 12), )

    
    legalEntityAgreement = property(__legalEntityAgreement.value, __legalEntityAgreement.set, None, None)

    _ElementMap.update({
        __legalEntityAgreement.name() : __legalEntityAgreement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityAgreementCreateRequest_ = legalEntityAgreementCreateRequest_
Namespace.addCategoryObject('typeBinding', 'legalEntityAgreementCreateRequest', legalEntityAgreementCreateRequest_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreement with content type ELEMENT_ONLY
class legalEntityAgreement (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreement with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreement')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1739, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreementType uses Python identifier legalEntityAgreementType
    __legalEntityAgreementType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreementType'), 'legalEntityAgreementType', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreement_httppayfac_vantivcnp_comapimerchantonboardlegalEntityAgreementType', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1741, 12), )

    
    legalEntityAgreementType = property(__legalEntityAgreementType.value, __legalEntityAgreementType.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}agreementVersion uses Python identifier agreementVersion
    __agreementVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agreementVersion'), 'agreementVersion', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreement_httppayfac_vantivcnp_comapimerchantonboardagreementVersion', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1742, 12), )

    
    agreementVersion = property(__agreementVersion.value, __agreementVersion.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}userFullName uses Python identifier userFullName
    __userFullName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'userFullName'), 'userFullName', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreement_httppayfac_vantivcnp_comapimerchantonboarduserFullName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1750, 12), )

    
    userFullName = property(__userFullName.value, __userFullName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}userSystemName uses Python identifier userSystemName
    __userSystemName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'userSystemName'), 'userSystemName', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreement_httppayfac_vantivcnp_comapimerchantonboarduserSystemName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1758, 12), )

    
    userSystemName = property(__userSystemName.value, __userSystemName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}userIPAddress uses Python identifier userIPAddress
    __userIPAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'userIPAddress'), 'userIPAddress', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreement_httppayfac_vantivcnp_comapimerchantonboarduserIPAddress', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1766, 12), )

    
    userIPAddress = property(__userIPAddress.value, __userIPAddress.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}manuallyEntered uses Python identifier manuallyEntered
    __manuallyEntered = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'manuallyEntered'), 'manuallyEntered', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreement_httppayfac_vantivcnp_comapimerchantonboardmanuallyEntered', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1775, 12), )

    
    manuallyEntered = property(__manuallyEntered.value, __manuallyEntered.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}acceptanceDateTime uses Python identifier acceptanceDateTime
    __acceptanceDateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'acceptanceDateTime'), 'acceptanceDateTime', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreement_httppayfac_vantivcnp_comapimerchantonboardacceptanceDateTime', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1776, 12), )

    
    acceptanceDateTime = property(__acceptanceDateTime.value, __acceptanceDateTime.set, None, None)

    _ElementMap.update({
        __legalEntityAgreementType.name() : __legalEntityAgreementType,
        __agreementVersion.name() : __agreementVersion,
        __userFullName.name() : __userFullName,
        __userSystemName.name() : __userSystemName,
        __userIPAddress.name() : __userIPAddress,
        __manuallyEntered.name() : __manuallyEntered,
        __acceptanceDateTime.name() : __acceptanceDateTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityAgreement = legalEntityAgreement
Namespace.addCategoryObject('typeBinding', 'legalEntityAgreement', legalEntityAgreement)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreementRetrievalResponse with content type ELEMENT_ONLY
class legalEntityAgreementRetrievalResponse_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreementRetrievalResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreementRetrievalResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1788, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityId uses Python identifier legalEntityId
    __legalEntityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), 'legalEntityId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreementRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardlegalEntityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1790, 12), )

    
    legalEntityId = property(__legalEntityId.value, __legalEntityId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreementRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardtransactionId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1798, 12), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}agreements uses Python identifier agreements
    __agreements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'agreements'), 'agreements', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreementRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardagreements', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1799, 12), )

    
    agreements = property(__agreements.value, __agreements.set, None, None)

    _ElementMap.update({
        __legalEntityId.name() : __legalEntityId,
        __transactionId.name() : __transactionId,
        __agreements.name() : __agreements
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityAgreementRetrievalResponse_ = legalEntityAgreementRetrievalResponse_
Namespace.addCategoryObject('typeBinding', 'legalEntityAgreementRetrievalResponse', legalEntityAgreementRetrievalResponse_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1800, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreement uses Python identifier legalEntityAgreement
    __legalEntityAgreement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreement'), 'legalEntityAgreement', '__httppayfac_vantivcnp_comapimerchantonboard_CTD_ANON_6_httppayfac_vantivcnp_comapimerchantonboardlegalEntityAgreement', True, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1802, 24), )

    
    legalEntityAgreement = property(__legalEntityAgreement.value, __legalEntityAgreement.set, None, None)

    _ElementMap.update({
        __legalEntityAgreement.name() : __legalEntityAgreement
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipalCreateResponseWithResponseFields with content type ELEMENT_ONLY
class legalEntityPrincipalCreateResponseWithResponseFields_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipalCreateResponseWithResponseFields with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipalCreateResponseWithResponseFields')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1838, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principalId uses Python identifier principalId
    __principalId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principalId'), 'principalId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalCreateResponseWithResponseFields__httppayfac_vantivcnp_comapimerchantonboardprincipalId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1840, 12), )

    
    principalId = property(__principalId.value, __principalId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstName'), 'firstName', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalCreateResponseWithResponseFields__httppayfac_vantivcnp_comapimerchantonboardfirstName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1841, 12), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastName'), 'lastName', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalCreateResponseWithResponseFields__httppayfac_vantivcnp_comapimerchantonboardlastName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1849, 12), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}responseCode uses Python identifier responseCode
    __responseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseCode'), 'responseCode', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalCreateResponseWithResponseFields__httppayfac_vantivcnp_comapimerchantonboardresponseCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1857, 12), )

    
    responseCode = property(__responseCode.value, __responseCode.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}responseDescription uses Python identifier responseDescription
    __responseDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseDescription'), 'responseDescription', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalCreateResponseWithResponseFields__httppayfac_vantivcnp_comapimerchantonboardresponseDescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1858, 12), )

    
    responseDescription = property(__responseDescription.value, __responseDescription.set, None, None)

    _ElementMap.update({
        __principalId.name() : __principalId,
        __firstName.name() : __firstName,
        __lastName.name() : __lastName,
        __responseCode.name() : __responseCode,
        __responseDescription.name() : __responseDescription
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityPrincipalCreateResponseWithResponseFields_ = legalEntityPrincipalCreateResponseWithResponseFields_
Namespace.addCategoryObject('typeBinding', 'legalEntityPrincipalCreateResponseWithResponseFields', legalEntityPrincipalCreateResponseWithResponseFields_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalCreateResponse with content type ELEMENT_ONLY
class principalCreateResponse_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalCreateResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalCreateResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1870, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityId uses Python identifier legalEntityId
    __legalEntityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), 'legalEntityId', '__httppayfac_vantivcnp_comapimerchantonboard_principalCreateResponse__httppayfac_vantivcnp_comapimerchantonboardlegalEntityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1872, 12), )

    
    legalEntityId = property(__legalEntityId.value, __legalEntityId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principal'), 'principal', '__httppayfac_vantivcnp_comapimerchantonboard_principalCreateResponse__httppayfac_vantivcnp_comapimerchantonboardprincipal', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1880, 12), )

    
    principal = property(__principal.value, __principal.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httppayfac_vantivcnp_comapimerchantonboard_principalCreateResponse__httppayfac_vantivcnp_comapimerchantonboardtransactionId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1881, 12), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, None)

    _ElementMap.update({
        __legalEntityId.name() : __legalEntityId,
        __principal.name() : __principal,
        __transactionId.name() : __transactionId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.principalCreateResponse_ = principalCreateResponse_
Namespace.addCategoryObject('typeBinding', 'principalCreateResponse', principalCreateResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalDeleteResponse with content type ELEMENT_ONLY
class principalDeleteResponse_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}principalDeleteResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'principalDeleteResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1887, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httppayfac_vantivcnp_comapimerchantonboard_principalDeleteResponse__httppayfac_vantivcnp_comapimerchantonboardtransactionId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1889, 12), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityId uses Python identifier legalEntityId
    __legalEntityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), 'legalEntityId', '__httppayfac_vantivcnp_comapimerchantonboard_principalDeleteResponse__httppayfac_vantivcnp_comapimerchantonboardlegalEntityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1890, 12), )

    
    legalEntityId = property(__legalEntityId.value, __legalEntityId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principalId uses Python identifier principalId
    __principalId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principalId'), 'principalId', '__httppayfac_vantivcnp_comapimerchantonboard_principalDeleteResponse__httppayfac_vantivcnp_comapimerchantonboardprincipalId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1898, 12), )

    
    principalId = property(__principalId.value, __principalId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}responseDescription uses Python identifier responseDescription
    __responseDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseDescription'), 'responseDescription', '__httppayfac_vantivcnp_comapimerchantonboard_principalDeleteResponse__httppayfac_vantivcnp_comapimerchantonboardresponseDescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1899, 12), )

    
    responseDescription = property(__responseDescription.value, __responseDescription.set, None, None)

    _ElementMap.update({
        __transactionId.name() : __transactionId,
        __legalEntityId.name() : __legalEntityId,
        __principalId.name() : __principalId,
        __responseDescription.name() : __responseDescription
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.principalDeleteResponse_ = principalDeleteResponse_
Namespace.addCategoryObject('typeBinding', 'principalDeleteResponse', principalDeleteResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityResponse with content type ELEMENT_ONLY
class legalEntityResponse_ (response_):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 532, 4)
    _ElementMap = response_._ElementMap.copy()
    _AttributeMap = response_._AttributeMap.copy()
    # Base type is response_
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}backgroundCheckResults uses Python identifier backgroundCheckResults
    __backgroundCheckResults = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckResults'), 'backgroundCheckResults', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityResponse__httppayfac_vantivcnp_comapimerchantonboardbackgroundCheckResults', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 229, 4), )

    
    backgroundCheckResults = property(__backgroundCheckResults.value, __backgroundCheckResults.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityId uses Python identifier legalEntityId
    __legalEntityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), 'legalEntityId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityResponse__httppayfac_vantivcnp_comapimerchantonboardlegalEntityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 536, 20), )

    
    legalEntityId = property(__legalEntityId.value, __legalEntityId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}responseCode uses Python identifier responseCode
    __responseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseCode'), 'responseCode', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityResponse__httppayfac_vantivcnp_comapimerchantonboardresponseCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 544, 20), )

    
    responseCode = property(__responseCode.value, __responseCode.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}responseDescription uses Python identifier responseDescription
    __responseDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseDescription'), 'responseDescription', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityResponse__httppayfac_vantivcnp_comapimerchantonboardresponseDescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 545, 20), )

    
    responseDescription = property(__responseDescription.value, __responseDescription.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}originallegalEntityId uses Python identifier originallegalEntityId
    __originallegalEntityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originallegalEntityId'), 'originallegalEntityId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityResponse__httppayfac_vantivcnp_comapimerchantonboardoriginallegalEntityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 553, 20), )

    
    originallegalEntityId = property(__originallegalEntityId.value, __originallegalEntityId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}originallegalEntityStatus uses Python identifier originallegalEntityStatus
    __originallegalEntityStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originallegalEntityStatus'), 'originallegalEntityStatus', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityResponse__httppayfac_vantivcnp_comapimerchantonboardoriginallegalEntityStatus', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 561, 20), )

    
    originallegalEntityStatus = property(__originallegalEntityStatus.value, __originallegalEntityStatus.set, None, None)

    
    # Element transactionId ({http://payfac.vantivcnp.com/api/merchant/onboard}transactionId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}response
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duplicate'), 'duplicate', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityResponse__duplicate', pyxb.binding.datatypes.boolean)
    __duplicate._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 571, 16)
    __duplicate._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 571, 16)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    _ElementMap.update({
        __backgroundCheckResults.name() : __backgroundCheckResults,
        __legalEntityId.name() : __legalEntityId,
        __responseCode.name() : __responseCode,
        __responseDescription.name() : __responseDescription,
        __originallegalEntityId.name() : __originallegalEntityId,
        __originallegalEntityStatus.name() : __originallegalEntityStatus
    })
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })
_module_typeBindings.legalEntityResponse_ = legalEntityResponse_
Namespace.addCategoryObject('typeBinding', 'legalEntityResponse', legalEntityResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipalCreateResponse with content type ELEMENT_ONLY
class legalEntityPrincipalCreateResponse_ (response_):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipalCreateResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipalCreateResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 591, 4)
    _ElementMap = response_._ElementMap.copy()
    _AttributeMap = response_._AttributeMap.copy()
    # Base type is response_
    
    # Element transactionId ({http://payfac.vantivcnp.com/api/merchant/onboard}transactionId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}response
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principalId uses Python identifier principalId
    __principalId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principalId'), 'principalId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalCreateResponse__httppayfac_vantivcnp_comapimerchantonboardprincipalId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 595, 20), )

    
    principalId = property(__principalId.value, __principalId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'firstName'), 'firstName', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalCreateResponse__httppayfac_vantivcnp_comapimerchantonboardfirstName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 596, 20), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lastName'), 'lastName', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalCreateResponse__httppayfac_vantivcnp_comapimerchantonboardlastName', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 604, 20), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)

    _ElementMap.update({
        __principalId.name() : __principalId,
        __firstName.name() : __firstName,
        __lastName.name() : __lastName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityPrincipalCreateResponse_ = legalEntityPrincipalCreateResponse_
Namespace.addCategoryObject('typeBinding', 'legalEntityPrincipalCreateResponse', legalEntityPrincipalCreateResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityRetrievalResponse with content type ELEMENT_ONLY
class legalEntityRetrievalResponse_ (legalEntityCreateRequest_):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityRetrievalResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityRetrievalResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 617, 4)
    _ElementMap = legalEntityCreateRequest_._ElementMap.copy()
    _AttributeMap = legalEntityCreateRequest_._AttributeMap.copy()
    # Base type is legalEntityCreateRequest_
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}backgroundCheckResults uses Python identifier backgroundCheckResults
    __backgroundCheckResults = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckResults'), 'backgroundCheckResults', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardbackgroundCheckResults', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 229, 4), )

    
    backgroundCheckResults = property(__backgroundCheckResults.value, __backgroundCheckResults.set, None, None)

    
    # Element legalEntityName ({http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityName) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element legalEntityType ({http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityType) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element legalEntityOwnershipType ({http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityOwnershipType) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element doingBusinessAs ({http://payfac.vantivcnp.com/api/merchant/onboard}doingBusinessAs) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element taxId ({http://payfac.vantivcnp.com/api/merchant/onboard}taxId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element contactPhone ({http://payfac.vantivcnp.com/api/merchant/onboard}contactPhone) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element annualCreditCardSalesVolume ({http://payfac.vantivcnp.com/api/merchant/onboard}annualCreditCardSalesVolume) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element hasAcceptedCreditCards ({http://payfac.vantivcnp.com/api/merchant/onboard}hasAcceptedCreditCards) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element address ({http://payfac.vantivcnp.com/api/merchant/onboard}address) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element principal ({http://payfac.vantivcnp.com/api/merchant/onboard}principal) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element yearsInBusiness ({http://payfac.vantivcnp.com/api/merchant/onboard}yearsInBusiness) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateRequest
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipal uses Python identifier legalEntityPrincipal
    __legalEntityPrincipal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipal'), 'legalEntityPrincipal', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardlegalEntityPrincipal', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 621, 20), )

    
    legalEntityPrincipal = property(__legalEntityPrincipal.value, __legalEntityPrincipal.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityId uses Python identifier legalEntityId
    __legalEntityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), 'legalEntityId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardlegalEntityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 622, 20), )

    
    legalEntityId = property(__legalEntityId.value, __legalEntityId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}responseCode uses Python identifier responseCode
    __responseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseCode'), 'responseCode', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardresponseCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 630, 20), )

    
    responseCode = property(__responseCode.value, __responseCode.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}responseDescription uses Python identifier responseDescription
    __responseDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseDescription'), 'responseDescription', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardresponseDescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 631, 20), )

    
    responseDescription = property(__responseDescription.value, __responseDescription.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardtransactionId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 640, 20), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}updateDate uses Python identifier updateDate
    __updateDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'updateDate'), 'updateDate', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardupdateDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 648, 20), )

    
    updateDate = property(__updateDate.value, __updateDate.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}decisionDate uses Python identifier decisionDate
    __decisionDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'decisionDate'), 'decisionDate', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboarddecisionDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 649, 20), )

    
    decisionDate = property(__decisionDate.value, __decisionDate.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}tinValidationStatus uses Python identifier tinValidationStatus
    __tinValidationStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tinValidationStatus'), 'tinValidationStatus', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardtinValidationStatus', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 650, 20), )

    
    tinValidationStatus = property(__tinValidationStatus.value, __tinValidationStatus.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}sub_merchant_processing_status uses Python identifier sub_merchant_processing_status
    __sub_merchant_processing_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sub_merchant_processing_status'), 'sub_merchant_processing_status', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardsub_merchant_processing_status', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 658, 20), )

    
    sub_merchant_processing_status = property(__sub_merchant_processing_status.value, __sub_merchant_processing_status.set, None, None)

    
    # Attribute overallStatus uses Python identifier overallStatus
    __overallStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'overallStatus'), 'overallStatus', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityRetrievalResponse__overallStatus', _module_typeBindings.STD_ANON_36)
    __overallStatus._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 660, 16)
    __overallStatus._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 660, 16)
    
    overallStatus = property(__overallStatus.value, __overallStatus.set, None, None)

    _ElementMap.update({
        __backgroundCheckResults.name() : __backgroundCheckResults,
        __legalEntityPrincipal.name() : __legalEntityPrincipal,
        __legalEntityId.name() : __legalEntityId,
        __responseCode.name() : __responseCode,
        __responseDescription.name() : __responseDescription,
        __transactionId.name() : __transactionId,
        __updateDate.name() : __updateDate,
        __decisionDate.name() : __decisionDate,
        __tinValidationStatus.name() : __tinValidationStatus,
        __sub_merchant_processing_status.name() : __sub_merchant_processing_status
    })
    _AttributeMap.update({
        __overallStatus.name() : __overallStatus
    })
_module_typeBindings.legalEntityRetrievalResponse_ = legalEntityRetrievalResponse_
Namespace.addCategoryObject('typeBinding', 'legalEntityRetrievalResponse', legalEntityRetrievalResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateResponse with content type ELEMENT_ONLY
class subMerchantCreateResponse_ (response_):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantCreateResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1425, 4)
    _ElementMap = response_._ElementMap.copy()
    _AttributeMap = response_._AttributeMap.copy()
    # Base type is response_
    
    # Element transactionId ({http://payfac.vantivcnp.com/api/merchant/onboard}transactionId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}response
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantId uses Python identifier subMerchantId
    __subMerchantId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subMerchantId'), 'subMerchantId', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateResponse__httppayfac_vantivcnp_comapimerchantonboardsubMerchantId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1429, 20), )

    
    subMerchantId = property(__subMerchantId.value, __subMerchantId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}merchantIdentString uses Python identifier merchantIdentString
    __merchantIdentString = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'merchantIdentString'), 'merchantIdentString', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateResponse__httppayfac_vantivcnp_comapimerchantonboardmerchantIdentString', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1437, 20), )

    
    merchantIdentString = property(__merchantIdentString.value, __merchantIdentString.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}originalSubMerchant uses Python identifier originalSubMerchant
    __originalSubMerchant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalSubMerchant'), 'originalSubMerchant', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateResponse__httppayfac_vantivcnp_comapimerchantonboardoriginalSubMerchant', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1445, 20), )

    
    originalSubMerchant = property(__originalSubMerchant.value, __originalSubMerchant.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}credentials uses Python identifier credentials
    __credentials = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'credentials'), 'credentials', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateResponse__httppayfac_vantivcnp_comapimerchantonboardcredentials', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1446, 20), )

    
    credentials = property(__credentials.value, __credentials.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}paypageCredentials uses Python identifier paypageCredentials
    __paypageCredentials = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paypageCredentials'), 'paypageCredentials', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateResponse__httppayfac_vantivcnp_comapimerchantonboardpaypageCredentials', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1447, 20), )

    
    paypageCredentials = property(__paypageCredentials.value, __paypageCredentials.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}amexSellerId uses Python identifier amexSellerId
    __amexSellerId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amexSellerId'), 'amexSellerId', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateResponse__httppayfac_vantivcnp_comapimerchantonboardamexSellerId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1454, 20), )

    
    amexSellerId = property(__amexSellerId.value, __amexSellerId.set, None, None)

    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duplicate'), 'duplicate', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantCreateResponse__duplicate', pyxb.binding.datatypes.boolean)
    __duplicate._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1463, 16)
    __duplicate._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1463, 16)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    _ElementMap.update({
        __subMerchantId.name() : __subMerchantId,
        __merchantIdentString.name() : __merchantIdentString,
        __originalSubMerchant.name() : __originalSubMerchant,
        __credentials.name() : __credentials,
        __paypageCredentials.name() : __paypageCredentials,
        __amexSellerId.name() : __amexSellerId
    })
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })
_module_typeBindings.subMerchantCreateResponse_ = subMerchantCreateResponse_
Namespace.addCategoryObject('typeBinding', 'subMerchantCreateResponse', subMerchantCreateResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantRetrievalResponse with content type ELEMENT_ONLY
class subMerchantRetrievalResponse_ (subMerchantCreateRequest_):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantRetrievalResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subMerchantRetrievalResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1468, 4)
    _ElementMap = subMerchantCreateRequest_._ElementMap.copy()
    _AttributeMap = subMerchantCreateRequest_._AttributeMap.copy()
    # Base type is subMerchantCreateRequest_
    
    # Element merchantName ({http://payfac.vantivcnp.com/api/merchant/onboard}merchantName) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element amexMid ({http://payfac.vantivcnp.com/api/merchant/onboard}amexMid) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element discoverConveyedMid ({http://payfac.vantivcnp.com/api/merchant/onboard}discoverConveyedMid) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element url ({http://payfac.vantivcnp.com/api/merchant/onboard}url) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element customerServiceNumber ({http://payfac.vantivcnp.com/api/merchant/onboard}customerServiceNumber) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element hardCodedBillingDescriptor ({http://payfac.vantivcnp.com/api/merchant/onboard}hardCodedBillingDescriptor) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element maxTransactionAmount ({http://payfac.vantivcnp.com/api/merchant/onboard}maxTransactionAmount) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element purchaseCurrency ({http://payfac.vantivcnp.com/api/merchant/onboard}purchaseCurrency) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element merchantCategoryCode ({http://payfac.vantivcnp.com/api/merchant/onboard}merchantCategoryCode) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element taxAuthority ({http://payfac.vantivcnp.com/api/merchant/onboard}taxAuthority) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element taxAuthorityState ({http://payfac.vantivcnp.com/api/merchant/onboard}taxAuthorityState) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element bankRoutingNumber ({http://payfac.vantivcnp.com/api/merchant/onboard}bankRoutingNumber) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element bankAccountNumber ({http://payfac.vantivcnp.com/api/merchant/onboard}bankAccountNumber) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element pspMerchantId ({http://payfac.vantivcnp.com/api/merchant/onboard}pspMerchantId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element fraud ({http://payfac.vantivcnp.com/api/merchant/onboard}fraud) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element amexAcquired ({http://payfac.vantivcnp.com/api/merchant/onboard}amexAcquired) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element address ({http://payfac.vantivcnp.com/api/merchant/onboard}address) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element primaryContact ({http://payfac.vantivcnp.com/api/merchant/onboard}primaryContact) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element createCredentials ({http://payfac.vantivcnp.com/api/merchant/onboard}createCredentials) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element eCheck ({http://payfac.vantivcnp.com/api/merchant/onboard}eCheck) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element subMerchantFunding ({http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantFunding) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element settlementCurrency ({http://payfac.vantivcnp.com/api/merchant/onboard}settlementCurrency) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantCreateRequest
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}subMerchantId uses Python identifier subMerchantId
    __subMerchantId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subMerchantId'), 'subMerchantId', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardsubMerchantId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1472, 20), )

    
    subMerchantId = property(__subMerchantId.value, __subMerchantId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}amexSellerId uses Python identifier amexSellerId
    __amexSellerId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'amexSellerId'), 'amexSellerId', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardamexSellerId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1480, 20), )

    
    amexSellerId = property(__amexSellerId.value, __amexSellerId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}disabled uses Python identifier disabled
    __disabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'disabled'), 'disabled', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboarddisabled', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1488, 20), )

    
    disabled = property(__disabled.value, __disabled.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), 'transactionId', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardtransactionId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1489, 20), )

    
    transactionId = property(__transactionId.value, __transactionId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}merchantIdentString uses Python identifier merchantIdentString
    __merchantIdentString = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'merchantIdentString'), 'merchantIdentString', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardmerchantIdentString', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1497, 20), )

    
    merchantIdentString = property(__merchantIdentString.value, __merchantIdentString.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}credentials uses Python identifier credentials
    __credentials = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'credentials'), 'credentials', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardcredentials', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1505, 20), )

    
    credentials = property(__credentials.value, __credentials.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}paypageCredentials uses Python identifier paypageCredentials
    __paypageCredentials = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'paypageCredentials'), 'paypageCredentials', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardpaypageCredentials', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1506, 20), )

    
    paypageCredentials = property(__paypageCredentials.value, __paypageCredentials.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}updateDate uses Python identifier updateDate
    __updateDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'updateDate'), 'updateDate', '__httppayfac_vantivcnp_comapimerchantonboard_subMerchantRetrievalResponse__httppayfac_vantivcnp_comapimerchantonboardupdateDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1513, 20), )

    
    updateDate = property(__updateDate.value, __updateDate.set, None, None)

    _ElementMap.update({
        __subMerchantId.name() : __subMerchantId,
        __amexSellerId.name() : __amexSellerId,
        __disabled.name() : __disabled,
        __transactionId.name() : __transactionId,
        __merchantIdentString.name() : __merchantIdentString,
        __credentials.name() : __credentials,
        __paypageCredentials.name() : __paypageCredentials,
        __updateDate.name() : __updateDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.subMerchantRetrievalResponse_ = subMerchantRetrievalResponse_
Namespace.addCategoryObject('typeBinding', 'subMerchantRetrievalResponse', subMerchantRetrievalResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}errorResponse with content type ELEMENT_ONLY
class errorResponse_ (response_):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}errorResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'errorResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1700, 4)
    _ElementMap = response_._ElementMap.copy()
    _AttributeMap = response_._AttributeMap.copy()
    # Base type is response_
    
    # Element transactionId ({http://payfac.vantivcnp.com/api/merchant/onboard}transactionId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}response
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}errors uses Python identifier errors
    __errors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errors'), 'errors', '__httppayfac_vantivcnp_comapimerchantonboard_errorResponse__httppayfac_vantivcnp_comapimerchantonboarderrors', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1704, 20), )

    
    errors = property(__errors.value, __errors.set, None, None)

    _ElementMap.update({
        __errors.name() : __errors
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.errorResponse_ = errorResponse_
Namespace.addCategoryObject('typeBinding', 'errorResponse', errorResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}approvedMccResponse with content type ELEMENT_ONLY
class approvedMccResponse_ (response_):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}approvedMccResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'approvedMccResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1716, 4)
    _ElementMap = response_._ElementMap.copy()
    _AttributeMap = response_._AttributeMap.copy()
    # Base type is response_
    
    # Element transactionId ({http://payfac.vantivcnp.com/api/merchant/onboard}transactionId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}response
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}approvedMccs uses Python identifier approvedMccs
    __approvedMccs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'approvedMccs'), 'approvedMccs', '__httppayfac_vantivcnp_comapimerchantonboard_approvedMccResponse__httppayfac_vantivcnp_comapimerchantonboardapprovedMccs', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1720, 20), )

    
    approvedMccs = property(__approvedMccs.value, __approvedMccs.set, None, None)

    _ElementMap.update({
        __approvedMccs.name() : __approvedMccs
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.approvedMccResponse_ = approvedMccResponse_
Namespace.addCategoryObject('typeBinding', 'approvedMccResponse', approvedMccResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreementCreateResponse with content type ELEMENT_ONLY
class legalEntityAgreementCreateResponse_ (response_):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityAgreementCreateResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreementCreateResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1780, 4)
    _ElementMap = response_._ElementMap.copy()
    _AttributeMap = response_._AttributeMap.copy()
    # Base type is response_
    
    # Element transactionId ({http://payfac.vantivcnp.com/api/merchant/onboard}transactionId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}response
    
    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duplicate'), 'duplicate', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityAgreementCreateResponse__duplicate', pyxb.binding.datatypes.boolean)
    __duplicate._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1783, 16)
    __duplicate._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1783, 16)
    
    duplicate = property(__duplicate.value, __duplicate.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })
_module_typeBindings.legalEntityAgreementCreateResponse_ = legalEntityAgreementCreateResponse_
Namespace.addCategoryObject('typeBinding', 'legalEntityAgreementCreateResponse', legalEntityAgreementCreateResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipalDeleteResponse with content type ELEMENT_ONLY
class legalEntityPrincipalDeleteResponse_ (response_):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityPrincipalDeleteResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipalDeleteResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1810, 4)
    _ElementMap = response_._ElementMap.copy()
    _AttributeMap = response_._AttributeMap.copy()
    # Base type is response_
    
    # Element transactionId ({http://payfac.vantivcnp.com/api/merchant/onboard}transactionId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}response
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityId uses Python identifier legalEntityId
    __legalEntityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), 'legalEntityId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalDeleteResponse__httppayfac_vantivcnp_comapimerchantonboardlegalEntityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1814, 20), )

    
    legalEntityId = property(__legalEntityId.value, __legalEntityId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principalId uses Python identifier principalId
    __principalId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principalId'), 'principalId', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalDeleteResponse__httppayfac_vantivcnp_comapimerchantonboardprincipalId', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1822, 20), )

    
    principalId = property(__principalId.value, __principalId.set, None, None)

    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}responseDescription uses Python identifier responseDescription
    __responseDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'responseDescription'), 'responseDescription', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityPrincipalDeleteResponse__httppayfac_vantivcnp_comapimerchantonboardresponseDescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1823, 20), )

    
    responseDescription = property(__responseDescription.value, __responseDescription.set, None, None)

    _ElementMap.update({
        __legalEntityId.name() : __legalEntityId,
        __principalId.name() : __principalId,
        __responseDescription.name() : __responseDescription
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityPrincipalDeleteResponse_ = legalEntityPrincipalDeleteResponse_
Namespace.addCategoryObject('typeBinding', 'legalEntityPrincipalDeleteResponse', legalEntityPrincipalDeleteResponse_)


# Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateResponse with content type ELEMENT_ONLY
class legalEntityCreateResponse_ (legalEntityResponse_):
    """Complex type {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityCreateResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'legalEntityCreateResponse')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 520, 4)
    _ElementMap = legalEntityResponse_._ElementMap.copy()
    _AttributeMap = legalEntityResponse_._AttributeMap.copy()
    # Base type is legalEntityResponse_
    
    # Element backgroundCheckResults ({http://payfac.vantivcnp.com/api/merchant/onboard}backgroundCheckResults) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityResponse
    
    # Element {http://payfac.vantivcnp.com/api/merchant/onboard}principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'principal'), 'principal', '__httppayfac_vantivcnp_comapimerchantonboard_legalEntityCreateResponse__httppayfac_vantivcnp_comapimerchantonboardprincipal', False, pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 524, 20), )

    
    principal = property(__principal.value, __principal.set, None, None)

    
    # Element legalEntityId ({http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityResponse
    
    # Element responseCode ({http://payfac.vantivcnp.com/api/merchant/onboard}responseCode) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityResponse
    
    # Element responseDescription ({http://payfac.vantivcnp.com/api/merchant/onboard}responseDescription) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityResponse
    
    # Element originallegalEntityId ({http://payfac.vantivcnp.com/api/merchant/onboard}originallegalEntityId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityResponse
    
    # Element originallegalEntityStatus ({http://payfac.vantivcnp.com/api/merchant/onboard}originallegalEntityStatus) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityResponse
    
    # Element transactionId ({http://payfac.vantivcnp.com/api/merchant/onboard}transactionId) inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}response
    
    # Attribute duplicate inherited from {http://payfac.vantivcnp.com/api/merchant/onboard}legalEntityResponse
    _ElementMap.update({
        __principal.name() : __principal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.legalEntityCreateResponse_ = legalEntityCreateResponse_
Namespace.addCategoryObject('typeBinding', 'legalEntityCreateResponse', legalEntityCreateResponse_)


backgroundCheckResults = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckResults'), backgroundCheckResults_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 229, 4))
Namespace.addCategoryObject('elementBinding', backgroundCheckResults.name().localName(), backgroundCheckResults)

legalEntityCreateRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityCreateRequest'), legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 233, 4))
Namespace.addCategoryObject('elementBinding', legalEntityCreateRequest.name().localName(), legalEntityCreateRequest)

legalEntityUpdateRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityUpdateRequest'), legalEntityUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 241, 4))
Namespace.addCategoryObject('elementBinding', legalEntityUpdateRequest.name().localName(), legalEntityUpdateRequest)

legalEntityPrincipalCreateRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipalCreateRequest'), legalEntityPrincipalCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 243, 4))
Namespace.addCategoryObject('elementBinding', legalEntityPrincipalCreateRequest.name().localName(), legalEntityPrincipalCreateRequest)

principalCreateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principalCreateResponse'), principalCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 245, 4))
Namespace.addCategoryObject('elementBinding', principalCreateResponse.name().localName(), principalCreateResponse)

legalEntityPrincipalCreateResponseWithResponseFields = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipalCreateResponseWithResponseFields'), legalEntityPrincipalCreateResponseWithResponseFields_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 247, 4))
Namespace.addCategoryObject('elementBinding', legalEntityPrincipalCreateResponseWithResponseFields.name().localName(), legalEntityPrincipalCreateResponseWithResponseFields)

response = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'response'), response_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 253, 4))
Namespace.addCategoryObject('elementBinding', response.name().localName(), response)

subMerchantCreateRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantCreateRequest'), subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 255, 4))
Namespace.addCategoryObject('elementBinding', subMerchantCreateRequest.name().localName(), subMerchantCreateRequest)

subMerchantECheckFeature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantECheckFeature'), subMerchantECheckFeature_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 259, 4))
Namespace.addCategoryObject('elementBinding', subMerchantECheckFeature.name().localName(), subMerchantECheckFeature)

subMerchantFraudFeature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantFraudFeature'), subMerchantFraudFeature_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 261, 4))
Namespace.addCategoryObject('elementBinding', subMerchantFraudFeature.name().localName(), subMerchantFraudFeature)

subMerchantAmexAcquiredFeature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantAmexAcquiredFeature'), subMerchantAmexAcquiredFeature_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 263, 4))
Namespace.addCategoryObject('elementBinding', subMerchantAmexAcquiredFeature.name().localName(), subMerchantAmexAcquiredFeature)

subMerchantUpdateRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantUpdateRequest'), subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 267, 4))
Namespace.addCategoryObject('elementBinding', subMerchantUpdateRequest.name().localName(), subMerchantUpdateRequest)

legalEntityAgreementCreateRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreementCreateRequest'), legalEntityAgreementCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 269, 4))
Namespace.addCategoryObject('elementBinding', legalEntityAgreementCreateRequest.name().localName(), legalEntityAgreementCreateRequest)

legalEntityAgreementRetrievalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreementRetrievalResponse'), legalEntityAgreementRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 273, 4))
Namespace.addCategoryObject('elementBinding', legalEntityAgreementRetrievalResponse.name().localName(), legalEntityAgreementRetrievalResponse)

principalDeleteResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principalDeleteResponse'), principalDeleteResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 275, 4))
Namespace.addCategoryObject('elementBinding', principalDeleteResponse.name().localName(), principalDeleteResponse)

approvedMccResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'approvedMccResponse'), approvedMccResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 227, 4))
Namespace.addCategoryObject('elementBinding', approvedMccResponse.name().localName(), approvedMccResponse)

errorResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errorResponse'), errorResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 231, 4))
Namespace.addCategoryObject('elementBinding', errorResponse.name().localName(), errorResponse)

legalEntityResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityResponse'), legalEntityResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 237, 4))
Namespace.addCategoryObject('elementBinding', legalEntityResponse.name().localName(), legalEntityResponse)

legalEntityRetrievalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityRetrievalResponse'), legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 239, 4))
Namespace.addCategoryObject('elementBinding', legalEntityRetrievalResponse.name().localName(), legalEntityRetrievalResponse)

legalEntityPrincipalCreateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipalCreateResponse'), legalEntityPrincipalCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 249, 4))
Namespace.addCategoryObject('elementBinding', legalEntityPrincipalCreateResponse.name().localName(), legalEntityPrincipalCreateResponse)

legalEntityPrincipalDeleteResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipalDeleteResponse'), legalEntityPrincipalDeleteResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 251, 4))
Namespace.addCategoryObject('elementBinding', legalEntityPrincipalDeleteResponse.name().localName(), legalEntityPrincipalDeleteResponse)

subMerchantCreateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantCreateResponse'), subMerchantCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 257, 4))
Namespace.addCategoryObject('elementBinding', subMerchantCreateResponse.name().localName(), subMerchantCreateResponse)

subMerchantRetrievalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantRetrievalResponse'), subMerchantRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 265, 4))
Namespace.addCategoryObject('elementBinding', subMerchantRetrievalResponse.name().localName(), subMerchantRetrievalResponse)

legalEntityAgreementCreateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreementCreateResponse'), legalEntityAgreementCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 271, 4))
Namespace.addCategoryObject('elementBinding', legalEntityAgreementCreateResponse.name().localName(), legalEntityAgreementCreateResponse)

legalEntityCreateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityCreateResponse'), legalEntityCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 235, 4))
Namespace.addCategoryObject('elementBinding', legalEntityCreateResponse.name().localName(), legalEntityCreateResponse)



legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityName'), STD_ANON, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 280, 12)))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityType'), legalEntityType, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 289, 12)))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityOwnershipType'), legalEntityOwnershipType, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 290, 12)))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'doingBusinessAs'), STD_ANON_, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 291, 12)))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxId'), STD_ANON_2, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 299, 12)))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contactPhone'), STD_ANON_3, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 307, 12)))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annualCreditCardSalesVolume'), pyxb.binding.datatypes.string, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 315, 12)))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasAcceptedCreditCards'), pyxb.binding.datatypes.boolean, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 316, 12)))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address'), address, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 317, 12)))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principal'), legalEntityPrincipal, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 318, 12)))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yearsInBusiness'), STD_ANON_4, scope=legalEntityCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 319, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 291, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 299, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 307, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 319, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 280, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityType')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 289, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityOwnershipType')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 290, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'doingBusinessAs')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 291, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 299, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contactPhone')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 307, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annualCreditCardSalesVolume')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 315, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasAcceptedCreditCards')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 316, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 317, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principal')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 318, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearsInBusiness')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 319, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
legalEntityCreateRequest_._Automaton = _BuildAutomaton()




address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1'), STD_ANON_5, scope=address, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 335, 12)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2'), STD_ANON_6, scope=address, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 343, 12)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), STD_ANON_7, scope=address, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 351, 12)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stateProvince'), STD_ANON_8, scope=address, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 359, 12)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), STD_ANON_9, scope=address, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 367, 12)))

address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), STD_ANON_10, scope=address, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 375, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 343, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 335, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 343, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 351, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stateProvince')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 359, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postalCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 367, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 375, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
address._Automaton = _BuildAutomaton_()




legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principalId'), pyxb.binding.datatypes.int, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 388, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), STD_ANON_11, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 389, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstName'), STD_ANON_12, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 397, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastName'), STD_ANON_13, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 405, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), STD_ANON_14, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 413, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ssn'), STD_ANON_15, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 421, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contactPhone'), STD_ANON_16, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 429, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dateOfBirth'), pyxb.binding.datatypes.date, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 437, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'driversLicense'), STD_ANON_17, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 438, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'driversLicenseState'), STD_ANON_18, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 446, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address'), principalAddress, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 454, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stakePercent'), STD_ANON_19, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 455, 12)))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principal'), principalResult, scope=legalEntityPrincipal, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 463, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 388, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 389, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 413, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 421, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 429, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 438, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 446, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 454, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 463, 12))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principalId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 388, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 389, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 397, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 405, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'emailAddress')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 413, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ssn')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 421, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contactPhone')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 429, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dateOfBirth')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 437, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'driversLicense')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 438, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'driversLicenseState')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 446, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 454, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stakePercent')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 455, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principal')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 463, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
legalEntityPrincipal._Automaton = _BuildAutomaton_2()




principalAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1'), STD_ANON_20, scope=principalAddress, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 469, 12)))

principalAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2'), STD_ANON_21, scope=principalAddress, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 477, 12)))

principalAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), STD_ANON_22, scope=principalAddress, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 485, 12)))

principalAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stateProvince'), STD_ANON_23, scope=principalAddress, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 493, 12)))

principalAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), STD_ANON_24, scope=principalAddress, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 501, 12)))

principalAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), STD_ANON_25, scope=principalAddress, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 509, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 469, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 477, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 485, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 493, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 501, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 509, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 469, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 477, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 485, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stateProvince')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 493, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postalCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 501, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 509, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
principalAddress._Automaton = _BuildAutomaton_3()




response_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), pyxb.binding.datatypes.long, scope=response_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(response_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
response_._Automaton = _BuildAutomaton_4()




legalEntityPrincipalCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principal'), legalEntityPrincipal, scope=legalEntityPrincipalCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 586, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principal')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 586, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
legalEntityPrincipalCreateRequest_._Automaton = _BuildAutomaton_5()




backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'business'), businessResult, scope=backgroundCheckResults_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 674, 12)))

backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principal'), principalResult, scope=backgroundCheckResults_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 675, 12)))

backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'businessToPrincipalAssociation'), businessToPrincipalAssociation, scope=backgroundCheckResults_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 676, 12)))

backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckDecisionNotes'), STD_ANON_37, scope=backgroundCheckResults_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 677, 12)))

backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bankruptcyData'), bankruptcyResult, scope=backgroundCheckResults_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 685, 12)))

backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lienResult'), lienResult, scope=backgroundCheckResults_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 686, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 674, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 675, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 676, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 677, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 685, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 686, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'business')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 674, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principal')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 675, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'businessToPrincipalAssociation')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 676, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckDecisionNotes')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 677, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bankruptcyData')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 685, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lienResult')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 686, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
backgroundCheckResults_._Automaton = _BuildAutomaton_6()




businessResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verificationResult'), businessVerificationResult, scope=businessResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 692, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 692, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(businessResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verificationResult')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 692, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
businessResult._Automaton = _BuildAutomaton_7()




businessVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'overallScore'), businessScore, scope=businessVerificationResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 698, 12)))

businessVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameAddressTaxIdAssociation'), nameAddressTaxIdAssociation, scope=businessVerificationResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 699, 12)))

businessVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameAddressPhoneAssociation'), businessNameAddressPhoneAssociation, scope=businessVerificationResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 700, 12)))

businessVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verificationIndicators'), businessVerificationIndicators, scope=businessVerificationResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 701, 12)))

businessVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'riskIndicators'), CTD_ANON, scope=businessVerificationResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 702, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 698, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 699, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 700, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 701, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 702, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(businessVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'overallScore')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 698, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(businessVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameAddressTaxIdAssociation')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 699, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(businessVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameAddressPhoneAssociation')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 700, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(businessVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verificationIndicators')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 701, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(businessVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'riskIndicators')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 702, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
businessVerificationResult._Automaton = _BuildAutomaton_8()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'riskIndicator'), potentialRiskIndicator, scope=CTD_ANON, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 705, 24)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 705, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'riskIndicator')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 705, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_9()




businessScore._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'score'), businessOverallScore, scope=businessScore, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 714, 12)))

businessScore._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), STD_ANON_38, scope=businessScore, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 715, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 714, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 715, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(businessScore._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'score')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 714, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(businessScore._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 715, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
businessScore._Automaton = _BuildAutomaton_10()




nameAddressTaxIdAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), nameAddressTaxIdAssociationCode, scope=nameAddressTaxIdAssociation, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 728, 12)))

nameAddressTaxIdAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), STD_ANON_39, scope=nameAddressTaxIdAssociation, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 729, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 728, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 729, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(nameAddressTaxIdAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 728, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(nameAddressTaxIdAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 729, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
nameAddressTaxIdAssociation._Automaton = _BuildAutomaton_11()




businessNameAddressPhoneAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), businessNameAddressPhoneAssociationCode, scope=businessNameAddressPhoneAssociation, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 742, 12)))

businessNameAddressPhoneAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), STD_ANON_40, scope=businessNameAddressPhoneAssociation, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 743, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 742, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 743, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(businessNameAddressPhoneAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 742, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(businessNameAddressPhoneAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 743, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
businessNameAddressPhoneAssociation._Automaton = _BuildAutomaton_12()




businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 756, 12)))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addressVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 757, 12)))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cityVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 758, 12)))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stateVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 759, 12)))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zipVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 760, 12)))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phoneVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 761, 12)))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxIdVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 762, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 756, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'addressVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 757, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cityVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 758, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stateVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 759, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zipVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 760, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phoneVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 761, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxIdVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 762, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
businessVerificationIndicators._Automaton = _BuildAutomaton_13()




potentialRiskIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), riskIndicatorCode, scope=potentialRiskIndicator, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 768, 12)))

potentialRiskIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), STD_ANON_41, scope=potentialRiskIndicator, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 769, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 768, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 769, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(potentialRiskIndicator._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 768, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(potentialRiskIndicator._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 769, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
potentialRiskIndicator._Automaton = _BuildAutomaton_14()




principalResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verificationResult'), principalVerificationResult, scope=principalResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 782, 12)))

principalResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckDecisionNotes'), STD_ANON_42, scope=principalResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 783, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 782, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 783, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(principalResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verificationResult')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 782, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(principalResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckDecisionNotes')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 783, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
principalResult._Automaton = _BuildAutomaton_15()




principalVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'overallScore'), principalScore, scope=principalVerificationResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 796, 12)))

principalVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameAddressSsnAssociation'), nameAddressSsnAssociation, scope=principalVerificationResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 797, 12)))

principalVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameAddressPhoneAssociation'), principalNameAddressPhoneAssociation, scope=principalVerificationResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 798, 12)))

principalVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verificationIndicators'), principalVerificationIndicators, scope=principalVerificationResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 799, 12)))

principalVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'riskIndicators'), CTD_ANON_, scope=principalVerificationResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 800, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 796, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 797, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 798, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 799, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 800, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(principalVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'overallScore')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 796, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(principalVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameAddressSsnAssociation')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 797, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(principalVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameAddressPhoneAssociation')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 798, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(principalVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verificationIndicators')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 799, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(principalVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'riskIndicators')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 800, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
principalVerificationResult._Automaton = _BuildAutomaton_16()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'riskIndicator'), potentialRiskIndicator, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 803, 24)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 803, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'riskIndicator')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 803, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_17()




principalScore._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'score'), principalOverallScore, scope=principalScore, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 812, 12)))

principalScore._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), STD_ANON_43, scope=principalScore, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 813, 12)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 812, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 813, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(principalScore._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'score')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 812, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(principalScore._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 813, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
principalScore._Automaton = _BuildAutomaton_18()




nameAddressSsnAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), nameAddressSsnAssociationCode, scope=nameAddressSsnAssociation, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 826, 12)))

nameAddressSsnAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), STD_ANON_44, scope=nameAddressSsnAssociation, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 827, 12)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 826, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 827, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(nameAddressSsnAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 826, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(nameAddressSsnAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 827, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
nameAddressSsnAssociation._Automaton = _BuildAutomaton_19()




principalNameAddressPhoneAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), principalNameAddressPhoneAssociationCode, scope=principalNameAddressPhoneAssociation, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 840, 12)))

principalNameAddressPhoneAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), STD_ANON_45, scope=principalNameAddressPhoneAssociation, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 841, 12)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 840, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 841, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(principalNameAddressPhoneAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 840, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(principalNameAddressPhoneAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 841, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
principalNameAddressPhoneAssociation._Automaton = _BuildAutomaton_20()




principalVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nameVerified'), pyxb.binding.datatypes.boolean, scope=principalVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 854, 12)))

principalVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'addressVerified'), pyxb.binding.datatypes.boolean, scope=principalVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 855, 12)))

principalVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phoneVerified'), pyxb.binding.datatypes.boolean, scope=principalVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 856, 12)))

principalVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ssnVerified'), pyxb.binding.datatypes.boolean, scope=principalVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 857, 12)))

principalVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dobVerified'), pyxb.binding.datatypes.boolean, scope=principalVerificationIndicators, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 858, 12)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(principalVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nameVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 854, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(principalVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'addressVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 855, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(principalVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phoneVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 856, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(principalVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ssnVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 857, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(principalVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dobVerified')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 858, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
principalVerificationIndicators._Automaton = _BuildAutomaton_21()




businessToPrincipalAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'score'), businessToPrincipalScore, scope=businessToPrincipalAssociation, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 864, 12)))

businessToPrincipalAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'description'), STD_ANON_46, scope=businessToPrincipalAssociation, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 865, 12)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 864, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 865, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(businessToPrincipalAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'score')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 864, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(businessToPrincipalAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'description')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 865, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
businessToPrincipalAssociation._Automaton = _BuildAutomaton_22()




bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bankruptcyType'), STD_ANON_47, scope=bankruptcyResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 878, 12)))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bankruptcyCount'), pyxb.binding.datatypes.int, scope=bankruptcyResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 886, 12)))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'companyName'), STD_ANON_48, scope=bankruptcyResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 887, 12)))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1'), STD_ANON_49, scope=bankruptcyResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 895, 12)))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2'), STD_ANON_50, scope=bankruptcyResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 903, 12)))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), STD_ANON_51, scope=bankruptcyResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 911, 12)))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'state'), STD_ANON_52, scope=bankruptcyResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 919, 12)))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zip'), STD_ANON_53, scope=bankruptcyResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 927, 12)))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zip4'), STD_ANON_54, scope=bankruptcyResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 935, 12)))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filingDate'), pyxb.binding.datatypes.date, scope=bankruptcyResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 943, 12)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 878, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 886, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 887, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 895, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 903, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 911, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 919, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 927, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 935, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 943, 12))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bankruptcyType')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 878, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bankruptcyCount')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 886, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'companyName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 887, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 895, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 903, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 911, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'state')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 919, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zip')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 927, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zip4')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 935, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filingDate')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 943, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
bankruptcyResult._Automaton = _BuildAutomaton_23()




lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lienType'), STD_ANON_55, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 949, 12)))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'releasedCount'), pyxb.binding.datatypes.int, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 957, 12)))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'unreleasedCount'), pyxb.binding.datatypes.int, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 958, 12)))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'companyName'), STD_ANON_56, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 959, 12)))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1'), STD_ANON_57, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 967, 12)))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2'), STD_ANON_58, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 975, 12)))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), STD_ANON_59, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 983, 12)))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'state'), STD_ANON_60, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 991, 12)))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zip'), STD_ANON_61, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 999, 12)))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'zip4'), STD_ANON_62, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1007, 12)))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filingDate'), pyxb.binding.datatypes.date, scope=lienResult, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1015, 12)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 949, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 957, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 958, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 959, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 967, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 975, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 983, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 991, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 999, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1007, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1015, 12))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lienType')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 949, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'releasedCount')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 957, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'unreleasedCount')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 958, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'companyName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 959, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 967, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 975, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 983, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'state')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 991, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zip')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 999, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'zip4')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1007, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filingDate')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1015, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
lienResult._Automaton = _BuildAutomaton_24()




legalEntityUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address'), addressUpdatable, scope=legalEntityUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1021, 12)))

legalEntityUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contactPhone'), STD_ANON_63, scope=legalEntityUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1022, 12)))

legalEntityUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'doingBusinessAs'), STD_ANON_64, scope=legalEntityUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1030, 12)))

legalEntityUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'annualCreditCardSalesVolume'), pyxb.binding.datatypes.long, scope=legalEntityUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1038, 12)))

legalEntityUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hasAcceptedCreditCards'), pyxb.binding.datatypes.boolean, scope=legalEntityUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1039, 12)))

legalEntityUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principal'), legalEntityPrincipalUpdatable, scope=legalEntityUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1040, 12)))

legalEntityUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckFields'), legalEntityBackgroundCheckFields, scope=legalEntityUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1041, 12)))

legalEntityUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityOwnershipType'), legalEntityOwnershipType, scope=legalEntityUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1042, 12)))

legalEntityUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yearsInBusiness'), STD_ANON_65, scope=legalEntityUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1043, 12)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1021, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1022, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1030, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1038, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1039, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1040, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1041, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1042, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1043, 12))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1021, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contactPhone')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1022, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'doingBusinessAs')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1030, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annualCreditCardSalesVolume')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1038, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasAcceptedCreditCards')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1039, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principal')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1040, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckFields')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1041, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityOwnershipType')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1042, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearsInBusiness')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1043, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
legalEntityUpdateRequest_._Automaton = _BuildAutomaton_25()




addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1'), STD_ANON_66, scope=addressUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1057, 12)))

addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2'), STD_ANON_67, scope=addressUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1065, 12)))

addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), STD_ANON_68, scope=addressUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1073, 12)))

addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stateProvince'), STD_ANON_69, scope=addressUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1081, 12)))

addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'postalCode'), STD_ANON_70, scope=addressUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1089, 12)))

addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryCode'), STD_ANON_71, scope=addressUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1097, 12)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1057, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1065, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1073, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1081, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1089, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1097, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress1')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1057, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'streetAddress2')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1065, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'city')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1073, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stateProvince')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1081, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'postalCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1089, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'countryCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1097, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
addressUpdatable._Automaton = _BuildAutomaton_26()




legalEntityPrincipalUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principalId'), pyxb.binding.datatypes.int, scope=legalEntityPrincipalUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1110, 12)))

legalEntityPrincipalUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), STD_ANON_72, scope=legalEntityPrincipalUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1111, 12)))

legalEntityPrincipalUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), STD_ANON_73, scope=legalEntityPrincipalUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1119, 12)))

legalEntityPrincipalUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contactPhone'), STD_ANON_74, scope=legalEntityPrincipalUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1127, 12)))

legalEntityPrincipalUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address'), principalAddress, scope=legalEntityPrincipalUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1135, 12)))

legalEntityPrincipalUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stakePercent'), STD_ANON_75, scope=legalEntityPrincipalUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1136, 12)))

legalEntityPrincipalUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckFields'), principalBackgroundCheckFields, scope=legalEntityPrincipalUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1144, 12)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1111, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1119, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1127, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1135, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1136, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1144, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principalId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1110, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'title')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1111, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'emailAddress')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1119, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contactPhone')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1127, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1135, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stakePercent')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1136, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckFields')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1144, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
legalEntityPrincipalUpdatable._Automaton = _BuildAutomaton_27()




principalBackgroundCheckFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstName'), STD_ANON_76, scope=principalBackgroundCheckFields, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1150, 12)))

principalBackgroundCheckFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastName'), STD_ANON_77, scope=principalBackgroundCheckFields, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1158, 12)))

principalBackgroundCheckFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ssn'), STD_ANON_78, scope=principalBackgroundCheckFields, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1166, 12)))

principalBackgroundCheckFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dateOfBirth'), pyxb.binding.datatypes.date, scope=principalBackgroundCheckFields, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1174, 12)))

principalBackgroundCheckFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'driversLicense'), STD_ANON_79, scope=principalBackgroundCheckFields, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1175, 12)))

principalBackgroundCheckFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'driversLicenseState'), STD_ANON_80, scope=principalBackgroundCheckFields, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1183, 12)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1150, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1158, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1166, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1174, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1175, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1183, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(principalBackgroundCheckFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1150, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(principalBackgroundCheckFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1158, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(principalBackgroundCheckFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ssn')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1166, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(principalBackgroundCheckFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dateOfBirth')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1174, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(principalBackgroundCheckFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'driversLicense')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1175, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(principalBackgroundCheckFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'driversLicenseState')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1183, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
principalBackgroundCheckFields._Automaton = _BuildAutomaton_28()




legalEntityBackgroundCheckFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityName'), STD_ANON_81, scope=legalEntityBackgroundCheckFields, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1196, 12)))

legalEntityBackgroundCheckFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityType'), legalEntityType, scope=legalEntityBackgroundCheckFields, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1205, 12)))

legalEntityBackgroundCheckFields._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxId'), STD_ANON_82, scope=legalEntityBackgroundCheckFields, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1206, 12)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1196, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1205, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1206, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityBackgroundCheckFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1196, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityBackgroundCheckFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityType')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1205, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityBackgroundCheckFields._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1206, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
legalEntityBackgroundCheckFields._Automaton = _BuildAutomaton_29()




subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'merchantName'), STD_ANON_83, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1219, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amexMid'), STD_ANON_84, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1227, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'discoverConveyedMid'), STD_ANON_85, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1235, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'url'), STD_ANON_86, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1243, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerServiceNumber'), STD_ANON_87, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1251, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hardCodedBillingDescriptor'), STD_ANON_88, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1259, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxTransactionAmount'), STD_ANON_89, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1267, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'purchaseCurrency'), STD_ANON_90, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1274, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'merchantCategoryCode'), STD_ANON_91, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1282, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxAuthority'), pyxb.binding.datatypes.string, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1290, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxAuthorityState'), pyxb.binding.datatypes.string, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1291, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bankRoutingNumber'), STD_ANON_92, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1292, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bankAccountNumber'), STD_ANON_93, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1300, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pspMerchantId'), STD_ANON_94, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1308, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fraud'), subMerchantFraudFeature_, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1316, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amexAcquired'), subMerchantAmexAcquiredFeature_, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1317, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address'), address, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1318, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'primaryContact'), subMerchantPrimaryContact, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1319, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'createCredentials'), pyxb.binding.datatypes.boolean, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1320, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eCheck'), subMerchantECheckFeature_, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1321, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantFunding'), subMerchantFunding, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1322, 12)))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'settlementCurrency'), STD_ANON_95, scope=subMerchantCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1323, 12)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1227, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1235, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1274, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1290, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1291, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1316, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1317, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1318, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1319, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1320, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1321, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1322, 12))
    counters.add(cc_11)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1219, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amexMid')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1227, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'discoverConveyedMid')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1235, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'url')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1243, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerServiceNumber')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1251, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hardCodedBillingDescriptor')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1259, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxTransactionAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1267, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'purchaseCurrency')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1274, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantCategoryCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1282, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxAuthority')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1290, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxAuthorityState')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1291, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bankRoutingNumber')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1292, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bankAccountNumber')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1300, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pspMerchantId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1308, 12))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fraud')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1316, 12))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amexAcquired')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1317, 12))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1318, 12))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'primaryContact')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1319, 12))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'createCredentials')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1320, 12))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eCheck')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1321, 12))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subMerchantFunding')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1322, 12))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'settlementCurrency')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1323, 12))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    st_21._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
subMerchantCreateRequest_._Automaton = _BuildAutomaton_30()




subMerchantPrimaryContact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstName'), STD_ANON_96, scope=subMerchantPrimaryContact, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1346, 12)))

subMerchantPrimaryContact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastName'), STD_ANON_97, scope=subMerchantPrimaryContact, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1354, 12)))

subMerchantPrimaryContact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), STD_ANON_98, scope=subMerchantPrimaryContact, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1362, 12)))

subMerchantPrimaryContact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phone'), STD_ANON_99, scope=subMerchantPrimaryContact, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1370, 12)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantPrimaryContact._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1346, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantPrimaryContact._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1354, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantPrimaryContact._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'emailAddress')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1362, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(subMerchantPrimaryContact._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phone')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1370, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
subMerchantPrimaryContact._Automaton = _BuildAutomaton_31()




subMerchantECheckFeature_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eCheckCompanyName'), STD_ANON_100, scope=subMerchantECheckFeature_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1383, 12)))

subMerchantECheckFeature_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eCheckBillingDescriptor'), STD_ANON_101, scope=subMerchantECheckFeature_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1391, 12)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1383, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1391, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantECheckFeature_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eCheckCompanyName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1383, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantECheckFeature_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eCheckBillingDescriptor')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1391, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
subMerchantECheckFeature_._Automaton = _BuildAutomaton_32()




subMerchantFunding._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'feeProfile'), STD_ANON_102, scope=subMerchantFunding, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1405, 12)))

subMerchantFunding._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fundingSubmerchantId'), STD_ANON_103, scope=subMerchantFunding, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1413, 12)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1405, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1413, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantFunding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'feeProfile')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1405, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantFunding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fundingSubmerchantId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1413, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
subMerchantFunding._Automaton = _BuildAutomaton_33()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paypageCredential'), paypageCredential, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1450, 32)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1450, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paypageCredential')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1450, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_34()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paypageCredential'), paypageCredential, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1509, 32)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1509, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paypageCredential')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1509, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_35()




subMerchantCredentials._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'username'), STD_ANON_111, scope=subMerchantCredentials, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1521, 12)))

subMerchantCredentials._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'password'), STD_ANON_112, scope=subMerchantCredentials, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1529, 12)))

subMerchantCredentials._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'passwordExpirationDate'), pyxb.binding.datatypes.dateTime, scope=subMerchantCredentials, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1537, 12)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1521, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1529, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1537, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantCredentials._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'username')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1521, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantCredentials._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'password')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1529, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantCredentials._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'passwordExpirationDate')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1537, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
subMerchantCredentials._Automaton = _BuildAutomaton_36()




paypageCredential._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'username'), STD_ANON_113, scope=paypageCredential, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1543, 12)))

paypageCredential._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paypageId'), STD_ANON_114, scope=paypageCredential, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1551, 12)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1543, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1551, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(paypageCredential._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'username')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1543, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(paypageCredential._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paypageId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1551, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
paypageCredential._Automaton = _BuildAutomaton_37()




subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'merchantName'), STD_ANON_115, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1564, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amexMid'), STD_ANON_116, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1572, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'discoverConveyedMid'), STD_ANON_117, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1580, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'url'), STD_ANON_118, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1588, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'customerServiceNumber'), STD_ANON_119, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1596, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'hardCodedBillingDescriptor'), STD_ANON_120, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1604, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maxTransactionAmount'), STD_ANON_121, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1612, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bankRoutingNumber'), STD_ANON_122, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1619, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'bankAccountNumber'), STD_ANON_123, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1627, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pspMerchantId'), STD_ANON_124, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1635, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'purchaseCurrency'), STD_ANON_125, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1643, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address'), addressUpdatable, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1651, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'primaryContact'), subMerchantPrimaryContactUpdatable, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1652, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'disable'), pyxb.binding.datatypes.boolean, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1653, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fraud'), subMerchantFraudFeature_, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1654, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amexAcquired'), subMerchantAmexAcquiredFeature_, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1655, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eCheck'), subMerchantECheckFeature_, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1656, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantFunding'), subMerchantFunding, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1657, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxAuthority'), pyxb.binding.datatypes.string, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1658, 12)))

subMerchantUpdateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'taxAuthorityState'), pyxb.binding.datatypes.string, scope=subMerchantUpdateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1659, 12)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1564, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1572, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1580, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1588, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1596, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1604, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1612, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1619, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1627, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1635, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1643, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1651, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1652, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1653, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1654, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1655, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1656, 12))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1657, 12))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1658, 12))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1659, 12))
    counters.add(cc_19)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1564, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amexMid')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1572, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'discoverConveyedMid')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1580, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'url')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1588, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerServiceNumber')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1596, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hardCodedBillingDescriptor')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1604, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxTransactionAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1612, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bankRoutingNumber')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1619, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bankAccountNumber')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1627, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pspMerchantId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1635, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'purchaseCurrency')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1643, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1651, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'primaryContact')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1652, 12))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'disable')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1653, 12))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fraud')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1654, 12))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amexAcquired')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1655, 12))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eCheck')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1656, 12))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subMerchantFunding')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1657, 12))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxAuthority')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1658, 12))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantUpdateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxAuthorityState')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1659, 12))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
subMerchantUpdateRequest_._Automaton = _BuildAutomaton_38()




subMerchantPrimaryContactUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstName'), STD_ANON_126, scope=subMerchantPrimaryContactUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1665, 12)))

subMerchantPrimaryContactUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastName'), STD_ANON_127, scope=subMerchantPrimaryContactUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1673, 12)))

subMerchantPrimaryContactUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'emailAddress'), STD_ANON_128, scope=subMerchantPrimaryContactUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1681, 12)))

subMerchantPrimaryContactUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phone'), STD_ANON_129, scope=subMerchantPrimaryContactUpdatable, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1689, 12)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1665, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1673, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1681, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1689, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantPrimaryContactUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1665, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantPrimaryContactUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1673, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantPrimaryContactUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'emailAddress')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1681, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantPrimaryContactUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phone')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1689, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
subMerchantPrimaryContactUpdatable._Automaton = _BuildAutomaton_39()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'error'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1707, 32)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1707, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'error')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1707, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_40()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'approvedMcc'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1723, 32)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1723, 32))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'approvedMcc')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1723, 32))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_41()




legalEntityAgreementCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreement'), legalEntityAgreement, scope=legalEntityAgreementCreateRequest_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1734, 12)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreementCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreement')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1734, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
legalEntityAgreementCreateRequest_._Automaton = _BuildAutomaton_42()




legalEntityAgreement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreementType'), legalEntityAgreementType, scope=legalEntityAgreement, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1741, 12)))

legalEntityAgreement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agreementVersion'), STD_ANON_130, scope=legalEntityAgreement, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1742, 12)))

legalEntityAgreement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'userFullName'), STD_ANON_131, scope=legalEntityAgreement, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1750, 12)))

legalEntityAgreement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'userSystemName'), STD_ANON_132, scope=legalEntityAgreement, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1758, 12)))

legalEntityAgreement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'userIPAddress'), STD_ANON_133, scope=legalEntityAgreement, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1766, 12)))

legalEntityAgreement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'manuallyEntered'), pyxb.binding.datatypes.boolean, scope=legalEntityAgreement, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1775, 12)))

legalEntityAgreement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'acceptanceDateTime'), pyxb.binding.datatypes.dateTime, scope=legalEntityAgreement, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1776, 12)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1766, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1775, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreement._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreementType')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1741, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreement._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agreementVersion')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1742, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreement._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'userFullName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1750, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreement._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'userSystemName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1758, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreement._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'userIPAddress')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1766, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreement._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'manuallyEntered')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1775, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreement._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'acceptanceDateTime')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1776, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
legalEntityAgreement._Automaton = _BuildAutomaton_43()




legalEntityAgreementRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), STD_ANON_134, scope=legalEntityAgreementRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1790, 12)))

legalEntityAgreementRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), pyxb.binding.datatypes.long, scope=legalEntityAgreementRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1798, 12)))

legalEntityAgreementRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agreements'), CTD_ANON_6, scope=legalEntityAgreementRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1799, 12)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1790, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1798, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1799, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreementRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1790, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreementRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1798, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreementRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'agreements')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1799, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
legalEntityAgreementRetrievalResponse_._Automaton = _BuildAutomaton_44()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreement'), legalEntityAgreement, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1802, 24)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1802, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityAgreement')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1802, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_45()




legalEntityPrincipalCreateResponseWithResponseFields_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principalId'), pyxb.binding.datatypes.int, scope=legalEntityPrincipalCreateResponseWithResponseFields_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1840, 12)))

legalEntityPrincipalCreateResponseWithResponseFields_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstName'), STD_ANON_137, scope=legalEntityPrincipalCreateResponseWithResponseFields_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1841, 12)))

legalEntityPrincipalCreateResponseWithResponseFields_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastName'), STD_ANON_138, scope=legalEntityPrincipalCreateResponseWithResponseFields_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1849, 12)))

legalEntityPrincipalCreateResponseWithResponseFields_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseCode'), pyxb.binding.datatypes.short, scope=legalEntityPrincipalCreateResponseWithResponseFields_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1857, 12)))

legalEntityPrincipalCreateResponseWithResponseFields_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseDescription'), STD_ANON_139, scope=legalEntityPrincipalCreateResponseWithResponseFields_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1858, 12)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1840, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1841, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1849, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1857, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1858, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalCreateResponseWithResponseFields_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principalId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1840, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalCreateResponseWithResponseFields_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1841, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalCreateResponseWithResponseFields_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1849, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalCreateResponseWithResponseFields_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1857, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalCreateResponseWithResponseFields_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseDescription')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1858, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
legalEntityPrincipalCreateResponseWithResponseFields_._Automaton = _BuildAutomaton_46()




principalCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), STD_ANON_140, scope=principalCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1872, 12)))

principalCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principal'), legalEntityPrincipalCreateResponseWithResponseFields_, scope=principalCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1880, 12)))

principalCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), pyxb.binding.datatypes.long, scope=principalCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1881, 12)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1872, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1880, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1881, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(principalCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1872, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(principalCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principal')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1880, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(principalCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1881, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
principalCreateResponse_._Automaton = _BuildAutomaton_47()




principalDeleteResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), pyxb.binding.datatypes.long, scope=principalDeleteResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1889, 12)))

principalDeleteResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), STD_ANON_141, scope=principalDeleteResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1890, 12)))

principalDeleteResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principalId'), pyxb.binding.datatypes.int, scope=principalDeleteResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1898, 12)))

principalDeleteResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseDescription'), STD_ANON_142, scope=principalDeleteResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1899, 12)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1889, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1890, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1898, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1899, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(principalDeleteResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1889, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(principalDeleteResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1890, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(principalDeleteResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principalId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1898, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(principalDeleteResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseDescription')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1899, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
principalDeleteResponse_._Automaton = _BuildAutomaton_48()




legalEntityResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckResults'), backgroundCheckResults_, scope=legalEntityResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 229, 4)))

legalEntityResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), STD_ANON_26, scope=legalEntityResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 536, 20)))

legalEntityResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseCode'), pyxb.binding.datatypes.short, scope=legalEntityResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 544, 20)))

legalEntityResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseDescription'), STD_ANON_27, scope=legalEntityResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 545, 20)))

legalEntityResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originallegalEntityId'), STD_ANON_28, scope=legalEntityResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 553, 20)))

legalEntityResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originallegalEntityStatus'), STD_ANON_29, scope=legalEntityResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 561, 20)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 536, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 544, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 545, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 553, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 561, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 569, 20))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 536, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 544, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseDescription')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 545, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originallegalEntityId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 553, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originallegalEntityStatus')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 561, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckResults')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 569, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
legalEntityResponse_._Automaton = _BuildAutomaton_49()




legalEntityPrincipalCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principalId'), pyxb.binding.datatypes.int, scope=legalEntityPrincipalCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 595, 20)))

legalEntityPrincipalCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'firstName'), STD_ANON_30, scope=legalEntityPrincipalCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 596, 20)))

legalEntityPrincipalCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lastName'), STD_ANON_31, scope=legalEntityPrincipalCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 604, 20)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 595, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 596, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 604, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principalId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 595, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'firstName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 596, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lastName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 604, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
legalEntityPrincipalCreateResponse_._Automaton = _BuildAutomaton_50()




legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckResults'), backgroundCheckResults_, scope=legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 229, 4)))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipal'), legalEntityPrincipal, scope=legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 621, 20)))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), STD_ANON_32, scope=legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 622, 20)))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseCode'), pyxb.binding.datatypes.short, scope=legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 630, 20)))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseDescription'), STD_ANON_33, scope=legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 631, 20)))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), STD_ANON_34, scope=legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 640, 20)))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'updateDate'), pyxb.binding.datatypes.dateTime, scope=legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 648, 20)))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'decisionDate'), pyxb.binding.datatypes.dateTime, scope=legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 649, 20)))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tinValidationStatus'), STD_ANON_35, scope=legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 650, 20)))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sub_merchant_processing_status'), pyxb.binding.datatypes.boolean, scope=legalEntityRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 658, 20)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 291, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 299, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 307, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 319, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 621, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 622, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 630, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 631, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 639, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 640, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 648, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 649, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 650, 20))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 280, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityType')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 289, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityOwnershipType')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 290, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'doingBusinessAs')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 291, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 299, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contactPhone')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 307, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'annualCreditCardSalesVolume')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 315, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hasAcceptedCreditCards')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 316, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 317, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principal')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 318, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearsInBusiness')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 319, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityPrincipal')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 621, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 622, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 630, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseDescription')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 631, 20))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckResults')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 639, 20))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 640, 20))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'updateDate')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 648, 20))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'decisionDate')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 649, 20))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tinValidationStatus')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 650, 20))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sub_merchant_processing_status')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 658, 20))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
legalEntityRetrievalResponse_._Automaton = _BuildAutomaton_51()




subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantId'), STD_ANON_104, scope=subMerchantCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1429, 20)))

subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'merchantIdentString'), STD_ANON_105, scope=subMerchantCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1437, 20)))

subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalSubMerchant'), subMerchantRetrievalResponse_, scope=subMerchantCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1445, 20)))

subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'credentials'), subMerchantCredentials, scope=subMerchantCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1446, 20)))

subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paypageCredentials'), CTD_ANON_2, scope=subMerchantCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1447, 20)))

subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amexSellerId'), STD_ANON_106, scope=subMerchantCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1454, 20)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1429, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1437, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1445, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1446, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1447, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1454, 20))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subMerchantId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1429, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantIdentString')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1437, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalSubMerchant')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1445, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credentials')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1446, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paypageCredentials')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1447, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amexSellerId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1454, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
subMerchantCreateResponse_._Automaton = _BuildAutomaton_52()




subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subMerchantId'), STD_ANON_107, scope=subMerchantRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1472, 20)))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'amexSellerId'), STD_ANON_108, scope=subMerchantRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1480, 20)))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'disabled'), pyxb.binding.datatypes.boolean, scope=subMerchantRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1488, 20)))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transactionId'), STD_ANON_109, scope=subMerchantRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1489, 20)))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'merchantIdentString'), STD_ANON_110, scope=subMerchantRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1497, 20)))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'credentials'), subMerchantCredentials, scope=subMerchantRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1505, 20)))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'paypageCredentials'), CTD_ANON_3, scope=subMerchantRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1506, 20)))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'updateDate'), pyxb.binding.datatypes.dateTime, scope=subMerchantRetrievalResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1513, 20)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1227, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1235, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1274, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1290, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1291, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1316, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1317, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1318, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1319, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1320, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1321, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1322, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1472, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1480, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1488, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1489, 20))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1497, 20))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1505, 20))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1506, 20))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1513, 20))
    counters.add(cc_19)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantName')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1219, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amexMid')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1227, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'discoverConveyedMid')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1235, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'url')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1243, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'customerServiceNumber')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1251, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'hardCodedBillingDescriptor')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1259, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maxTransactionAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1267, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'purchaseCurrency')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1274, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantCategoryCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1282, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxAuthority')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1290, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'taxAuthorityState')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1291, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bankRoutingNumber')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1292, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'bankAccountNumber')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1300, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pspMerchantId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1308, 12))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fraud')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1316, 12))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amexAcquired')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1317, 12))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1318, 12))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'primaryContact')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1319, 12))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'createCredentials')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1320, 12))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'eCheck')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1321, 12))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subMerchantFunding')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1322, 12))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'settlementCurrency')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1323, 12))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subMerchantId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1472, 20))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'amexSellerId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1480, 20))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'disabled')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1488, 20))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1489, 20))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantIdentString')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1497, 20))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'credentials')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1505, 20))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'paypageCredentials')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1506, 20))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'updateDate')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1513, 20))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, True) ]))
    st_29._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
subMerchantRetrievalResponse_._Automaton = _BuildAutomaton_53()




errorResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errors'), CTD_ANON_4, scope=errorResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1704, 20)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1704, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(errorResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(errorResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errors')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1704, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
errorResponse_._Automaton = _BuildAutomaton_54()




approvedMccResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'approvedMccs'), CTD_ANON_5, scope=approvedMccResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1720, 20)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1720, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(approvedMccResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(approvedMccResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'approvedMccs')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1720, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
approvedMccResponse_._Automaton = _BuildAutomaton_55()




def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityAgreementCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
legalEntityAgreementCreateResponse_._Automaton = _BuildAutomaton_56()




legalEntityPrincipalDeleteResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId'), STD_ANON_135, scope=legalEntityPrincipalDeleteResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1814, 20)))

legalEntityPrincipalDeleteResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principalId'), pyxb.binding.datatypes.int, scope=legalEntityPrincipalDeleteResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1822, 20)))

legalEntityPrincipalDeleteResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'responseDescription'), STD_ANON_136, scope=legalEntityPrincipalDeleteResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1823, 20)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1814, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1822, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1823, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalDeleteResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalDeleteResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1814, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalDeleteResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principalId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1822, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityPrincipalDeleteResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseDescription')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 1823, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
legalEntityPrincipalDeleteResponse_._Automaton = _BuildAutomaton_57()




legalEntityCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'principal'), legalEntityPrincipalCreateResponse_, scope=legalEntityCreateResponse_, location=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 524, 20)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 536, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 544, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 545, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 553, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 561, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 569, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 524, 20))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transactionId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 578, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'legalEntityId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 536, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseCode')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 544, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'responseDescription')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 545, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originallegalEntityId')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 553, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originallegalEntityStatus')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 561, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'backgroundCheckResults')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 569, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'principal')), pyxb.utils.utility.Location('/usr/local/litle-home/cchang/git/payfac-mp-sdk-python/schema/merchant-onboard-api-v13.xsd', 524, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
legalEntityCreateResponse_._Automaton = _BuildAutomaton_58()

