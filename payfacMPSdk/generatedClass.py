#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 23 10:59:30 2020 by generateDS.py version 2.35.20.
# Python 2.7.14 (default, Apr 23 2020, 08:59:37)  [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)]
#
# Command line options:
#   ('--namespacedef', 'xmlns:http://payfac.vantivcnp.com/api/merchant/onboard')
#   ('-o', 'generatedClass.py')
#
# Command line arguments:
#   /usr/local/litle-home/aviano/git/payfac-mp-sdk-python/payfacMPSdk/schema/merchant-onboard-api-v13.1.xsd
#
# Command line:
#   /usr/local/litle-home/aviano/git/payfac-mp-sdk-python/env27/bin/generateDS.py --namespacedef="xmlns:http://payfac.vantivcnp.com/api/merchant/onboard" -o "generatedClass.py" /usr/local/litle-home/aviano/git/payfac-mp-sdk-python/payfacMPSdk/schema/merchant-onboard-api-v13.1.xsd
#
# Current working directory (os.getcwd()):
#   payfac-mp-sdk-python
#

from six.moves import zip_longest
import os
import sys
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ImportError:
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ImportError:
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ImportError:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ImportError:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ImportError:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer valuess')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return ('%s' % input_data).rstrip('0')
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class businessNameAddressPhoneAssociationCode(Enum):
    NOT_VERIFIED='NOT_VERIFIED'
    WRONG_PHONE='WRONG_PHONE'
    NAME_OR_ADDRESS='NAME_OR_ADDRESS'
    BAD_NAME='BAD_NAME'
    BAD_ADDRESS='BAD_ADDRESS'
    MISSING_ADDRESS='MISSING_ADDRESS'
    NAME_AND_ADDRESS_BAD_PHONE='NAME_AND_ADDRESS_BAD_PHONE'
    NAME_AND_ADDRESS_NO_PHONE='NAME_AND_ADDRESS_NO_PHONE'
    NAME_ADDRESS_PHONE='NAME_ADDRESS_PHONE'


class businessOverallScore(Enum):
    _0='0'
    _1_0='10'
    _2_0='20'
    _3_0='30'
    _4_0='40'
    _5_0='50'


class businessToPrincipalScore(Enum):
    _0='0'
    _1_0='10'
    _2_0='20'
    _3_0='30'
    _4_0='40'
    _5_0='50'


class legalEntityAgreementType(Enum):
    MERCHANT_AGREEMENT='MERCHANT_AGREEMENT'


class legalEntityOwnershipType(Enum):
    PUBLIC='PUBLIC'
    PRIVATE='PRIVATE'


class legalEntityType(Enum):
    INDIVIDUAL_SOLE_PROPRIETORSHIP='INDIVIDUAL_SOLE_PROPRIETORSHIP'
    CORPORATION='CORPORATION'
    LIMITED_LIABILITY_COMPANY='LIMITED_LIABILITY_COMPANY'
    PARTNERSHIP='PARTNERSHIP'
    LIMITED_PARTNERSHIP='LIMITED_PARTNERSHIP'
    GENERAL_PARTNERSHIP='GENERAL_PARTNERSHIP'
    TAX_EXEMPT_ORGANIZATION='TAX_EXEMPT_ORGANIZATION'
    GOVERNMENT_AGENCY='GOVERNMENT_AGENCY'


class nameAddressSsnAssociationCode(Enum):
    NOTHING='NOTHING'
    WRONG_SSN='WRONG_SSN'
    FIRST_LAST='FIRST_LAST'
    FIRST_ADDRESS='FIRST_ADDRESS'
    FIRST_SSN='FIRST_SSN'
    LAST_ADDRESS='LAST_ADDRESS'
    ADDRESS_SSN='ADDRESS_SSN'
    LAST_SSN='LAST_SSN'
    FIRST_LAST_ADDRESS='FIRST_LAST_ADDRESS'
    FIRST_LAST_SSN='FIRST_LAST_SSN'
    FIRST_ADDRESS_SSN='FIRST_ADDRESS_SSN'
    LAST_ADDRESS_SSN='LAST_ADDRESS_SSN'
    FIRST_LAST_ADDRESS_SSN='FIRST_LAST_ADDRESS_SSN'


class nameAddressTaxIdAssociationCode(Enum):
    NOT_VERIFIED='NOT_VERIFIED'
    WRONG_TAX_ID='WRONG_TAX_ID'
    NAME_OR_ADDRESS='NAME_OR_ADDRESS'
    BAD_NAME='BAD_NAME'
    BAD_ADDRESS='BAD_ADDRESS'
    MISSING_ADDRESS='MISSING_ADDRESS'
    NAME_AND_ADDRESS_BAD_TAX_ID='NAME_AND_ADDRESS_BAD_TAX_ID'
    NAME_AND_ADDRESS_NO_TAX_ID='NAME_AND_ADDRESS_NO_TAX_ID'
    NAME_ADDRESS_TAX_ID='NAME_ADDRESS_TAX_ID'


class principalNameAddressPhoneAssociationCode(Enum):
    NOTHING='NOTHING'
    WRONG_PHONE='WRONG_PHONE'
    FIRST_LAST='FIRST_LAST'
    FIRST_ADDRESS='FIRST_ADDRESS'
    FIRST_PHONE='FIRST_PHONE'
    LAST_ADDRESS='LAST_ADDRESS'
    ADDRESS_PHONE='ADDRESS_PHONE'
    LAST_PHONE='LAST_PHONE'
    FIRST_LAST_ADDRESS='FIRST_LAST_ADDRESS'
    FIRST_LAST_PHONE='FIRST_LAST_PHONE'
    FIRST_ADDRESS_PHONE='FIRST_ADDRESS_PHONE'
    LAST_ADDRESS_PHONE='LAST_ADDRESS_PHONE'
    FIRST_LAST_ADDRESS_PHONE='FIRST_LAST_ADDRESS_PHONE'


class principalOverallScore(Enum):
    _0='0'
    _1_0='10'
    _2_0='20'
    _3_0='30'
    _4_0='40'
    _5_0='50'


class riskIndicatorCode(Enum):
    UNKNOWN='UNKNOWN'
    SSN_DECEASED='SSN_DECEASED'
    SSN_PRIOR_TO_DOB='SSN_PRIOR_TO_DOB'
    SSN_ADDRESS_PHONE_NOT_MATCH='SSN_ADDRESS_PHONE_NOT_MATCH'
    SSN_INVALID='SSN_INVALID'
    PHONE_NUMBER_DISCONNECTED='PHONE_NUMBER_DISCONNECTED'
    PHONE_NUMBER_INVALID='PHONE_NUMBER_INVALID'
    PHONE_NUMBER_PAGER='PHONE_NUMBER_PAGER'
    PHONE_NUMBER_MOBILE='PHONE_NUMBER_MOBILE'
    ADDRESS_INVALID='ADDRESS_INVALID'
    ZIP_BELONGS_POST_OFFICE='ZIP_BELONGS_POST_OFFICE'
    ADDRESS_INVALID_APARTMENT_DESIGNATION='ADDRESS_INVALID_APARTMENT_DESIGNATION'
    ADDRESS_COMMERCIAL='ADDRESS_COMMERCIAL'
    PHONE_NUMBER_COMMERCIAL='PHONE_NUMBER_COMMERCIAL'
    PHONE_NUMBER_ZIP_INVALID='PHONE_NUMBER_ZIP_INVALID'
    UNABLE_TO_VERIFY_NAS='UNABLE_TO_VERIFY_NAS'
    UNABLE_TO_VERIFY_ADDRESS='UNABLE_TO_VERIFY_ADDRESS'
    UNABLE_TO_VERIFY_SSN='UNABLE_TO_VERIFY_SSN'
    UNABLE_TO_VERIFY_PHONE='UNABLE_TO_VERIFY_PHONE'
    UNABLE_TO_VERIFY_DOB='UNABLE_TO_VERIFY_DOB'
    SSN_MISKEYED='SSN_MISKEYED'
    ADDRESS_MISKEYED='ADDRESS_MISKEYED'
    PHONE_NUMBER_MISKEYED='PHONE_NUMBER_MISKEYED'
    NAME_MATCHES_OFAC='NAME_MATCHES_OFAC'
    UNABLE_TO_VERIFY_NAME='UNABLE_TO_VERIFY_NAME'
    SSN_MATCHES_MULTI_NAMES='SSN_MATCHES_MULTI_NAMES'
    SSN_RECENTLY_ISSUED='SSN_RECENTLY_ISSUED'
    ZIP_CORPORATE_MILITARY='ZIP_CORPORATE_MILITARY'
    DLL_INVALID='DLL_INVALID'
    NAME_ADDRESS_MATCH_BANKRUPTCY='NAME_ADDRESS_MATCH_BANKRUPTCY'
    PHONE_AREA_CODE_CHANGING='PHONE_AREA_CODE_CHANGING'
    WORK_PHONE_PAGER='WORK_PHONE_PAGER'
    UNABLE_TO_VERIFY_FIRST_NAME='UNABLE_TO_VERIFY_FIRST_NAME'
    PHONE_ADDRESS_DISTANT='PHONE_ADDRESS_DISTANT'
    ADDRESS_MATCHES_PRISON='ADDRESS_MATCHES_PRISON'
    SSN_LAST_NAME_NO_MATCH='SSN_LAST_NAME_NO_MATCH'
    SSN_FIRST_NAME_NO_MATCH='SSN_FIRST_NAME_NO_MATCH'
    WORK_HOME_PHONE_DISTANT='WORK_HOME_PHONE_DISTANT'
    NAME_ADDRESS_TIN_MISMATCH='NAME_ADDRESS_TIN_MISMATCH'
    WORK_PHONE_INVALID='WORK_PHONE_INVALID'
    WORK_PHONE_DISCONNECTED='WORK_PHONE_DISCONNECTED'
    WORK_PHONE_MOBILE='WORK_PHONE_MOBILE'
    ADDRESS_RETURNS_DIFF_PHONE='ADDRESS_RETURNS_DIFF_PHONE'
    SSN_LNAME_NOT_MATCHED_FNAME_MATCHED='SSN_LNAME_NOT_MATCHED_FNAME_MATCHED'
    PHONE_RESIDENTIAL_LISTING='PHONE_RESIDENTIAL_LISTING'
    SINGLE_FAMILY_DWELLING='SINGLE_FAMILY_DWELLING'
    SSN_NOT_FOUND='SSN_NOT_FOUND'
    SSN_BELONGS_TO_DIFF_NAME_ADDRESS='SSN_BELONGS_TO_DIFF_NAME_ADDRESS'
    PHONE_BELONGS_TO_DIFF_NAME_ADDRESS='PHONE_BELONGS_TO_DIFF_NAME_ADDRESS'
    NAME_ADDRESS_UNLISTED='NAME_ADDRESS_UNLISTED'
    NAME_MISKEYED='NAME_MISKEYED'
    NAME_MISSING='NAME_MISSING'
    ADDRESS_MISSING='ADDRESS_MISSING'
    SSN_MISSING='SSN_MISSING'
    PHONE_NUMBER_MISSING='PHONE_NUMBER_MISSING'
    DOB_MISSING='DOB_MISSING'
    NAME_ADDRESS_RETURN_DIFF_PHONE='NAME_ADDRESS_RETURN_DIFF_PHONE'
    DOB_MISKEYED='DOB_MISKEYED'
    SSN_NON_US_CITIZEN='SSN_NON_US_CITIZEN'
    ALTERNATE_BUSINESS_NAME_FOUND='ALTERNATE_BUSINESS_NAME_FOUND'
    DBA_MATCH_PUBLIC_RECORDS='DBA_MATCH_PUBLIC_RECORDS'
    SSN_RECENT='SSN_RECENT'
    SSN_TOO_OLD='SSN_TOO_OLD'
    TIN_NAME_ADDRESS_MISMATCH='TIN_NAME_ADDRESS_MISMATCH'
    BUSINESS_NOT_IN_GOOD_STANDING='BUSINESS_NOT_IN_GOOD_STANDING'
    NAME_ADDRESS_MATCH_JUDGMENT='NAME_ADDRESS_MATCH_JUDGMENT'
    BUSINESS_INACTIVE='BUSINESS_INACTIVE'
    NO_UPDATE_IN_LAST_THREE_YEARS='NO_UPDATE_IN_LAST_THREE_YEARS'
    SSN_NOT_PRIMARY='SSN_NOT_PRIMARY'
    ZIP_CORP_ONLY='ZIP_CORP_ONLY'
    ADDRESS_MISMATCH='ADDRESS_MISMATCH'
    DL_DIFFERENT='DL_DIFFERENT'
    DL_NOT_FOUND='DL_NOT_FOUND'
    DL_MISKEYED='DL_MISKEYED'
    UNABLE_TO_VERIFY_DL='UNABLE_TO_VERIFY_DL'
    SSN_INVALID_SSA='SSN_INVALID_SSA'
    SSN_IS_ITIN='SSN_IS_ITIN'
    SSN_MULTI_IDENTITY='SSN_MULTI_IDENTITY'
    ZIP_MILITARY='ZIP_MILITARY'
    MULTIPLE_SSN_FOUND='MULTIPLE_SSN_FOUND'
    ADDRESS_DISCREPANCY='ADDRESS_DISCREPANCY'
    ADDRESS_PO_BOX='ADDRESS_PO_BOX'
    SSN_RANDOM_SSA='SSN_RANDOM_SSA'
    ADDRESS_MISMATCH_SECONDARY='ADDRESS_MISMATCH_SECONDARY'
    NAME_MATCHES_NON_OFAC='NAME_MATCHES_NON_OFAC'
    UNABLE_TO_VERIFY_ZIP_CODE='UNABLE_TO_VERIFY_ZIP_CODE'
    IP_ADDRESS_UNKNOWN='IP_ADDRESS_UNKNOWN'
    IP_ADDRESS_DIFFERENT_STATE='IP_ADDRESS_DIFFERENT_STATE'
    IP_ADDRESS_DIFFERENT_ZIP='IP_ADDRESS_DIFFERENT_ZIP'
    IP_ADDRESS_DIFFERENT_PHONE='IP_ADDRESS_DIFFERENT_PHONE'
    IP_ADDRESS_DOMAIN_UNKNOWN='IP_ADDRESS_DOMAIN_UNKNOWN'
    IP_ADDRESS_NOT_ASSIGNED_TO_USA='IP_ADDRESS_NOT_ASSIGNED_TO_USA'
    IP_ADDRESS_NON_ROUTABLE='IP_ADDRESS_NON_ROUTABLE'


class legalEntityCreateRequest(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, legalEntityName=None, legalEntityType=None, legalEntityOwnershipType=None, doingBusinessAs=None, taxId=None, contactPhone=None, annualCreditCardSalesVolume=None, hasAcceptedCreditCards=None, address=None, principal=None, yearsInBusiness=None, sdkVersion=None, language=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.legalEntityName = legalEntityName
        self.validate_legalEntityNameType(self.legalEntityName)
        self.legalEntityName_nsprefix_ = None
        self.legalEntityType = legalEntityType
        self.validate_legalEntityType(self.legalEntityType)
        self.legalEntityType_nsprefix_ = None
        self.legalEntityOwnershipType = legalEntityOwnershipType
        self.validate_legalEntityOwnershipType(self.legalEntityOwnershipType)
        self.legalEntityOwnershipType_nsprefix_ = None
        self.doingBusinessAs = doingBusinessAs
        self.validate_doingBusinessAsType(self.doingBusinessAs)
        self.doingBusinessAs_nsprefix_ = None
        self.taxId = taxId
        self.validate_taxIdType(self.taxId)
        self.taxId_nsprefix_ = None
        self.contactPhone = contactPhone
        self.validate_contactPhoneType(self.contactPhone)
        self.contactPhone_nsprefix_ = None
        self.annualCreditCardSalesVolume = annualCreditCardSalesVolume
        self.annualCreditCardSalesVolume_nsprefix_ = None
        self.hasAcceptedCreditCards = hasAcceptedCreditCards
        self.hasAcceptedCreditCards_nsprefix_ = None
        self.address = address
        self.address_nsprefix_ = None
        self.principal = principal
        self.principal_nsprefix_ = None
        self.yearsInBusiness = yearsInBusiness
        self.validate_yearsInBusinessType(self.yearsInBusiness)
        self.yearsInBusiness_nsprefix_ = None
        self.sdkVersion = sdkVersion
        self.validate_sdkVersionType(self.sdkVersion)
        self.sdkVersion_nsprefix_ = None
        self.language = language
        self.validate_languageType(self.language)
        self.language_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityCreateRequest)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityCreateRequest.subclass:
            return legalEntityCreateRequest.subclass(*args_, **kwargs_)
        else:
            return legalEntityCreateRequest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_legalEntityName(self):
        return self.legalEntityName
    def set_legalEntityName(self, legalEntityName):
        self.legalEntityName = legalEntityName
    def get_legalEntityType(self):
        return self.legalEntityType
    def set_legalEntityType(self, legalEntityType):
        self.legalEntityType = legalEntityType
    def get_legalEntityOwnershipType(self):
        return self.legalEntityOwnershipType
    def set_legalEntityOwnershipType(self, legalEntityOwnershipType):
        self.legalEntityOwnershipType = legalEntityOwnershipType
    def get_doingBusinessAs(self):
        return self.doingBusinessAs
    def set_doingBusinessAs(self, doingBusinessAs):
        self.doingBusinessAs = doingBusinessAs
    def get_taxId(self):
        return self.taxId
    def set_taxId(self, taxId):
        self.taxId = taxId
    def get_contactPhone(self):
        return self.contactPhone
    def set_contactPhone(self, contactPhone):
        self.contactPhone = contactPhone
    def get_annualCreditCardSalesVolume(self):
        return self.annualCreditCardSalesVolume
    def set_annualCreditCardSalesVolume(self, annualCreditCardSalesVolume):
        self.annualCreditCardSalesVolume = annualCreditCardSalesVolume
    def get_hasAcceptedCreditCards(self):
        return self.hasAcceptedCreditCards
    def set_hasAcceptedCreditCards(self, hasAcceptedCreditCards):
        self.hasAcceptedCreditCards = hasAcceptedCreditCards
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_principal(self):
        return self.principal
    def set_principal(self, principal):
        self.principal = principal
    def get_yearsInBusiness(self):
        return self.yearsInBusiness
    def set_yearsInBusiness(self, yearsInBusiness):
        self.yearsInBusiness = yearsInBusiness
    def get_sdkVersion(self):
        return self.sdkVersion
    def set_sdkVersion(self, sdkVersion):
        self.sdkVersion = sdkVersion
    def get_language(self):
        return self.language
    def set_language(self, language):
        self.language = language
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_legalEntityNameType(self, value):
        result = True
        # Validate type legalEntityNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on legalEntityNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on legalEntityNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_legalEntityNameType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_legalEntityNameType_patterns_, ))
                result = False
        return result
    validate_legalEntityNameType_patterns_ = [[u'^([\x00-\x7f]*)$']]
    def validate_legalEntityType(self, value):
        result = True
        # Validate type legalEntityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['INDIVIDUAL_SOLE_PROPRIETORSHIP', 'CORPORATION', 'LIMITED_LIABILITY_COMPANY', 'PARTNERSHIP', 'LIMITED_PARTNERSHIP', 'GENERAL_PARTNERSHIP', 'TAX_EXEMPT_ORGANIZATION', 'GOVERNMENT_AGENCY']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on legalEntityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_legalEntityOwnershipType(self, value):
        result = True
        # Validate type legalEntityOwnershipType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['PUBLIC', 'PRIVATE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on legalEntityOwnershipType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_doingBusinessAsType(self, value):
        result = True
        # Validate type doingBusinessAsType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on doingBusinessAsType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on doingBusinessAsType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_taxIdType(self, value):
        result = True
        # Validate type taxIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 25:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on taxIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 9:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on taxIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_contactPhoneType(self, value):
        result = True
        # Validate type contactPhoneType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on contactPhoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on contactPhoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_yearsInBusinessType(self, value):
        result = True
        # Validate type yearsInBusinessType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on yearsInBusinessType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on yearsInBusinessType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_yearsInBusinessType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_yearsInBusinessType_patterns_, ))
                result = False
        return result
    validate_yearsInBusinessType_patterns_ = [[u'^([0-9]{0,3})$']]
    def validate_sdkVersionType(self, value):
        result = True
        # Validate type sdkVersionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on sdkVersionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on sdkVersionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_sdkVersionType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_sdkVersionType_patterns_, ))
                result = False
        return result
    validate_sdkVersionType_patterns_ = [[u'^([\x00-\x7f]*)$']]
    def validate_languageType(self, value):
        result = True
        # Validate type languageType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on languageType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on languageType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_languageType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_languageType_patterns_, ))
                result = False
        return result
    validate_languageType_patterns_ = [[u'^([\x00-\x7f]*)$']]
    def hasContent_(self):
        if (
            self.legalEntityName is not None or
            self.legalEntityType is not None or
            self.legalEntityOwnershipType is not None or
            self.doingBusinessAs is not None or
            self.taxId is not None or
            self.contactPhone is not None or
            self.annualCreditCardSalesVolume is not None or
            self.hasAcceptedCreditCards is not None or
            self.address is not None or
            self.principal is not None or
            self.yearsInBusiness is not None or
            self.sdkVersion is not None or
            self.language is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityCreateRequest', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityCreateRequest')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityCreateRequest':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityCreateRequest')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityCreateRequest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityCreateRequest'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityCreateRequest', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.legalEntityName is not None:
            namespaceprefix_ = self.legalEntityName_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityName>%s</%slegalEntityName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityName), input_name='legalEntityName')), namespaceprefix_ , eol_))
        if self.legalEntityType is not None:
            namespaceprefix_ = self.legalEntityType_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityType>%s</%slegalEntityType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityType), input_name='legalEntityType')), namespaceprefix_ , eol_))
        if self.legalEntityOwnershipType is not None:
            namespaceprefix_ = self.legalEntityOwnershipType_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityOwnershipType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityOwnershipType>%s</%slegalEntityOwnershipType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityOwnershipType), input_name='legalEntityOwnershipType')), namespaceprefix_ , eol_))
        if self.doingBusinessAs is not None:
            namespaceprefix_ = self.doingBusinessAs_nsprefix_ + ':' if (UseCapturedNS_ and self.doingBusinessAs_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdoingBusinessAs>%s</%sdoingBusinessAs>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.doingBusinessAs), input_name='doingBusinessAs')), namespaceprefix_ , eol_))
        if self.taxId is not None:
            namespaceprefix_ = self.taxId_nsprefix_ + ':' if (UseCapturedNS_ and self.taxId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxId>%s</%staxId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxId), input_name='taxId')), namespaceprefix_ , eol_))
        if self.contactPhone is not None:
            namespaceprefix_ = self.contactPhone_nsprefix_ + ':' if (UseCapturedNS_ and self.contactPhone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontactPhone>%s</%scontactPhone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contactPhone), input_name='contactPhone')), namespaceprefix_ , eol_))
        if self.annualCreditCardSalesVolume is not None:
            namespaceprefix_ = self.annualCreditCardSalesVolume_nsprefix_ + ':' if (UseCapturedNS_ and self.annualCreditCardSalesVolume_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sannualCreditCardSalesVolume>%s</%sannualCreditCardSalesVolume>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.annualCreditCardSalesVolume), input_name='annualCreditCardSalesVolume')), namespaceprefix_ , eol_))
        if self.hasAcceptedCreditCards is not None:
            namespaceprefix_ = self.hasAcceptedCreditCards_nsprefix_ + ':' if (UseCapturedNS_ and self.hasAcceptedCreditCards_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shasAcceptedCreditCards>%s</%shasAcceptedCreditCards>%s' % (namespaceprefix_ , self.gds_format_boolean(self.hasAcceptedCreditCards, input_name='hasAcceptedCreditCards'), namespaceprefix_ , eol_))
        if self.address is not None:
            namespaceprefix_ = self.address_nsprefix_ + ':' if (UseCapturedNS_ and self.address_nsprefix_) else ''
            self.address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address', pretty_print=pretty_print)
        if self.principal is not None:
            namespaceprefix_ = self.principal_nsprefix_ + ':' if (UseCapturedNS_ and self.principal_nsprefix_) else ''
            self.principal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='principal', pretty_print=pretty_print)
        if self.yearsInBusiness is not None:
            namespaceprefix_ = self.yearsInBusiness_nsprefix_ + ':' if (UseCapturedNS_ and self.yearsInBusiness_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%syearsInBusiness>%s</%syearsInBusiness>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.yearsInBusiness), input_name='yearsInBusiness')), namespaceprefix_ , eol_))
        if self.sdkVersion is not None:
            namespaceprefix_ = self.sdkVersion_nsprefix_ + ':' if (UseCapturedNS_ and self.sdkVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssdkVersion>%s</%ssdkVersion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.sdkVersion), input_name='sdkVersion')), namespaceprefix_ , eol_))
        if self.language is not None:
            namespaceprefix_ = self.language_nsprefix_ + ':' if (UseCapturedNS_ and self.language_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slanguage>%s</%slanguage>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.language), input_name='language')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityName')
            value_ = self.gds_validate_string(value_, node, 'legalEntityName')
            self.legalEntityName = value_
            self.legalEntityName_nsprefix_ = child_.prefix
            # validate type legalEntityNameType
            self.validate_legalEntityNameType(self.legalEntityName)
        elif nodeName_ == 'legalEntityType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityType')
            value_ = self.gds_validate_string(value_, node, 'legalEntityType')
            self.legalEntityType = value_
            self.legalEntityType_nsprefix_ = child_.prefix
            # validate type legalEntityType
            self.validate_legalEntityType(self.legalEntityType)
        elif nodeName_ == 'legalEntityOwnershipType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityOwnershipType')
            value_ = self.gds_validate_string(value_, node, 'legalEntityOwnershipType')
            self.legalEntityOwnershipType = value_
            self.legalEntityOwnershipType_nsprefix_ = child_.prefix
            # validate type legalEntityOwnershipType
            self.validate_legalEntityOwnershipType(self.legalEntityOwnershipType)
        elif nodeName_ == 'doingBusinessAs':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'doingBusinessAs')
            value_ = self.gds_validate_string(value_, node, 'doingBusinessAs')
            self.doingBusinessAs = value_
            self.doingBusinessAs_nsprefix_ = child_.prefix
            # validate type doingBusinessAsType
            self.validate_doingBusinessAsType(self.doingBusinessAs)
        elif nodeName_ == 'taxId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxId')
            value_ = self.gds_validate_string(value_, node, 'taxId')
            self.taxId = value_
            self.taxId_nsprefix_ = child_.prefix
            # validate type taxIdType
            self.validate_taxIdType(self.taxId)
        elif nodeName_ == 'contactPhone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactPhone')
            value_ = self.gds_validate_string(value_, node, 'contactPhone')
            self.contactPhone = value_
            self.contactPhone_nsprefix_ = child_.prefix
            # validate type contactPhoneType
            self.validate_contactPhoneType(self.contactPhone)
        elif nodeName_ == 'annualCreditCardSalesVolume':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'annualCreditCardSalesVolume')
            value_ = self.gds_validate_string(value_, node, 'annualCreditCardSalesVolume')
            self.annualCreditCardSalesVolume = value_
            self.annualCreditCardSalesVolume_nsprefix_ = child_.prefix
        elif nodeName_ == 'hasAcceptedCreditCards':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'hasAcceptedCreditCards')
            ival_ = self.gds_validate_boolean(ival_, node, 'hasAcceptedCreditCards')
            self.hasAcceptedCreditCards = ival_
            self.hasAcceptedCreditCards_nsprefix_ = child_.prefix
        elif nodeName_ == 'address':
            obj_ = address.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'principal':
            obj_ = legalEntityPrincipal.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.principal = obj_
            obj_.original_tagname_ = 'principal'
        elif nodeName_ == 'yearsInBusiness':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'yearsInBusiness')
            value_ = self.gds_validate_string(value_, node, 'yearsInBusiness')
            self.yearsInBusiness = value_
            self.yearsInBusiness_nsprefix_ = child_.prefix
            # validate type yearsInBusinessType
            self.validate_yearsInBusinessType(self.yearsInBusiness)
        elif nodeName_ == 'sdkVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'sdkVersion')
            value_ = self.gds_validate_string(value_, node, 'sdkVersion')
            self.sdkVersion = value_
            self.sdkVersion_nsprefix_ = child_.prefix
            # validate type sdkVersionType
            self.validate_sdkVersionType(self.sdkVersion)
        elif nodeName_ == 'language':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'language')
            value_ = self.gds_validate_string(value_, node, 'language')
            self.language = value_
            self.language_nsprefix_ = child_.prefix
            # validate type languageType
            self.validate_languageType(self.language)
# end class legalEntityCreateRequest


class address(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, streetAddress1=None, streetAddress2=None, city=None, stateProvince=None, postalCode=None, countryCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.streetAddress1 = streetAddress1
        self.validate_streetAddress1Type(self.streetAddress1)
        self.streetAddress1_nsprefix_ = None
        self.streetAddress2 = streetAddress2
        self.validate_streetAddress2Type(self.streetAddress2)
        self.streetAddress2_nsprefix_ = None
        self.city = city
        self.validate_cityType(self.city)
        self.city_nsprefix_ = None
        self.stateProvince = stateProvince
        self.validate_stateProvinceType(self.stateProvince)
        self.stateProvince_nsprefix_ = None
        self.postalCode = postalCode
        self.validate_postalCodeType(self.postalCode)
        self.postalCode_nsprefix_ = None
        self.countryCode = countryCode
        self.validate_countryCodeType(self.countryCode)
        self.countryCode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, address)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if address.subclass:
            return address.subclass(*args_, **kwargs_)
        else:
            return address(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_streetAddress1(self):
        return self.streetAddress1
    def set_streetAddress1(self, streetAddress1):
        self.streetAddress1 = streetAddress1
    def get_streetAddress2(self):
        return self.streetAddress2
    def set_streetAddress2(self, streetAddress2):
        self.streetAddress2 = streetAddress2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_stateProvince(self):
        return self.stateProvince
    def set_stateProvince(self, stateProvince):
        self.stateProvince = stateProvince
    def get_postalCode(self):
        return self.postalCode
    def set_postalCode(self, postalCode):
        self.postalCode = postalCode
    def get_countryCode(self):
        return self.countryCode
    def set_countryCode(self, countryCode):
        self.countryCode = countryCode
    def validate_streetAddress1Type(self, value):
        result = True
        # Validate type streetAddress1Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on streetAddress1Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on streetAddress1Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_streetAddress2Type(self, value):
        result = True
        # Validate type streetAddress2Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on streetAddress2Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on streetAddress2Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_cityType(self, value):
        result = True
        # Validate type cityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on cityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_stateProvinceType(self, value):
        result = True
        # Validate type stateProvinceType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on stateProvinceType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on stateProvinceType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_postalCodeType(self, value):
        result = True
        # Validate type postalCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on postalCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on postalCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_countryCodeType(self, value):
        result = True
        # Validate type countryCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on countryCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on countryCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.streetAddress1 is not None or
            self.streetAddress2 is not None or
            self.city is not None or
            self.stateProvince is not None or
            self.postalCode is not None or
            self.countryCode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='address', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('address')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'address':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='address')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='address', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='address'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='address', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.streetAddress1 is not None:
            namespaceprefix_ = self.streetAddress1_nsprefix_ + ':' if (UseCapturedNS_ and self.streetAddress1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress1>%s</%sstreetAddress1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.streetAddress1), input_name='streetAddress1')), namespaceprefix_ , eol_))
        if self.streetAddress2 is not None:
            namespaceprefix_ = self.streetAddress2_nsprefix_ + ':' if (UseCapturedNS_ and self.streetAddress2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress2>%s</%sstreetAddress2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.streetAddress2), input_name='streetAddress2')), namespaceprefix_ , eol_))
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.stateProvince is not None:
            namespaceprefix_ = self.stateProvince_nsprefix_ + ':' if (UseCapturedNS_ and self.stateProvince_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstateProvince>%s</%sstateProvince>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.stateProvince), input_name='stateProvince')), namespaceprefix_ , eol_))
        if self.postalCode is not None:
            namespaceprefix_ = self.postalCode_nsprefix_ + ':' if (UseCapturedNS_ and self.postalCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostalCode>%s</%spostalCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postalCode), input_name='postalCode')), namespaceprefix_ , eol_))
        if self.countryCode is not None:
            namespaceprefix_ = self.countryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.countryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountryCode>%s</%scountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.countryCode), input_name='countryCode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'streetAddress1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress1')
            value_ = self.gds_validate_string(value_, node, 'streetAddress1')
            self.streetAddress1 = value_
            self.streetAddress1_nsprefix_ = child_.prefix
            # validate type streetAddress1Type
            self.validate_streetAddress1Type(self.streetAddress1)
        elif nodeName_ == 'streetAddress2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress2')
            value_ = self.gds_validate_string(value_, node, 'streetAddress2')
            self.streetAddress2 = value_
            self.streetAddress2_nsprefix_ = child_.prefix
            # validate type streetAddress2Type
            self.validate_streetAddress2Type(self.streetAddress2)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType
            self.validate_cityType(self.city)
        elif nodeName_ == 'stateProvince':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'stateProvince')
            value_ = self.gds_validate_string(value_, node, 'stateProvince')
            self.stateProvince = value_
            self.stateProvince_nsprefix_ = child_.prefix
            # validate type stateProvinceType
            self.validate_stateProvinceType(self.stateProvince)
        elif nodeName_ == 'postalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postalCode')
            value_ = self.gds_validate_string(value_, node, 'postalCode')
            self.postalCode = value_
            self.postalCode_nsprefix_ = child_.prefix
            # validate type postalCodeType
            self.validate_postalCodeType(self.postalCode)
        elif nodeName_ == 'countryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'countryCode')
            value_ = self.gds_validate_string(value_, node, 'countryCode')
            self.countryCode = value_
            self.countryCode_nsprefix_ = child_.prefix
            # validate type countryCodeType
            self.validate_countryCodeType(self.countryCode)
# end class address


class legalEntityPrincipal(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, principalId=None, title=None, firstName=None, lastName=None, emailAddress=None, ssn=None, contactPhone=None, dateOfBirth=None, driversLicense=None, driversLicenseState=None, address=None, stakePercent=None, principal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.principalId = principalId
        self.principalId_nsprefix_ = None
        self.title = title
        self.validate_titleType(self.title)
        self.title_nsprefix_ = None
        self.firstName = firstName
        self.validate_firstNameType(self.firstName)
        self.firstName_nsprefix_ = None
        self.lastName = lastName
        self.validate_lastNameType(self.lastName)
        self.lastName_nsprefix_ = None
        self.emailAddress = emailAddress
        self.validate_emailAddressType(self.emailAddress)
        self.emailAddress_nsprefix_ = None
        self.ssn = ssn
        self.validate_ssnType(self.ssn)
        self.ssn_nsprefix_ = None
        self.contactPhone = contactPhone
        self.validate_contactPhoneType1(self.contactPhone)
        self.contactPhone_nsprefix_ = None
        if isinstance(dateOfBirth, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateOfBirth, '%Y-%m-%d').date()
        else:
            initvalue_ = dateOfBirth
        self.dateOfBirth = initvalue_
        self.dateOfBirth_nsprefix_ = None
        self.driversLicense = driversLicense
        self.validate_driversLicenseType(self.driversLicense)
        self.driversLicense_nsprefix_ = None
        self.driversLicenseState = driversLicenseState
        self.validate_driversLicenseStateType(self.driversLicenseState)
        self.driversLicenseState_nsprefix_ = None
        self.address = address
        self.address_nsprefix_ = None
        self.stakePercent = stakePercent
        self.validate_stakePercentType(self.stakePercent)
        self.stakePercent_nsprefix_ = None
        self.principal = principal
        self.principal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityPrincipal)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityPrincipal.subclass:
            return legalEntityPrincipal.subclass(*args_, **kwargs_)
        else:
            return legalEntityPrincipal(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_principalId(self):
        return self.principalId
    def set_principalId(self, principalId):
        self.principalId = principalId
    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title
    def get_firstName(self):
        return self.firstName
    def set_firstName(self, firstName):
        self.firstName = firstName
    def get_lastName(self):
        return self.lastName
    def set_lastName(self, lastName):
        self.lastName = lastName
    def get_emailAddress(self):
        return self.emailAddress
    def set_emailAddress(self, emailAddress):
        self.emailAddress = emailAddress
    def get_ssn(self):
        return self.ssn
    def set_ssn(self, ssn):
        self.ssn = ssn
    def get_contactPhone(self):
        return self.contactPhone
    def set_contactPhone(self, contactPhone):
        self.contactPhone = contactPhone
    def get_dateOfBirth(self):
        return self.dateOfBirth
    def set_dateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth
    def get_driversLicense(self):
        return self.driversLicense
    def set_driversLicense(self, driversLicense):
        self.driversLicense = driversLicense
    def get_driversLicenseState(self):
        return self.driversLicenseState
    def set_driversLicenseState(self, driversLicenseState):
        self.driversLicenseState = driversLicenseState
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_stakePercent(self):
        return self.stakePercent
    def set_stakePercent(self, stakePercent):
        self.stakePercent = stakePercent
    def get_principal(self):
        return self.principal
    def set_principal(self, principal):
        self.principal = principal
    def validate_titleType(self, value):
        result = True
        # Validate type titleType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on titleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on titleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_firstNameType(self, value):
        result = True
        # Validate type firstNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on firstNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on firstNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_lastNameType(self, value):
        result = True
        # Validate type lastNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on lastNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on lastNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_emailAddressType(self, value):
        result = True
        # Validate type emailAddressType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on emailAddressType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on emailAddressType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ssnType(self, value):
        result = True
        # Validate type ssnType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 25:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ssnType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 9:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ssnType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_contactPhoneType1(self, value):
        result = True
        # Validate type contactPhoneType1, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on contactPhoneType1' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on contactPhoneType1' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_driversLicenseType(self, value):
        result = True
        # Validate type driversLicenseType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 25:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on driversLicenseType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on driversLicenseType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_driversLicenseStateType(self, value):
        result = True
        # Validate type driversLicenseStateType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on driversLicenseStateType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on driversLicenseStateType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_stakePercentType(self, value):
        result = True
        # Validate type stakePercentType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on stakePercentType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on stakePercentType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.principalId is not None or
            self.title is not None or
            self.firstName is not None or
            self.lastName is not None or
            self.emailAddress is not None or
            self.ssn is not None or
            self.contactPhone is not None or
            self.dateOfBirth is not None or
            self.driversLicense is not None or
            self.driversLicenseState is not None or
            self.address is not None or
            self.stakePercent is not None or
            self.principal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipal', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityPrincipal')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityPrincipal':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityPrincipal')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityPrincipal', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityPrincipal'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipal', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.principalId is not None:
            namespaceprefix_ = self.principalId_nsprefix_ + ':' if (UseCapturedNS_ and self.principalId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprincipalId>%s</%sprincipalId>%s' % (namespaceprefix_ , self.gds_format_integer(self.principalId, input_name='principalId'), namespaceprefix_ , eol_))
        if self.title is not None:
            namespaceprefix_ = self.title_nsprefix_ + ':' if (UseCapturedNS_ and self.title_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stitle>%s</%stitle>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.title), input_name='title')), namespaceprefix_ , eol_))
        if self.firstName is not None:
            namespaceprefix_ = self.firstName_nsprefix_ + ':' if (UseCapturedNS_ and self.firstName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfirstName>%s</%sfirstName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.firstName), input_name='firstName')), namespaceprefix_ , eol_))
        if self.lastName is not None:
            namespaceprefix_ = self.lastName_nsprefix_ + ':' if (UseCapturedNS_ and self.lastName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slastName>%s</%slastName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lastName), input_name='lastName')), namespaceprefix_ , eol_))
        if self.emailAddress is not None:
            namespaceprefix_ = self.emailAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.emailAddress_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%semailAddress>%s</%semailAddress>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.emailAddress), input_name='emailAddress')), namespaceprefix_ , eol_))
        if self.ssn is not None:
            namespaceprefix_ = self.ssn_nsprefix_ + ':' if (UseCapturedNS_ and self.ssn_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sssn>%s</%sssn>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ssn), input_name='ssn')), namespaceprefix_ , eol_))
        if self.contactPhone is not None:
            namespaceprefix_ = self.contactPhone_nsprefix_ + ':' if (UseCapturedNS_ and self.contactPhone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontactPhone>%s</%scontactPhone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contactPhone), input_name='contactPhone')), namespaceprefix_ , eol_))
        if self.dateOfBirth is not None:
            namespaceprefix_ = self.dateOfBirth_nsprefix_ + ':' if (UseCapturedNS_ and self.dateOfBirth_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateOfBirth>%s</%sdateOfBirth>%s' % (namespaceprefix_ , self.gds_format_date(self.dateOfBirth, input_name='dateOfBirth'), namespaceprefix_ , eol_))
        if self.driversLicense is not None:
            namespaceprefix_ = self.driversLicense_nsprefix_ + ':' if (UseCapturedNS_ and self.driversLicense_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdriversLicense>%s</%sdriversLicense>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.driversLicense), input_name='driversLicense')), namespaceprefix_ , eol_))
        if self.driversLicenseState is not None:
            namespaceprefix_ = self.driversLicenseState_nsprefix_ + ':' if (UseCapturedNS_ and self.driversLicenseState_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdriversLicenseState>%s</%sdriversLicenseState>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.driversLicenseState), input_name='driversLicenseState')), namespaceprefix_ , eol_))
        if self.address is not None:
            namespaceprefix_ = self.address_nsprefix_ + ':' if (UseCapturedNS_ and self.address_nsprefix_) else ''
            self.address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address', pretty_print=pretty_print)
        if self.stakePercent is not None:
            namespaceprefix_ = self.stakePercent_nsprefix_ + ':' if (UseCapturedNS_ and self.stakePercent_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstakePercent>%s</%sstakePercent>%s' % (namespaceprefix_ , self.gds_format_integer(self.stakePercent, input_name='stakePercent'), namespaceprefix_ , eol_))
        if self.principal is not None:
            namespaceprefix_ = self.principal_nsprefix_ + ':' if (UseCapturedNS_ and self.principal_nsprefix_) else ''
            self.principal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='principal', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'principalId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'principalId')
            ival_ = self.gds_validate_integer(ival_, node, 'principalId')
            self.principalId = ival_
            self.principalId_nsprefix_ = child_.prefix
        elif nodeName_ == 'title':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'title')
            value_ = self.gds_validate_string(value_, node, 'title')
            self.title = value_
            self.title_nsprefix_ = child_.prefix
            # validate type titleType
            self.validate_titleType(self.title)
        elif nodeName_ == 'firstName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firstName')
            value_ = self.gds_validate_string(value_, node, 'firstName')
            self.firstName = value_
            self.firstName_nsprefix_ = child_.prefix
            # validate type firstNameType
            self.validate_firstNameType(self.firstName)
        elif nodeName_ == 'lastName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lastName')
            value_ = self.gds_validate_string(value_, node, 'lastName')
            self.lastName = value_
            self.lastName_nsprefix_ = child_.prefix
            # validate type lastNameType
            self.validate_lastNameType(self.lastName)
        elif nodeName_ == 'emailAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'emailAddress')
            value_ = self.gds_validate_string(value_, node, 'emailAddress')
            self.emailAddress = value_
            self.emailAddress_nsprefix_ = child_.prefix
            # validate type emailAddressType
            self.validate_emailAddressType(self.emailAddress)
        elif nodeName_ == 'ssn':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ssn')
            value_ = self.gds_validate_string(value_, node, 'ssn')
            self.ssn = value_
            self.ssn_nsprefix_ = child_.prefix
            # validate type ssnType
            self.validate_ssnType(self.ssn)
        elif nodeName_ == 'contactPhone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactPhone')
            value_ = self.gds_validate_string(value_, node, 'contactPhone')
            self.contactPhone = value_
            self.contactPhone_nsprefix_ = child_.prefix
            # validate type contactPhoneType1
            self.validate_contactPhoneType1(self.contactPhone)
        elif nodeName_ == 'dateOfBirth':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dateOfBirth = dval_
            self.dateOfBirth_nsprefix_ = child_.prefix
        elif nodeName_ == 'driversLicense':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'driversLicense')
            value_ = self.gds_validate_string(value_, node, 'driversLicense')
            self.driversLicense = value_
            self.driversLicense_nsprefix_ = child_.prefix
            # validate type driversLicenseType
            self.validate_driversLicenseType(self.driversLicense)
        elif nodeName_ == 'driversLicenseState':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'driversLicenseState')
            value_ = self.gds_validate_string(value_, node, 'driversLicenseState')
            self.driversLicenseState = value_
            self.driversLicenseState_nsprefix_ = child_.prefix
            # validate type driversLicenseStateType
            self.validate_driversLicenseStateType(self.driversLicenseState)
        elif nodeName_ == 'address':
            obj_ = principalAddress.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'stakePercent' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'stakePercent')
            ival_ = self.gds_validate_integer(ival_, node, 'stakePercent')
            self.stakePercent = ival_
            self.stakePercent_nsprefix_ = child_.prefix
            # validate type stakePercentType
            self.validate_stakePercentType(self.stakePercent)
        elif nodeName_ == 'principal':
            obj_ = principalResult.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.principal = obj_
            obj_.original_tagname_ = 'principal'
# end class legalEntityPrincipal


class principalAddress(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, streetAddress1=None, streetAddress2=None, city=None, stateProvince=None, postalCode=None, countryCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.streetAddress1 = streetAddress1
        self.validate_streetAddress1Type2(self.streetAddress1)
        self.streetAddress1_nsprefix_ = None
        self.streetAddress2 = streetAddress2
        self.validate_streetAddress2Type3(self.streetAddress2)
        self.streetAddress2_nsprefix_ = None
        self.city = city
        self.validate_cityType4(self.city)
        self.city_nsprefix_ = None
        self.stateProvince = stateProvince
        self.validate_stateProvinceType5(self.stateProvince)
        self.stateProvince_nsprefix_ = None
        self.postalCode = postalCode
        self.validate_postalCodeType6(self.postalCode)
        self.postalCode_nsprefix_ = None
        self.countryCode = countryCode
        self.validate_countryCodeType7(self.countryCode)
        self.countryCode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, principalAddress)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if principalAddress.subclass:
            return principalAddress.subclass(*args_, **kwargs_)
        else:
            return principalAddress(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_streetAddress1(self):
        return self.streetAddress1
    def set_streetAddress1(self, streetAddress1):
        self.streetAddress1 = streetAddress1
    def get_streetAddress2(self):
        return self.streetAddress2
    def set_streetAddress2(self, streetAddress2):
        self.streetAddress2 = streetAddress2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_stateProvince(self):
        return self.stateProvince
    def set_stateProvince(self, stateProvince):
        self.stateProvince = stateProvince
    def get_postalCode(self):
        return self.postalCode
    def set_postalCode(self, postalCode):
        self.postalCode = postalCode
    def get_countryCode(self):
        return self.countryCode
    def set_countryCode(self, countryCode):
        self.countryCode = countryCode
    def validate_streetAddress1Type2(self, value):
        result = True
        # Validate type streetAddress1Type2, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on streetAddress1Type2' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on streetAddress1Type2' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_streetAddress2Type3(self, value):
        result = True
        # Validate type streetAddress2Type3, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on streetAddress2Type3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on streetAddress2Type3' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_cityType4(self, value):
        result = True
        # Validate type cityType4, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType4' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on cityType4' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_stateProvinceType5(self, value):
        result = True
        # Validate type stateProvinceType5, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on stateProvinceType5' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on stateProvinceType5' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_postalCodeType6(self, value):
        result = True
        # Validate type postalCodeType6, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on postalCodeType6' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on postalCodeType6' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_countryCodeType7(self, value):
        result = True
        # Validate type countryCodeType7, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on countryCodeType7' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on countryCodeType7' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.streetAddress1 is not None or
            self.streetAddress2 is not None or
            self.city is not None or
            self.stateProvince is not None or
            self.postalCode is not None or
            self.countryCode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalAddress', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('principalAddress')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'principalAddress':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='principalAddress')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='principalAddress', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='principalAddress'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalAddress', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.streetAddress1 is not None:
            namespaceprefix_ = self.streetAddress1_nsprefix_ + ':' if (UseCapturedNS_ and self.streetAddress1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress1>%s</%sstreetAddress1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.streetAddress1), input_name='streetAddress1')), namespaceprefix_ , eol_))
        if self.streetAddress2 is not None:
            namespaceprefix_ = self.streetAddress2_nsprefix_ + ':' if (UseCapturedNS_ and self.streetAddress2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress2>%s</%sstreetAddress2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.streetAddress2), input_name='streetAddress2')), namespaceprefix_ , eol_))
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.stateProvince is not None:
            namespaceprefix_ = self.stateProvince_nsprefix_ + ':' if (UseCapturedNS_ and self.stateProvince_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstateProvince>%s</%sstateProvince>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.stateProvince), input_name='stateProvince')), namespaceprefix_ , eol_))
        if self.postalCode is not None:
            namespaceprefix_ = self.postalCode_nsprefix_ + ':' if (UseCapturedNS_ and self.postalCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostalCode>%s</%spostalCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postalCode), input_name='postalCode')), namespaceprefix_ , eol_))
        if self.countryCode is not None:
            namespaceprefix_ = self.countryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.countryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountryCode>%s</%scountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.countryCode), input_name='countryCode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'streetAddress1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress1')
            value_ = self.gds_validate_string(value_, node, 'streetAddress1')
            self.streetAddress1 = value_
            self.streetAddress1_nsprefix_ = child_.prefix
            # validate type streetAddress1Type2
            self.validate_streetAddress1Type2(self.streetAddress1)
        elif nodeName_ == 'streetAddress2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress2')
            value_ = self.gds_validate_string(value_, node, 'streetAddress2')
            self.streetAddress2 = value_
            self.streetAddress2_nsprefix_ = child_.prefix
            # validate type streetAddress2Type3
            self.validate_streetAddress2Type3(self.streetAddress2)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType4
            self.validate_cityType4(self.city)
        elif nodeName_ == 'stateProvince':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'stateProvince')
            value_ = self.gds_validate_string(value_, node, 'stateProvince')
            self.stateProvince = value_
            self.stateProvince_nsprefix_ = child_.prefix
            # validate type stateProvinceType5
            self.validate_stateProvinceType5(self.stateProvince)
        elif nodeName_ == 'postalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postalCode')
            value_ = self.gds_validate_string(value_, node, 'postalCode')
            self.postalCode = value_
            self.postalCode_nsprefix_ = child_.prefix
            # validate type postalCodeType6
            self.validate_postalCodeType6(self.postalCode)
        elif nodeName_ == 'countryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'countryCode')
            value_ = self.gds_validate_string(value_, node, 'countryCode')
            self.countryCode = value_
            self.countryCode_nsprefix_ = child_.prefix
            # validate type countryCodeType7
            self.validate_countryCodeType7(self.countryCode)
# end class principalAddress


class response(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, transactionId=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.transactionId = transactionId
        self.transactionId_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, response)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if response.subclass:
            return response.subclass(*args_, **kwargs_)
        else:
            return response(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_transactionId(self):
        return self.transactionId
    def set_transactionId(self, transactionId):
        self.transactionId = transactionId
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.transactionId is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='response', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('response')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'response':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='response')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='response', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='response'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='response', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.transactionId is not None:
            namespaceprefix_ = self.transactionId_nsprefix_ + ':' if (UseCapturedNS_ and self.transactionId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransactionId>%s</%stransactionId>%s' % (namespaceprefix_ , self.gds_format_integer(self.transactionId, input_name='transactionId'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'transactionId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'transactionId')
            ival_ = self.gds_validate_integer(ival_, node, 'transactionId')
            self.transactionId = ival_
            self.transactionId_nsprefix_ = child_.prefix
# end class response


class legalEntityPrincipalCreateRequest(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, principal=None, sdkVersion=None, language=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.principal = principal
        self.principal_nsprefix_ = None
        self.sdkVersion = sdkVersion
        self.validate_sdkVersionType8(self.sdkVersion)
        self.sdkVersion_nsprefix_ = None
        self.language = language
        self.validate_languageType9(self.language)
        self.language_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityPrincipalCreateRequest)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityPrincipalCreateRequest.subclass:
            return legalEntityPrincipalCreateRequest.subclass(*args_, **kwargs_)
        else:
            return legalEntityPrincipalCreateRequest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_principal(self):
        return self.principal
    def set_principal(self, principal):
        self.principal = principal
    def get_sdkVersion(self):
        return self.sdkVersion
    def set_sdkVersion(self, sdkVersion):
        self.sdkVersion = sdkVersion
    def get_language(self):
        return self.language
    def set_language(self, language):
        self.language = language
    def validate_sdkVersionType8(self, value):
        result = True
        # Validate type sdkVersionType8, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on sdkVersionType8' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on sdkVersionType8' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_sdkVersionType8_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_sdkVersionType8_patterns_, ))
                result = False
        return result
    validate_sdkVersionType8_patterns_ = [[u'^([\x00-\x7f]*)$']]
    def validate_languageType9(self, value):
        result = True
        # Validate type languageType9, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on languageType9' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on languageType9' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_languageType9_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_languageType9_patterns_, ))
                result = False
        return result
    validate_languageType9_patterns_ = [[u'^([\x00-\x7f]*)$']]
    def hasContent_(self):
        if (
            self.principal is not None or
            self.sdkVersion is not None or
            self.language is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipalCreateRequest', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityPrincipalCreateRequest')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityPrincipalCreateRequest':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityPrincipalCreateRequest')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityPrincipalCreateRequest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityPrincipalCreateRequest'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipalCreateRequest', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.principal is not None:
            namespaceprefix_ = self.principal_nsprefix_ + ':' if (UseCapturedNS_ and self.principal_nsprefix_) else ''
            self.principal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='principal', pretty_print=pretty_print)
        if self.sdkVersion is not None:
            namespaceprefix_ = self.sdkVersion_nsprefix_ + ':' if (UseCapturedNS_ and self.sdkVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssdkVersion>%s</%ssdkVersion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.sdkVersion), input_name='sdkVersion')), namespaceprefix_ , eol_))
        if self.language is not None:
            namespaceprefix_ = self.language_nsprefix_ + ':' if (UseCapturedNS_ and self.language_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slanguage>%s</%slanguage>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.language), input_name='language')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'principal':
            obj_ = legalEntityPrincipal.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.principal = obj_
            obj_.original_tagname_ = 'principal'
        elif nodeName_ == 'sdkVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'sdkVersion')
            value_ = self.gds_validate_string(value_, node, 'sdkVersion')
            self.sdkVersion = value_
            self.sdkVersion_nsprefix_ = child_.prefix
            # validate type sdkVersionType8
            self.validate_sdkVersionType8(self.sdkVersion)
        elif nodeName_ == 'language':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'language')
            value_ = self.gds_validate_string(value_, node, 'language')
            self.language = value_
            self.language_nsprefix_ = child_.prefix
            # validate type languageType9
            self.validate_languageType9(self.language)
# end class legalEntityPrincipalCreateRequest


class legalEntityPrincipalCreateResponse(response):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = response
    def __init__(self, transactionId=None, principalId=None, firstName=None, lastName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(legalEntityPrincipalCreateResponse, self).__init__(transactionId,  **kwargs_)
        self.principalId = principalId
        self.principalId_nsprefix_ = None
        self.firstName = firstName
        self.validate_firstNameType10(self.firstName)
        self.firstName_nsprefix_ = None
        self.lastName = lastName
        self.validate_lastNameType11(self.lastName)
        self.lastName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityPrincipalCreateResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityPrincipalCreateResponse.subclass:
            return legalEntityPrincipalCreateResponse.subclass(*args_, **kwargs_)
        else:
            return legalEntityPrincipalCreateResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_principalId(self):
        return self.principalId
    def set_principalId(self, principalId):
        self.principalId = principalId
    def get_firstName(self):
        return self.firstName
    def set_firstName(self, firstName):
        self.firstName = firstName
    def get_lastName(self):
        return self.lastName
    def set_lastName(self, lastName):
        self.lastName = lastName
    def validate_firstNameType10(self, value):
        result = True
        # Validate type firstNameType10, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on firstNameType10' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on firstNameType10' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_lastNameType11(self, value):
        result = True
        # Validate type lastNameType11, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on lastNameType11' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on lastNameType11' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.principalId is not None or
            self.firstName is not None or
            self.lastName is not None or
            super(legalEntityPrincipalCreateResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipalCreateResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityPrincipalCreateResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityPrincipalCreateResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityPrincipalCreateResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityPrincipalCreateResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityPrincipalCreateResponse'):
        super(legalEntityPrincipalCreateResponse, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityPrincipalCreateResponse')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipalCreateResponse', fromsubclass_=False, pretty_print=True):
        super(legalEntityPrincipalCreateResponse, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.principalId is not None:
            namespaceprefix_ = self.principalId_nsprefix_ + ':' if (UseCapturedNS_ and self.principalId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprincipalId>%s</%sprincipalId>%s' % (namespaceprefix_ , self.gds_format_integer(self.principalId, input_name='principalId'), namespaceprefix_ , eol_))
        if self.firstName is not None:
            namespaceprefix_ = self.firstName_nsprefix_ + ':' if (UseCapturedNS_ and self.firstName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfirstName>%s</%sfirstName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.firstName), input_name='firstName')), namespaceprefix_ , eol_))
        if self.lastName is not None:
            namespaceprefix_ = self.lastName_nsprefix_ + ':' if (UseCapturedNS_ and self.lastName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slastName>%s</%slastName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lastName), input_name='lastName')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(legalEntityPrincipalCreateResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'principalId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'principalId')
            ival_ = self.gds_validate_integer(ival_, node, 'principalId')
            self.principalId = ival_
            self.principalId_nsprefix_ = child_.prefix
        elif nodeName_ == 'firstName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firstName')
            value_ = self.gds_validate_string(value_, node, 'firstName')
            self.firstName = value_
            self.firstName_nsprefix_ = child_.prefix
            # validate type firstNameType10
            self.validate_firstNameType10(self.firstName)
        elif nodeName_ == 'lastName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lastName')
            value_ = self.gds_validate_string(value_, node, 'lastName')
            self.lastName = value_
            self.lastName_nsprefix_ = child_.prefix
            # validate type lastNameType11
            self.validate_lastNameType11(self.lastName)
        super(legalEntityPrincipalCreateResponse, self).buildChildren(child_, node, nodeName_, True)
# end class legalEntityPrincipalCreateResponse


class legalEntityRetrievalResponse(legalEntityCreateRequest):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = legalEntityCreateRequest
    def __init__(self, legalEntityName=None, legalEntityType=None, legalEntityOwnershipType=None, doingBusinessAs=None, taxId=None, contactPhone=None, annualCreditCardSalesVolume=None, hasAcceptedCreditCards=None, address=None, principal=None, yearsInBusiness=None, sdkVersion=None, language=None, overallStatus=None, legalEntityPrincipal=None, legalEntityId=None, responseCode=None, responseDescription=None, backgroundCheckResults=None, transactionId=None, updateDate=None, decisionDate=None, tinValidationStatus=None, sub_merchant_processing_status=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(legalEntityRetrievalResponse, self).__init__(legalEntityName, legalEntityType, legalEntityOwnershipType, doingBusinessAs, taxId, contactPhone, annualCreditCardSalesVolume, hasAcceptedCreditCards, address, principal, yearsInBusiness, sdkVersion, language,  **kwargs_)
        self.overallStatus = _cast(None, overallStatus)
        self.overallStatus_nsprefix_ = None
        self.legalEntityPrincipal = legalEntityPrincipal
        self.legalEntityPrincipal_nsprefix_ = None
        self.legalEntityId = legalEntityId
        self.validate_legalEntityIdType12(self.legalEntityId)
        self.legalEntityId_nsprefix_ = None
        self.responseCode = responseCode
        self.responseCode_nsprefix_ = None
        self.responseDescription = responseDescription
        self.validate_responseDescriptionType13(self.responseDescription)
        self.responseDescription_nsprefix_ = None
        self.backgroundCheckResults = backgroundCheckResults
        self.backgroundCheckResults_nsprefix_ = None
        self.transactionId = transactionId
        self.validate_transactionIdType(self.transactionId)
        self.transactionId_nsprefix_ = None
        if isinstance(updateDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updateDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updateDate
        self.updateDate = initvalue_
        self.updateDate_nsprefix_ = None
        if isinstance(decisionDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(decisionDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = decisionDate
        self.decisionDate = initvalue_
        self.decisionDate_nsprefix_ = None
        self.tinValidationStatus = tinValidationStatus
        self.validate_tinValidationStatusType(self.tinValidationStatus)
        self.tinValidationStatus_nsprefix_ = None
        self.sub_merchant_processing_status = sub_merchant_processing_status
        self.sub_merchant_processing_status_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityRetrievalResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityRetrievalResponse.subclass:
            return legalEntityRetrievalResponse.subclass(*args_, **kwargs_)
        else:
            return legalEntityRetrievalResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_legalEntityPrincipal(self):
        return self.legalEntityPrincipal
    def set_legalEntityPrincipal(self, legalEntityPrincipal):
        self.legalEntityPrincipal = legalEntityPrincipal
    def get_legalEntityId(self):
        return self.legalEntityId
    def set_legalEntityId(self, legalEntityId):
        self.legalEntityId = legalEntityId
    def get_responseCode(self):
        return self.responseCode
    def set_responseCode(self, responseCode):
        self.responseCode = responseCode
    def get_responseDescription(self):
        return self.responseDescription
    def set_responseDescription(self, responseDescription):
        self.responseDescription = responseDescription
    def get_backgroundCheckResults(self):
        return self.backgroundCheckResults
    def set_backgroundCheckResults(self, backgroundCheckResults):
        self.backgroundCheckResults = backgroundCheckResults
    def get_transactionId(self):
        return self.transactionId
    def set_transactionId(self, transactionId):
        self.transactionId = transactionId
    def get_updateDate(self):
        return self.updateDate
    def set_updateDate(self, updateDate):
        self.updateDate = updateDate
    def get_decisionDate(self):
        return self.decisionDate
    def set_decisionDate(self, decisionDate):
        self.decisionDate = decisionDate
    def get_tinValidationStatus(self):
        return self.tinValidationStatus
    def set_tinValidationStatus(self, tinValidationStatus):
        self.tinValidationStatus = tinValidationStatus
    def get_sub_merchant_processing_status(self):
        return self.sub_merchant_processing_status
    def set_sub_merchant_processing_status(self, sub_merchant_processing_status):
        self.sub_merchant_processing_status = sub_merchant_processing_status
    def get_overallStatus(self):
        return self.overallStatus
    def set_overallStatus(self, overallStatus):
        self.overallStatus = overallStatus
    def validate_legalEntityIdType12(self, value):
        result = True
        # Validate type legalEntityIdType12, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on legalEntityIdType12' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on legalEntityIdType12' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_responseDescriptionType13(self, value):
        result = True
        # Validate type responseDescriptionType13, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on responseDescriptionType13' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on responseDescriptionType13' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_transactionIdType(self, value):
        result = True
        # Validate type transactionIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on transactionIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on transactionIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tinValidationStatusType(self, value):
        result = True
        # Validate type tinValidationStatusType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tinValidationStatusType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tinValidationStatusType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.legalEntityPrincipal is not None or
            self.legalEntityId is not None or
            self.responseCode is not None or
            self.responseDescription is not None or
            self.backgroundCheckResults is not None or
            self.transactionId is not None or
            self.updateDate is not None or
            self.decisionDate is not None or
            self.tinValidationStatus is not None or
            self.sub_merchant_processing_status is not None or
            super(legalEntityRetrievalResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityRetrievalResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityRetrievalResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityRetrievalResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityRetrievalResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityRetrievalResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityRetrievalResponse'):
        super(legalEntityRetrievalResponse, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityRetrievalResponse')
        if self.overallStatus is not None and 'overallStatus' not in already_processed:
            already_processed.add('overallStatus')
            outfile.write(' overallStatus=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.overallStatus), input_name='overallStatus')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityRetrievalResponse', fromsubclass_=False, pretty_print=True):
        super(legalEntityRetrievalResponse, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.legalEntityPrincipal is not None:
            namespaceprefix_ = self.legalEntityPrincipal_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityPrincipal_nsprefix_) else ''
            self.legalEntityPrincipal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='legalEntityPrincipal', pretty_print=pretty_print)
        if self.legalEntityId is not None:
            namespaceprefix_ = self.legalEntityId_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityId>%s</%slegalEntityId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityId), input_name='legalEntityId')), namespaceprefix_ , eol_))
        if self.responseCode is not None:
            namespaceprefix_ = self.responseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.responseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sresponseCode>%s</%sresponseCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.responseCode, input_name='responseCode'), namespaceprefix_ , eol_))
        if self.responseDescription is not None:
            namespaceprefix_ = self.responseDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.responseDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sresponseDescription>%s</%sresponseDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.responseDescription), input_name='responseDescription')), namespaceprefix_ , eol_))
        if self.backgroundCheckResults is not None:
            namespaceprefix_ = self.backgroundCheckResults_nsprefix_ + ':' if (UseCapturedNS_ and self.backgroundCheckResults_nsprefix_) else ''
            self.backgroundCheckResults.export(outfile, level, namespaceprefix_='tns:', namespacedef_='', name_='backgroundCheckResults', pretty_print=pretty_print)
        if self.transactionId is not None:
            namespaceprefix_ = self.transactionId_nsprefix_ + ':' if (UseCapturedNS_ and self.transactionId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransactionId>%s</%stransactionId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.transactionId), input_name='transactionId')), namespaceprefix_ , eol_))
        if self.updateDate is not None:
            namespaceprefix_ = self.updateDate_nsprefix_ + ':' if (UseCapturedNS_ and self.updateDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%supdateDate>%s</%supdateDate>%s' % (namespaceprefix_ , self.gds_format_datetime(self.updateDate, input_name='updateDate'), namespaceprefix_ , eol_))
        if self.decisionDate is not None:
            namespaceprefix_ = self.decisionDate_nsprefix_ + ':' if (UseCapturedNS_ and self.decisionDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdecisionDate>%s</%sdecisionDate>%s' % (namespaceprefix_ , self.gds_format_datetime(self.decisionDate, input_name='decisionDate'), namespaceprefix_ , eol_))
        if self.tinValidationStatus is not None:
            namespaceprefix_ = self.tinValidationStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.tinValidationStatus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stinValidationStatus>%s</%stinValidationStatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tinValidationStatus), input_name='tinValidationStatus')), namespaceprefix_ , eol_))
        if self.sub_merchant_processing_status is not None:
            namespaceprefix_ = self.sub_merchant_processing_status_nsprefix_ + ':' if (UseCapturedNS_ and self.sub_merchant_processing_status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssub_merchant_processing_status>%s</%ssub_merchant_processing_status>%s' % (namespaceprefix_ , self.gds_format_boolean(self.sub_merchant_processing_status, input_name='sub_merchant_processing_status'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('overallStatus', node)
        if value is not None and 'overallStatus' not in already_processed:
            already_processed.add('overallStatus')
            self.overallStatus = value
        super(legalEntityRetrievalResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityPrincipal':
            obj_ = legalEntityPrincipal.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.legalEntityPrincipal = obj_
            obj_.original_tagname_ = 'legalEntityPrincipal'
        elif nodeName_ == 'legalEntityId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityId')
            value_ = self.gds_validate_string(value_, node, 'legalEntityId')
            self.legalEntityId = value_
            self.legalEntityId_nsprefix_ = child_.prefix
            # validate type legalEntityIdType12
            self.validate_legalEntityIdType12(self.legalEntityId)
        elif nodeName_ == 'responseCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'responseCode')
            ival_ = self.gds_validate_integer(ival_, node, 'responseCode')
            self.responseCode = ival_
            self.responseCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'responseDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'responseDescription')
            value_ = self.gds_validate_string(value_, node, 'responseDescription')
            self.responseDescription = value_
            self.responseDescription_nsprefix_ = child_.prefix
            # validate type responseDescriptionType13
            self.validate_responseDescriptionType13(self.responseDescription)
        elif nodeName_ == 'backgroundCheckResults':
            obj_ = backgroundCheckResults.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.backgroundCheckResults = obj_
            obj_.original_tagname_ = 'backgroundCheckResults'
        elif nodeName_ == 'transactionId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'transactionId')
            value_ = self.gds_validate_string(value_, node, 'transactionId')
            self.transactionId = value_
            self.transactionId_nsprefix_ = child_.prefix
            # validate type transactionIdType
            self.validate_transactionIdType(self.transactionId)
        elif nodeName_ == 'updateDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.updateDate = dval_
            self.updateDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'decisionDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.decisionDate = dval_
            self.decisionDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'tinValidationStatus':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tinValidationStatus')
            value_ = self.gds_validate_string(value_, node, 'tinValidationStatus')
            self.tinValidationStatus = value_
            self.tinValidationStatus_nsprefix_ = child_.prefix
            # validate type tinValidationStatusType
            self.validate_tinValidationStatusType(self.tinValidationStatus)
        elif nodeName_ == 'sub_merchant_processing_status':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'sub_merchant_processing_status')
            ival_ = self.gds_validate_boolean(ival_, node, 'sub_merchant_processing_status')
            self.sub_merchant_processing_status = ival_
            self.sub_merchant_processing_status_nsprefix_ = child_.prefix
        super(legalEntityRetrievalResponse, self).buildChildren(child_, node, nodeName_, True)
# end class legalEntityRetrievalResponse


class backgroundCheckResults(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, business=None, principal=None, businessToPrincipalAssociation=None, backgroundCheckDecisionNotes=None, bankruptcyData=None, lienResult=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.business = business
        self.business_nsprefix_ = None
        self.principal = principal
        self.principal_nsprefix_ = None
        self.businessToPrincipalAssociation = businessToPrincipalAssociation
        self.businessToPrincipalAssociation_nsprefix_ = None
        self.backgroundCheckDecisionNotes = backgroundCheckDecisionNotes
        self.validate_backgroundCheckDecisionNotesType(self.backgroundCheckDecisionNotes)
        self.backgroundCheckDecisionNotes_nsprefix_ = None
        self.bankruptcyData = bankruptcyData
        self.bankruptcyData_nsprefix_ = None
        self.lienResult = lienResult
        self.lienResult_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, backgroundCheckResults)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if backgroundCheckResults.subclass:
            return backgroundCheckResults.subclass(*args_, **kwargs_)
        else:
            return backgroundCheckResults(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_business(self):
        return self.business
    def set_business(self, business):
        self.business = business
    def get_principal(self):
        return self.principal
    def set_principal(self, principal):
        self.principal = principal
    def get_businessToPrincipalAssociation(self):
        return self.businessToPrincipalAssociation
    def set_businessToPrincipalAssociation(self, businessToPrincipalAssociation):
        self.businessToPrincipalAssociation = businessToPrincipalAssociation
    def get_backgroundCheckDecisionNotes(self):
        return self.backgroundCheckDecisionNotes
    def set_backgroundCheckDecisionNotes(self, backgroundCheckDecisionNotes):
        self.backgroundCheckDecisionNotes = backgroundCheckDecisionNotes
    def get_bankruptcyData(self):
        return self.bankruptcyData
    def set_bankruptcyData(self, bankruptcyData):
        self.bankruptcyData = bankruptcyData
    def get_lienResult(self):
        return self.lienResult
    def set_lienResult(self, lienResult):
        self.lienResult = lienResult
    def validate_backgroundCheckDecisionNotesType(self, value):
        result = True
        # Validate type backgroundCheckDecisionNotesType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on backgroundCheckDecisionNotesType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on backgroundCheckDecisionNotesType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.business is not None or
            self.principal is not None or
            self.businessToPrincipalAssociation is not None or
            self.backgroundCheckDecisionNotes is not None or
            self.bankruptcyData is not None or
            self.lienResult is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='backgroundCheckResults', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('backgroundCheckResults')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'backgroundCheckResults':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='backgroundCheckResults')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='backgroundCheckResults', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='backgroundCheckResults'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='backgroundCheckResults', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.business is not None:
            namespaceprefix_ = self.business_nsprefix_ + ':' if (UseCapturedNS_ and self.business_nsprefix_) else ''
            self.business.export(outfile, level, namespaceprefix_, namespacedef_='', name_='business', pretty_print=pretty_print)
        if self.principal is not None:
            namespaceprefix_ = self.principal_nsprefix_ + ':' if (UseCapturedNS_ and self.principal_nsprefix_) else ''
            self.principal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='principal', pretty_print=pretty_print)
        if self.businessToPrincipalAssociation is not None:
            namespaceprefix_ = self.businessToPrincipalAssociation_nsprefix_ + ':' if (UseCapturedNS_ and self.businessToPrincipalAssociation_nsprefix_) else ''
            self.businessToPrincipalAssociation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='businessToPrincipalAssociation', pretty_print=pretty_print)
        if self.backgroundCheckDecisionNotes is not None:
            namespaceprefix_ = self.backgroundCheckDecisionNotes_nsprefix_ + ':' if (UseCapturedNS_ and self.backgroundCheckDecisionNotes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbackgroundCheckDecisionNotes>%s</%sbackgroundCheckDecisionNotes>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.backgroundCheckDecisionNotes), input_name='backgroundCheckDecisionNotes')), namespaceprefix_ , eol_))
        if self.bankruptcyData is not None:
            namespaceprefix_ = self.bankruptcyData_nsprefix_ + ':' if (UseCapturedNS_ and self.bankruptcyData_nsprefix_) else ''
            self.bankruptcyData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='bankruptcyData', pretty_print=pretty_print)
        if self.lienResult is not None:
            namespaceprefix_ = self.lienResult_nsprefix_ + ':' if (UseCapturedNS_ and self.lienResult_nsprefix_) else ''
            self.lienResult.export(outfile, level, namespaceprefix_, namespacedef_='', name_='lienResult', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'business':
            obj_ = businessResult.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.business = obj_
            obj_.original_tagname_ = 'business'
        elif nodeName_ == 'principal':
            obj_ = principalResult.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.principal = obj_
            obj_.original_tagname_ = 'principal'
        elif nodeName_ == 'businessToPrincipalAssociation':
            obj_ = businessToPrincipalAssociation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.businessToPrincipalAssociation = obj_
            obj_.original_tagname_ = 'businessToPrincipalAssociation'
        elif nodeName_ == 'backgroundCheckDecisionNotes':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'backgroundCheckDecisionNotes')
            value_ = self.gds_validate_string(value_, node, 'backgroundCheckDecisionNotes')
            self.backgroundCheckDecisionNotes = value_
            self.backgroundCheckDecisionNotes_nsprefix_ = child_.prefix
            # validate type backgroundCheckDecisionNotesType
            self.validate_backgroundCheckDecisionNotesType(self.backgroundCheckDecisionNotes)
        elif nodeName_ == 'bankruptcyData':
            obj_ = bankruptcyResult.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.bankruptcyData = obj_
            obj_.original_tagname_ = 'bankruptcyData'
        elif nodeName_ == 'lienResult':
            obj_ = lienResult.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.lienResult = obj_
            obj_.original_tagname_ = 'lienResult'
# end class backgroundCheckResults


class businessResult(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, verificationResult=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.verificationResult = verificationResult
        self.verificationResult_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, businessResult)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if businessResult.subclass:
            return businessResult.subclass(*args_, **kwargs_)
        else:
            return businessResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_verificationResult(self):
        return self.verificationResult
    def set_verificationResult(self, verificationResult):
        self.verificationResult = verificationResult
    def hasContent_(self):
        if (
            self.verificationResult is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessResult', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('businessResult')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'businessResult':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='businessResult')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='businessResult', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='businessResult'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessResult', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.verificationResult is not None:
            namespaceprefix_ = self.verificationResult_nsprefix_ + ':' if (UseCapturedNS_ and self.verificationResult_nsprefix_) else ''
            self.verificationResult.export(outfile, level, namespaceprefix_, namespacedef_='', name_='verificationResult', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'verificationResult':
            obj_ = businessVerificationResult.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.verificationResult = obj_
            obj_.original_tagname_ = 'verificationResult'
# end class businessResult


class businessVerificationResult(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, overallScore=None, nameAddressTaxIdAssociation=None, nameAddressPhoneAssociation=None, verificationIndicators=None, riskIndicators=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.overallScore = overallScore
        self.overallScore_nsprefix_ = None
        self.nameAddressTaxIdAssociation = nameAddressTaxIdAssociation
        self.nameAddressTaxIdAssociation_nsprefix_ = None
        self.nameAddressPhoneAssociation = nameAddressPhoneAssociation
        self.nameAddressPhoneAssociation_nsprefix_ = None
        self.verificationIndicators = verificationIndicators
        self.verificationIndicators_nsprefix_ = None
        self.riskIndicators = riskIndicators
        self.riskIndicators_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, businessVerificationResult)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if businessVerificationResult.subclass:
            return businessVerificationResult.subclass(*args_, **kwargs_)
        else:
            return businessVerificationResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_overallScore(self):
        return self.overallScore
    def set_overallScore(self, overallScore):
        self.overallScore = overallScore
    def get_nameAddressTaxIdAssociation(self):
        return self.nameAddressTaxIdAssociation
    def set_nameAddressTaxIdAssociation(self, nameAddressTaxIdAssociation):
        self.nameAddressTaxIdAssociation = nameAddressTaxIdAssociation
    def get_nameAddressPhoneAssociation(self):
        return self.nameAddressPhoneAssociation
    def set_nameAddressPhoneAssociation(self, nameAddressPhoneAssociation):
        self.nameAddressPhoneAssociation = nameAddressPhoneAssociation
    def get_verificationIndicators(self):
        return self.verificationIndicators
    def set_verificationIndicators(self, verificationIndicators):
        self.verificationIndicators = verificationIndicators
    def get_riskIndicators(self):
        return self.riskIndicators
    def set_riskIndicators(self, riskIndicators):
        self.riskIndicators = riskIndicators
    def hasContent_(self):
        if (
            self.overallScore is not None or
            self.nameAddressTaxIdAssociation is not None or
            self.nameAddressPhoneAssociation is not None or
            self.verificationIndicators is not None or
            self.riskIndicators is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessVerificationResult', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('businessVerificationResult')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'businessVerificationResult':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='businessVerificationResult')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='businessVerificationResult', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='businessVerificationResult'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessVerificationResult', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.overallScore is not None:
            namespaceprefix_ = self.overallScore_nsprefix_ + ':' if (UseCapturedNS_ and self.overallScore_nsprefix_) else ''
            self.overallScore.export(outfile, level, namespaceprefix_, namespacedef_='', name_='overallScore', pretty_print=pretty_print)
        if self.nameAddressTaxIdAssociation is not None:
            namespaceprefix_ = self.nameAddressTaxIdAssociation_nsprefix_ + ':' if (UseCapturedNS_ and self.nameAddressTaxIdAssociation_nsprefix_) else ''
            self.nameAddressTaxIdAssociation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='nameAddressTaxIdAssociation', pretty_print=pretty_print)
        if self.nameAddressPhoneAssociation is not None:
            namespaceprefix_ = self.nameAddressPhoneAssociation_nsprefix_ + ':' if (UseCapturedNS_ and self.nameAddressPhoneAssociation_nsprefix_) else ''
            self.nameAddressPhoneAssociation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='nameAddressPhoneAssociation', pretty_print=pretty_print)
        if self.verificationIndicators is not None:
            namespaceprefix_ = self.verificationIndicators_nsprefix_ + ':' if (UseCapturedNS_ and self.verificationIndicators_nsprefix_) else ''
            self.verificationIndicators.export(outfile, level, namespaceprefix_, namespacedef_='', name_='verificationIndicators', pretty_print=pretty_print)
        if self.riskIndicators is not None:
            namespaceprefix_ = self.riskIndicators_nsprefix_ + ':' if (UseCapturedNS_ and self.riskIndicators_nsprefix_) else ''
            self.riskIndicators.export(outfile, level, namespaceprefix_, namespacedef_='', name_='riskIndicators', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'overallScore':
            obj_ = businessScore.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.overallScore = obj_
            obj_.original_tagname_ = 'overallScore'
        elif nodeName_ == 'nameAddressTaxIdAssociation':
            obj_ = nameAddressTaxIdAssociation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.nameAddressTaxIdAssociation = obj_
            obj_.original_tagname_ = 'nameAddressTaxIdAssociation'
        elif nodeName_ == 'nameAddressPhoneAssociation':
            obj_ = businessNameAddressPhoneAssociation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.nameAddressPhoneAssociation = obj_
            obj_.original_tagname_ = 'nameAddressPhoneAssociation'
        elif nodeName_ == 'verificationIndicators':
            obj_ = businessVerificationIndicators.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.verificationIndicators = obj_
            obj_.original_tagname_ = 'verificationIndicators'
        elif nodeName_ == 'riskIndicators':
            obj_ = riskIndicatorsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.riskIndicators = obj_
            obj_.original_tagname_ = 'riskIndicators'
# end class businessVerificationResult


class businessScore(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, score=None, description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.score = score
        self.validate_businessOverallScore(self.score)
        self.score_nsprefix_ = None
        self.description = description
        self.validate_descriptionType(self.description)
        self.description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, businessScore)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if businessScore.subclass:
            return businessScore.subclass(*args_, **kwargs_)
        else:
            return businessScore(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_score(self):
        return self.score
    def set_score(self, score):
        self.score = score
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def validate_businessOverallScore(self, value):
        result = True
        # Validate type businessOverallScore, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0, 10, 20, 30, 40, 50]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on businessOverallScore' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_descriptionType(self, value):
        result = True
        # Validate type descriptionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 110:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on descriptionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on descriptionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.score is not None or
            self.description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessScore', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('businessScore')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'businessScore':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='businessScore')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='businessScore', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='businessScore'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessScore', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.score is not None:
            namespaceprefix_ = self.score_nsprefix_ + ':' if (UseCapturedNS_ and self.score_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sscore>%s</%sscore>%s' % (namespaceprefix_ , self.gds_format_integer(self.score, input_name='score'), namespaceprefix_ , eol_))
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdescription>%s</%sdescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.description), input_name='description')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'score' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'score')
            ival_ = self.gds_validate_integer(ival_, node, 'score')
            self.score = ival_
            self.score_nsprefix_ = child_.prefix
            # validate type businessOverallScore
            self.validate_businessOverallScore(self.score)
        elif nodeName_ == 'description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'description')
            value_ = self.gds_validate_string(value_, node, 'description')
            self.description = value_
            self.description_nsprefix_ = child_.prefix
            # validate type descriptionType
            self.validate_descriptionType(self.description)
# end class businessScore


class nameAddressTaxIdAssociation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, code=None, description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_nameAddressTaxIdAssociationCode(self.code)
        self.code_nsprefix_ = None
        self.description = description
        self.validate_descriptionType14(self.description)
        self.description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, nameAddressTaxIdAssociation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if nameAddressTaxIdAssociation.subclass:
            return nameAddressTaxIdAssociation.subclass(*args_, **kwargs_)
        else:
            return nameAddressTaxIdAssociation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def validate_nameAddressTaxIdAssociationCode(self, value):
        result = True
        # Validate type nameAddressTaxIdAssociationCode, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['NOT_VERIFIED', 'WRONG_TAX_ID', 'NAME_OR_ADDRESS', 'BAD_NAME', 'BAD_ADDRESS', 'MISSING_ADDRESS', 'NAME_AND_ADDRESS_BAD_TAX_ID', 'NAME_AND_ADDRESS_NO_TAX_ID', 'NAME_ADDRESS_TAX_ID']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on nameAddressTaxIdAssociationCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_descriptionType14(self, value):
        result = True
        # Validate type descriptionType14, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 120:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on descriptionType14' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on descriptionType14' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='nameAddressTaxIdAssociation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('nameAddressTaxIdAssociation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'nameAddressTaxIdAssociation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='nameAddressTaxIdAssociation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='nameAddressTaxIdAssociation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='nameAddressTaxIdAssociation'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='nameAddressTaxIdAssociation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdescription>%s</%sdescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.description), input_name='description')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type nameAddressTaxIdAssociationCode
            self.validate_nameAddressTaxIdAssociationCode(self.code)
        elif nodeName_ == 'description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'description')
            value_ = self.gds_validate_string(value_, node, 'description')
            self.description = value_
            self.description_nsprefix_ = child_.prefix
            # validate type descriptionType14
            self.validate_descriptionType14(self.description)
# end class nameAddressTaxIdAssociation


class businessNameAddressPhoneAssociation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, code=None, description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_businessNameAddressPhoneAssociationCode(self.code)
        self.code_nsprefix_ = None
        self.description = description
        self.validate_descriptionType15(self.description)
        self.description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, businessNameAddressPhoneAssociation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if businessNameAddressPhoneAssociation.subclass:
            return businessNameAddressPhoneAssociation.subclass(*args_, **kwargs_)
        else:
            return businessNameAddressPhoneAssociation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def validate_businessNameAddressPhoneAssociationCode(self, value):
        result = True
        # Validate type businessNameAddressPhoneAssociationCode, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['NOT_VERIFIED', 'WRONG_PHONE', 'NAME_OR_ADDRESS', 'BAD_NAME', 'BAD_ADDRESS', 'MISSING_ADDRESS', 'NAME_AND_ADDRESS_BAD_PHONE', 'NAME_AND_ADDRESS_NO_PHONE', 'NAME_ADDRESS_PHONE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on businessNameAddressPhoneAssociationCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_descriptionType15(self, value):
        result = True
        # Validate type descriptionType15, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 120:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on descriptionType15' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on descriptionType15' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessNameAddressPhoneAssociation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('businessNameAddressPhoneAssociation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'businessNameAddressPhoneAssociation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='businessNameAddressPhoneAssociation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='businessNameAddressPhoneAssociation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='businessNameAddressPhoneAssociation'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessNameAddressPhoneAssociation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdescription>%s</%sdescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.description), input_name='description')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type businessNameAddressPhoneAssociationCode
            self.validate_businessNameAddressPhoneAssociationCode(self.code)
        elif nodeName_ == 'description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'description')
            value_ = self.gds_validate_string(value_, node, 'description')
            self.description = value_
            self.description_nsprefix_ = child_.prefix
            # validate type descriptionType15
            self.validate_descriptionType15(self.description)
# end class businessNameAddressPhoneAssociation


class businessVerificationIndicators(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, nameVerified=None, addressVerified=None, cityVerified=None, stateVerified=None, zipVerified=None, phoneVerified=None, taxIdVerified=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.nameVerified = nameVerified
        self.nameVerified_nsprefix_ = None
        self.addressVerified = addressVerified
        self.addressVerified_nsprefix_ = None
        self.cityVerified = cityVerified
        self.cityVerified_nsprefix_ = None
        self.stateVerified = stateVerified
        self.stateVerified_nsprefix_ = None
        self.zipVerified = zipVerified
        self.zipVerified_nsprefix_ = None
        self.phoneVerified = phoneVerified
        self.phoneVerified_nsprefix_ = None
        self.taxIdVerified = taxIdVerified
        self.taxIdVerified_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, businessVerificationIndicators)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if businessVerificationIndicators.subclass:
            return businessVerificationIndicators.subclass(*args_, **kwargs_)
        else:
            return businessVerificationIndicators(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_nameVerified(self):
        return self.nameVerified
    def set_nameVerified(self, nameVerified):
        self.nameVerified = nameVerified
    def get_addressVerified(self):
        return self.addressVerified
    def set_addressVerified(self, addressVerified):
        self.addressVerified = addressVerified
    def get_cityVerified(self):
        return self.cityVerified
    def set_cityVerified(self, cityVerified):
        self.cityVerified = cityVerified
    def get_stateVerified(self):
        return self.stateVerified
    def set_stateVerified(self, stateVerified):
        self.stateVerified = stateVerified
    def get_zipVerified(self):
        return self.zipVerified
    def set_zipVerified(self, zipVerified):
        self.zipVerified = zipVerified
    def get_phoneVerified(self):
        return self.phoneVerified
    def set_phoneVerified(self, phoneVerified):
        self.phoneVerified = phoneVerified
    def get_taxIdVerified(self):
        return self.taxIdVerified
    def set_taxIdVerified(self, taxIdVerified):
        self.taxIdVerified = taxIdVerified
    def hasContent_(self):
        if (
            self.nameVerified is not None or
            self.addressVerified is not None or
            self.cityVerified is not None or
            self.stateVerified is not None or
            self.zipVerified is not None or
            self.phoneVerified is not None or
            self.taxIdVerified is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessVerificationIndicators', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('businessVerificationIndicators')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'businessVerificationIndicators':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='businessVerificationIndicators')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='businessVerificationIndicators', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='businessVerificationIndicators'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessVerificationIndicators', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.nameVerified is not None:
            namespaceprefix_ = self.nameVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.nameVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snameVerified>%s</%snameVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.nameVerified, input_name='nameVerified'), namespaceprefix_ , eol_))
        if self.addressVerified is not None:
            namespaceprefix_ = self.addressVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.addressVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddressVerified>%s</%saddressVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.addressVerified, input_name='addressVerified'), namespaceprefix_ , eol_))
        if self.cityVerified is not None:
            namespaceprefix_ = self.cityVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.cityVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scityVerified>%s</%scityVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.cityVerified, input_name='cityVerified'), namespaceprefix_ , eol_))
        if self.stateVerified is not None:
            namespaceprefix_ = self.stateVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.stateVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstateVerified>%s</%sstateVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.stateVerified, input_name='stateVerified'), namespaceprefix_ , eol_))
        if self.zipVerified is not None:
            namespaceprefix_ = self.zipVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.zipVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szipVerified>%s</%szipVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.zipVerified, input_name='zipVerified'), namespaceprefix_ , eol_))
        if self.phoneVerified is not None:
            namespaceprefix_ = self.phoneVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.phoneVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sphoneVerified>%s</%sphoneVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.phoneVerified, input_name='phoneVerified'), namespaceprefix_ , eol_))
        if self.taxIdVerified is not None:
            namespaceprefix_ = self.taxIdVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.taxIdVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxIdVerified>%s</%staxIdVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.taxIdVerified, input_name='taxIdVerified'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'nameVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'nameVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'nameVerified')
            self.nameVerified = ival_
            self.nameVerified_nsprefix_ = child_.prefix
        elif nodeName_ == 'addressVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'addressVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'addressVerified')
            self.addressVerified = ival_
            self.addressVerified_nsprefix_ = child_.prefix
        elif nodeName_ == 'cityVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'cityVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'cityVerified')
            self.cityVerified = ival_
            self.cityVerified_nsprefix_ = child_.prefix
        elif nodeName_ == 'stateVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'stateVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'stateVerified')
            self.stateVerified = ival_
            self.stateVerified_nsprefix_ = child_.prefix
        elif nodeName_ == 'zipVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'zipVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'zipVerified')
            self.zipVerified = ival_
            self.zipVerified_nsprefix_ = child_.prefix
        elif nodeName_ == 'phoneVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'phoneVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'phoneVerified')
            self.phoneVerified = ival_
            self.phoneVerified_nsprefix_ = child_.prefix
        elif nodeName_ == 'taxIdVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'taxIdVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'taxIdVerified')
            self.taxIdVerified = ival_
            self.taxIdVerified_nsprefix_ = child_.prefix
# end class businessVerificationIndicators


class potentialRiskIndicator(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, code=None, description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_riskIndicatorCode(self.code)
        self.code_nsprefix_ = None
        self.description = description
        self.validate_descriptionType16(self.description)
        self.description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, potentialRiskIndicator)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if potentialRiskIndicator.subclass:
            return potentialRiskIndicator.subclass(*args_, **kwargs_)
        else:
            return potentialRiskIndicator(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def validate_riskIndicatorCode(self, value):
        result = True
        # Validate type riskIndicatorCode, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['UNKNOWN', 'SSN_DECEASED', 'SSN_PRIOR_TO_DOB', 'SSN_ADDRESS_PHONE_NOT_MATCH', 'SSN_INVALID', 'PHONE_NUMBER_DISCONNECTED', 'PHONE_NUMBER_INVALID', 'PHONE_NUMBER_PAGER', 'PHONE_NUMBER_MOBILE', 'ADDRESS_INVALID', 'ZIP_BELONGS_POST_OFFICE', 'ADDRESS_INVALID_APARTMENT_DESIGNATION', 'ADDRESS_COMMERCIAL', 'PHONE_NUMBER_COMMERCIAL', 'PHONE_NUMBER_ZIP_INVALID', 'UNABLE_TO_VERIFY_NAS', 'UNABLE_TO_VERIFY_ADDRESS', 'UNABLE_TO_VERIFY_SSN', 'UNABLE_TO_VERIFY_PHONE', 'UNABLE_TO_VERIFY_DOB', 'SSN_MISKEYED', 'ADDRESS_MISKEYED', 'PHONE_NUMBER_MISKEYED', 'NAME_MATCHES_OFAC', 'UNABLE_TO_VERIFY_NAME', 'SSN_MATCHES_MULTI_NAMES', 'SSN_RECENTLY_ISSUED', 'ZIP_CORPORATE_MILITARY', 'DLL_INVALID', 'NAME_ADDRESS_MATCH_BANKRUPTCY', 'PHONE_AREA_CODE_CHANGING', 'WORK_PHONE_PAGER', 'UNABLE_TO_VERIFY_FIRST_NAME', 'PHONE_ADDRESS_DISTANT', 'ADDRESS_MATCHES_PRISON', 'SSN_LAST_NAME_NO_MATCH', 'SSN_FIRST_NAME_NO_MATCH', 'WORK_HOME_PHONE_DISTANT', 'NAME_ADDRESS_TIN_MISMATCH', 'WORK_PHONE_INVALID', 'WORK_PHONE_DISCONNECTED', 'WORK_PHONE_MOBILE', 'ADDRESS_RETURNS_DIFF_PHONE', 'SSN_LNAME_NOT_MATCHED_FNAME_MATCHED', 'PHONE_RESIDENTIAL_LISTING', 'SINGLE_FAMILY_DWELLING', 'SSN_NOT_FOUND', 'SSN_BELONGS_TO_DIFF_NAME_ADDRESS', 'PHONE_BELONGS_TO_DIFF_NAME_ADDRESS', 'NAME_ADDRESS_UNLISTED', 'NAME_MISKEYED', 'NAME_MISSING', 'ADDRESS_MISSING', 'SSN_MISSING', 'PHONE_NUMBER_MISSING', 'DOB_MISSING', 'NAME_ADDRESS_RETURN_DIFF_PHONE', 'DOB_MISKEYED', 'SSN_NON_US_CITIZEN', 'ALTERNATE_BUSINESS_NAME_FOUND', 'DBA_MATCH_PUBLIC_RECORDS', 'SSN_RECENT', 'SSN_TOO_OLD', 'TIN_NAME_ADDRESS_MISMATCH', 'BUSINESS_NOT_IN_GOOD_STANDING', 'NAME_ADDRESS_MATCH_JUDGMENT', 'BUSINESS_INACTIVE', 'NO_UPDATE_IN_LAST_THREE_YEARS', 'SSN_NOT_PRIMARY', 'ZIP_CORP_ONLY', 'ADDRESS_MISMATCH', 'DL_DIFFERENT', 'DL_NOT_FOUND', 'DL_MISKEYED', 'UNABLE_TO_VERIFY_DL', 'SSN_INVALID_SSA', 'SSN_IS_ITIN', 'SSN_MULTI_IDENTITY', 'ZIP_MILITARY', 'MULTIPLE_SSN_FOUND', 'ADDRESS_DISCREPANCY', 'ADDRESS_PO_BOX', 'SSN_RANDOM_SSA', 'ADDRESS_MISMATCH_SECONDARY', 'NAME_MATCHES_NON_OFAC', 'UNABLE_TO_VERIFY_ZIP_CODE', 'IP_ADDRESS_UNKNOWN', 'IP_ADDRESS_DIFFERENT_STATE', 'IP_ADDRESS_DIFFERENT_ZIP', 'IP_ADDRESS_DIFFERENT_PHONE', 'IP_ADDRESS_DOMAIN_UNKNOWN', 'IP_ADDRESS_NOT_ASSIGNED_TO_USA', 'IP_ADDRESS_NON_ROUTABLE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on riskIndicatorCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_descriptionType16(self, value):
        result = True
        # Validate type descriptionType16, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 120:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on descriptionType16' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on descriptionType16' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='potentialRiskIndicator', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('potentialRiskIndicator')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'potentialRiskIndicator':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='potentialRiskIndicator')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='potentialRiskIndicator', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='potentialRiskIndicator'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='potentialRiskIndicator', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdescription>%s</%sdescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.description), input_name='description')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type riskIndicatorCode
            self.validate_riskIndicatorCode(self.code)
        elif nodeName_ == 'description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'description')
            value_ = self.gds_validate_string(value_, node, 'description')
            self.description = value_
            self.description_nsprefix_ = child_.prefix
            # validate type descriptionType16
            self.validate_descriptionType16(self.description)
# end class potentialRiskIndicator


class principalResult(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, verificationResult=None, backgroundCheckDecisionNotes=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.verificationResult = verificationResult
        self.verificationResult_nsprefix_ = None
        self.backgroundCheckDecisionNotes = backgroundCheckDecisionNotes
        self.validate_backgroundCheckDecisionNotesType17(self.backgroundCheckDecisionNotes)
        self.backgroundCheckDecisionNotes_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, principalResult)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if principalResult.subclass:
            return principalResult.subclass(*args_, **kwargs_)
        else:
            return principalResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_verificationResult(self):
        return self.verificationResult
    def set_verificationResult(self, verificationResult):
        self.verificationResult = verificationResult
    def get_backgroundCheckDecisionNotes(self):
        return self.backgroundCheckDecisionNotes
    def set_backgroundCheckDecisionNotes(self, backgroundCheckDecisionNotes):
        self.backgroundCheckDecisionNotes = backgroundCheckDecisionNotes
    def validate_backgroundCheckDecisionNotesType17(self, value):
        result = True
        # Validate type backgroundCheckDecisionNotesType17, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on backgroundCheckDecisionNotesType17' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on backgroundCheckDecisionNotesType17' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.verificationResult is not None or
            self.backgroundCheckDecisionNotes is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalResult', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('principalResult')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'principalResult':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='principalResult')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='principalResult', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='principalResult'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalResult', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.verificationResult is not None:
            namespaceprefix_ = self.verificationResult_nsprefix_ + ':' if (UseCapturedNS_ and self.verificationResult_nsprefix_) else ''
            self.verificationResult.export(outfile, level, namespaceprefix_, namespacedef_='', name_='verificationResult', pretty_print=pretty_print)
        if self.backgroundCheckDecisionNotes is not None:
            namespaceprefix_ = self.backgroundCheckDecisionNotes_nsprefix_ + ':' if (UseCapturedNS_ and self.backgroundCheckDecisionNotes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbackgroundCheckDecisionNotes>%s</%sbackgroundCheckDecisionNotes>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.backgroundCheckDecisionNotes), input_name='backgroundCheckDecisionNotes')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'verificationResult':
            obj_ = principalVerificationResult.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.verificationResult = obj_
            obj_.original_tagname_ = 'verificationResult'
        elif nodeName_ == 'backgroundCheckDecisionNotes':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'backgroundCheckDecisionNotes')
            value_ = self.gds_validate_string(value_, node, 'backgroundCheckDecisionNotes')
            self.backgroundCheckDecisionNotes = value_
            self.backgroundCheckDecisionNotes_nsprefix_ = child_.prefix
            # validate type backgroundCheckDecisionNotesType17
            self.validate_backgroundCheckDecisionNotesType17(self.backgroundCheckDecisionNotes)
# end class principalResult


class principalVerificationResult(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, overallScore=None, nameAddressSsnAssociation=None, nameAddressPhoneAssociation=None, verificationIndicators=None, riskIndicators=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.overallScore = overallScore
        self.overallScore_nsprefix_ = None
        self.nameAddressSsnAssociation = nameAddressSsnAssociation
        self.nameAddressSsnAssociation_nsprefix_ = None
        self.nameAddressPhoneAssociation = nameAddressPhoneAssociation
        self.nameAddressPhoneAssociation_nsprefix_ = None
        self.verificationIndicators = verificationIndicators
        self.verificationIndicators_nsprefix_ = None
        self.riskIndicators = riskIndicators
        self.riskIndicators_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, principalVerificationResult)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if principalVerificationResult.subclass:
            return principalVerificationResult.subclass(*args_, **kwargs_)
        else:
            return principalVerificationResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_overallScore(self):
        return self.overallScore
    def set_overallScore(self, overallScore):
        self.overallScore = overallScore
    def get_nameAddressSsnAssociation(self):
        return self.nameAddressSsnAssociation
    def set_nameAddressSsnAssociation(self, nameAddressSsnAssociation):
        self.nameAddressSsnAssociation = nameAddressSsnAssociation
    def get_nameAddressPhoneAssociation(self):
        return self.nameAddressPhoneAssociation
    def set_nameAddressPhoneAssociation(self, nameAddressPhoneAssociation):
        self.nameAddressPhoneAssociation = nameAddressPhoneAssociation
    def get_verificationIndicators(self):
        return self.verificationIndicators
    def set_verificationIndicators(self, verificationIndicators):
        self.verificationIndicators = verificationIndicators
    def get_riskIndicators(self):
        return self.riskIndicators
    def set_riskIndicators(self, riskIndicators):
        self.riskIndicators = riskIndicators
    def hasContent_(self):
        if (
            self.overallScore is not None or
            self.nameAddressSsnAssociation is not None or
            self.nameAddressPhoneAssociation is not None or
            self.verificationIndicators is not None or
            self.riskIndicators is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalVerificationResult', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('principalVerificationResult')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'principalVerificationResult':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='principalVerificationResult')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='principalVerificationResult', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='principalVerificationResult'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalVerificationResult', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.overallScore is not None:
            namespaceprefix_ = self.overallScore_nsprefix_ + ':' if (UseCapturedNS_ and self.overallScore_nsprefix_) else ''
            self.overallScore.export(outfile, level, namespaceprefix_, namespacedef_='', name_='overallScore', pretty_print=pretty_print)
        if self.nameAddressSsnAssociation is not None:
            namespaceprefix_ = self.nameAddressSsnAssociation_nsprefix_ + ':' if (UseCapturedNS_ and self.nameAddressSsnAssociation_nsprefix_) else ''
            self.nameAddressSsnAssociation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='nameAddressSsnAssociation', pretty_print=pretty_print)
        if self.nameAddressPhoneAssociation is not None:
            namespaceprefix_ = self.nameAddressPhoneAssociation_nsprefix_ + ':' if (UseCapturedNS_ and self.nameAddressPhoneAssociation_nsprefix_) else ''
            self.nameAddressPhoneAssociation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='nameAddressPhoneAssociation', pretty_print=pretty_print)
        if self.verificationIndicators is not None:
            namespaceprefix_ = self.verificationIndicators_nsprefix_ + ':' if (UseCapturedNS_ and self.verificationIndicators_nsprefix_) else ''
            self.verificationIndicators.export(outfile, level, namespaceprefix_, namespacedef_='', name_='verificationIndicators', pretty_print=pretty_print)
        if self.riskIndicators is not None:
            namespaceprefix_ = self.riskIndicators_nsprefix_ + ':' if (UseCapturedNS_ and self.riskIndicators_nsprefix_) else ''
            self.riskIndicators.export(outfile, level, namespaceprefix_, namespacedef_='', name_='riskIndicators', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'overallScore':
            obj_ = principalScore.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.overallScore = obj_
            obj_.original_tagname_ = 'overallScore'
        elif nodeName_ == 'nameAddressSsnAssociation':
            obj_ = nameAddressSsnAssociation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.nameAddressSsnAssociation = obj_
            obj_.original_tagname_ = 'nameAddressSsnAssociation'
        elif nodeName_ == 'nameAddressPhoneAssociation':
            obj_ = principalNameAddressPhoneAssociation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.nameAddressPhoneAssociation = obj_
            obj_.original_tagname_ = 'nameAddressPhoneAssociation'
        elif nodeName_ == 'verificationIndicators':
            obj_ = principalVerificationIndicators.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.verificationIndicators = obj_
            obj_.original_tagname_ = 'verificationIndicators'
        elif nodeName_ == 'riskIndicators':
            obj_ = riskIndicatorsType18.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.riskIndicators = obj_
            obj_.original_tagname_ = 'riskIndicators'
# end class principalVerificationResult


class principalScore(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, score=None, description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.score = score
        self.validate_principalOverallScore(self.score)
        self.score_nsprefix_ = None
        self.description = description
        self.validate_descriptionType19(self.description)
        self.description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, principalScore)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if principalScore.subclass:
            return principalScore.subclass(*args_, **kwargs_)
        else:
            return principalScore(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_score(self):
        return self.score
    def set_score(self, score):
        self.score = score
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def validate_principalOverallScore(self, value):
        result = True
        # Validate type principalOverallScore, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0, 10, 20, 30, 40, 50]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on principalOverallScore' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_descriptionType19(self, value):
        result = True
        # Validate type descriptionType19, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 200:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on descriptionType19' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on descriptionType19' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.score is not None or
            self.description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalScore', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('principalScore')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'principalScore':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='principalScore')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='principalScore', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='principalScore'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalScore', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.score is not None:
            namespaceprefix_ = self.score_nsprefix_ + ':' if (UseCapturedNS_ and self.score_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sscore>%s</%sscore>%s' % (namespaceprefix_ , self.gds_format_integer(self.score, input_name='score'), namespaceprefix_ , eol_))
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdescription>%s</%sdescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.description), input_name='description')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'score' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'score')
            ival_ = self.gds_validate_integer(ival_, node, 'score')
            self.score = ival_
            self.score_nsprefix_ = child_.prefix
            # validate type principalOverallScore
            self.validate_principalOverallScore(self.score)
        elif nodeName_ == 'description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'description')
            value_ = self.gds_validate_string(value_, node, 'description')
            self.description = value_
            self.description_nsprefix_ = child_.prefix
            # validate type descriptionType19
            self.validate_descriptionType19(self.description)
# end class principalScore


class nameAddressSsnAssociation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, code=None, description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_nameAddressSsnAssociationCode(self.code)
        self.code_nsprefix_ = None
        self.description = description
        self.validate_descriptionType20(self.description)
        self.description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, nameAddressSsnAssociation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if nameAddressSsnAssociation.subclass:
            return nameAddressSsnAssociation.subclass(*args_, **kwargs_)
        else:
            return nameAddressSsnAssociation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def validate_nameAddressSsnAssociationCode(self, value):
        result = True
        # Validate type nameAddressSsnAssociationCode, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['NOTHING', 'WRONG_SSN', 'FIRST_LAST', 'FIRST_ADDRESS', 'FIRST_SSN', 'LAST_ADDRESS', 'ADDRESS_SSN', 'LAST_SSN', 'FIRST_LAST_ADDRESS', 'FIRST_LAST_SSN', 'FIRST_ADDRESS_SSN', 'LAST_ADDRESS_SSN', 'FIRST_LAST_ADDRESS_SSN']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on nameAddressSsnAssociationCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_descriptionType20(self, value):
        result = True
        # Validate type descriptionType20, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on descriptionType20' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on descriptionType20' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='nameAddressSsnAssociation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('nameAddressSsnAssociation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'nameAddressSsnAssociation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='nameAddressSsnAssociation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='nameAddressSsnAssociation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='nameAddressSsnAssociation'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='nameAddressSsnAssociation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdescription>%s</%sdescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.description), input_name='description')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type nameAddressSsnAssociationCode
            self.validate_nameAddressSsnAssociationCode(self.code)
        elif nodeName_ == 'description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'description')
            value_ = self.gds_validate_string(value_, node, 'description')
            self.description = value_
            self.description_nsprefix_ = child_.prefix
            # validate type descriptionType20
            self.validate_descriptionType20(self.description)
# end class nameAddressSsnAssociation


class principalNameAddressPhoneAssociation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, code=None, description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_principalNameAddressPhoneAssociationCode(self.code)
        self.code_nsprefix_ = None
        self.description = description
        self.validate_descriptionType21(self.description)
        self.description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, principalNameAddressPhoneAssociation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if principalNameAddressPhoneAssociation.subclass:
            return principalNameAddressPhoneAssociation.subclass(*args_, **kwargs_)
        else:
            return principalNameAddressPhoneAssociation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_code(self):
        return self.code
    def set_code(self, code):
        self.code = code
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def validate_principalNameAddressPhoneAssociationCode(self, value):
        result = True
        # Validate type principalNameAddressPhoneAssociationCode, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['NOTHING', 'WRONG_PHONE', 'FIRST_LAST', 'FIRST_ADDRESS', 'FIRST_PHONE', 'LAST_ADDRESS', 'ADDRESS_PHONE', 'LAST_PHONE', 'FIRST_LAST_ADDRESS', 'FIRST_LAST_PHONE', 'FIRST_ADDRESS_PHONE', 'LAST_ADDRESS_PHONE', 'FIRST_LAST_ADDRESS_PHONE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on principalNameAddressPhoneAssociationCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_descriptionType21(self, value):
        result = True
        # Validate type descriptionType21, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on descriptionType21' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on descriptionType21' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalNameAddressPhoneAssociation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('principalNameAddressPhoneAssociation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'principalNameAddressPhoneAssociation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='principalNameAddressPhoneAssociation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='principalNameAddressPhoneAssociation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='principalNameAddressPhoneAssociation'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalNameAddressPhoneAssociation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.code is not None:
            namespaceprefix_ = self.code_nsprefix_ + ':' if (UseCapturedNS_ and self.code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scode>%s</%scode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.code), input_name='code')), namespaceprefix_ , eol_))
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdescription>%s</%sdescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.description), input_name='description')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type principalNameAddressPhoneAssociationCode
            self.validate_principalNameAddressPhoneAssociationCode(self.code)
        elif nodeName_ == 'description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'description')
            value_ = self.gds_validate_string(value_, node, 'description')
            self.description = value_
            self.description_nsprefix_ = child_.prefix
            # validate type descriptionType21
            self.validate_descriptionType21(self.description)
# end class principalNameAddressPhoneAssociation


class principalVerificationIndicators(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, nameVerified=None, addressVerified=None, phoneVerified=None, ssnVerified=None, dobVerified=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.nameVerified = nameVerified
        self.nameVerified_nsprefix_ = None
        self.addressVerified = addressVerified
        self.addressVerified_nsprefix_ = None
        self.phoneVerified = phoneVerified
        self.phoneVerified_nsprefix_ = None
        self.ssnVerified = ssnVerified
        self.ssnVerified_nsprefix_ = None
        self.dobVerified = dobVerified
        self.dobVerified_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, principalVerificationIndicators)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if principalVerificationIndicators.subclass:
            return principalVerificationIndicators.subclass(*args_, **kwargs_)
        else:
            return principalVerificationIndicators(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_nameVerified(self):
        return self.nameVerified
    def set_nameVerified(self, nameVerified):
        self.nameVerified = nameVerified
    def get_addressVerified(self):
        return self.addressVerified
    def set_addressVerified(self, addressVerified):
        self.addressVerified = addressVerified
    def get_phoneVerified(self):
        return self.phoneVerified
    def set_phoneVerified(self, phoneVerified):
        self.phoneVerified = phoneVerified
    def get_ssnVerified(self):
        return self.ssnVerified
    def set_ssnVerified(self, ssnVerified):
        self.ssnVerified = ssnVerified
    def get_dobVerified(self):
        return self.dobVerified
    def set_dobVerified(self, dobVerified):
        self.dobVerified = dobVerified
    def hasContent_(self):
        if (
            self.nameVerified is not None or
            self.addressVerified is not None or
            self.phoneVerified is not None or
            self.ssnVerified is not None or
            self.dobVerified is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalVerificationIndicators', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('principalVerificationIndicators')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'principalVerificationIndicators':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='principalVerificationIndicators')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='principalVerificationIndicators', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='principalVerificationIndicators'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalVerificationIndicators', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.nameVerified is not None:
            namespaceprefix_ = self.nameVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.nameVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snameVerified>%s</%snameVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.nameVerified, input_name='nameVerified'), namespaceprefix_ , eol_))
        if self.addressVerified is not None:
            namespaceprefix_ = self.addressVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.addressVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddressVerified>%s</%saddressVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.addressVerified, input_name='addressVerified'), namespaceprefix_ , eol_))
        if self.phoneVerified is not None:
            namespaceprefix_ = self.phoneVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.phoneVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sphoneVerified>%s</%sphoneVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.phoneVerified, input_name='phoneVerified'), namespaceprefix_ , eol_))
        if self.ssnVerified is not None:
            namespaceprefix_ = self.ssnVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.ssnVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sssnVerified>%s</%sssnVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.ssnVerified, input_name='ssnVerified'), namespaceprefix_ , eol_))
        if self.dobVerified is not None:
            namespaceprefix_ = self.dobVerified_nsprefix_ + ':' if (UseCapturedNS_ and self.dobVerified_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdobVerified>%s</%sdobVerified>%s' % (namespaceprefix_ , self.gds_format_boolean(self.dobVerified, input_name='dobVerified'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'nameVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'nameVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'nameVerified')
            self.nameVerified = ival_
            self.nameVerified_nsprefix_ = child_.prefix
        elif nodeName_ == 'addressVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'addressVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'addressVerified')
            self.addressVerified = ival_
            self.addressVerified_nsprefix_ = child_.prefix
        elif nodeName_ == 'phoneVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'phoneVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'phoneVerified')
            self.phoneVerified = ival_
            self.phoneVerified_nsprefix_ = child_.prefix
        elif nodeName_ == 'ssnVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'ssnVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'ssnVerified')
            self.ssnVerified = ival_
            self.ssnVerified_nsprefix_ = child_.prefix
        elif nodeName_ == 'dobVerified':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'dobVerified')
            ival_ = self.gds_validate_boolean(ival_, node, 'dobVerified')
            self.dobVerified = ival_
            self.dobVerified_nsprefix_ = child_.prefix
# end class principalVerificationIndicators


class businessToPrincipalAssociation(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, score=None, description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.score = score
        self.validate_businessToPrincipalScore(self.score)
        self.score_nsprefix_ = None
        self.description = description
        self.validate_descriptionType22(self.description)
        self.description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, businessToPrincipalAssociation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if businessToPrincipalAssociation.subclass:
            return businessToPrincipalAssociation.subclass(*args_, **kwargs_)
        else:
            return businessToPrincipalAssociation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_score(self):
        return self.score
    def set_score(self, score):
        self.score = score
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def validate_businessToPrincipalScore(self, value):
        result = True
        # Validate type businessToPrincipalScore, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0, 10, 20, 30, 40, 50]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on businessToPrincipalScore' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_descriptionType22(self, value):
        result = True
        # Validate type descriptionType22, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 95:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on descriptionType22' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on descriptionType22' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.score is not None or
            self.description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessToPrincipalAssociation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('businessToPrincipalAssociation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'businessToPrincipalAssociation':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='businessToPrincipalAssociation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='businessToPrincipalAssociation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='businessToPrincipalAssociation'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='businessToPrincipalAssociation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.score is not None:
            namespaceprefix_ = self.score_nsprefix_ + ':' if (UseCapturedNS_ and self.score_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sscore>%s</%sscore>%s' % (namespaceprefix_ , self.gds_format_integer(self.score, input_name='score'), namespaceprefix_ , eol_))
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdescription>%s</%sdescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.description), input_name='description')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'score' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'score')
            ival_ = self.gds_validate_integer(ival_, node, 'score')
            self.score = ival_
            self.score_nsprefix_ = child_.prefix
            # validate type businessToPrincipalScore
            self.validate_businessToPrincipalScore(self.score)
        elif nodeName_ == 'description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'description')
            value_ = self.gds_validate_string(value_, node, 'description')
            self.description = value_
            self.description_nsprefix_ = child_.prefix
            # validate type descriptionType22
            self.validate_descriptionType22(self.description)
# end class businessToPrincipalAssociation


class bankruptcyResult(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, bankruptcyType=None, bankruptcyCount=None, companyName=None, streetAddress1=None, streetAddress2=None, city=None, state=None, zip=None, zip4=None, filingDate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.bankruptcyType = bankruptcyType
        self.validate_bankruptcyTypeType(self.bankruptcyType)
        self.bankruptcyType_nsprefix_ = None
        self.bankruptcyCount = bankruptcyCount
        self.bankruptcyCount_nsprefix_ = None
        self.companyName = companyName
        self.validate_companyNameType(self.companyName)
        self.companyName_nsprefix_ = None
        self.streetAddress1 = streetAddress1
        self.validate_streetAddress1Type23(self.streetAddress1)
        self.streetAddress1_nsprefix_ = None
        self.streetAddress2 = streetAddress2
        self.validate_streetAddress2Type24(self.streetAddress2)
        self.streetAddress2_nsprefix_ = None
        self.city = city
        self.validate_cityType25(self.city)
        self.city_nsprefix_ = None
        self.state = state
        self.validate_stateType(self.state)
        self.state_nsprefix_ = None
        self.zip = zip
        self.validate_zipType(self.zip)
        self.zip_nsprefix_ = None
        self.zip4 = zip4
        self.validate_zip4Type(self.zip4)
        self.zip4_nsprefix_ = None
        if isinstance(filingDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(filingDate, '%Y-%m-%d').date()
        else:
            initvalue_ = filingDate
        self.filingDate = initvalue_
        self.filingDate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, bankruptcyResult)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if bankruptcyResult.subclass:
            return bankruptcyResult.subclass(*args_, **kwargs_)
        else:
            return bankruptcyResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_bankruptcyType(self):
        return self.bankruptcyType
    def set_bankruptcyType(self, bankruptcyType):
        self.bankruptcyType = bankruptcyType
    def get_bankruptcyCount(self):
        return self.bankruptcyCount
    def set_bankruptcyCount(self, bankruptcyCount):
        self.bankruptcyCount = bankruptcyCount
    def get_companyName(self):
        return self.companyName
    def set_companyName(self, companyName):
        self.companyName = companyName
    def get_streetAddress1(self):
        return self.streetAddress1
    def set_streetAddress1(self, streetAddress1):
        self.streetAddress1 = streetAddress1
    def get_streetAddress2(self):
        return self.streetAddress2
    def set_streetAddress2(self, streetAddress2):
        self.streetAddress2 = streetAddress2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_zip(self):
        return self.zip
    def set_zip(self, zip):
        self.zip = zip
    def get_zip4(self):
        return self.zip4
    def set_zip4(self, zip4):
        self.zip4 = zip4
    def get_filingDate(self):
        return self.filingDate
    def set_filingDate(self, filingDate):
        self.filingDate = filingDate
    def validate_bankruptcyTypeType(self, value):
        result = True
        # Validate type bankruptcyTypeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on bankruptcyTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on bankruptcyTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_companyNameType(self, value):
        result = True
        # Validate type companyNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 120:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on companyNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on companyNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_streetAddress1Type23(self, value):
        result = True
        # Validate type streetAddress1Type23, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on streetAddress1Type23' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on streetAddress1Type23' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_streetAddress2Type24(self, value):
        result = True
        # Validate type streetAddress2Type24, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on streetAddress2Type24' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on streetAddress2Type24' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_cityType25(self, value):
        result = True
        # Validate type cityType25, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType25' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on cityType25' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_stateType(self, value):
        result = True
        # Validate type stateType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on stateType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on stateType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_zipType(self, value):
        result = True
        # Validate type zipType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on zipType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on zipType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_zip4Type(self, value):
        result = True
        # Validate type zip4Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on zip4Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on zip4Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.bankruptcyType is not None or
            self.bankruptcyCount is not None or
            self.companyName is not None or
            self.streetAddress1 is not None or
            self.streetAddress2 is not None or
            self.city is not None or
            self.state is not None or
            self.zip is not None or
            self.zip4 is not None or
            self.filingDate is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='bankruptcyResult', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('bankruptcyResult')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'bankruptcyResult':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='bankruptcyResult')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='bankruptcyResult', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='bankruptcyResult'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='bankruptcyResult', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.bankruptcyType is not None:
            namespaceprefix_ = self.bankruptcyType_nsprefix_ + ':' if (UseCapturedNS_ and self.bankruptcyType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbankruptcyType>%s</%sbankruptcyType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.bankruptcyType), input_name='bankruptcyType')), namespaceprefix_ , eol_))
        if self.bankruptcyCount is not None:
            namespaceprefix_ = self.bankruptcyCount_nsprefix_ + ':' if (UseCapturedNS_ and self.bankruptcyCount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbankruptcyCount>%s</%sbankruptcyCount>%s' % (namespaceprefix_ , self.gds_format_integer(self.bankruptcyCount, input_name='bankruptcyCount'), namespaceprefix_ , eol_))
        if self.companyName is not None:
            namespaceprefix_ = self.companyName_nsprefix_ + ':' if (UseCapturedNS_ and self.companyName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompanyName>%s</%scompanyName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.companyName), input_name='companyName')), namespaceprefix_ , eol_))
        if self.streetAddress1 is not None:
            namespaceprefix_ = self.streetAddress1_nsprefix_ + ':' if (UseCapturedNS_ and self.streetAddress1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress1>%s</%sstreetAddress1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.streetAddress1), input_name='streetAddress1')), namespaceprefix_ , eol_))
        if self.streetAddress2 is not None:
            namespaceprefix_ = self.streetAddress2_nsprefix_ + ':' if (UseCapturedNS_ and self.streetAddress2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress2>%s</%sstreetAddress2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.streetAddress2), input_name='streetAddress2')), namespaceprefix_ , eol_))
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.state is not None:
            namespaceprefix_ = self.state_nsprefix_ + ':' if (UseCapturedNS_ and self.state_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstate>%s</%sstate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.state), input_name='state')), namespaceprefix_ , eol_))
        if self.zip is not None:
            namespaceprefix_ = self.zip_nsprefix_ + ':' if (UseCapturedNS_ and self.zip_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szip>%s</%szip>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zip), input_name='zip')), namespaceprefix_ , eol_))
        if self.zip4 is not None:
            namespaceprefix_ = self.zip4_nsprefix_ + ':' if (UseCapturedNS_ and self.zip4_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szip4>%s</%szip4>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zip4), input_name='zip4')), namespaceprefix_ , eol_))
        if self.filingDate is not None:
            namespaceprefix_ = self.filingDate_nsprefix_ + ':' if (UseCapturedNS_ and self.filingDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfilingDate>%s</%sfilingDate>%s' % (namespaceprefix_ , self.gds_format_date(self.filingDate, input_name='filingDate'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'bankruptcyType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'bankruptcyType')
            value_ = self.gds_validate_string(value_, node, 'bankruptcyType')
            self.bankruptcyType = value_
            self.bankruptcyType_nsprefix_ = child_.prefix
            # validate type bankruptcyTypeType
            self.validate_bankruptcyTypeType(self.bankruptcyType)
        elif nodeName_ == 'bankruptcyCount' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'bankruptcyCount')
            ival_ = self.gds_validate_integer(ival_, node, 'bankruptcyCount')
            self.bankruptcyCount = ival_
            self.bankruptcyCount_nsprefix_ = child_.prefix
        elif nodeName_ == 'companyName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'companyName')
            value_ = self.gds_validate_string(value_, node, 'companyName')
            self.companyName = value_
            self.companyName_nsprefix_ = child_.prefix
            # validate type companyNameType
            self.validate_companyNameType(self.companyName)
        elif nodeName_ == 'streetAddress1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress1')
            value_ = self.gds_validate_string(value_, node, 'streetAddress1')
            self.streetAddress1 = value_
            self.streetAddress1_nsprefix_ = child_.prefix
            # validate type streetAddress1Type23
            self.validate_streetAddress1Type23(self.streetAddress1)
        elif nodeName_ == 'streetAddress2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress2')
            value_ = self.gds_validate_string(value_, node, 'streetAddress2')
            self.streetAddress2 = value_
            self.streetAddress2_nsprefix_ = child_.prefix
            # validate type streetAddress2Type24
            self.validate_streetAddress2Type24(self.streetAddress2)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType25
            self.validate_cityType25(self.city)
        elif nodeName_ == 'state':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'state')
            value_ = self.gds_validate_string(value_, node, 'state')
            self.state = value_
            self.state_nsprefix_ = child_.prefix
            # validate type stateType
            self.validate_stateType(self.state)
        elif nodeName_ == 'zip':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zip')
            value_ = self.gds_validate_string(value_, node, 'zip')
            self.zip = value_
            self.zip_nsprefix_ = child_.prefix
            # validate type zipType
            self.validate_zipType(self.zip)
        elif nodeName_ == 'zip4':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zip4')
            value_ = self.gds_validate_string(value_, node, 'zip4')
            self.zip4 = value_
            self.zip4_nsprefix_ = child_.prefix
            # validate type zip4Type
            self.validate_zip4Type(self.zip4)
        elif nodeName_ == 'filingDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.filingDate = dval_
            self.filingDate_nsprefix_ = child_.prefix
# end class bankruptcyResult


class lienResult(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lienType=None, releasedCount=None, unreleasedCount=None, companyName=None, streetAddress1=None, streetAddress2=None, city=None, state=None, zip=None, zip4=None, filingDate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lienType = lienType
        self.validate_lienTypeType(self.lienType)
        self.lienType_nsprefix_ = None
        self.releasedCount = releasedCount
        self.releasedCount_nsprefix_ = None
        self.unreleasedCount = unreleasedCount
        self.unreleasedCount_nsprefix_ = None
        self.companyName = companyName
        self.validate_companyNameType26(self.companyName)
        self.companyName_nsprefix_ = None
        self.streetAddress1 = streetAddress1
        self.validate_streetAddress1Type27(self.streetAddress1)
        self.streetAddress1_nsprefix_ = None
        self.streetAddress2 = streetAddress2
        self.validate_streetAddress2Type28(self.streetAddress2)
        self.streetAddress2_nsprefix_ = None
        self.city = city
        self.validate_cityType29(self.city)
        self.city_nsprefix_ = None
        self.state = state
        self.validate_stateType30(self.state)
        self.state_nsprefix_ = None
        self.zip = zip
        self.validate_zipType31(self.zip)
        self.zip_nsprefix_ = None
        self.zip4 = zip4
        self.validate_zip4Type32(self.zip4)
        self.zip4_nsprefix_ = None
        if isinstance(filingDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(filingDate, '%Y-%m-%d').date()
        else:
            initvalue_ = filingDate
        self.filingDate = initvalue_
        self.filingDate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, lienResult)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if lienResult.subclass:
            return lienResult.subclass(*args_, **kwargs_)
        else:
            return lienResult(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lienType(self):
        return self.lienType
    def set_lienType(self, lienType):
        self.lienType = lienType
    def get_releasedCount(self):
        return self.releasedCount
    def set_releasedCount(self, releasedCount):
        self.releasedCount = releasedCount
    def get_unreleasedCount(self):
        return self.unreleasedCount
    def set_unreleasedCount(self, unreleasedCount):
        self.unreleasedCount = unreleasedCount
    def get_companyName(self):
        return self.companyName
    def set_companyName(self, companyName):
        self.companyName = companyName
    def get_streetAddress1(self):
        return self.streetAddress1
    def set_streetAddress1(self, streetAddress1):
        self.streetAddress1 = streetAddress1
    def get_streetAddress2(self):
        return self.streetAddress2
    def set_streetAddress2(self, streetAddress2):
        self.streetAddress2 = streetAddress2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_zip(self):
        return self.zip
    def set_zip(self, zip):
        self.zip = zip
    def get_zip4(self):
        return self.zip4
    def set_zip4(self, zip4):
        self.zip4 = zip4
    def get_filingDate(self):
        return self.filingDate
    def set_filingDate(self, filingDate):
        self.filingDate = filingDate
    def validate_lienTypeType(self, value):
        result = True
        # Validate type lienTypeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on lienTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on lienTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_companyNameType26(self, value):
        result = True
        # Validate type companyNameType26, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 120:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on companyNameType26' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on companyNameType26' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_streetAddress1Type27(self, value):
        result = True
        # Validate type streetAddress1Type27, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on streetAddress1Type27' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on streetAddress1Type27' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_streetAddress2Type28(self, value):
        result = True
        # Validate type streetAddress2Type28, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on streetAddress2Type28' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on streetAddress2Type28' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_cityType29(self, value):
        result = True
        # Validate type cityType29, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType29' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on cityType29' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_stateType30(self, value):
        result = True
        # Validate type stateType30, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on stateType30' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on stateType30' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_zipType31(self, value):
        result = True
        # Validate type zipType31, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on zipType31' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on zipType31' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_zip4Type32(self, value):
        result = True
        # Validate type zip4Type32, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on zip4Type32' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on zip4Type32' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.lienType is not None or
            self.releasedCount is not None or
            self.unreleasedCount is not None or
            self.companyName is not None or
            self.streetAddress1 is not None or
            self.streetAddress2 is not None or
            self.city is not None or
            self.state is not None or
            self.zip is not None or
            self.zip4 is not None or
            self.filingDate is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='lienResult', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('lienResult')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'lienResult':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='lienResult')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='lienResult', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='lienResult'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='lienResult', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lienType is not None:
            namespaceprefix_ = self.lienType_nsprefix_ + ':' if (UseCapturedNS_ and self.lienType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slienType>%s</%slienType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lienType), input_name='lienType')), namespaceprefix_ , eol_))
        if self.releasedCount is not None:
            namespaceprefix_ = self.releasedCount_nsprefix_ + ':' if (UseCapturedNS_ and self.releasedCount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreleasedCount>%s</%sreleasedCount>%s' % (namespaceprefix_ , self.gds_format_integer(self.releasedCount, input_name='releasedCount'), namespaceprefix_ , eol_))
        if self.unreleasedCount is not None:
            namespaceprefix_ = self.unreleasedCount_nsprefix_ + ':' if (UseCapturedNS_ and self.unreleasedCount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunreleasedCount>%s</%sunreleasedCount>%s' % (namespaceprefix_ , self.gds_format_integer(self.unreleasedCount, input_name='unreleasedCount'), namespaceprefix_ , eol_))
        if self.companyName is not None:
            namespaceprefix_ = self.companyName_nsprefix_ + ':' if (UseCapturedNS_ and self.companyName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompanyName>%s</%scompanyName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.companyName), input_name='companyName')), namespaceprefix_ , eol_))
        if self.streetAddress1 is not None:
            namespaceprefix_ = self.streetAddress1_nsprefix_ + ':' if (UseCapturedNS_ and self.streetAddress1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress1>%s</%sstreetAddress1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.streetAddress1), input_name='streetAddress1')), namespaceprefix_ , eol_))
        if self.streetAddress2 is not None:
            namespaceprefix_ = self.streetAddress2_nsprefix_ + ':' if (UseCapturedNS_ and self.streetAddress2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress2>%s</%sstreetAddress2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.streetAddress2), input_name='streetAddress2')), namespaceprefix_ , eol_))
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.state is not None:
            namespaceprefix_ = self.state_nsprefix_ + ':' if (UseCapturedNS_ and self.state_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstate>%s</%sstate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.state), input_name='state')), namespaceprefix_ , eol_))
        if self.zip is not None:
            namespaceprefix_ = self.zip_nsprefix_ + ':' if (UseCapturedNS_ and self.zip_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szip>%s</%szip>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zip), input_name='zip')), namespaceprefix_ , eol_))
        if self.zip4 is not None:
            namespaceprefix_ = self.zip4_nsprefix_ + ':' if (UseCapturedNS_ and self.zip4_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%szip4>%s</%szip4>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.zip4), input_name='zip4')), namespaceprefix_ , eol_))
        if self.filingDate is not None:
            namespaceprefix_ = self.filingDate_nsprefix_ + ':' if (UseCapturedNS_ and self.filingDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfilingDate>%s</%sfilingDate>%s' % (namespaceprefix_ , self.gds_format_date(self.filingDate, input_name='filingDate'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'lienType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lienType')
            value_ = self.gds_validate_string(value_, node, 'lienType')
            self.lienType = value_
            self.lienType_nsprefix_ = child_.prefix
            # validate type lienTypeType
            self.validate_lienTypeType(self.lienType)
        elif nodeName_ == 'releasedCount' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'releasedCount')
            ival_ = self.gds_validate_integer(ival_, node, 'releasedCount')
            self.releasedCount = ival_
            self.releasedCount_nsprefix_ = child_.prefix
        elif nodeName_ == 'unreleasedCount' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'unreleasedCount')
            ival_ = self.gds_validate_integer(ival_, node, 'unreleasedCount')
            self.unreleasedCount = ival_
            self.unreleasedCount_nsprefix_ = child_.prefix
        elif nodeName_ == 'companyName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'companyName')
            value_ = self.gds_validate_string(value_, node, 'companyName')
            self.companyName = value_
            self.companyName_nsprefix_ = child_.prefix
            # validate type companyNameType26
            self.validate_companyNameType26(self.companyName)
        elif nodeName_ == 'streetAddress1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress1')
            value_ = self.gds_validate_string(value_, node, 'streetAddress1')
            self.streetAddress1 = value_
            self.streetAddress1_nsprefix_ = child_.prefix
            # validate type streetAddress1Type27
            self.validate_streetAddress1Type27(self.streetAddress1)
        elif nodeName_ == 'streetAddress2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress2')
            value_ = self.gds_validate_string(value_, node, 'streetAddress2')
            self.streetAddress2 = value_
            self.streetAddress2_nsprefix_ = child_.prefix
            # validate type streetAddress2Type28
            self.validate_streetAddress2Type28(self.streetAddress2)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType29
            self.validate_cityType29(self.city)
        elif nodeName_ == 'state':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'state')
            value_ = self.gds_validate_string(value_, node, 'state')
            self.state = value_
            self.state_nsprefix_ = child_.prefix
            # validate type stateType30
            self.validate_stateType30(self.state)
        elif nodeName_ == 'zip':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zip')
            value_ = self.gds_validate_string(value_, node, 'zip')
            self.zip = value_
            self.zip_nsprefix_ = child_.prefix
            # validate type zipType31
            self.validate_zipType31(self.zip)
        elif nodeName_ == 'zip4':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'zip4')
            value_ = self.gds_validate_string(value_, node, 'zip4')
            self.zip4 = value_
            self.zip4_nsprefix_ = child_.prefix
            # validate type zip4Type32
            self.validate_zip4Type32(self.zip4)
        elif nodeName_ == 'filingDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.filingDate = dval_
            self.filingDate_nsprefix_ = child_.prefix
# end class lienResult


class legalEntityUpdateRequest(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, address=None, contactPhone=None, doingBusinessAs=None, annualCreditCardSalesVolume=None, hasAcceptedCreditCards=None, principal=None, backgroundCheckFields=None, legalEntityOwnershipType=None, yearsInBusiness=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.address = address
        self.address_nsprefix_ = None
        self.contactPhone = contactPhone
        self.validate_contactPhoneType33(self.contactPhone)
        self.contactPhone_nsprefix_ = None
        self.doingBusinessAs = doingBusinessAs
        self.validate_doingBusinessAsType34(self.doingBusinessAs)
        self.doingBusinessAs_nsprefix_ = None
        self.annualCreditCardSalesVolume = annualCreditCardSalesVolume
        self.annualCreditCardSalesVolume_nsprefix_ = None
        self.hasAcceptedCreditCards = hasAcceptedCreditCards
        self.hasAcceptedCreditCards_nsprefix_ = None
        self.principal = principal
        self.principal_nsprefix_ = None
        self.backgroundCheckFields = backgroundCheckFields
        self.backgroundCheckFields_nsprefix_ = None
        self.legalEntityOwnershipType = legalEntityOwnershipType
        self.validate_legalEntityOwnershipType(self.legalEntityOwnershipType)
        self.legalEntityOwnershipType_nsprefix_ = None
        self.yearsInBusiness = yearsInBusiness
        self.validate_yearsInBusinessType35(self.yearsInBusiness)
        self.yearsInBusiness_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityUpdateRequest)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityUpdateRequest.subclass:
            return legalEntityUpdateRequest.subclass(*args_, **kwargs_)
        else:
            return legalEntityUpdateRequest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_contactPhone(self):
        return self.contactPhone
    def set_contactPhone(self, contactPhone):
        self.contactPhone = contactPhone
    def get_doingBusinessAs(self):
        return self.doingBusinessAs
    def set_doingBusinessAs(self, doingBusinessAs):
        self.doingBusinessAs = doingBusinessAs
    def get_annualCreditCardSalesVolume(self):
        return self.annualCreditCardSalesVolume
    def set_annualCreditCardSalesVolume(self, annualCreditCardSalesVolume):
        self.annualCreditCardSalesVolume = annualCreditCardSalesVolume
    def get_hasAcceptedCreditCards(self):
        return self.hasAcceptedCreditCards
    def set_hasAcceptedCreditCards(self, hasAcceptedCreditCards):
        self.hasAcceptedCreditCards = hasAcceptedCreditCards
    def get_principal(self):
        return self.principal
    def set_principal(self, principal):
        self.principal = principal
    def get_backgroundCheckFields(self):
        return self.backgroundCheckFields
    def set_backgroundCheckFields(self, backgroundCheckFields):
        self.backgroundCheckFields = backgroundCheckFields
    def get_legalEntityOwnershipType(self):
        return self.legalEntityOwnershipType
    def set_legalEntityOwnershipType(self, legalEntityOwnershipType):
        self.legalEntityOwnershipType = legalEntityOwnershipType
    def get_yearsInBusiness(self):
        return self.yearsInBusiness
    def set_yearsInBusiness(self, yearsInBusiness):
        self.yearsInBusiness = yearsInBusiness
    def validate_contactPhoneType33(self, value):
        result = True
        # Validate type contactPhoneType33, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on contactPhoneType33' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on contactPhoneType33' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_doingBusinessAsType34(self, value):
        result = True
        # Validate type doingBusinessAsType34, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on doingBusinessAsType34' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on doingBusinessAsType34' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_legalEntityOwnershipType(self, value):
        result = True
        # Validate type legalEntityOwnershipType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['PUBLIC', 'PRIVATE']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on legalEntityOwnershipType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_yearsInBusinessType35(self, value):
        result = True
        # Validate type yearsInBusinessType35, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on yearsInBusinessType35' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on yearsInBusinessType35' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_yearsInBusinessType35_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_yearsInBusinessType35_patterns_, ))
                result = False
        return result
    validate_yearsInBusinessType35_patterns_ = [[u'^([0-9]{0,3})$']]
    def hasContent_(self):
        if (
            self.address is not None or
            self.contactPhone is not None or
            self.doingBusinessAs is not None or
            self.annualCreditCardSalesVolume is not None or
            self.hasAcceptedCreditCards is not None or
            self.principal is not None or
            self.backgroundCheckFields is not None or
            self.legalEntityOwnershipType is not None or
            self.yearsInBusiness is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityUpdateRequest', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityUpdateRequest')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityUpdateRequest':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityUpdateRequest')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityUpdateRequest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityUpdateRequest'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityUpdateRequest', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.address is not None:
            namespaceprefix_ = self.address_nsprefix_ + ':' if (UseCapturedNS_ and self.address_nsprefix_) else ''
            self.address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address', pretty_print=pretty_print)
        if self.contactPhone is not None:
            namespaceprefix_ = self.contactPhone_nsprefix_ + ':' if (UseCapturedNS_ and self.contactPhone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontactPhone>%s</%scontactPhone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contactPhone), input_name='contactPhone')), namespaceprefix_ , eol_))
        if self.doingBusinessAs is not None:
            namespaceprefix_ = self.doingBusinessAs_nsprefix_ + ':' if (UseCapturedNS_ and self.doingBusinessAs_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdoingBusinessAs>%s</%sdoingBusinessAs>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.doingBusinessAs), input_name='doingBusinessAs')), namespaceprefix_ , eol_))
        if self.annualCreditCardSalesVolume is not None:
            namespaceprefix_ = self.annualCreditCardSalesVolume_nsprefix_ + ':' if (UseCapturedNS_ and self.annualCreditCardSalesVolume_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sannualCreditCardSalesVolume>%s</%sannualCreditCardSalesVolume>%s' % (namespaceprefix_ , self.gds_format_integer(self.annualCreditCardSalesVolume, input_name='annualCreditCardSalesVolume'), namespaceprefix_ , eol_))
        if self.hasAcceptedCreditCards is not None:
            namespaceprefix_ = self.hasAcceptedCreditCards_nsprefix_ + ':' if (UseCapturedNS_ and self.hasAcceptedCreditCards_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shasAcceptedCreditCards>%s</%shasAcceptedCreditCards>%s' % (namespaceprefix_ , self.gds_format_boolean(self.hasAcceptedCreditCards, input_name='hasAcceptedCreditCards'), namespaceprefix_ , eol_))
        if self.principal is not None:
            namespaceprefix_ = self.principal_nsprefix_ + ':' if (UseCapturedNS_ and self.principal_nsprefix_) else ''
            self.principal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='principal', pretty_print=pretty_print)
        if self.backgroundCheckFields is not None:
            namespaceprefix_ = self.backgroundCheckFields_nsprefix_ + ':' if (UseCapturedNS_ and self.backgroundCheckFields_nsprefix_) else ''
            self.backgroundCheckFields.export(outfile, level, namespaceprefix_, namespacedef_='', name_='backgroundCheckFields', pretty_print=pretty_print)
        if self.legalEntityOwnershipType is not None:
            namespaceprefix_ = self.legalEntityOwnershipType_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityOwnershipType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityOwnershipType>%s</%slegalEntityOwnershipType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityOwnershipType), input_name='legalEntityOwnershipType')), namespaceprefix_ , eol_))
        if self.yearsInBusiness is not None:
            namespaceprefix_ = self.yearsInBusiness_nsprefix_ + ':' if (UseCapturedNS_ and self.yearsInBusiness_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%syearsInBusiness>%s</%syearsInBusiness>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.yearsInBusiness), input_name='yearsInBusiness')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'address':
            obj_ = addressUpdatable.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'contactPhone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactPhone')
            value_ = self.gds_validate_string(value_, node, 'contactPhone')
            self.contactPhone = value_
            self.contactPhone_nsprefix_ = child_.prefix
            # validate type contactPhoneType33
            self.validate_contactPhoneType33(self.contactPhone)
        elif nodeName_ == 'doingBusinessAs':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'doingBusinessAs')
            value_ = self.gds_validate_string(value_, node, 'doingBusinessAs')
            self.doingBusinessAs = value_
            self.doingBusinessAs_nsprefix_ = child_.prefix
            # validate type doingBusinessAsType34
            self.validate_doingBusinessAsType34(self.doingBusinessAs)
        elif nodeName_ == 'annualCreditCardSalesVolume' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'annualCreditCardSalesVolume')
            ival_ = self.gds_validate_integer(ival_, node, 'annualCreditCardSalesVolume')
            self.annualCreditCardSalesVolume = ival_
            self.annualCreditCardSalesVolume_nsprefix_ = child_.prefix
        elif nodeName_ == 'hasAcceptedCreditCards':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'hasAcceptedCreditCards')
            ival_ = self.gds_validate_boolean(ival_, node, 'hasAcceptedCreditCards')
            self.hasAcceptedCreditCards = ival_
            self.hasAcceptedCreditCards_nsprefix_ = child_.prefix
        elif nodeName_ == 'principal':
            obj_ = legalEntityPrincipalUpdatable.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.principal = obj_
            obj_.original_tagname_ = 'principal'
        elif nodeName_ == 'backgroundCheckFields':
            obj_ = legalEntityBackgroundCheckFields.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.backgroundCheckFields = obj_
            obj_.original_tagname_ = 'backgroundCheckFields'
        elif nodeName_ == 'legalEntityOwnershipType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityOwnershipType')
            value_ = self.gds_validate_string(value_, node, 'legalEntityOwnershipType')
            self.legalEntityOwnershipType = value_
            self.legalEntityOwnershipType_nsprefix_ = child_.prefix
            # validate type legalEntityOwnershipType
            self.validate_legalEntityOwnershipType(self.legalEntityOwnershipType)
        elif nodeName_ == 'yearsInBusiness':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'yearsInBusiness')
            value_ = self.gds_validate_string(value_, node, 'yearsInBusiness')
            self.yearsInBusiness = value_
            self.yearsInBusiness_nsprefix_ = child_.prefix
            # validate type yearsInBusinessType35
            self.validate_yearsInBusinessType35(self.yearsInBusiness)
# end class legalEntityUpdateRequest


class addressUpdatable(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, streetAddress1=None, streetAddress2=None, city=None, stateProvince=None, postalCode=None, countryCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.streetAddress1 = streetAddress1
        self.validate_streetAddress1Type36(self.streetAddress1)
        self.streetAddress1_nsprefix_ = None
        self.streetAddress2 = streetAddress2
        self.validate_streetAddress2Type37(self.streetAddress2)
        self.streetAddress2_nsprefix_ = None
        self.city = city
        self.validate_cityType38(self.city)
        self.city_nsprefix_ = None
        self.stateProvince = stateProvince
        self.validate_stateProvinceType39(self.stateProvince)
        self.stateProvince_nsprefix_ = None
        self.postalCode = postalCode
        self.validate_postalCodeType40(self.postalCode)
        self.postalCode_nsprefix_ = None
        self.countryCode = countryCode
        self.validate_countryCodeType41(self.countryCode)
        self.countryCode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, addressUpdatable)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if addressUpdatable.subclass:
            return addressUpdatable.subclass(*args_, **kwargs_)
        else:
            return addressUpdatable(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_streetAddress1(self):
        return self.streetAddress1
    def set_streetAddress1(self, streetAddress1):
        self.streetAddress1 = streetAddress1
    def get_streetAddress2(self):
        return self.streetAddress2
    def set_streetAddress2(self, streetAddress2):
        self.streetAddress2 = streetAddress2
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_stateProvince(self):
        return self.stateProvince
    def set_stateProvince(self, stateProvince):
        self.stateProvince = stateProvince
    def get_postalCode(self):
        return self.postalCode
    def set_postalCode(self, postalCode):
        self.postalCode = postalCode
    def get_countryCode(self):
        return self.countryCode
    def set_countryCode(self, countryCode):
        self.countryCode = countryCode
    def validate_streetAddress1Type36(self, value):
        result = True
        # Validate type streetAddress1Type36, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on streetAddress1Type36' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on streetAddress1Type36' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_streetAddress2Type37(self, value):
        result = True
        # Validate type streetAddress2Type37, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on streetAddress2Type37' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on streetAddress2Type37' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_cityType38(self, value):
        result = True
        # Validate type cityType38, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType38' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on cityType38' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_stateProvinceType39(self, value):
        result = True
        # Validate type stateProvinceType39, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on stateProvinceType39' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on stateProvinceType39' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_postalCodeType40(self, value):
        result = True
        # Validate type postalCodeType40, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on postalCodeType40' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on postalCodeType40' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_countryCodeType41(self, value):
        result = True
        # Validate type countryCodeType41, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on countryCodeType41' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on countryCodeType41' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.streetAddress1 is not None or
            self.streetAddress2 is not None or
            self.city is not None or
            self.stateProvince is not None or
            self.postalCode is not None or
            self.countryCode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='addressUpdatable', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('addressUpdatable')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'addressUpdatable':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='addressUpdatable')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='addressUpdatable', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='addressUpdatable'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='addressUpdatable', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.streetAddress1 is not None:
            namespaceprefix_ = self.streetAddress1_nsprefix_ + ':' if (UseCapturedNS_ and self.streetAddress1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress1>%s</%sstreetAddress1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.streetAddress1), input_name='streetAddress1')), namespaceprefix_ , eol_))
        if self.streetAddress2 is not None:
            namespaceprefix_ = self.streetAddress2_nsprefix_ + ':' if (UseCapturedNS_ and self.streetAddress2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetAddress2>%s</%sstreetAddress2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.streetAddress2), input_name='streetAddress2')), namespaceprefix_ , eol_))
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.stateProvince is not None:
            namespaceprefix_ = self.stateProvince_nsprefix_ + ':' if (UseCapturedNS_ and self.stateProvince_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstateProvince>%s</%sstateProvince>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.stateProvince), input_name='stateProvince')), namespaceprefix_ , eol_))
        if self.postalCode is not None:
            namespaceprefix_ = self.postalCode_nsprefix_ + ':' if (UseCapturedNS_ and self.postalCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostalCode>%s</%spostalCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postalCode), input_name='postalCode')), namespaceprefix_ , eol_))
        if self.countryCode is not None:
            namespaceprefix_ = self.countryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.countryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountryCode>%s</%scountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.countryCode), input_name='countryCode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'streetAddress1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress1')
            value_ = self.gds_validate_string(value_, node, 'streetAddress1')
            self.streetAddress1 = value_
            self.streetAddress1_nsprefix_ = child_.prefix
            # validate type streetAddress1Type36
            self.validate_streetAddress1Type36(self.streetAddress1)
        elif nodeName_ == 'streetAddress2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetAddress2')
            value_ = self.gds_validate_string(value_, node, 'streetAddress2')
            self.streetAddress2 = value_
            self.streetAddress2_nsprefix_ = child_.prefix
            # validate type streetAddress2Type37
            self.validate_streetAddress2Type37(self.streetAddress2)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType38
            self.validate_cityType38(self.city)
        elif nodeName_ == 'stateProvince':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'stateProvince')
            value_ = self.gds_validate_string(value_, node, 'stateProvince')
            self.stateProvince = value_
            self.stateProvince_nsprefix_ = child_.prefix
            # validate type stateProvinceType39
            self.validate_stateProvinceType39(self.stateProvince)
        elif nodeName_ == 'postalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postalCode')
            value_ = self.gds_validate_string(value_, node, 'postalCode')
            self.postalCode = value_
            self.postalCode_nsprefix_ = child_.prefix
            # validate type postalCodeType40
            self.validate_postalCodeType40(self.postalCode)
        elif nodeName_ == 'countryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'countryCode')
            value_ = self.gds_validate_string(value_, node, 'countryCode')
            self.countryCode = value_
            self.countryCode_nsprefix_ = child_.prefix
            # validate type countryCodeType41
            self.validate_countryCodeType41(self.countryCode)
# end class addressUpdatable


class legalEntityPrincipalUpdatable(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, principalId=None, title=None, emailAddress=None, contactPhone=None, address=None, stakePercent=None, backgroundCheckFields=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.principalId = principalId
        self.principalId_nsprefix_ = None
        self.title = title
        self.validate_titleType42(self.title)
        self.title_nsprefix_ = None
        self.emailAddress = emailAddress
        self.validate_emailAddressType43(self.emailAddress)
        self.emailAddress_nsprefix_ = None
        self.contactPhone = contactPhone
        self.validate_contactPhoneType44(self.contactPhone)
        self.contactPhone_nsprefix_ = None
        self.address = address
        self.address_nsprefix_ = None
        self.stakePercent = stakePercent
        self.validate_stakePercentType45(self.stakePercent)
        self.stakePercent_nsprefix_ = None
        self.backgroundCheckFields = backgroundCheckFields
        self.backgroundCheckFields_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityPrincipalUpdatable)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityPrincipalUpdatable.subclass:
            return legalEntityPrincipalUpdatable.subclass(*args_, **kwargs_)
        else:
            return legalEntityPrincipalUpdatable(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_principalId(self):
        return self.principalId
    def set_principalId(self, principalId):
        self.principalId = principalId
    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title
    def get_emailAddress(self):
        return self.emailAddress
    def set_emailAddress(self, emailAddress):
        self.emailAddress = emailAddress
    def get_contactPhone(self):
        return self.contactPhone
    def set_contactPhone(self, contactPhone):
        self.contactPhone = contactPhone
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_stakePercent(self):
        return self.stakePercent
    def set_stakePercent(self, stakePercent):
        self.stakePercent = stakePercent
    def get_backgroundCheckFields(self):
        return self.backgroundCheckFields
    def set_backgroundCheckFields(self, backgroundCheckFields):
        self.backgroundCheckFields = backgroundCheckFields
    def validate_titleType42(self, value):
        result = True
        # Validate type titleType42, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on titleType42' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on titleType42' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_emailAddressType43(self, value):
        result = True
        # Validate type emailAddressType43, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on emailAddressType43' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on emailAddressType43' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_contactPhoneType44(self, value):
        result = True
        # Validate type contactPhoneType44, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 13:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on contactPhoneType44' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on contactPhoneType44' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_stakePercentType45(self, value):
        result = True
        # Validate type stakePercentType45, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on stakePercentType45' % {"value": value, "lineno": lineno} )
                result = False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on stakePercentType45' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.principalId is not None or
            self.title is not None or
            self.emailAddress is not None or
            self.contactPhone is not None or
            self.address is not None or
            self.stakePercent is not None or
            self.backgroundCheckFields is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipalUpdatable', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityPrincipalUpdatable')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityPrincipalUpdatable':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityPrincipalUpdatable')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityPrincipalUpdatable', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityPrincipalUpdatable'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipalUpdatable', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.principalId is not None:
            namespaceprefix_ = self.principalId_nsprefix_ + ':' if (UseCapturedNS_ and self.principalId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprincipalId>%s</%sprincipalId>%s' % (namespaceprefix_ , self.gds_format_integer(self.principalId, input_name='principalId'), namespaceprefix_ , eol_))
        if self.title is not None:
            namespaceprefix_ = self.title_nsprefix_ + ':' if (UseCapturedNS_ and self.title_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stitle>%s</%stitle>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.title), input_name='title')), namespaceprefix_ , eol_))
        if self.emailAddress is not None:
            namespaceprefix_ = self.emailAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.emailAddress_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%semailAddress>%s</%semailAddress>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.emailAddress), input_name='emailAddress')), namespaceprefix_ , eol_))
        if self.contactPhone is not None:
            namespaceprefix_ = self.contactPhone_nsprefix_ + ':' if (UseCapturedNS_ and self.contactPhone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontactPhone>%s</%scontactPhone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contactPhone), input_name='contactPhone')), namespaceprefix_ , eol_))
        if self.address is not None:
            namespaceprefix_ = self.address_nsprefix_ + ':' if (UseCapturedNS_ and self.address_nsprefix_) else ''
            self.address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address', pretty_print=pretty_print)
        if self.stakePercent is not None:
            namespaceprefix_ = self.stakePercent_nsprefix_ + ':' if (UseCapturedNS_ and self.stakePercent_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstakePercent>%s</%sstakePercent>%s' % (namespaceprefix_ , self.gds_format_integer(self.stakePercent, input_name='stakePercent'), namespaceprefix_ , eol_))
        if self.backgroundCheckFields is not None:
            namespaceprefix_ = self.backgroundCheckFields_nsprefix_ + ':' if (UseCapturedNS_ and self.backgroundCheckFields_nsprefix_) else ''
            self.backgroundCheckFields.export(outfile, level, namespaceprefix_, namespacedef_='', name_='backgroundCheckFields', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'principalId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'principalId')
            ival_ = self.gds_validate_integer(ival_, node, 'principalId')
            self.principalId = ival_
            self.principalId_nsprefix_ = child_.prefix
        elif nodeName_ == 'title':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'title')
            value_ = self.gds_validate_string(value_, node, 'title')
            self.title = value_
            self.title_nsprefix_ = child_.prefix
            # validate type titleType42
            self.validate_titleType42(self.title)
        elif nodeName_ == 'emailAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'emailAddress')
            value_ = self.gds_validate_string(value_, node, 'emailAddress')
            self.emailAddress = value_
            self.emailAddress_nsprefix_ = child_.prefix
            # validate type emailAddressType43
            self.validate_emailAddressType43(self.emailAddress)
        elif nodeName_ == 'contactPhone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactPhone')
            value_ = self.gds_validate_string(value_, node, 'contactPhone')
            self.contactPhone = value_
            self.contactPhone_nsprefix_ = child_.prefix
            # validate type contactPhoneType44
            self.validate_contactPhoneType44(self.contactPhone)
        elif nodeName_ == 'address':
            obj_ = principalAddress.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'stakePercent' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'stakePercent')
            ival_ = self.gds_validate_integer(ival_, node, 'stakePercent')
            self.stakePercent = ival_
            self.stakePercent_nsprefix_ = child_.prefix
            # validate type stakePercentType45
            self.validate_stakePercentType45(self.stakePercent)
        elif nodeName_ == 'backgroundCheckFields':
            obj_ = principalBackgroundCheckFields.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.backgroundCheckFields = obj_
            obj_.original_tagname_ = 'backgroundCheckFields'
# end class legalEntityPrincipalUpdatable


class principalBackgroundCheckFields(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, firstName=None, lastName=None, ssn=None, dateOfBirth=None, driversLicense=None, driversLicenseState=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.firstName = firstName
        self.validate_firstNameType46(self.firstName)
        self.firstName_nsprefix_ = None
        self.lastName = lastName
        self.validate_lastNameType47(self.lastName)
        self.lastName_nsprefix_ = None
        self.ssn = ssn
        self.validate_ssnType48(self.ssn)
        self.ssn_nsprefix_ = None
        if isinstance(dateOfBirth, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateOfBirth, '%Y-%m-%d').date()
        else:
            initvalue_ = dateOfBirth
        self.dateOfBirth = initvalue_
        self.dateOfBirth_nsprefix_ = None
        self.driversLicense = driversLicense
        self.validate_driversLicenseType49(self.driversLicense)
        self.driversLicense_nsprefix_ = None
        self.driversLicenseState = driversLicenseState
        self.validate_driversLicenseStateType50(self.driversLicenseState)
        self.driversLicenseState_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, principalBackgroundCheckFields)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if principalBackgroundCheckFields.subclass:
            return principalBackgroundCheckFields.subclass(*args_, **kwargs_)
        else:
            return principalBackgroundCheckFields(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_firstName(self):
        return self.firstName
    def set_firstName(self, firstName):
        self.firstName = firstName
    def get_lastName(self):
        return self.lastName
    def set_lastName(self, lastName):
        self.lastName = lastName
    def get_ssn(self):
        return self.ssn
    def set_ssn(self, ssn):
        self.ssn = ssn
    def get_dateOfBirth(self):
        return self.dateOfBirth
    def set_dateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth
    def get_driversLicense(self):
        return self.driversLicense
    def set_driversLicense(self, driversLicense):
        self.driversLicense = driversLicense
    def get_driversLicenseState(self):
        return self.driversLicenseState
    def set_driversLicenseState(self, driversLicenseState):
        self.driversLicenseState = driversLicenseState
    def validate_firstNameType46(self, value):
        result = True
        # Validate type firstNameType46, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on firstNameType46' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on firstNameType46' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_lastNameType47(self, value):
        result = True
        # Validate type lastNameType47, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on lastNameType47' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on lastNameType47' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ssnType48(self, value):
        result = True
        # Validate type ssnType48, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 25:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ssnType48' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 9:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ssnType48' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_driversLicenseType49(self, value):
        result = True
        # Validate type driversLicenseType49, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 25:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on driversLicenseType49' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on driversLicenseType49' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_driversLicenseStateType50(self, value):
        result = True
        # Validate type driversLicenseStateType50, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on driversLicenseStateType50' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on driversLicenseStateType50' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.firstName is not None or
            self.lastName is not None or
            self.ssn is not None or
            self.dateOfBirth is not None or
            self.driversLicense is not None or
            self.driversLicenseState is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalBackgroundCheckFields', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('principalBackgroundCheckFields')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'principalBackgroundCheckFields':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='principalBackgroundCheckFields')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='principalBackgroundCheckFields', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='principalBackgroundCheckFields'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalBackgroundCheckFields', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.firstName is not None:
            namespaceprefix_ = self.firstName_nsprefix_ + ':' if (UseCapturedNS_ and self.firstName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfirstName>%s</%sfirstName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.firstName), input_name='firstName')), namespaceprefix_ , eol_))
        if self.lastName is not None:
            namespaceprefix_ = self.lastName_nsprefix_ + ':' if (UseCapturedNS_ and self.lastName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slastName>%s</%slastName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lastName), input_name='lastName')), namespaceprefix_ , eol_))
        if self.ssn is not None:
            namespaceprefix_ = self.ssn_nsprefix_ + ':' if (UseCapturedNS_ and self.ssn_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sssn>%s</%sssn>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ssn), input_name='ssn')), namespaceprefix_ , eol_))
        if self.dateOfBirth is not None:
            namespaceprefix_ = self.dateOfBirth_nsprefix_ + ':' if (UseCapturedNS_ and self.dateOfBirth_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateOfBirth>%s</%sdateOfBirth>%s' % (namespaceprefix_ , self.gds_format_date(self.dateOfBirth, input_name='dateOfBirth'), namespaceprefix_ , eol_))
        if self.driversLicense is not None:
            namespaceprefix_ = self.driversLicense_nsprefix_ + ':' if (UseCapturedNS_ and self.driversLicense_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdriversLicense>%s</%sdriversLicense>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.driversLicense), input_name='driversLicense')), namespaceprefix_ , eol_))
        if self.driversLicenseState is not None:
            namespaceprefix_ = self.driversLicenseState_nsprefix_ + ':' if (UseCapturedNS_ and self.driversLicenseState_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdriversLicenseState>%s</%sdriversLicenseState>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.driversLicenseState), input_name='driversLicenseState')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'firstName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firstName')
            value_ = self.gds_validate_string(value_, node, 'firstName')
            self.firstName = value_
            self.firstName_nsprefix_ = child_.prefix
            # validate type firstNameType46
            self.validate_firstNameType46(self.firstName)
        elif nodeName_ == 'lastName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lastName')
            value_ = self.gds_validate_string(value_, node, 'lastName')
            self.lastName = value_
            self.lastName_nsprefix_ = child_.prefix
            # validate type lastNameType47
            self.validate_lastNameType47(self.lastName)
        elif nodeName_ == 'ssn':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ssn')
            value_ = self.gds_validate_string(value_, node, 'ssn')
            self.ssn = value_
            self.ssn_nsprefix_ = child_.prefix
            # validate type ssnType48
            self.validate_ssnType48(self.ssn)
        elif nodeName_ == 'dateOfBirth':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dateOfBirth = dval_
            self.dateOfBirth_nsprefix_ = child_.prefix
        elif nodeName_ == 'driversLicense':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'driversLicense')
            value_ = self.gds_validate_string(value_, node, 'driversLicense')
            self.driversLicense = value_
            self.driversLicense_nsprefix_ = child_.prefix
            # validate type driversLicenseType49
            self.validate_driversLicenseType49(self.driversLicense)
        elif nodeName_ == 'driversLicenseState':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'driversLicenseState')
            value_ = self.gds_validate_string(value_, node, 'driversLicenseState')
            self.driversLicenseState = value_
            self.driversLicenseState_nsprefix_ = child_.prefix
            # validate type driversLicenseStateType50
            self.validate_driversLicenseStateType50(self.driversLicenseState)
# end class principalBackgroundCheckFields


class legalEntityBackgroundCheckFields(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, legalEntityName=None, legalEntityType=None, taxId=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.legalEntityName = legalEntityName
        self.validate_legalEntityNameType51(self.legalEntityName)
        self.legalEntityName_nsprefix_ = None
        self.legalEntityType = legalEntityType
        self.validate_legalEntityType(self.legalEntityType)
        self.legalEntityType_nsprefix_ = None
        self.taxId = taxId
        self.validate_taxIdType52(self.taxId)
        self.taxId_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityBackgroundCheckFields)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityBackgroundCheckFields.subclass:
            return legalEntityBackgroundCheckFields.subclass(*args_, **kwargs_)
        else:
            return legalEntityBackgroundCheckFields(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_legalEntityName(self):
        return self.legalEntityName
    def set_legalEntityName(self, legalEntityName):
        self.legalEntityName = legalEntityName
    def get_legalEntityType(self):
        return self.legalEntityType
    def set_legalEntityType(self, legalEntityType):
        self.legalEntityType = legalEntityType
    def get_taxId(self):
        return self.taxId
    def set_taxId(self, taxId):
        self.taxId = taxId
    def validate_legalEntityNameType51(self, value):
        result = True
        # Validate type legalEntityNameType51, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on legalEntityNameType51' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on legalEntityNameType51' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_legalEntityNameType51_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_legalEntityNameType51_patterns_, ))
                result = False
        return result
    validate_legalEntityNameType51_patterns_ = [[u'^([\x00-\x7f]*)$']]
    def validate_legalEntityType(self, value):
        result = True
        # Validate type legalEntityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['INDIVIDUAL_SOLE_PROPRIETORSHIP', 'CORPORATION', 'LIMITED_LIABILITY_COMPANY', 'PARTNERSHIP', 'LIMITED_PARTNERSHIP', 'GENERAL_PARTNERSHIP', 'TAX_EXEMPT_ORGANIZATION', 'GOVERNMENT_AGENCY']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on legalEntityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_taxIdType52(self, value):
        result = True
        # Validate type taxIdType52, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 25:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on taxIdType52' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 9:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on taxIdType52' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.legalEntityName is not None or
            self.legalEntityType is not None or
            self.taxId is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityBackgroundCheckFields', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityBackgroundCheckFields')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityBackgroundCheckFields':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityBackgroundCheckFields')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityBackgroundCheckFields', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityBackgroundCheckFields'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityBackgroundCheckFields', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.legalEntityName is not None:
            namespaceprefix_ = self.legalEntityName_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityName>%s</%slegalEntityName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityName), input_name='legalEntityName')), namespaceprefix_ , eol_))
        if self.legalEntityType is not None:
            namespaceprefix_ = self.legalEntityType_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityType>%s</%slegalEntityType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityType), input_name='legalEntityType')), namespaceprefix_ , eol_))
        if self.taxId is not None:
            namespaceprefix_ = self.taxId_nsprefix_ + ':' if (UseCapturedNS_ and self.taxId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxId>%s</%staxId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxId), input_name='taxId')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityName')
            value_ = self.gds_validate_string(value_, node, 'legalEntityName')
            self.legalEntityName = value_
            self.legalEntityName_nsprefix_ = child_.prefix
            # validate type legalEntityNameType51
            self.validate_legalEntityNameType51(self.legalEntityName)
        elif nodeName_ == 'legalEntityType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityType')
            value_ = self.gds_validate_string(value_, node, 'legalEntityType')
            self.legalEntityType = value_
            self.legalEntityType_nsprefix_ = child_.prefix
            # validate type legalEntityType
            self.validate_legalEntityType(self.legalEntityType)
        elif nodeName_ == 'taxId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxId')
            value_ = self.gds_validate_string(value_, node, 'taxId')
            self.taxId = value_
            self.taxId_nsprefix_ = child_.prefix
            # validate type taxIdType52
            self.validate_taxIdType52(self.taxId)
# end class legalEntityBackgroundCheckFields


class subMerchantCreateRequest(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, merchantName=None, amexMid=None, discoverConveyedMid=None, url=None, customerServiceNumber=None, hardCodedBillingDescriptor=None, maxTransactionAmount=None, purchaseCurrency=None, merchantCategoryCode=None, taxAuthority=None, taxAuthorityState=None, bankRoutingNumber=None, bankAccountNumber=None, pspMerchantId=None, fraud=None, amexAcquired=None, address=None, primaryContact=None, createCredentials=None, eCheck=None, subMerchantFunding=None, settlementCurrency=None, sdkVersion=None, language=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.merchantName = merchantName
        self.validate_merchantNameType(self.merchantName)
        self.merchantName_nsprefix_ = None
        self.amexMid = amexMid
        self.validate_amexMidType(self.amexMid)
        self.amexMid_nsprefix_ = None
        self.discoverConveyedMid = discoverConveyedMid
        self.validate_discoverConveyedMidType(self.discoverConveyedMid)
        self.discoverConveyedMid_nsprefix_ = None
        self.url = url
        self.validate_urlType(self.url)
        self.url_nsprefix_ = None
        self.customerServiceNumber = customerServiceNumber
        self.validate_customerServiceNumberType(self.customerServiceNumber)
        self.customerServiceNumber_nsprefix_ = None
        self.hardCodedBillingDescriptor = hardCodedBillingDescriptor
        self.validate_hardCodedBillingDescriptorType(self.hardCodedBillingDescriptor)
        self.hardCodedBillingDescriptor_nsprefix_ = None
        self.maxTransactionAmount = maxTransactionAmount
        self.validate_maxTransactionAmountType(self.maxTransactionAmount)
        self.maxTransactionAmount_nsprefix_ = None
        self.purchaseCurrency = purchaseCurrency
        self.validate_purchaseCurrencyType(self.purchaseCurrency)
        self.purchaseCurrency_nsprefix_ = None
        self.merchantCategoryCode = merchantCategoryCode
        self.validate_merchantCategoryCodeType(self.merchantCategoryCode)
        self.merchantCategoryCode_nsprefix_ = None
        self.taxAuthority = taxAuthority
        self.taxAuthority_nsprefix_ = None
        self.taxAuthorityState = taxAuthorityState
        self.taxAuthorityState_nsprefix_ = None
        self.bankRoutingNumber = bankRoutingNumber
        self.validate_bankRoutingNumberType(self.bankRoutingNumber)
        self.bankRoutingNumber_nsprefix_ = None
        self.bankAccountNumber = bankAccountNumber
        self.validate_bankAccountNumberType(self.bankAccountNumber)
        self.bankAccountNumber_nsprefix_ = None
        self.pspMerchantId = pspMerchantId
        self.validate_pspMerchantIdType(self.pspMerchantId)
        self.pspMerchantId_nsprefix_ = None
        self.fraud = fraud
        self.fraud_nsprefix_ = None
        self.amexAcquired = amexAcquired
        self.amexAcquired_nsprefix_ = None
        self.address = address
        self.address_nsprefix_ = None
        self.primaryContact = primaryContact
        self.primaryContact_nsprefix_ = None
        self.createCredentials = createCredentials
        self.createCredentials_nsprefix_ = None
        self.eCheck = eCheck
        self.eCheck_nsprefix_ = None
        self.subMerchantFunding = subMerchantFunding
        self.subMerchantFunding_nsprefix_ = None
        self.settlementCurrency = settlementCurrency
        self.validate_settlementCurrencyType(self.settlementCurrency)
        self.settlementCurrency_nsprefix_ = None
        self.sdkVersion = sdkVersion
        self.validate_sdkVersionType53(self.sdkVersion)
        self.sdkVersion_nsprefix_ = None
        self.language = language
        self.validate_languageType54(self.language)
        self.language_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantCreateRequest)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantCreateRequest.subclass:
            return subMerchantCreateRequest.subclass(*args_, **kwargs_)
        else:
            return subMerchantCreateRequest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_merchantName(self):
        return self.merchantName
    def set_merchantName(self, merchantName):
        self.merchantName = merchantName
    def get_amexMid(self):
        return self.amexMid
    def set_amexMid(self, amexMid):
        self.amexMid = amexMid
    def get_discoverConveyedMid(self):
        return self.discoverConveyedMid
    def set_discoverConveyedMid(self, discoverConveyedMid):
        self.discoverConveyedMid = discoverConveyedMid
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_customerServiceNumber(self):
        return self.customerServiceNumber
    def set_customerServiceNumber(self, customerServiceNumber):
        self.customerServiceNumber = customerServiceNumber
    def get_hardCodedBillingDescriptor(self):
        return self.hardCodedBillingDescriptor
    def set_hardCodedBillingDescriptor(self, hardCodedBillingDescriptor):
        self.hardCodedBillingDescriptor = hardCodedBillingDescriptor
    def get_maxTransactionAmount(self):
        return self.maxTransactionAmount
    def set_maxTransactionAmount(self, maxTransactionAmount):
        self.maxTransactionAmount = maxTransactionAmount
    def get_purchaseCurrency(self):
        return self.purchaseCurrency
    def set_purchaseCurrency(self, purchaseCurrency):
        self.purchaseCurrency = purchaseCurrency
    def get_merchantCategoryCode(self):
        return self.merchantCategoryCode
    def set_merchantCategoryCode(self, merchantCategoryCode):
        self.merchantCategoryCode = merchantCategoryCode
    def get_taxAuthority(self):
        return self.taxAuthority
    def set_taxAuthority(self, taxAuthority):
        self.taxAuthority = taxAuthority
    def get_taxAuthorityState(self):
        return self.taxAuthorityState
    def set_taxAuthorityState(self, taxAuthorityState):
        self.taxAuthorityState = taxAuthorityState
    def get_bankRoutingNumber(self):
        return self.bankRoutingNumber
    def set_bankRoutingNumber(self, bankRoutingNumber):
        self.bankRoutingNumber = bankRoutingNumber
    def get_bankAccountNumber(self):
        return self.bankAccountNumber
    def set_bankAccountNumber(self, bankAccountNumber):
        self.bankAccountNumber = bankAccountNumber
    def get_pspMerchantId(self):
        return self.pspMerchantId
    def set_pspMerchantId(self, pspMerchantId):
        self.pspMerchantId = pspMerchantId
    def get_fraud(self):
        return self.fraud
    def set_fraud(self, fraud):
        self.fraud = fraud
    def get_amexAcquired(self):
        return self.amexAcquired
    def set_amexAcquired(self, amexAcquired):
        self.amexAcquired = amexAcquired
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_primaryContact(self):
        return self.primaryContact
    def set_primaryContact(self, primaryContact):
        self.primaryContact = primaryContact
    def get_createCredentials(self):
        return self.createCredentials
    def set_createCredentials(self, createCredentials):
        self.createCredentials = createCredentials
    def get_eCheck(self):
        return self.eCheck
    def set_eCheck(self, eCheck):
        self.eCheck = eCheck
    def get_subMerchantFunding(self):
        return self.subMerchantFunding
    def set_subMerchantFunding(self, subMerchantFunding):
        self.subMerchantFunding = subMerchantFunding
    def get_settlementCurrency(self):
        return self.settlementCurrency
    def set_settlementCurrency(self, settlementCurrency):
        self.settlementCurrency = settlementCurrency
    def get_sdkVersion(self):
        return self.sdkVersion
    def set_sdkVersion(self, sdkVersion):
        self.sdkVersion = sdkVersion
    def get_language(self):
        return self.language
    def set_language(self, language):
        self.language = language
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_merchantNameType(self, value):
        result = True
        # Validate type merchantNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchantNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on merchantNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_amexMidType(self, value):
        result = True
        # Validate type amexMidType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on amexMidType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on amexMidType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_discoverConveyedMidType(self, value):
        result = True
        # Validate type discoverConveyedMidType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on discoverConveyedMidType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on discoverConveyedMidType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_urlType(self, value):
        result = True
        # Validate type urlType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 120:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on urlType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on urlType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_customerServiceNumberType(self, value):
        result = True
        # Validate type customerServiceNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 13:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on customerServiceNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on customerServiceNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_hardCodedBillingDescriptorType(self, value):
        result = True
        # Validate type hardCodedBillingDescriptorType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 25:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on hardCodedBillingDescriptorType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on hardCodedBillingDescriptorType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_maxTransactionAmountType(self, value):
        result = True
        # Validate type maxTransactionAmountType, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on maxTransactionAmountType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_purchaseCurrencyType(self, value):
        result = True
        # Validate type purchaseCurrencyType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on purchaseCurrencyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on purchaseCurrencyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_merchantCategoryCodeType(self, value):
        result = True
        # Validate type merchantCategoryCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchantCategoryCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on merchantCategoryCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_bankRoutingNumberType(self, value):
        result = True
        # Validate type bankRoutingNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on bankRoutingNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on bankRoutingNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_bankAccountNumberType(self, value):
        result = True
        # Validate type bankAccountNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on bankAccountNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on bankAccountNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_pspMerchantIdType(self, value):
        result = True
        # Validate type pspMerchantIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on pspMerchantIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on pspMerchantIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_settlementCurrencyType(self, value):
        result = True
        # Validate type settlementCurrencyType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on settlementCurrencyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on settlementCurrencyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_sdkVersionType53(self, value):
        result = True
        # Validate type sdkVersionType53, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on sdkVersionType53' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on sdkVersionType53' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_sdkVersionType53_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_sdkVersionType53_patterns_, ))
                result = False
        return result
    validate_sdkVersionType53_patterns_ = [[u'^([\x00-\x7f]*)$']]
    def validate_languageType54(self, value):
        result = True
        # Validate type languageType54, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on languageType54' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on languageType54' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_languageType54_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_languageType54_patterns_, ))
                result = False
        return result
    validate_languageType54_patterns_ = [[u'^([\x00-\x7f]*)$']]
    def hasContent_(self):
        if (
            self.merchantName is not None or
            self.amexMid is not None or
            self.discoverConveyedMid is not None or
            self.url is not None or
            self.customerServiceNumber is not None or
            self.hardCodedBillingDescriptor is not None or
            self.maxTransactionAmount is not None or
            self.purchaseCurrency is not None or
            self.merchantCategoryCode is not None or
            self.taxAuthority is not None or
            self.taxAuthorityState is not None or
            self.bankRoutingNumber is not None or
            self.bankAccountNumber is not None or
            self.pspMerchantId is not None or
            self.fraud is not None or
            self.amexAcquired is not None or
            self.address is not None or
            self.primaryContact is not None or
            self.createCredentials is not None or
            self.eCheck is not None or
            self.subMerchantFunding is not None or
            self.settlementCurrency is not None or
            self.sdkVersion is not None or
            self.language is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantCreateRequest', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantCreateRequest')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantCreateRequest':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantCreateRequest')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantCreateRequest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantCreateRequest'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantCreateRequest', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.merchantName is not None:
            namespaceprefix_ = self.merchantName_nsprefix_ + ':' if (UseCapturedNS_ and self.merchantName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchantName>%s</%smerchantName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchantName), input_name='merchantName')), namespaceprefix_ , eol_))
        if self.amexMid is not None:
            namespaceprefix_ = self.amexMid_nsprefix_ + ':' if (UseCapturedNS_ and self.amexMid_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%samexMid>%s</%samexMid>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.amexMid), input_name='amexMid')), namespaceprefix_ , eol_))
        if self.discoverConveyedMid is not None:
            namespaceprefix_ = self.discoverConveyedMid_nsprefix_ + ':' if (UseCapturedNS_ and self.discoverConveyedMid_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiscoverConveyedMid>%s</%sdiscoverConveyedMid>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.discoverConveyedMid), input_name='discoverConveyedMid')), namespaceprefix_ , eol_))
        if self.url is not None:
            namespaceprefix_ = self.url_nsprefix_ + ':' if (UseCapturedNS_ and self.url_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%surl>%s</%surl>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.url), input_name='url')), namespaceprefix_ , eol_))
        if self.customerServiceNumber is not None:
            namespaceprefix_ = self.customerServiceNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.customerServiceNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomerServiceNumber>%s</%scustomerServiceNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customerServiceNumber), input_name='customerServiceNumber')), namespaceprefix_ , eol_))
        if self.hardCodedBillingDescriptor is not None:
            namespaceprefix_ = self.hardCodedBillingDescriptor_nsprefix_ + ':' if (UseCapturedNS_ and self.hardCodedBillingDescriptor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shardCodedBillingDescriptor>%s</%shardCodedBillingDescriptor>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.hardCodedBillingDescriptor), input_name='hardCodedBillingDescriptor')), namespaceprefix_ , eol_))
        if self.maxTransactionAmount is not None:
            namespaceprefix_ = self.maxTransactionAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.maxTransactionAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smaxTransactionAmount>%s</%smaxTransactionAmount>%s' % (namespaceprefix_ , self.gds_format_integer(self.maxTransactionAmount, input_name='maxTransactionAmount'), namespaceprefix_ , eol_))
        if self.purchaseCurrency is not None:
            namespaceprefix_ = self.purchaseCurrency_nsprefix_ + ':' if (UseCapturedNS_ and self.purchaseCurrency_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spurchaseCurrency>%s</%spurchaseCurrency>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.purchaseCurrency), input_name='purchaseCurrency')), namespaceprefix_ , eol_))
        if self.merchantCategoryCode is not None:
            namespaceprefix_ = self.merchantCategoryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.merchantCategoryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchantCategoryCode>%s</%smerchantCategoryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchantCategoryCode), input_name='merchantCategoryCode')), namespaceprefix_ , eol_))
        if self.taxAuthority is not None:
            namespaceprefix_ = self.taxAuthority_nsprefix_ + ':' if (UseCapturedNS_ and self.taxAuthority_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxAuthority>%s</%staxAuthority>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxAuthority), input_name='taxAuthority')), namespaceprefix_ , eol_))
        if self.taxAuthorityState is not None:
            namespaceprefix_ = self.taxAuthorityState_nsprefix_ + ':' if (UseCapturedNS_ and self.taxAuthorityState_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxAuthorityState>%s</%staxAuthorityState>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxAuthorityState), input_name='taxAuthorityState')), namespaceprefix_ , eol_))
        if self.bankRoutingNumber is not None:
            namespaceprefix_ = self.bankRoutingNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.bankRoutingNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbankRoutingNumber>%s</%sbankRoutingNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.bankRoutingNumber), input_name='bankRoutingNumber')), namespaceprefix_ , eol_))
        if self.bankAccountNumber is not None:
            namespaceprefix_ = self.bankAccountNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.bankAccountNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbankAccountNumber>%s</%sbankAccountNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.bankAccountNumber), input_name='bankAccountNumber')), namespaceprefix_ , eol_))
        if self.pspMerchantId is not None:
            namespaceprefix_ = self.pspMerchantId_nsprefix_ + ':' if (UseCapturedNS_ and self.pspMerchantId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spspMerchantId>%s</%spspMerchantId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pspMerchantId), input_name='pspMerchantId')), namespaceprefix_ , eol_))
        if self.fraud is not None:
            namespaceprefix_ = self.fraud_nsprefix_ + ':' if (UseCapturedNS_ and self.fraud_nsprefix_) else ''
            self.fraud.export(outfile, level, namespaceprefix_, namespacedef_='', name_='fraud', pretty_print=pretty_print)
        if self.amexAcquired is not None:
            namespaceprefix_ = self.amexAcquired_nsprefix_ + ':' if (UseCapturedNS_ and self.amexAcquired_nsprefix_) else ''
            self.amexAcquired.export(outfile, level, namespaceprefix_, namespacedef_='', name_='amexAcquired', pretty_print=pretty_print)
        if self.address is not None:
            namespaceprefix_ = self.address_nsprefix_ + ':' if (UseCapturedNS_ and self.address_nsprefix_) else ''
            self.address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address', pretty_print=pretty_print)
        if self.primaryContact is not None:
            namespaceprefix_ = self.primaryContact_nsprefix_ + ':' if (UseCapturedNS_ and self.primaryContact_nsprefix_) else ''
            self.primaryContact.export(outfile, level, namespaceprefix_, namespacedef_='', name_='primaryContact', pretty_print=pretty_print)
        if self.createCredentials is not None:
            namespaceprefix_ = self.createCredentials_nsprefix_ + ':' if (UseCapturedNS_ and self.createCredentials_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%screateCredentials>%s</%screateCredentials>%s' % (namespaceprefix_ , self.gds_format_boolean(self.createCredentials, input_name='createCredentials'), namespaceprefix_ , eol_))
        if self.eCheck is not None:
            namespaceprefix_ = self.eCheck_nsprefix_ + ':' if (UseCapturedNS_ and self.eCheck_nsprefix_) else ''
            self.eCheck.export(outfile, level, namespaceprefix_, namespacedef_='', name_='eCheck', pretty_print=pretty_print)
        if self.subMerchantFunding is not None:
            namespaceprefix_ = self.subMerchantFunding_nsprefix_ + ':' if (UseCapturedNS_ and self.subMerchantFunding_nsprefix_) else ''
            self.subMerchantFunding.export(outfile, level, namespaceprefix_, namespacedef_='', name_='subMerchantFunding', pretty_print=pretty_print)
        if self.settlementCurrency is not None:
            namespaceprefix_ = self.settlementCurrency_nsprefix_ + ':' if (UseCapturedNS_ and self.settlementCurrency_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssettlementCurrency>%s</%ssettlementCurrency>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.settlementCurrency), input_name='settlementCurrency')), namespaceprefix_ , eol_))
        if self.sdkVersion is not None:
            namespaceprefix_ = self.sdkVersion_nsprefix_ + ':' if (UseCapturedNS_ and self.sdkVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssdkVersion>%s</%ssdkVersion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.sdkVersion), input_name='sdkVersion')), namespaceprefix_ , eol_))
        if self.language is not None:
            namespaceprefix_ = self.language_nsprefix_ + ':' if (UseCapturedNS_ and self.language_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slanguage>%s</%slanguage>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.language), input_name='language')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'merchantName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchantName')
            value_ = self.gds_validate_string(value_, node, 'merchantName')
            self.merchantName = value_
            self.merchantName_nsprefix_ = child_.prefix
            # validate type merchantNameType
            self.validate_merchantNameType(self.merchantName)
        elif nodeName_ == 'amexMid':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'amexMid')
            value_ = self.gds_validate_string(value_, node, 'amexMid')
            self.amexMid = value_
            self.amexMid_nsprefix_ = child_.prefix
            # validate type amexMidType
            self.validate_amexMidType(self.amexMid)
        elif nodeName_ == 'discoverConveyedMid':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'discoverConveyedMid')
            value_ = self.gds_validate_string(value_, node, 'discoverConveyedMid')
            self.discoverConveyedMid = value_
            self.discoverConveyedMid_nsprefix_ = child_.prefix
            # validate type discoverConveyedMidType
            self.validate_discoverConveyedMidType(self.discoverConveyedMid)
        elif nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
            # validate type urlType
            self.validate_urlType(self.url)
        elif nodeName_ == 'customerServiceNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customerServiceNumber')
            value_ = self.gds_validate_string(value_, node, 'customerServiceNumber')
            self.customerServiceNumber = value_
            self.customerServiceNumber_nsprefix_ = child_.prefix
            # validate type customerServiceNumberType
            self.validate_customerServiceNumberType(self.customerServiceNumber)
        elif nodeName_ == 'hardCodedBillingDescriptor':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'hardCodedBillingDescriptor')
            value_ = self.gds_validate_string(value_, node, 'hardCodedBillingDescriptor')
            self.hardCodedBillingDescriptor = value_
            self.hardCodedBillingDescriptor_nsprefix_ = child_.prefix
            # validate type hardCodedBillingDescriptorType
            self.validate_hardCodedBillingDescriptorType(self.hardCodedBillingDescriptor)
        elif nodeName_ == 'maxTransactionAmount' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'maxTransactionAmount')
            ival_ = self.gds_validate_integer(ival_, node, 'maxTransactionAmount')
            self.maxTransactionAmount = ival_
            self.maxTransactionAmount_nsprefix_ = child_.prefix
            # validate type maxTransactionAmountType
            self.validate_maxTransactionAmountType(self.maxTransactionAmount)
        elif nodeName_ == 'purchaseCurrency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'purchaseCurrency')
            value_ = self.gds_validate_string(value_, node, 'purchaseCurrency')
            self.purchaseCurrency = value_
            self.purchaseCurrency_nsprefix_ = child_.prefix
            # validate type purchaseCurrencyType
            self.validate_purchaseCurrencyType(self.purchaseCurrency)
        elif nodeName_ == 'merchantCategoryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchantCategoryCode')
            value_ = self.gds_validate_string(value_, node, 'merchantCategoryCode')
            self.merchantCategoryCode = value_
            self.merchantCategoryCode_nsprefix_ = child_.prefix
            # validate type merchantCategoryCodeType
            self.validate_merchantCategoryCodeType(self.merchantCategoryCode)
        elif nodeName_ == 'taxAuthority':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxAuthority')
            value_ = self.gds_validate_string(value_, node, 'taxAuthority')
            self.taxAuthority = value_
            self.taxAuthority_nsprefix_ = child_.prefix
        elif nodeName_ == 'taxAuthorityState':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxAuthorityState')
            value_ = self.gds_validate_string(value_, node, 'taxAuthorityState')
            self.taxAuthorityState = value_
            self.taxAuthorityState_nsprefix_ = child_.prefix
        elif nodeName_ == 'bankRoutingNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'bankRoutingNumber')
            value_ = self.gds_validate_string(value_, node, 'bankRoutingNumber')
            self.bankRoutingNumber = value_
            self.bankRoutingNumber_nsprefix_ = child_.prefix
            # validate type bankRoutingNumberType
            self.validate_bankRoutingNumberType(self.bankRoutingNumber)
        elif nodeName_ == 'bankAccountNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'bankAccountNumber')
            value_ = self.gds_validate_string(value_, node, 'bankAccountNumber')
            self.bankAccountNumber = value_
            self.bankAccountNumber_nsprefix_ = child_.prefix
            # validate type bankAccountNumberType
            self.validate_bankAccountNumberType(self.bankAccountNumber)
        elif nodeName_ == 'pspMerchantId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pspMerchantId')
            value_ = self.gds_validate_string(value_, node, 'pspMerchantId')
            self.pspMerchantId = value_
            self.pspMerchantId_nsprefix_ = child_.prefix
            # validate type pspMerchantIdType
            self.validate_pspMerchantIdType(self.pspMerchantId)
        elif nodeName_ == 'fraud':
            obj_ = subMerchantFraudFeature.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.fraud = obj_
            obj_.original_tagname_ = 'fraud'
        elif nodeName_ == 'amexAcquired':
            obj_ = subMerchantAmexAcquiredFeature.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.amexAcquired = obj_
            obj_.original_tagname_ = 'amexAcquired'
        elif nodeName_ == 'address':
            obj_ = address.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'primaryContact':
            obj_ = subMerchantPrimaryContact.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.primaryContact = obj_
            obj_.original_tagname_ = 'primaryContact'
        elif nodeName_ == 'createCredentials':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'createCredentials')
            ival_ = self.gds_validate_boolean(ival_, node, 'createCredentials')
            self.createCredentials = ival_
            self.createCredentials_nsprefix_ = child_.prefix
        elif nodeName_ == 'eCheck':
            obj_ = subMerchantECheckFeature.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.eCheck = obj_
            obj_.original_tagname_ = 'eCheck'
        elif nodeName_ == 'subMerchantFunding':
            obj_ = subMerchantFunding.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.subMerchantFunding = obj_
            obj_.original_tagname_ = 'subMerchantFunding'
        elif nodeName_ == 'settlementCurrency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'settlementCurrency')
            value_ = self.gds_validate_string(value_, node, 'settlementCurrency')
            self.settlementCurrency = value_
            self.settlementCurrency_nsprefix_ = child_.prefix
            # validate type settlementCurrencyType
            self.validate_settlementCurrencyType(self.settlementCurrency)
        elif nodeName_ == 'sdkVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'sdkVersion')
            value_ = self.gds_validate_string(value_, node, 'sdkVersion')
            self.sdkVersion = value_
            self.sdkVersion_nsprefix_ = child_.prefix
            # validate type sdkVersionType53
            self.validate_sdkVersionType53(self.sdkVersion)
        elif nodeName_ == 'language':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'language')
            value_ = self.gds_validate_string(value_, node, 'language')
            self.language = value_
            self.language_nsprefix_ = child_.prefix
            # validate type languageType54
            self.validate_languageType54(self.language)
# end class subMerchantCreateRequest


class subMerchantFraudFeature(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, enabled=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.enabled = _cast(bool, enabled)
        self.enabled_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantFraudFeature)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantFraudFeature.subclass:
            return subMerchantFraudFeature.subclass(*args_, **kwargs_)
        else:
            return subMerchantFraudFeature(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_enabled(self):
        return self.enabled
    def set_enabled(self, enabled):
        self.enabled = enabled
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantFraudFeature', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantFraudFeature')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantFraudFeature':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantFraudFeature')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantFraudFeature', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantFraudFeature'):
        if self.enabled is not None and 'enabled' not in already_processed:
            already_processed.add('enabled')
            outfile.write(' enabled="%s"' % self.gds_format_boolean(self.enabled, input_name='enabled'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantFraudFeature', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('enabled', node)
        if value is not None and 'enabled' not in already_processed:
            already_processed.add('enabled')
            if value in ('true', '1'):
                self.enabled = True
            elif value in ('false', '0'):
                self.enabled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class subMerchantFraudFeature


class subMerchantAmexAcquiredFeature(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, enabled=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.enabled = _cast(bool, enabled)
        self.enabled_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantAmexAcquiredFeature)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantAmexAcquiredFeature.subclass:
            return subMerchantAmexAcquiredFeature.subclass(*args_, **kwargs_)
        else:
            return subMerchantAmexAcquiredFeature(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_enabled(self):
        return self.enabled
    def set_enabled(self, enabled):
        self.enabled = enabled
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantAmexAcquiredFeature', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantAmexAcquiredFeature')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantAmexAcquiredFeature':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantAmexAcquiredFeature')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantAmexAcquiredFeature', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantAmexAcquiredFeature'):
        if self.enabled is not None and 'enabled' not in already_processed:
            already_processed.add('enabled')
            outfile.write(' enabled="%s"' % self.gds_format_boolean(self.enabled, input_name='enabled'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantAmexAcquiredFeature', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('enabled', node)
        if value is not None and 'enabled' not in already_processed:
            already_processed.add('enabled')
            if value in ('true', '1'):
                self.enabled = True
            elif value in ('false', '0'):
                self.enabled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class subMerchantAmexAcquiredFeature


class subMerchantPrimaryContact(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, firstName=None, lastName=None, emailAddress=None, phone=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.firstName = firstName
        self.validate_firstNameType55(self.firstName)
        self.firstName_nsprefix_ = None
        self.lastName = lastName
        self.validate_lastNameType56(self.lastName)
        self.lastName_nsprefix_ = None
        self.emailAddress = emailAddress
        self.validate_emailAddressType57(self.emailAddress)
        self.emailAddress_nsprefix_ = None
        self.phone = phone
        self.validate_phoneType(self.phone)
        self.phone_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantPrimaryContact)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantPrimaryContact.subclass:
            return subMerchantPrimaryContact.subclass(*args_, **kwargs_)
        else:
            return subMerchantPrimaryContact(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_firstName(self):
        return self.firstName
    def set_firstName(self, firstName):
        self.firstName = firstName
    def get_lastName(self):
        return self.lastName
    def set_lastName(self, lastName):
        self.lastName = lastName
    def get_emailAddress(self):
        return self.emailAddress
    def set_emailAddress(self, emailAddress):
        self.emailAddress = emailAddress
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def validate_firstNameType55(self, value):
        result = True
        # Validate type firstNameType55, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on firstNameType55' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on firstNameType55' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_lastNameType56(self, value):
        result = True
        # Validate type lastNameType56, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on lastNameType56' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on lastNameType56' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_emailAddressType57(self, value):
        result = True
        # Validate type emailAddressType57, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on emailAddressType57' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on emailAddressType57' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_phoneType(self, value):
        result = True
        # Validate type phoneType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 13:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.firstName is not None or
            self.lastName is not None or
            self.emailAddress is not None or
            self.phone is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantPrimaryContact', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantPrimaryContact')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantPrimaryContact':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantPrimaryContact')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantPrimaryContact', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantPrimaryContact'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantPrimaryContact', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.firstName is not None:
            namespaceprefix_ = self.firstName_nsprefix_ + ':' if (UseCapturedNS_ and self.firstName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfirstName>%s</%sfirstName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.firstName), input_name='firstName')), namespaceprefix_ , eol_))
        if self.lastName is not None:
            namespaceprefix_ = self.lastName_nsprefix_ + ':' if (UseCapturedNS_ and self.lastName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slastName>%s</%slastName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lastName), input_name='lastName')), namespaceprefix_ , eol_))
        if self.emailAddress is not None:
            namespaceprefix_ = self.emailAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.emailAddress_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%semailAddress>%s</%semailAddress>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.emailAddress), input_name='emailAddress')), namespaceprefix_ , eol_))
        if self.phone is not None:
            namespaceprefix_ = self.phone_nsprefix_ + ':' if (UseCapturedNS_ and self.phone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sphone>%s</%sphone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.phone), input_name='phone')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'firstName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firstName')
            value_ = self.gds_validate_string(value_, node, 'firstName')
            self.firstName = value_
            self.firstName_nsprefix_ = child_.prefix
            # validate type firstNameType55
            self.validate_firstNameType55(self.firstName)
        elif nodeName_ == 'lastName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lastName')
            value_ = self.gds_validate_string(value_, node, 'lastName')
            self.lastName = value_
            self.lastName_nsprefix_ = child_.prefix
            # validate type lastNameType56
            self.validate_lastNameType56(self.lastName)
        elif nodeName_ == 'emailAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'emailAddress')
            value_ = self.gds_validate_string(value_, node, 'emailAddress')
            self.emailAddress = value_
            self.emailAddress_nsprefix_ = child_.prefix
            # validate type emailAddressType57
            self.validate_emailAddressType57(self.emailAddress)
        elif nodeName_ == 'phone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'phone')
            value_ = self.gds_validate_string(value_, node, 'phone')
            self.phone = value_
            self.phone_nsprefix_ = child_.prefix
            # validate type phoneType
            self.validate_phoneType(self.phone)
# end class subMerchantPrimaryContact


class subMerchantECheckFeature(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, enabled=None, eCheckCompanyName=None, eCheckBillingDescriptor=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.enabled = _cast(bool, enabled)
        self.enabled_nsprefix_ = None
        self.eCheckCompanyName = eCheckCompanyName
        self.validate_eCheckCompanyNameType(self.eCheckCompanyName)
        self.eCheckCompanyName_nsprefix_ = None
        self.eCheckBillingDescriptor = eCheckBillingDescriptor
        self.validate_eCheckBillingDescriptorType(self.eCheckBillingDescriptor)
        self.eCheckBillingDescriptor_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantECheckFeature)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantECheckFeature.subclass:
            return subMerchantECheckFeature.subclass(*args_, **kwargs_)
        else:
            return subMerchantECheckFeature(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_eCheckCompanyName(self):
        return self.eCheckCompanyName
    def set_eCheckCompanyName(self, eCheckCompanyName):
        self.eCheckCompanyName = eCheckCompanyName
    def get_eCheckBillingDescriptor(self):
        return self.eCheckBillingDescriptor
    def set_eCheckBillingDescriptor(self, eCheckBillingDescriptor):
        self.eCheckBillingDescriptor = eCheckBillingDescriptor
    def get_enabled(self):
        return self.enabled
    def set_enabled(self, enabled):
        self.enabled = enabled
    def validate_eCheckCompanyNameType(self, value):
        result = True
        # Validate type eCheckCompanyNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on eCheckCompanyNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on eCheckCompanyNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_eCheckBillingDescriptorType(self, value):
        result = True
        # Validate type eCheckBillingDescriptorType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on eCheckBillingDescriptorType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on eCheckBillingDescriptorType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.eCheckCompanyName is not None or
            self.eCheckBillingDescriptor is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantECheckFeature', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantECheckFeature')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantECheckFeature':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantECheckFeature')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantECheckFeature', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantECheckFeature'):
        if self.enabled is not None and 'enabled' not in already_processed:
            already_processed.add('enabled')
            outfile.write(' enabled="%s"' % self.gds_format_boolean(self.enabled, input_name='enabled'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantECheckFeature', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.eCheckCompanyName is not None:
            namespaceprefix_ = self.eCheckCompanyName_nsprefix_ + ':' if (UseCapturedNS_ and self.eCheckCompanyName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%seCheckCompanyName>%s</%seCheckCompanyName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.eCheckCompanyName), input_name='eCheckCompanyName')), namespaceprefix_ , eol_))
        if self.eCheckBillingDescriptor is not None:
            namespaceprefix_ = self.eCheckBillingDescriptor_nsprefix_ + ':' if (UseCapturedNS_ and self.eCheckBillingDescriptor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%seCheckBillingDescriptor>%s</%seCheckBillingDescriptor>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.eCheckBillingDescriptor), input_name='eCheckBillingDescriptor')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('enabled', node)
        if value is not None and 'enabled' not in already_processed:
            already_processed.add('enabled')
            if value in ('true', '1'):
                self.enabled = True
            elif value in ('false', '0'):
                self.enabled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'eCheckCompanyName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'eCheckCompanyName')
            value_ = self.gds_validate_string(value_, node, 'eCheckCompanyName')
            self.eCheckCompanyName = value_
            self.eCheckCompanyName_nsprefix_ = child_.prefix
            # validate type eCheckCompanyNameType
            self.validate_eCheckCompanyNameType(self.eCheckCompanyName)
        elif nodeName_ == 'eCheckBillingDescriptor':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'eCheckBillingDescriptor')
            value_ = self.gds_validate_string(value_, node, 'eCheckBillingDescriptor')
            self.eCheckBillingDescriptor = value_
            self.eCheckBillingDescriptor_nsprefix_ = child_.prefix
            # validate type eCheckBillingDescriptorType
            self.validate_eCheckBillingDescriptorType(self.eCheckBillingDescriptor)
# end class subMerchantECheckFeature


class subMerchantFunding(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, enabled=None, feeProfile=None, fundingSubmerchantId=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.enabled = _cast(bool, enabled)
        self.enabled_nsprefix_ = None
        self.feeProfile = feeProfile
        self.validate_feeProfileType(self.feeProfile)
        self.feeProfile_nsprefix_ = None
        self.fundingSubmerchantId = fundingSubmerchantId
        self.validate_fundingSubmerchantIdType(self.fundingSubmerchantId)
        self.fundingSubmerchantId_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantFunding)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantFunding.subclass:
            return subMerchantFunding.subclass(*args_, **kwargs_)
        else:
            return subMerchantFunding(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_feeProfile(self):
        return self.feeProfile
    def set_feeProfile(self, feeProfile):
        self.feeProfile = feeProfile
    def get_fundingSubmerchantId(self):
        return self.fundingSubmerchantId
    def set_fundingSubmerchantId(self, fundingSubmerchantId):
        self.fundingSubmerchantId = fundingSubmerchantId
    def get_enabled(self):
        return self.enabled
    def set_enabled(self, enabled):
        self.enabled = enabled
    def validate_feeProfileType(self, value):
        result = True
        # Validate type feeProfileType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 150:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on feeProfileType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on feeProfileType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_fundingSubmerchantIdType(self, value):
        result = True
        # Validate type fundingSubmerchantIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on fundingSubmerchantIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on fundingSubmerchantIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.feeProfile is not None or
            self.fundingSubmerchantId is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantFunding', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantFunding')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantFunding':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantFunding')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantFunding', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantFunding'):
        if self.enabled is not None and 'enabled' not in already_processed:
            already_processed.add('enabled')
            outfile.write(' enabled="%s"' % self.gds_format_boolean(self.enabled, input_name='enabled'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantFunding', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.feeProfile is not None:
            namespaceprefix_ = self.feeProfile_nsprefix_ + ':' if (UseCapturedNS_ and self.feeProfile_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfeeProfile>%s</%sfeeProfile>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.feeProfile), input_name='feeProfile')), namespaceprefix_ , eol_))
        if self.fundingSubmerchantId is not None:
            namespaceprefix_ = self.fundingSubmerchantId_nsprefix_ + ':' if (UseCapturedNS_ and self.fundingSubmerchantId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfundingSubmerchantId>%s</%sfundingSubmerchantId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.fundingSubmerchantId), input_name='fundingSubmerchantId')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('enabled', node)
        if value is not None and 'enabled' not in already_processed:
            already_processed.add('enabled')
            if value in ('true', '1'):
                self.enabled = True
            elif value in ('false', '0'):
                self.enabled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'feeProfile':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'feeProfile')
            value_ = self.gds_validate_string(value_, node, 'feeProfile')
            self.feeProfile = value_
            self.feeProfile_nsprefix_ = child_.prefix
            # validate type feeProfileType
            self.validate_feeProfileType(self.feeProfile)
        elif nodeName_ == 'fundingSubmerchantId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fundingSubmerchantId')
            value_ = self.gds_validate_string(value_, node, 'fundingSubmerchantId')
            self.fundingSubmerchantId = value_
            self.fundingSubmerchantId_nsprefix_ = child_.prefix
            # validate type fundingSubmerchantIdType
            self.validate_fundingSubmerchantIdType(self.fundingSubmerchantId)
# end class subMerchantFunding


class subMerchantCreateResponse(response):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = response
    def __init__(self, transactionId=None, duplicate=None, subMerchantId=None, merchantIdentString=None, originalSubMerchant=None, credentials=None, paypageCredentials=None, amexSellerId=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(subMerchantCreateResponse, self).__init__(transactionId,  **kwargs_)
        self.duplicate = _cast(bool, duplicate)
        self.duplicate_nsprefix_ = None
        self.subMerchantId = subMerchantId
        self.validate_subMerchantIdType(self.subMerchantId)
        self.subMerchantId_nsprefix_ = None
        self.merchantIdentString = merchantIdentString
        self.validate_merchantIdentStringType(self.merchantIdentString)
        self.merchantIdentString_nsprefix_ = None
        self.originalSubMerchant = originalSubMerchant
        self.originalSubMerchant_nsprefix_ = None
        self.credentials = credentials
        self.credentials_nsprefix_ = None
        self.paypageCredentials = paypageCredentials
        self.paypageCredentials_nsprefix_ = None
        self.amexSellerId = amexSellerId
        self.validate_amexSellerIdType(self.amexSellerId)
        self.amexSellerId_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantCreateResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantCreateResponse.subclass:
            return subMerchantCreateResponse.subclass(*args_, **kwargs_)
        else:
            return subMerchantCreateResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_subMerchantId(self):
        return self.subMerchantId
    def set_subMerchantId(self, subMerchantId):
        self.subMerchantId = subMerchantId
    def get_merchantIdentString(self):
        return self.merchantIdentString
    def set_merchantIdentString(self, merchantIdentString):
        self.merchantIdentString = merchantIdentString
    def get_originalSubMerchant(self):
        return self.originalSubMerchant
    def set_originalSubMerchant(self, originalSubMerchant):
        self.originalSubMerchant = originalSubMerchant
    def get_credentials(self):
        return self.credentials
    def set_credentials(self, credentials):
        self.credentials = credentials
    def get_paypageCredentials(self):
        return self.paypageCredentials
    def set_paypageCredentials(self, paypageCredentials):
        self.paypageCredentials = paypageCredentials
    def get_amexSellerId(self):
        return self.amexSellerId
    def set_amexSellerId(self, amexSellerId):
        self.amexSellerId = amexSellerId
    def get_duplicate(self):
        return self.duplicate
    def set_duplicate(self, duplicate):
        self.duplicate = duplicate
    def validate_subMerchantIdType(self, value):
        result = True
        # Validate type subMerchantIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on subMerchantIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on subMerchantIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_merchantIdentStringType(self, value):
        result = True
        # Validate type merchantIdentStringType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchantIdentStringType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on merchantIdentStringType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_amexSellerIdType(self, value):
        result = True
        # Validate type amexSellerIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on amexSellerIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on amexSellerIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.subMerchantId is not None or
            self.merchantIdentString is not None or
            self.originalSubMerchant is not None or
            self.credentials is not None or
            self.paypageCredentials is not None or
            self.amexSellerId is not None or
            super(subMerchantCreateResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantCreateResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantCreateResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantCreateResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantCreateResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantCreateResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantCreateResponse'):
        super(subMerchantCreateResponse, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantCreateResponse')
        if self.duplicate is not None and 'duplicate' not in already_processed:
            already_processed.add('duplicate')
            outfile.write(' duplicate="%s"' % self.gds_format_boolean(self.duplicate, input_name='duplicate'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantCreateResponse', fromsubclass_=False, pretty_print=True):
        super(subMerchantCreateResponse, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.subMerchantId is not None:
            namespaceprefix_ = self.subMerchantId_nsprefix_ + ':' if (UseCapturedNS_ and self.subMerchantId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssubMerchantId>%s</%ssubMerchantId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.subMerchantId), input_name='subMerchantId')), namespaceprefix_ , eol_))
        if self.merchantIdentString is not None:
            namespaceprefix_ = self.merchantIdentString_nsprefix_ + ':' if (UseCapturedNS_ and self.merchantIdentString_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchantIdentString>%s</%smerchantIdentString>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchantIdentString), input_name='merchantIdentString')), namespaceprefix_ , eol_))
        if self.originalSubMerchant is not None:
            namespaceprefix_ = self.originalSubMerchant_nsprefix_ + ':' if (UseCapturedNS_ and self.originalSubMerchant_nsprefix_) else ''
            self.originalSubMerchant.export(outfile, level, namespaceprefix_, namespacedef_='', name_='originalSubMerchant', pretty_print=pretty_print)
        if self.credentials is not None:
            namespaceprefix_ = self.credentials_nsprefix_ + ':' if (UseCapturedNS_ and self.credentials_nsprefix_) else ''
            self.credentials.export(outfile, level, namespaceprefix_, namespacedef_='', name_='credentials', pretty_print=pretty_print)
        if self.paypageCredentials is not None:
            namespaceprefix_ = self.paypageCredentials_nsprefix_ + ':' if (UseCapturedNS_ and self.paypageCredentials_nsprefix_) else ''
            self.paypageCredentials.export(outfile, level, namespaceprefix_, namespacedef_='', name_='paypageCredentials', pretty_print=pretty_print)
        if self.amexSellerId is not None:
            namespaceprefix_ = self.amexSellerId_nsprefix_ + ':' if (UseCapturedNS_ and self.amexSellerId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%samexSellerId>%s</%samexSellerId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.amexSellerId), input_name='amexSellerId')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('duplicate', node)
        if value is not None and 'duplicate' not in already_processed:
            already_processed.add('duplicate')
            if value in ('true', '1'):
                self.duplicate = True
            elif value in ('false', '0'):
                self.duplicate = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(subMerchantCreateResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'subMerchantId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'subMerchantId')
            value_ = self.gds_validate_string(value_, node, 'subMerchantId')
            self.subMerchantId = value_
            self.subMerchantId_nsprefix_ = child_.prefix
            # validate type subMerchantIdType
            self.validate_subMerchantIdType(self.subMerchantId)
        elif nodeName_ == 'merchantIdentString':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchantIdentString')
            value_ = self.gds_validate_string(value_, node, 'merchantIdentString')
            self.merchantIdentString = value_
            self.merchantIdentString_nsprefix_ = child_.prefix
            # validate type merchantIdentStringType
            self.validate_merchantIdentStringType(self.merchantIdentString)
        elif nodeName_ == 'originalSubMerchant':
            obj_ = subMerchantRetrievalResponse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.originalSubMerchant = obj_
            obj_.original_tagname_ = 'originalSubMerchant'
        elif nodeName_ == 'credentials':
            obj_ = subMerchantCredentials.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.credentials = obj_
            obj_.original_tagname_ = 'credentials'
        elif nodeName_ == 'paypageCredentials':
            obj_ = paypageCredentialsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.paypageCredentials = obj_
            obj_.original_tagname_ = 'paypageCredentials'
        elif nodeName_ == 'amexSellerId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'amexSellerId')
            value_ = self.gds_validate_string(value_, node, 'amexSellerId')
            self.amexSellerId = value_
            self.amexSellerId_nsprefix_ = child_.prefix
            # validate type amexSellerIdType
            self.validate_amexSellerIdType(self.amexSellerId)
        super(subMerchantCreateResponse, self).buildChildren(child_, node, nodeName_, True)
# end class subMerchantCreateResponse


class subMerchantRetrievalResponse(subMerchantCreateRequest):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = subMerchantCreateRequest
    def __init__(self, merchantName=None, amexMid=None, discoverConveyedMid=None, url=None, customerServiceNumber=None, hardCodedBillingDescriptor=None, maxTransactionAmount=None, purchaseCurrency=None, merchantCategoryCode=None, taxAuthority=None, taxAuthorityState=None, bankRoutingNumber=None, bankAccountNumber=None, pspMerchantId=None, fraud=None, amexAcquired=None, address=None, primaryContact=None, createCredentials=None, eCheck=None, subMerchantFunding=None, settlementCurrency=None, sdkVersion=None, language=None, subMerchantId=None, amexSellerId=None, disabled=None, transactionId=None, merchantIdentString=None, credentials=None, paypageCredentials=None, updateDate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(subMerchantRetrievalResponse, self).__init__(merchantName, amexMid, discoverConveyedMid, url, customerServiceNumber, hardCodedBillingDescriptor, maxTransactionAmount, purchaseCurrency, merchantCategoryCode, taxAuthority, taxAuthorityState, bankRoutingNumber, bankAccountNumber, pspMerchantId, fraud, amexAcquired, address, primaryContact, createCredentials, eCheck, subMerchantFunding, settlementCurrency, sdkVersion, language,  **kwargs_)
        self.subMerchantId = subMerchantId
        self.validate_subMerchantIdType58(self.subMerchantId)
        self.subMerchantId_nsprefix_ = None
        self.amexSellerId = amexSellerId
        self.validate_amexSellerIdType59(self.amexSellerId)
        self.amexSellerId_nsprefix_ = None
        self.disabled = disabled
        self.disabled_nsprefix_ = None
        self.transactionId = transactionId
        self.validate_transactionIdType60(self.transactionId)
        self.transactionId_nsprefix_ = None
        self.merchantIdentString = merchantIdentString
        self.validate_merchantIdentStringType61(self.merchantIdentString)
        self.merchantIdentString_nsprefix_ = None
        self.credentials = credentials
        self.credentials_nsprefix_ = None
        self.paypageCredentials = paypageCredentials
        self.paypageCredentials_nsprefix_ = None
        if isinstance(updateDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(updateDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = updateDate
        self.updateDate = initvalue_
        self.updateDate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantRetrievalResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantRetrievalResponse.subclass:
            return subMerchantRetrievalResponse.subclass(*args_, **kwargs_)
        else:
            return subMerchantRetrievalResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_subMerchantId(self):
        return self.subMerchantId
    def set_subMerchantId(self, subMerchantId):
        self.subMerchantId = subMerchantId
    def get_amexSellerId(self):
        return self.amexSellerId
    def set_amexSellerId(self, amexSellerId):
        self.amexSellerId = amexSellerId
    def get_disabled(self):
        return self.disabled
    def set_disabled(self, disabled):
        self.disabled = disabled
    def get_transactionId(self):
        return self.transactionId
    def set_transactionId(self, transactionId):
        self.transactionId = transactionId
    def get_merchantIdentString(self):
        return self.merchantIdentString
    def set_merchantIdentString(self, merchantIdentString):
        self.merchantIdentString = merchantIdentString
    def get_credentials(self):
        return self.credentials
    def set_credentials(self, credentials):
        self.credentials = credentials
    def get_paypageCredentials(self):
        return self.paypageCredentials
    def set_paypageCredentials(self, paypageCredentials):
        self.paypageCredentials = paypageCredentials
    def get_updateDate(self):
        return self.updateDate
    def set_updateDate(self, updateDate):
        self.updateDate = updateDate
    def validate_subMerchantIdType58(self, value):
        result = True
        # Validate type subMerchantIdType58, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on subMerchantIdType58' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on subMerchantIdType58' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_amexSellerIdType59(self, value):
        result = True
        # Validate type amexSellerIdType59, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on amexSellerIdType59' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on amexSellerIdType59' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_transactionIdType60(self, value):
        result = True
        # Validate type transactionIdType60, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on transactionIdType60' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on transactionIdType60' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_merchantIdentStringType61(self, value):
        result = True
        # Validate type merchantIdentStringType61, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchantIdentStringType61' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on merchantIdentStringType61' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.subMerchantId is not None or
            self.amexSellerId is not None or
            self.disabled is not None or
            self.transactionId is not None or
            self.merchantIdentString is not None or
            self.credentials is not None or
            self.paypageCredentials is not None or
            self.updateDate is not None or
            super(subMerchantRetrievalResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantRetrievalResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantRetrievalResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantRetrievalResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantRetrievalResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantRetrievalResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantRetrievalResponse'):
        super(subMerchantRetrievalResponse, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantRetrievalResponse')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantRetrievalResponse', fromsubclass_=False, pretty_print=True):
        super(subMerchantRetrievalResponse, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.subMerchantId is not None:
            namespaceprefix_ = self.subMerchantId_nsprefix_ + ':' if (UseCapturedNS_ and self.subMerchantId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssubMerchantId>%s</%ssubMerchantId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.subMerchantId), input_name='subMerchantId')), namespaceprefix_ , eol_))
        if self.amexSellerId is not None:
            namespaceprefix_ = self.amexSellerId_nsprefix_ + ':' if (UseCapturedNS_ and self.amexSellerId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%samexSellerId>%s</%samexSellerId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.amexSellerId), input_name='amexSellerId')), namespaceprefix_ , eol_))
        if self.disabled is not None:
            namespaceprefix_ = self.disabled_nsprefix_ + ':' if (UseCapturedNS_ and self.disabled_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdisabled>%s</%sdisabled>%s' % (namespaceprefix_ , self.gds_format_boolean(self.disabled, input_name='disabled'), namespaceprefix_ , eol_))
        if self.transactionId is not None:
            namespaceprefix_ = self.transactionId_nsprefix_ + ':' if (UseCapturedNS_ and self.transactionId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransactionId>%s</%stransactionId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.transactionId), input_name='transactionId')), namespaceprefix_ , eol_))
        if self.merchantIdentString is not None:
            namespaceprefix_ = self.merchantIdentString_nsprefix_ + ':' if (UseCapturedNS_ and self.merchantIdentString_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchantIdentString>%s</%smerchantIdentString>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchantIdentString), input_name='merchantIdentString')), namespaceprefix_ , eol_))
        if self.credentials is not None:
            namespaceprefix_ = self.credentials_nsprefix_ + ':' if (UseCapturedNS_ and self.credentials_nsprefix_) else ''
            self.credentials.export(outfile, level, namespaceprefix_, namespacedef_='', name_='credentials', pretty_print=pretty_print)
        if self.paypageCredentials is not None:
            namespaceprefix_ = self.paypageCredentials_nsprefix_ + ':' if (UseCapturedNS_ and self.paypageCredentials_nsprefix_) else ''
            self.paypageCredentials.export(outfile, level, namespaceprefix_, namespacedef_='', name_='paypageCredentials', pretty_print=pretty_print)
        if self.updateDate is not None:
            namespaceprefix_ = self.updateDate_nsprefix_ + ':' if (UseCapturedNS_ and self.updateDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%supdateDate>%s</%supdateDate>%s' % (namespaceprefix_ , self.gds_format_datetime(self.updateDate, input_name='updateDate'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(subMerchantRetrievalResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'subMerchantId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'subMerchantId')
            value_ = self.gds_validate_string(value_, node, 'subMerchantId')
            self.subMerchantId = value_
            self.subMerchantId_nsprefix_ = child_.prefix
            # validate type subMerchantIdType58
            self.validate_subMerchantIdType58(self.subMerchantId)
        elif nodeName_ == 'amexSellerId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'amexSellerId')
            value_ = self.gds_validate_string(value_, node, 'amexSellerId')
            self.amexSellerId = value_
            self.amexSellerId_nsprefix_ = child_.prefix
            # validate type amexSellerIdType59
            self.validate_amexSellerIdType59(self.amexSellerId)
        elif nodeName_ == 'disabled':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'disabled')
            ival_ = self.gds_validate_boolean(ival_, node, 'disabled')
            self.disabled = ival_
            self.disabled_nsprefix_ = child_.prefix
        elif nodeName_ == 'transactionId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'transactionId')
            value_ = self.gds_validate_string(value_, node, 'transactionId')
            self.transactionId = value_
            self.transactionId_nsprefix_ = child_.prefix
            # validate type transactionIdType60
            self.validate_transactionIdType60(self.transactionId)
        elif nodeName_ == 'merchantIdentString':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchantIdentString')
            value_ = self.gds_validate_string(value_, node, 'merchantIdentString')
            self.merchantIdentString = value_
            self.merchantIdentString_nsprefix_ = child_.prefix
            # validate type merchantIdentStringType61
            self.validate_merchantIdentStringType61(self.merchantIdentString)
        elif nodeName_ == 'credentials':
            obj_ = subMerchantCredentials.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.credentials = obj_
            obj_.original_tagname_ = 'credentials'
        elif nodeName_ == 'paypageCredentials':
            obj_ = paypageCredentialsType62.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.paypageCredentials = obj_
            obj_.original_tagname_ = 'paypageCredentials'
        elif nodeName_ == 'updateDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.updateDate = dval_
            self.updateDate_nsprefix_ = child_.prefix
        super(subMerchantRetrievalResponse, self).buildChildren(child_, node, nodeName_, True)
# end class subMerchantRetrievalResponse


class subMerchantCredentials(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, username=None, password=None, passwordExpirationDate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.username = username
        self.validate_usernameType(self.username)
        self.username_nsprefix_ = None
        self.password = password
        self.validate_passwordType(self.password)
        self.password_nsprefix_ = None
        if isinstance(passwordExpirationDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(passwordExpirationDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = passwordExpirationDate
        self.passwordExpirationDate = initvalue_
        self.passwordExpirationDate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantCredentials)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantCredentials.subclass:
            return subMerchantCredentials.subclass(*args_, **kwargs_)
        else:
            return subMerchantCredentials(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
    def get_password(self):
        return self.password
    def set_password(self, password):
        self.password = password
    def get_passwordExpirationDate(self):
        return self.passwordExpirationDate
    def set_passwordExpirationDate(self, passwordExpirationDate):
        self.passwordExpirationDate = passwordExpirationDate
    def validate_usernameType(self, value):
        result = True
        # Validate type usernameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 72:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on usernameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on usernameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_passwordType(self, value):
        result = True
        # Validate type passwordType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 72:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on passwordType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on passwordType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.username is not None or
            self.password is not None or
            self.passwordExpirationDate is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantCredentials', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantCredentials')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantCredentials':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantCredentials')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantCredentials', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantCredentials'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantCredentials', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.username is not None:
            namespaceprefix_ = self.username_nsprefix_ + ':' if (UseCapturedNS_ and self.username_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%susername>%s</%susername>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.username), input_name='username')), namespaceprefix_ , eol_))
        if self.password is not None:
            namespaceprefix_ = self.password_nsprefix_ + ':' if (UseCapturedNS_ and self.password_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spassword>%s</%spassword>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.password), input_name='password')), namespaceprefix_ , eol_))
        if self.passwordExpirationDate is not None:
            namespaceprefix_ = self.passwordExpirationDate_nsprefix_ + ':' if (UseCapturedNS_ and self.passwordExpirationDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spasswordExpirationDate>%s</%spasswordExpirationDate>%s' % (namespaceprefix_ , self.gds_format_datetime(self.passwordExpirationDate, input_name='passwordExpirationDate'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'username':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'username')
            value_ = self.gds_validate_string(value_, node, 'username')
            self.username = value_
            self.username_nsprefix_ = child_.prefix
            # validate type usernameType
            self.validate_usernameType(self.username)
        elif nodeName_ == 'password':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'password')
            value_ = self.gds_validate_string(value_, node, 'password')
            self.password = value_
            self.password_nsprefix_ = child_.prefix
            # validate type passwordType
            self.validate_passwordType(self.password)
        elif nodeName_ == 'passwordExpirationDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.passwordExpirationDate = dval_
            self.passwordExpirationDate_nsprefix_ = child_.prefix
# end class subMerchantCredentials


class paypageCredential(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, username=None, paypageId=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.username = username
        self.validate_usernameType63(self.username)
        self.username_nsprefix_ = None
        self.paypageId = paypageId
        self.validate_paypageIdType(self.paypageId)
        self.paypageId_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, paypageCredential)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if paypageCredential.subclass:
            return paypageCredential.subclass(*args_, **kwargs_)
        else:
            return paypageCredential(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
    def get_paypageId(self):
        return self.paypageId
    def set_paypageId(self, paypageId):
        self.paypageId = paypageId
    def validate_usernameType63(self, value):
        result = True
        # Validate type usernameType63, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 72:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on usernameType63' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on usernameType63' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_paypageIdType(self, value):
        result = True
        # Validate type paypageIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on paypageIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on paypageIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.username is not None or
            self.paypageId is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='paypageCredential', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('paypageCredential')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'paypageCredential':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='paypageCredential')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='paypageCredential', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='paypageCredential'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='paypageCredential', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.username is not None:
            namespaceprefix_ = self.username_nsprefix_ + ':' if (UseCapturedNS_ and self.username_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%susername>%s</%susername>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.username), input_name='username')), namespaceprefix_ , eol_))
        if self.paypageId is not None:
            namespaceprefix_ = self.paypageId_nsprefix_ + ':' if (UseCapturedNS_ and self.paypageId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spaypageId>%s</%spaypageId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.paypageId), input_name='paypageId')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'username':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'username')
            value_ = self.gds_validate_string(value_, node, 'username')
            self.username = value_
            self.username_nsprefix_ = child_.prefix
            # validate type usernameType63
            self.validate_usernameType63(self.username)
        elif nodeName_ == 'paypageId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'paypageId')
            value_ = self.gds_validate_string(value_, node, 'paypageId')
            self.paypageId = value_
            self.paypageId_nsprefix_ = child_.prefix
            # validate type paypageIdType
            self.validate_paypageIdType(self.paypageId)
# end class paypageCredential


class subMerchantUpdateRequest(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, merchantName=None, amexMid=None, discoverConveyedMid=None, url=None, customerServiceNumber=None, hardCodedBillingDescriptor=None, maxTransactionAmount=None, bankRoutingNumber=None, bankAccountNumber=None, pspMerchantId=None, purchaseCurrency=None, address=None, primaryContact=None, disable=None, fraud=None, amexAcquired=None, eCheck=None, subMerchantFunding=None, taxAuthority=None, taxAuthorityState=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.merchantName = merchantName
        self.validate_merchantNameType64(self.merchantName)
        self.merchantName_nsprefix_ = None
        self.amexMid = amexMid
        self.validate_amexMidType65(self.amexMid)
        self.amexMid_nsprefix_ = None
        self.discoverConveyedMid = discoverConveyedMid
        self.validate_discoverConveyedMidType66(self.discoverConveyedMid)
        self.discoverConveyedMid_nsprefix_ = None
        self.url = url
        self.validate_urlType67(self.url)
        self.url_nsprefix_ = None
        self.customerServiceNumber = customerServiceNumber
        self.validate_customerServiceNumberType68(self.customerServiceNumber)
        self.customerServiceNumber_nsprefix_ = None
        self.hardCodedBillingDescriptor = hardCodedBillingDescriptor
        self.validate_hardCodedBillingDescriptorType69(self.hardCodedBillingDescriptor)
        self.hardCodedBillingDescriptor_nsprefix_ = None
        self.maxTransactionAmount = maxTransactionAmount
        self.validate_maxTransactionAmountType70(self.maxTransactionAmount)
        self.maxTransactionAmount_nsprefix_ = None
        self.bankRoutingNumber = bankRoutingNumber
        self.validate_bankRoutingNumberType71(self.bankRoutingNumber)
        self.bankRoutingNumber_nsprefix_ = None
        self.bankAccountNumber = bankAccountNumber
        self.validate_bankAccountNumberType72(self.bankAccountNumber)
        self.bankAccountNumber_nsprefix_ = None
        self.pspMerchantId = pspMerchantId
        self.validate_pspMerchantIdType73(self.pspMerchantId)
        self.pspMerchantId_nsprefix_ = None
        self.purchaseCurrency = purchaseCurrency
        self.validate_purchaseCurrencyType74(self.purchaseCurrency)
        self.purchaseCurrency_nsprefix_ = None
        self.address = address
        self.address_nsprefix_ = None
        self.primaryContact = primaryContact
        self.primaryContact_nsprefix_ = None
        self.disable = disable
        self.disable_nsprefix_ = None
        self.fraud = fraud
        self.fraud_nsprefix_ = None
        self.amexAcquired = amexAcquired
        self.amexAcquired_nsprefix_ = None
        self.eCheck = eCheck
        self.eCheck_nsprefix_ = None
        self.subMerchantFunding = subMerchantFunding
        self.subMerchantFunding_nsprefix_ = None
        self.taxAuthority = taxAuthority
        self.taxAuthority_nsprefix_ = None
        self.taxAuthorityState = taxAuthorityState
        self.taxAuthorityState_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantUpdateRequest)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantUpdateRequest.subclass:
            return subMerchantUpdateRequest.subclass(*args_, **kwargs_)
        else:
            return subMerchantUpdateRequest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_merchantName(self):
        return self.merchantName
    def set_merchantName(self, merchantName):
        self.merchantName = merchantName
    def get_amexMid(self):
        return self.amexMid
    def set_amexMid(self, amexMid):
        self.amexMid = amexMid
    def get_discoverConveyedMid(self):
        return self.discoverConveyedMid
    def set_discoverConveyedMid(self, discoverConveyedMid):
        self.discoverConveyedMid = discoverConveyedMid
    def get_url(self):
        return self.url
    def set_url(self, url):
        self.url = url
    def get_customerServiceNumber(self):
        return self.customerServiceNumber
    def set_customerServiceNumber(self, customerServiceNumber):
        self.customerServiceNumber = customerServiceNumber
    def get_hardCodedBillingDescriptor(self):
        return self.hardCodedBillingDescriptor
    def set_hardCodedBillingDescriptor(self, hardCodedBillingDescriptor):
        self.hardCodedBillingDescriptor = hardCodedBillingDescriptor
    def get_maxTransactionAmount(self):
        return self.maxTransactionAmount
    def set_maxTransactionAmount(self, maxTransactionAmount):
        self.maxTransactionAmount = maxTransactionAmount
    def get_bankRoutingNumber(self):
        return self.bankRoutingNumber
    def set_bankRoutingNumber(self, bankRoutingNumber):
        self.bankRoutingNumber = bankRoutingNumber
    def get_bankAccountNumber(self):
        return self.bankAccountNumber
    def set_bankAccountNumber(self, bankAccountNumber):
        self.bankAccountNumber = bankAccountNumber
    def get_pspMerchantId(self):
        return self.pspMerchantId
    def set_pspMerchantId(self, pspMerchantId):
        self.pspMerchantId = pspMerchantId
    def get_purchaseCurrency(self):
        return self.purchaseCurrency
    def set_purchaseCurrency(self, purchaseCurrency):
        self.purchaseCurrency = purchaseCurrency
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def get_primaryContact(self):
        return self.primaryContact
    def set_primaryContact(self, primaryContact):
        self.primaryContact = primaryContact
    def get_disable(self):
        return self.disable
    def set_disable(self, disable):
        self.disable = disable
    def get_fraud(self):
        return self.fraud
    def set_fraud(self, fraud):
        self.fraud = fraud
    def get_amexAcquired(self):
        return self.amexAcquired
    def set_amexAcquired(self, amexAcquired):
        self.amexAcquired = amexAcquired
    def get_eCheck(self):
        return self.eCheck
    def set_eCheck(self, eCheck):
        self.eCheck = eCheck
    def get_subMerchantFunding(self):
        return self.subMerchantFunding
    def set_subMerchantFunding(self, subMerchantFunding):
        self.subMerchantFunding = subMerchantFunding
    def get_taxAuthority(self):
        return self.taxAuthority
    def set_taxAuthority(self, taxAuthority):
        self.taxAuthority = taxAuthority
    def get_taxAuthorityState(self):
        return self.taxAuthorityState
    def set_taxAuthorityState(self, taxAuthorityState):
        self.taxAuthorityState = taxAuthorityState
    def validate_merchantNameType64(self, value):
        result = True
        # Validate type merchantNameType64, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchantNameType64' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on merchantNameType64' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_amexMidType65(self, value):
        result = True
        # Validate type amexMidType65, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on amexMidType65' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on amexMidType65' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_discoverConveyedMidType66(self, value):
        result = True
        # Validate type discoverConveyedMidType66, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on discoverConveyedMidType66' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on discoverConveyedMidType66' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_urlType67(self, value):
        result = True
        # Validate type urlType67, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 120:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on urlType67' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on urlType67' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_customerServiceNumberType68(self, value):
        result = True
        # Validate type customerServiceNumberType68, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 13:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on customerServiceNumberType68' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on customerServiceNumberType68' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_hardCodedBillingDescriptorType69(self, value):
        result = True
        # Validate type hardCodedBillingDescriptorType69, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 25:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on hardCodedBillingDescriptorType69' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on hardCodedBillingDescriptorType69' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_maxTransactionAmountType70(self, value):
        result = True
        # Validate type maxTransactionAmountType70, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on maxTransactionAmountType70' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_bankRoutingNumberType71(self, value):
        result = True
        # Validate type bankRoutingNumberType71, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on bankRoutingNumberType71' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on bankRoutingNumberType71' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_bankAccountNumberType72(self, value):
        result = True
        # Validate type bankAccountNumberType72, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on bankAccountNumberType72' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on bankAccountNumberType72' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_pspMerchantIdType73(self, value):
        result = True
        # Validate type pspMerchantIdType73, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on pspMerchantIdType73' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on pspMerchantIdType73' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_purchaseCurrencyType74(self, value):
        result = True
        # Validate type purchaseCurrencyType74, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on purchaseCurrencyType74' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on purchaseCurrencyType74' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.merchantName is not None or
            self.amexMid is not None or
            self.discoverConveyedMid is not None or
            self.url is not None or
            self.customerServiceNumber is not None or
            self.hardCodedBillingDescriptor is not None or
            self.maxTransactionAmount is not None or
            self.bankRoutingNumber is not None or
            self.bankAccountNumber is not None or
            self.pspMerchantId is not None or
            self.purchaseCurrency is not None or
            self.address is not None or
            self.primaryContact is not None or
            self.disable is not None or
            self.fraud is not None or
            self.amexAcquired is not None or
            self.eCheck is not None or
            self.subMerchantFunding is not None or
            self.taxAuthority is not None or
            self.taxAuthorityState is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantUpdateRequest', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantUpdateRequest')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantUpdateRequest':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantUpdateRequest')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantUpdateRequest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantUpdateRequest'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantUpdateRequest', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.merchantName is not None:
            namespaceprefix_ = self.merchantName_nsprefix_ + ':' if (UseCapturedNS_ and self.merchantName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchantName>%s</%smerchantName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchantName), input_name='merchantName')), namespaceprefix_ , eol_))
        if self.amexMid is not None:
            namespaceprefix_ = self.amexMid_nsprefix_ + ':' if (UseCapturedNS_ and self.amexMid_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%samexMid>%s</%samexMid>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.amexMid), input_name='amexMid')), namespaceprefix_ , eol_))
        if self.discoverConveyedMid is not None:
            namespaceprefix_ = self.discoverConveyedMid_nsprefix_ + ':' if (UseCapturedNS_ and self.discoverConveyedMid_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdiscoverConveyedMid>%s</%sdiscoverConveyedMid>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.discoverConveyedMid), input_name='discoverConveyedMid')), namespaceprefix_ , eol_))
        if self.url is not None:
            namespaceprefix_ = self.url_nsprefix_ + ':' if (UseCapturedNS_ and self.url_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%surl>%s</%surl>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.url), input_name='url')), namespaceprefix_ , eol_))
        if self.customerServiceNumber is not None:
            namespaceprefix_ = self.customerServiceNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.customerServiceNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomerServiceNumber>%s</%scustomerServiceNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customerServiceNumber), input_name='customerServiceNumber')), namespaceprefix_ , eol_))
        if self.hardCodedBillingDescriptor is not None:
            namespaceprefix_ = self.hardCodedBillingDescriptor_nsprefix_ + ':' if (UseCapturedNS_ and self.hardCodedBillingDescriptor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shardCodedBillingDescriptor>%s</%shardCodedBillingDescriptor>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.hardCodedBillingDescriptor), input_name='hardCodedBillingDescriptor')), namespaceprefix_ , eol_))
        if self.maxTransactionAmount is not None:
            namespaceprefix_ = self.maxTransactionAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.maxTransactionAmount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smaxTransactionAmount>%s</%smaxTransactionAmount>%s' % (namespaceprefix_ , self.gds_format_integer(self.maxTransactionAmount, input_name='maxTransactionAmount'), namespaceprefix_ , eol_))
        if self.bankRoutingNumber is not None:
            namespaceprefix_ = self.bankRoutingNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.bankRoutingNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbankRoutingNumber>%s</%sbankRoutingNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.bankRoutingNumber), input_name='bankRoutingNumber')), namespaceprefix_ , eol_))
        if self.bankAccountNumber is not None:
            namespaceprefix_ = self.bankAccountNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.bankAccountNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbankAccountNumber>%s</%sbankAccountNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.bankAccountNumber), input_name='bankAccountNumber')), namespaceprefix_ , eol_))
        if self.pspMerchantId is not None:
            namespaceprefix_ = self.pspMerchantId_nsprefix_ + ':' if (UseCapturedNS_ and self.pspMerchantId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spspMerchantId>%s</%spspMerchantId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pspMerchantId), input_name='pspMerchantId')), namespaceprefix_ , eol_))
        if self.purchaseCurrency is not None:
            namespaceprefix_ = self.purchaseCurrency_nsprefix_ + ':' if (UseCapturedNS_ and self.purchaseCurrency_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spurchaseCurrency>%s</%spurchaseCurrency>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.purchaseCurrency), input_name='purchaseCurrency')), namespaceprefix_ , eol_))
        if self.address is not None:
            namespaceprefix_ = self.address_nsprefix_ + ':' if (UseCapturedNS_ and self.address_nsprefix_) else ''
            self.address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='address', pretty_print=pretty_print)
        if self.primaryContact is not None:
            namespaceprefix_ = self.primaryContact_nsprefix_ + ':' if (UseCapturedNS_ and self.primaryContact_nsprefix_) else ''
            self.primaryContact.export(outfile, level, namespaceprefix_, namespacedef_='', name_='primaryContact', pretty_print=pretty_print)
        if self.disable is not None:
            namespaceprefix_ = self.disable_nsprefix_ + ':' if (UseCapturedNS_ and self.disable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdisable>%s</%sdisable>%s' % (namespaceprefix_ , self.gds_format_boolean(self.disable, input_name='disable'), namespaceprefix_ , eol_))
        if self.fraud is not None:
            namespaceprefix_ = self.fraud_nsprefix_ + ':' if (UseCapturedNS_ and self.fraud_nsprefix_) else ''
            self.fraud.export(outfile, level, namespaceprefix_, namespacedef_='', name_='fraud', pretty_print=pretty_print)
        if self.amexAcquired is not None:
            namespaceprefix_ = self.amexAcquired_nsprefix_ + ':' if (UseCapturedNS_ and self.amexAcquired_nsprefix_) else ''
            self.amexAcquired.export(outfile, level, namespaceprefix_, namespacedef_='', name_='amexAcquired', pretty_print=pretty_print)
        if self.eCheck is not None:
            namespaceprefix_ = self.eCheck_nsprefix_ + ':' if (UseCapturedNS_ and self.eCheck_nsprefix_) else ''
            self.eCheck.export(outfile, level, namespaceprefix_, namespacedef_='', name_='eCheck', pretty_print=pretty_print)
        if self.subMerchantFunding is not None:
            namespaceprefix_ = self.subMerchantFunding_nsprefix_ + ':' if (UseCapturedNS_ and self.subMerchantFunding_nsprefix_) else ''
            self.subMerchantFunding.export(outfile, level, namespaceprefix_, namespacedef_='', name_='subMerchantFunding', pretty_print=pretty_print)
        if self.taxAuthority is not None:
            namespaceprefix_ = self.taxAuthority_nsprefix_ + ':' if (UseCapturedNS_ and self.taxAuthority_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxAuthority>%s</%staxAuthority>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxAuthority), input_name='taxAuthority')), namespaceprefix_ , eol_))
        if self.taxAuthorityState is not None:
            namespaceprefix_ = self.taxAuthorityState_nsprefix_ + ':' if (UseCapturedNS_ and self.taxAuthorityState_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%staxAuthorityState>%s</%staxAuthorityState>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.taxAuthorityState), input_name='taxAuthorityState')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'merchantName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchantName')
            value_ = self.gds_validate_string(value_, node, 'merchantName')
            self.merchantName = value_
            self.merchantName_nsprefix_ = child_.prefix
            # validate type merchantNameType64
            self.validate_merchantNameType64(self.merchantName)
        elif nodeName_ == 'amexMid':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'amexMid')
            value_ = self.gds_validate_string(value_, node, 'amexMid')
            self.amexMid = value_
            self.amexMid_nsprefix_ = child_.prefix
            # validate type amexMidType65
            self.validate_amexMidType65(self.amexMid)
        elif nodeName_ == 'discoverConveyedMid':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'discoverConveyedMid')
            value_ = self.gds_validate_string(value_, node, 'discoverConveyedMid')
            self.discoverConveyedMid = value_
            self.discoverConveyedMid_nsprefix_ = child_.prefix
            # validate type discoverConveyedMidType66
            self.validate_discoverConveyedMidType66(self.discoverConveyedMid)
        elif nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
            # validate type urlType67
            self.validate_urlType67(self.url)
        elif nodeName_ == 'customerServiceNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customerServiceNumber')
            value_ = self.gds_validate_string(value_, node, 'customerServiceNumber')
            self.customerServiceNumber = value_
            self.customerServiceNumber_nsprefix_ = child_.prefix
            # validate type customerServiceNumberType68
            self.validate_customerServiceNumberType68(self.customerServiceNumber)
        elif nodeName_ == 'hardCodedBillingDescriptor':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'hardCodedBillingDescriptor')
            value_ = self.gds_validate_string(value_, node, 'hardCodedBillingDescriptor')
            self.hardCodedBillingDescriptor = value_
            self.hardCodedBillingDescriptor_nsprefix_ = child_.prefix
            # validate type hardCodedBillingDescriptorType69
            self.validate_hardCodedBillingDescriptorType69(self.hardCodedBillingDescriptor)
        elif nodeName_ == 'maxTransactionAmount' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'maxTransactionAmount')
            ival_ = self.gds_validate_integer(ival_, node, 'maxTransactionAmount')
            self.maxTransactionAmount = ival_
            self.maxTransactionAmount_nsprefix_ = child_.prefix
            # validate type maxTransactionAmountType70
            self.validate_maxTransactionAmountType70(self.maxTransactionAmount)
        elif nodeName_ == 'bankRoutingNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'bankRoutingNumber')
            value_ = self.gds_validate_string(value_, node, 'bankRoutingNumber')
            self.bankRoutingNumber = value_
            self.bankRoutingNumber_nsprefix_ = child_.prefix
            # validate type bankRoutingNumberType71
            self.validate_bankRoutingNumberType71(self.bankRoutingNumber)
        elif nodeName_ == 'bankAccountNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'bankAccountNumber')
            value_ = self.gds_validate_string(value_, node, 'bankAccountNumber')
            self.bankAccountNumber = value_
            self.bankAccountNumber_nsprefix_ = child_.prefix
            # validate type bankAccountNumberType72
            self.validate_bankAccountNumberType72(self.bankAccountNumber)
        elif nodeName_ == 'pspMerchantId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pspMerchantId')
            value_ = self.gds_validate_string(value_, node, 'pspMerchantId')
            self.pspMerchantId = value_
            self.pspMerchantId_nsprefix_ = child_.prefix
            # validate type pspMerchantIdType73
            self.validate_pspMerchantIdType73(self.pspMerchantId)
        elif nodeName_ == 'purchaseCurrency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'purchaseCurrency')
            value_ = self.gds_validate_string(value_, node, 'purchaseCurrency')
            self.purchaseCurrency = value_
            self.purchaseCurrency_nsprefix_ = child_.prefix
            # validate type purchaseCurrencyType74
            self.validate_purchaseCurrencyType74(self.purchaseCurrency)
        elif nodeName_ == 'address':
            obj_ = addressUpdatable.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.address = obj_
            obj_.original_tagname_ = 'address'
        elif nodeName_ == 'primaryContact':
            obj_ = subMerchantPrimaryContactUpdatable.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.primaryContact = obj_
            obj_.original_tagname_ = 'primaryContact'
        elif nodeName_ == 'disable':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'disable')
            ival_ = self.gds_validate_boolean(ival_, node, 'disable')
            self.disable = ival_
            self.disable_nsprefix_ = child_.prefix
        elif nodeName_ == 'fraud':
            obj_ = subMerchantFraudFeature.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.fraud = obj_
            obj_.original_tagname_ = 'fraud'
        elif nodeName_ == 'amexAcquired':
            obj_ = subMerchantAmexAcquiredFeature.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.amexAcquired = obj_
            obj_.original_tagname_ = 'amexAcquired'
        elif nodeName_ == 'eCheck':
            obj_ = subMerchantECheckFeature.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.eCheck = obj_
            obj_.original_tagname_ = 'eCheck'
        elif nodeName_ == 'subMerchantFunding':
            obj_ = subMerchantFunding.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.subMerchantFunding = obj_
            obj_.original_tagname_ = 'subMerchantFunding'
        elif nodeName_ == 'taxAuthority':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxAuthority')
            value_ = self.gds_validate_string(value_, node, 'taxAuthority')
            self.taxAuthority = value_
            self.taxAuthority_nsprefix_ = child_.prefix
        elif nodeName_ == 'taxAuthorityState':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxAuthorityState')
            value_ = self.gds_validate_string(value_, node, 'taxAuthorityState')
            self.taxAuthorityState = value_
            self.taxAuthorityState_nsprefix_ = child_.prefix
# end class subMerchantUpdateRequest


class subMerchantPrimaryContactUpdatable(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, firstName=None, lastName=None, emailAddress=None, phone=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.firstName = firstName
        self.validate_firstNameType75(self.firstName)
        self.firstName_nsprefix_ = None
        self.lastName = lastName
        self.validate_lastNameType76(self.lastName)
        self.lastName_nsprefix_ = None
        self.emailAddress = emailAddress
        self.validate_emailAddressType77(self.emailAddress)
        self.emailAddress_nsprefix_ = None
        self.phone = phone
        self.validate_phoneType78(self.phone)
        self.phone_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, subMerchantPrimaryContactUpdatable)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if subMerchantPrimaryContactUpdatable.subclass:
            return subMerchantPrimaryContactUpdatable.subclass(*args_, **kwargs_)
        else:
            return subMerchantPrimaryContactUpdatable(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_firstName(self):
        return self.firstName
    def set_firstName(self, firstName):
        self.firstName = firstName
    def get_lastName(self):
        return self.lastName
    def set_lastName(self, lastName):
        self.lastName = lastName
    def get_emailAddress(self):
        return self.emailAddress
    def set_emailAddress(self, emailAddress):
        self.emailAddress = emailAddress
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def validate_firstNameType75(self, value):
        result = True
        # Validate type firstNameType75, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on firstNameType75' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on firstNameType75' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_lastNameType76(self, value):
        result = True
        # Validate type lastNameType76, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on lastNameType76' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on lastNameType76' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_emailAddressType77(self, value):
        result = True
        # Validate type emailAddressType77, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on emailAddressType77' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on emailAddressType77' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_phoneType78(self, value):
        result = True
        # Validate type phoneType78, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 13:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on phoneType78' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on phoneType78' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.firstName is not None or
            self.lastName is not None or
            self.emailAddress is not None or
            self.phone is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantPrimaryContactUpdatable', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('subMerchantPrimaryContactUpdatable')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'subMerchantPrimaryContactUpdatable':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='subMerchantPrimaryContactUpdatable')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='subMerchantPrimaryContactUpdatable', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='subMerchantPrimaryContactUpdatable'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='subMerchantPrimaryContactUpdatable', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.firstName is not None:
            namespaceprefix_ = self.firstName_nsprefix_ + ':' if (UseCapturedNS_ and self.firstName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfirstName>%s</%sfirstName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.firstName), input_name='firstName')), namespaceprefix_ , eol_))
        if self.lastName is not None:
            namespaceprefix_ = self.lastName_nsprefix_ + ':' if (UseCapturedNS_ and self.lastName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slastName>%s</%slastName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lastName), input_name='lastName')), namespaceprefix_ , eol_))
        if self.emailAddress is not None:
            namespaceprefix_ = self.emailAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.emailAddress_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%semailAddress>%s</%semailAddress>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.emailAddress), input_name='emailAddress')), namespaceprefix_ , eol_))
        if self.phone is not None:
            namespaceprefix_ = self.phone_nsprefix_ + ':' if (UseCapturedNS_ and self.phone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sphone>%s</%sphone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.phone), input_name='phone')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'firstName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firstName')
            value_ = self.gds_validate_string(value_, node, 'firstName')
            self.firstName = value_
            self.firstName_nsprefix_ = child_.prefix
            # validate type firstNameType75
            self.validate_firstNameType75(self.firstName)
        elif nodeName_ == 'lastName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lastName')
            value_ = self.gds_validate_string(value_, node, 'lastName')
            self.lastName = value_
            self.lastName_nsprefix_ = child_.prefix
            # validate type lastNameType76
            self.validate_lastNameType76(self.lastName)
        elif nodeName_ == 'emailAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'emailAddress')
            value_ = self.gds_validate_string(value_, node, 'emailAddress')
            self.emailAddress = value_
            self.emailAddress_nsprefix_ = child_.prefix
            # validate type emailAddressType77
            self.validate_emailAddressType77(self.emailAddress)
        elif nodeName_ == 'phone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'phone')
            value_ = self.gds_validate_string(value_, node, 'phone')
            self.phone = value_
            self.phone_nsprefix_ = child_.prefix
            # validate type phoneType78
            self.validate_phoneType78(self.phone)
# end class subMerchantPrimaryContactUpdatable


class errorResponse(response):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = response
    def __init__(self, transactionId=None, errors=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(errorResponse, self).__init__(transactionId,  **kwargs_)
        self.errors = errors
        self.errors_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, errorResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if errorResponse.subclass:
            return errorResponse.subclass(*args_, **kwargs_)
        else:
            return errorResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_errors(self):
        return self.errors
    def set_errors(self, errors):
        self.errors = errors
    def hasContent_(self):
        if (
            self.errors is not None or
            super(errorResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='errorResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('errorResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'errorResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='errorResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='errorResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='errorResponse'):
        super(errorResponse, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='errorResponse')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='errorResponse', fromsubclass_=False, pretty_print=True):
        super(errorResponse, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.errors is not None:
            namespaceprefix_ = self.errors_nsprefix_ + ':' if (UseCapturedNS_ and self.errors_nsprefix_) else ''
            self.errors.export(outfile, level, namespaceprefix_, namespacedef_='', name_='errors', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(errorResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'errors':
            obj_ = errorsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.errors = obj_
            obj_.original_tagname_ = 'errors'
        super(errorResponse, self).buildChildren(child_, node, nodeName_, True)
# end class errorResponse


class approvedMccResponse(response):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = response
    def __init__(self, transactionId=None, approvedMccs=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(approvedMccResponse, self).__init__(transactionId,  **kwargs_)
        self.approvedMccs = approvedMccs
        self.approvedMccs_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, approvedMccResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if approvedMccResponse.subclass:
            return approvedMccResponse.subclass(*args_, **kwargs_)
        else:
            return approvedMccResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_approvedMccs(self):
        return self.approvedMccs
    def set_approvedMccs(self, approvedMccs):
        self.approvedMccs = approvedMccs
    def hasContent_(self):
        if (
            self.approvedMccs is not None or
            super(approvedMccResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='approvedMccResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('approvedMccResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'approvedMccResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='approvedMccResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='approvedMccResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='approvedMccResponse'):
        super(approvedMccResponse, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='approvedMccResponse')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='approvedMccResponse', fromsubclass_=False, pretty_print=True):
        super(approvedMccResponse, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.approvedMccs is not None:
            namespaceprefix_ = self.approvedMccs_nsprefix_ + ':' if (UseCapturedNS_ and self.approvedMccs_nsprefix_) else ''
            self.approvedMccs.export(outfile, level, namespaceprefix_, namespacedef_='', name_='approvedMccs', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(approvedMccResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'approvedMccs':
            obj_ = approvedMccsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.approvedMccs = obj_
            obj_.original_tagname_ = 'approvedMccs'
        super(approvedMccResponse, self).buildChildren(child_, node, nodeName_, True)
# end class approvedMccResponse


class legalEntityAgreementCreateRequest(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, legalEntityAgreement=None, sdkVersion=None, language=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.legalEntityAgreement = legalEntityAgreement
        self.legalEntityAgreement_nsprefix_ = None
        self.sdkVersion = sdkVersion
        self.validate_sdkVersionType79(self.sdkVersion)
        self.sdkVersion_nsprefix_ = None
        self.language = language
        self.validate_languageType80(self.language)
        self.language_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityAgreementCreateRequest)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityAgreementCreateRequest.subclass:
            return legalEntityAgreementCreateRequest.subclass(*args_, **kwargs_)
        else:
            return legalEntityAgreementCreateRequest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_legalEntityAgreement(self):
        return self.legalEntityAgreement
    def set_legalEntityAgreement(self, legalEntityAgreement):
        self.legalEntityAgreement = legalEntityAgreement
    def get_sdkVersion(self):
        return self.sdkVersion
    def set_sdkVersion(self, sdkVersion):
        self.sdkVersion = sdkVersion
    def get_language(self):
        return self.language
    def set_language(self, language):
        self.language = language
    def validate_sdkVersionType79(self, value):
        result = True
        # Validate type sdkVersionType79, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on sdkVersionType79' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on sdkVersionType79' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_sdkVersionType79_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_sdkVersionType79_patterns_, ))
                result = False
        return result
    validate_sdkVersionType79_patterns_ = [[u'^([\x00-\x7f]*)$']]
    def validate_languageType80(self, value):
        result = True
        # Validate type languageType80, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on languageType80' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on languageType80' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_languageType80_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_languageType80_patterns_, ))
                result = False
        return result
    validate_languageType80_patterns_ = [[u'^([\x00-\x7f]*)$']]
    def hasContent_(self):
        if (
            self.legalEntityAgreement is not None or
            self.sdkVersion is not None or
            self.language is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityAgreementCreateRequest', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityAgreementCreateRequest')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityAgreementCreateRequest':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityAgreementCreateRequest')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityAgreementCreateRequest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityAgreementCreateRequest'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityAgreementCreateRequest', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.legalEntityAgreement is not None:
            namespaceprefix_ = self.legalEntityAgreement_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityAgreement_nsprefix_) else ''
            self.legalEntityAgreement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='legalEntityAgreement', pretty_print=pretty_print)
        if self.sdkVersion is not None:
            namespaceprefix_ = self.sdkVersion_nsprefix_ + ':' if (UseCapturedNS_ and self.sdkVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssdkVersion>%s</%ssdkVersion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.sdkVersion), input_name='sdkVersion')), namespaceprefix_ , eol_))
        if self.language is not None:
            namespaceprefix_ = self.language_nsprefix_ + ':' if (UseCapturedNS_ and self.language_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slanguage>%s</%slanguage>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.language), input_name='language')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityAgreement':
            obj_ = legalEntityAgreement.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.legalEntityAgreement = obj_
            obj_.original_tagname_ = 'legalEntityAgreement'
        elif nodeName_ == 'sdkVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'sdkVersion')
            value_ = self.gds_validate_string(value_, node, 'sdkVersion')
            self.sdkVersion = value_
            self.sdkVersion_nsprefix_ = child_.prefix
            # validate type sdkVersionType79
            self.validate_sdkVersionType79(self.sdkVersion)
        elif nodeName_ == 'language':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'language')
            value_ = self.gds_validate_string(value_, node, 'language')
            self.language = value_
            self.language_nsprefix_ = child_.prefix
            # validate type languageType80
            self.validate_languageType80(self.language)
# end class legalEntityAgreementCreateRequest


class legalEntityAgreement(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, legalEntityAgreementType=None, agreementVersion=None, userFullName=None, userSystemName=None, userIPAddress=None, manuallyEntered=None, acceptanceDateTime=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.legalEntityAgreementType = legalEntityAgreementType
        self.validate_legalEntityAgreementType(self.legalEntityAgreementType)
        self.legalEntityAgreementType_nsprefix_ = None
        self.agreementVersion = agreementVersion
        self.validate_agreementVersionType(self.agreementVersion)
        self.agreementVersion_nsprefix_ = None
        self.userFullName = userFullName
        self.validate_userFullNameType(self.userFullName)
        self.userFullName_nsprefix_ = None
        self.userSystemName = userSystemName
        self.validate_userSystemNameType(self.userSystemName)
        self.userSystemName_nsprefix_ = None
        self.userIPAddress = userIPAddress
        self.validate_userIPAddressType(self.userIPAddress)
        self.userIPAddress_nsprefix_ = None
        self.manuallyEntered = manuallyEntered
        self.manuallyEntered_nsprefix_ = None
        if isinstance(acceptanceDateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(acceptanceDateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = acceptanceDateTime
        self.acceptanceDateTime = initvalue_
        self.acceptanceDateTime_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityAgreement)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityAgreement.subclass:
            return legalEntityAgreement.subclass(*args_, **kwargs_)
        else:
            return legalEntityAgreement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_legalEntityAgreementType(self):
        return self.legalEntityAgreementType
    def set_legalEntityAgreementType(self, legalEntityAgreementType):
        self.legalEntityAgreementType = legalEntityAgreementType
    def get_agreementVersion(self):
        return self.agreementVersion
    def set_agreementVersion(self, agreementVersion):
        self.agreementVersion = agreementVersion
    def get_userFullName(self):
        return self.userFullName
    def set_userFullName(self, userFullName):
        self.userFullName = userFullName
    def get_userSystemName(self):
        return self.userSystemName
    def set_userSystemName(self, userSystemName):
        self.userSystemName = userSystemName
    def get_userIPAddress(self):
        return self.userIPAddress
    def set_userIPAddress(self, userIPAddress):
        self.userIPAddress = userIPAddress
    def get_manuallyEntered(self):
        return self.manuallyEntered
    def set_manuallyEntered(self, manuallyEntered):
        self.manuallyEntered = manuallyEntered
    def get_acceptanceDateTime(self):
        return self.acceptanceDateTime
    def set_acceptanceDateTime(self, acceptanceDateTime):
        self.acceptanceDateTime = acceptanceDateTime
    def validate_legalEntityAgreementType(self, value):
        result = True
        # Validate type legalEntityAgreementType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['MERCHANT_AGREEMENT']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on legalEntityAgreementType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_agreementVersionType(self, value):
        result = True
        # Validate type agreementVersionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on agreementVersionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on agreementVersionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_userFullNameType(self, value):
        result = True
        # Validate type userFullNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on userFullNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on userFullNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_userSystemNameType(self, value):
        result = True
        # Validate type userSystemNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on userSystemNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on userSystemNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_userIPAddressType(self, value):
        result = True
        # Validate type userIPAddressType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on userIPAddressType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on userIPAddressType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_userIPAddressType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_userIPAddressType_patterns_, ))
                result = False
        return result
    validate_userIPAddressType_patterns_ = [[u'^(([a-zA-Z0-9.:])*)$']]
    def hasContent_(self):
        if (
            self.legalEntityAgreementType is not None or
            self.agreementVersion is not None or
            self.userFullName is not None or
            self.userSystemName is not None or
            self.userIPAddress is not None or
            self.manuallyEntered is not None or
            self.acceptanceDateTime is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityAgreement', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityAgreement')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityAgreement':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityAgreement')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityAgreement', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityAgreement'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityAgreement', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.legalEntityAgreementType is not None:
            namespaceprefix_ = self.legalEntityAgreementType_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityAgreementType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityAgreementType>%s</%slegalEntityAgreementType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityAgreementType), input_name='legalEntityAgreementType')), namespaceprefix_ , eol_))
        if self.agreementVersion is not None:
            namespaceprefix_ = self.agreementVersion_nsprefix_ + ':' if (UseCapturedNS_ and self.agreementVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sagreementVersion>%s</%sagreementVersion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.agreementVersion), input_name='agreementVersion')), namespaceprefix_ , eol_))
        if self.userFullName is not None:
            namespaceprefix_ = self.userFullName_nsprefix_ + ':' if (UseCapturedNS_ and self.userFullName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suserFullName>%s</%suserFullName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.userFullName), input_name='userFullName')), namespaceprefix_ , eol_))
        if self.userSystemName is not None:
            namespaceprefix_ = self.userSystemName_nsprefix_ + ':' if (UseCapturedNS_ and self.userSystemName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suserSystemName>%s</%suserSystemName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.userSystemName), input_name='userSystemName')), namespaceprefix_ , eol_))
        if self.userIPAddress is not None:
            namespaceprefix_ = self.userIPAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.userIPAddress_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suserIPAddress>%s</%suserIPAddress>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.userIPAddress), input_name='userIPAddress')), namespaceprefix_ , eol_))
        if self.manuallyEntered is not None:
            namespaceprefix_ = self.manuallyEntered_nsprefix_ + ':' if (UseCapturedNS_ and self.manuallyEntered_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smanuallyEntered>%s</%smanuallyEntered>%s' % (namespaceprefix_ , self.gds_format_boolean(self.manuallyEntered, input_name='manuallyEntered'), namespaceprefix_ , eol_))
        if self.acceptanceDateTime is not None:
            namespaceprefix_ = self.acceptanceDateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.acceptanceDateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sacceptanceDateTime>%s</%sacceptanceDateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.acceptanceDateTime, input_name='acceptanceDateTime'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityAgreementType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityAgreementType')
            value_ = self.gds_validate_string(value_, node, 'legalEntityAgreementType')
            self.legalEntityAgreementType = value_
            self.legalEntityAgreementType_nsprefix_ = child_.prefix
            # validate type legalEntityAgreementType
            self.validate_legalEntityAgreementType(self.legalEntityAgreementType)
        elif nodeName_ == 'agreementVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'agreementVersion')
            value_ = self.gds_validate_string(value_, node, 'agreementVersion')
            self.agreementVersion = value_
            self.agreementVersion_nsprefix_ = child_.prefix
            # validate type agreementVersionType
            self.validate_agreementVersionType(self.agreementVersion)
        elif nodeName_ == 'userFullName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'userFullName')
            value_ = self.gds_validate_string(value_, node, 'userFullName')
            self.userFullName = value_
            self.userFullName_nsprefix_ = child_.prefix
            # validate type userFullNameType
            self.validate_userFullNameType(self.userFullName)
        elif nodeName_ == 'userSystemName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'userSystemName')
            value_ = self.gds_validate_string(value_, node, 'userSystemName')
            self.userSystemName = value_
            self.userSystemName_nsprefix_ = child_.prefix
            # validate type userSystemNameType
            self.validate_userSystemNameType(self.userSystemName)
        elif nodeName_ == 'userIPAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'userIPAddress')
            value_ = self.gds_validate_string(value_, node, 'userIPAddress')
            self.userIPAddress = value_
            self.userIPAddress_nsprefix_ = child_.prefix
            # validate type userIPAddressType
            self.validate_userIPAddressType(self.userIPAddress)
        elif nodeName_ == 'manuallyEntered':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'manuallyEntered')
            ival_ = self.gds_validate_boolean(ival_, node, 'manuallyEntered')
            self.manuallyEntered = ival_
            self.manuallyEntered_nsprefix_ = child_.prefix
        elif nodeName_ == 'acceptanceDateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.acceptanceDateTime = dval_
            self.acceptanceDateTime_nsprefix_ = child_.prefix
# end class legalEntityAgreement


class legalEntityAgreementCreateResponse(response):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = response
    def __init__(self, transactionId=None, duplicate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(legalEntityAgreementCreateResponse, self).__init__(transactionId,  **kwargs_)
        self.duplicate = _cast(bool, duplicate)
        self.duplicate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityAgreementCreateResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityAgreementCreateResponse.subclass:
            return legalEntityAgreementCreateResponse.subclass(*args_, **kwargs_)
        else:
            return legalEntityAgreementCreateResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_duplicate(self):
        return self.duplicate
    def set_duplicate(self, duplicate):
        self.duplicate = duplicate
    def hasContent_(self):
        if (
            super(legalEntityAgreementCreateResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityAgreementCreateResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityAgreementCreateResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityAgreementCreateResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityAgreementCreateResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityAgreementCreateResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityAgreementCreateResponse'):
        super(legalEntityAgreementCreateResponse, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityAgreementCreateResponse')
        if self.duplicate is not None and 'duplicate' not in already_processed:
            already_processed.add('duplicate')
            outfile.write(' duplicate="%s"' % self.gds_format_boolean(self.duplicate, input_name='duplicate'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityAgreementCreateResponse', fromsubclass_=False, pretty_print=True):
        super(legalEntityAgreementCreateResponse, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('duplicate', node)
        if value is not None and 'duplicate' not in already_processed:
            already_processed.add('duplicate')
            if value in ('true', '1'):
                self.duplicate = True
            elif value in ('false', '0'):
                self.duplicate = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(legalEntityAgreementCreateResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(legalEntityAgreementCreateResponse, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class legalEntityAgreementCreateResponse


class legalEntityAgreementRetrievalResponse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, legalEntityId=None, transactionId=None, agreements=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.legalEntityId = legalEntityId
        self.validate_legalEntityIdType81(self.legalEntityId)
        self.legalEntityId_nsprefix_ = None
        self.transactionId = transactionId
        self.transactionId_nsprefix_ = None
        self.agreements = agreements
        self.agreements_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityAgreementRetrievalResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityAgreementRetrievalResponse.subclass:
            return legalEntityAgreementRetrievalResponse.subclass(*args_, **kwargs_)
        else:
            return legalEntityAgreementRetrievalResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_legalEntityId(self):
        return self.legalEntityId
    def set_legalEntityId(self, legalEntityId):
        self.legalEntityId = legalEntityId
    def get_transactionId(self):
        return self.transactionId
    def set_transactionId(self, transactionId):
        self.transactionId = transactionId
    def get_agreements(self):
        return self.agreements
    def set_agreements(self, agreements):
        self.agreements = agreements
    def validate_legalEntityIdType81(self, value):
        result = True
        # Validate type legalEntityIdType81, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on legalEntityIdType81' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on legalEntityIdType81' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.legalEntityId is not None or
            self.transactionId is not None or
            self.agreements is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityAgreementRetrievalResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityAgreementRetrievalResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityAgreementRetrievalResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityAgreementRetrievalResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityAgreementRetrievalResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityAgreementRetrievalResponse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityAgreementRetrievalResponse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.legalEntityId is not None:
            namespaceprefix_ = self.legalEntityId_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityId>%s</%slegalEntityId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityId), input_name='legalEntityId')), namespaceprefix_ , eol_))
        if self.transactionId is not None:
            namespaceprefix_ = self.transactionId_nsprefix_ + ':' if (UseCapturedNS_ and self.transactionId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransactionId>%s</%stransactionId>%s' % (namespaceprefix_ , self.gds_format_integer(self.transactionId, input_name='transactionId'), namespaceprefix_ , eol_))
        if self.agreements is not None:
            namespaceprefix_ = self.agreements_nsprefix_ + ':' if (UseCapturedNS_ and self.agreements_nsprefix_) else ''
            self.agreements.export(outfile, level, namespaceprefix_, namespacedef_='', name_='agreements', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityId')
            value_ = self.gds_validate_string(value_, node, 'legalEntityId')
            self.legalEntityId = value_
            self.legalEntityId_nsprefix_ = child_.prefix
            # validate type legalEntityIdType81
            self.validate_legalEntityIdType81(self.legalEntityId)
        elif nodeName_ == 'transactionId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'transactionId')
            ival_ = self.gds_validate_integer(ival_, node, 'transactionId')
            self.transactionId = ival_
            self.transactionId_nsprefix_ = child_.prefix
        elif nodeName_ == 'agreements':
            obj_ = agreementsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.agreements = obj_
            obj_.original_tagname_ = 'agreements'
# end class legalEntityAgreementRetrievalResponse


class legalEntityPrincipalDeleteResponse(response):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = response
    def __init__(self, transactionId=None, legalEntityId=None, principalId=None, responseDescription=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(legalEntityPrincipalDeleteResponse, self).__init__(transactionId,  **kwargs_)
        self.legalEntityId = legalEntityId
        self.validate_legalEntityIdType82(self.legalEntityId)
        self.legalEntityId_nsprefix_ = None
        self.principalId = principalId
        self.principalId_nsprefix_ = None
        self.responseDescription = responseDescription
        self.validate_responseDescriptionType83(self.responseDescription)
        self.responseDescription_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityPrincipalDeleteResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityPrincipalDeleteResponse.subclass:
            return legalEntityPrincipalDeleteResponse.subclass(*args_, **kwargs_)
        else:
            return legalEntityPrincipalDeleteResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_legalEntityId(self):
        return self.legalEntityId
    def set_legalEntityId(self, legalEntityId):
        self.legalEntityId = legalEntityId
    def get_principalId(self):
        return self.principalId
    def set_principalId(self, principalId):
        self.principalId = principalId
    def get_responseDescription(self):
        return self.responseDescription
    def set_responseDescription(self, responseDescription):
        self.responseDescription = responseDescription
    def validate_legalEntityIdType82(self, value):
        result = True
        # Validate type legalEntityIdType82, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on legalEntityIdType82' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on legalEntityIdType82' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_responseDescriptionType83(self, value):
        result = True
        # Validate type responseDescriptionType83, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on responseDescriptionType83' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on responseDescriptionType83' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.legalEntityId is not None or
            self.principalId is not None or
            self.responseDescription is not None or
            super(legalEntityPrincipalDeleteResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipalDeleteResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityPrincipalDeleteResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityPrincipalDeleteResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityPrincipalDeleteResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityPrincipalDeleteResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityPrincipalDeleteResponse'):
        super(legalEntityPrincipalDeleteResponse, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityPrincipalDeleteResponse')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipalDeleteResponse', fromsubclass_=False, pretty_print=True):
        super(legalEntityPrincipalDeleteResponse, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.legalEntityId is not None:
            namespaceprefix_ = self.legalEntityId_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityId>%s</%slegalEntityId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityId), input_name='legalEntityId')), namespaceprefix_ , eol_))
        if self.principalId is not None:
            namespaceprefix_ = self.principalId_nsprefix_ + ':' if (UseCapturedNS_ and self.principalId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprincipalId>%s</%sprincipalId>%s' % (namespaceprefix_ , self.gds_format_integer(self.principalId, input_name='principalId'), namespaceprefix_ , eol_))
        if self.responseDescription is not None:
            namespaceprefix_ = self.responseDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.responseDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sresponseDescription>%s</%sresponseDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.responseDescription), input_name='responseDescription')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(legalEntityPrincipalDeleteResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityId')
            value_ = self.gds_validate_string(value_, node, 'legalEntityId')
            self.legalEntityId = value_
            self.legalEntityId_nsprefix_ = child_.prefix
            # validate type legalEntityIdType82
            self.validate_legalEntityIdType82(self.legalEntityId)
        elif nodeName_ == 'principalId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'principalId')
            ival_ = self.gds_validate_integer(ival_, node, 'principalId')
            self.principalId = ival_
            self.principalId_nsprefix_ = child_.prefix
        elif nodeName_ == 'responseDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'responseDescription')
            value_ = self.gds_validate_string(value_, node, 'responseDescription')
            self.responseDescription = value_
            self.responseDescription_nsprefix_ = child_.prefix
            # validate type responseDescriptionType83
            self.validate_responseDescriptionType83(self.responseDescription)
        super(legalEntityPrincipalDeleteResponse, self).buildChildren(child_, node, nodeName_, True)
# end class legalEntityPrincipalDeleteResponse


class legalEntityPrincipalCreateResponseWithResponseFields(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, principalId=None, firstName=None, lastName=None, responseCode=None, responseDescription=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.principalId = principalId
        self.principalId_nsprefix_ = None
        self.firstName = firstName
        self.validate_firstNameType84(self.firstName)
        self.firstName_nsprefix_ = None
        self.lastName = lastName
        self.validate_lastNameType85(self.lastName)
        self.lastName_nsprefix_ = None
        self.responseCode = responseCode
        self.responseCode_nsprefix_ = None
        self.responseDescription = responseDescription
        self.validate_responseDescriptionType86(self.responseDescription)
        self.responseDescription_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityPrincipalCreateResponseWithResponseFields)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityPrincipalCreateResponseWithResponseFields.subclass:
            return legalEntityPrincipalCreateResponseWithResponseFields.subclass(*args_, **kwargs_)
        else:
            return legalEntityPrincipalCreateResponseWithResponseFields(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_principalId(self):
        return self.principalId
    def set_principalId(self, principalId):
        self.principalId = principalId
    def get_firstName(self):
        return self.firstName
    def set_firstName(self, firstName):
        self.firstName = firstName
    def get_lastName(self):
        return self.lastName
    def set_lastName(self, lastName):
        self.lastName = lastName
    def get_responseCode(self):
        return self.responseCode
    def set_responseCode(self, responseCode):
        self.responseCode = responseCode
    def get_responseDescription(self):
        return self.responseDescription
    def set_responseDescription(self, responseDescription):
        self.responseDescription = responseDescription
    def validate_firstNameType84(self, value):
        result = True
        # Validate type firstNameType84, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on firstNameType84' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on firstNameType84' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_lastNameType85(self, value):
        result = True
        # Validate type lastNameType85, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on lastNameType85' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on lastNameType85' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_responseDescriptionType86(self, value):
        result = True
        # Validate type responseDescriptionType86, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on responseDescriptionType86' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on responseDescriptionType86' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.principalId is not None or
            self.firstName is not None or
            self.lastName is not None or
            self.responseCode is not None or
            self.responseDescription is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipalCreateResponseWithResponseFields', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityPrincipalCreateResponseWithResponseFields')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityPrincipalCreateResponseWithResponseFields':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityPrincipalCreateResponseWithResponseFields')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityPrincipalCreateResponseWithResponseFields', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityPrincipalCreateResponseWithResponseFields'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='legalEntityPrincipalCreateResponseWithResponseFields', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.principalId is not None:
            namespaceprefix_ = self.principalId_nsprefix_ + ':' if (UseCapturedNS_ and self.principalId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprincipalId>%s</%sprincipalId>%s' % (namespaceprefix_ , self.gds_format_integer(self.principalId, input_name='principalId'), namespaceprefix_ , eol_))
        if self.firstName is not None:
            namespaceprefix_ = self.firstName_nsprefix_ + ':' if (UseCapturedNS_ and self.firstName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfirstName>%s</%sfirstName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.firstName), input_name='firstName')), namespaceprefix_ , eol_))
        if self.lastName is not None:
            namespaceprefix_ = self.lastName_nsprefix_ + ':' if (UseCapturedNS_ and self.lastName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slastName>%s</%slastName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.lastName), input_name='lastName')), namespaceprefix_ , eol_))
        if self.responseCode is not None:
            namespaceprefix_ = self.responseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.responseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sresponseCode>%s</%sresponseCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.responseCode, input_name='responseCode'), namespaceprefix_ , eol_))
        if self.responseDescription is not None:
            namespaceprefix_ = self.responseDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.responseDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sresponseDescription>%s</%sresponseDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.responseDescription), input_name='responseDescription')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'principalId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'principalId')
            ival_ = self.gds_validate_integer(ival_, node, 'principalId')
            self.principalId = ival_
            self.principalId_nsprefix_ = child_.prefix
        elif nodeName_ == 'firstName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firstName')
            value_ = self.gds_validate_string(value_, node, 'firstName')
            self.firstName = value_
            self.firstName_nsprefix_ = child_.prefix
            # validate type firstNameType84
            self.validate_firstNameType84(self.firstName)
        elif nodeName_ == 'lastName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lastName')
            value_ = self.gds_validate_string(value_, node, 'lastName')
            self.lastName = value_
            self.lastName_nsprefix_ = child_.prefix
            # validate type lastNameType85
            self.validate_lastNameType85(self.lastName)
        elif nodeName_ == 'responseCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'responseCode')
            ival_ = self.gds_validate_integer(ival_, node, 'responseCode')
            self.responseCode = ival_
            self.responseCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'responseDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'responseDescription')
            value_ = self.gds_validate_string(value_, node, 'responseDescription')
            self.responseDescription = value_
            self.responseDescription_nsprefix_ = child_.prefix
            # validate type responseDescriptionType86
            self.validate_responseDescriptionType86(self.responseDescription)
# end class legalEntityPrincipalCreateResponseWithResponseFields


class principalCreateResponse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, legalEntityId=None, principal=None, transactionId=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.legalEntityId = legalEntityId
        self.validate_legalEntityIdType87(self.legalEntityId)
        self.legalEntityId_nsprefix_ = None
        self.principal = principal
        self.principal_nsprefix_ = None
        self.transactionId = transactionId
        self.transactionId_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, principalCreateResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if principalCreateResponse.subclass:
            return principalCreateResponse.subclass(*args_, **kwargs_)
        else:
            return principalCreateResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_legalEntityId(self):
        return self.legalEntityId
    def set_legalEntityId(self, legalEntityId):
        self.legalEntityId = legalEntityId
    def get_principal(self):
        return self.principal
    def set_principal(self, principal):
        self.principal = principal
    def get_transactionId(self):
        return self.transactionId
    def set_transactionId(self, transactionId):
        self.transactionId = transactionId
    def validate_legalEntityIdType87(self, value):
        result = True
        # Validate type legalEntityIdType87, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on legalEntityIdType87' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on legalEntityIdType87' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.legalEntityId is not None or
            self.principal is not None or
            self.transactionId is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalCreateResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('principalCreateResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'principalCreateResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='principalCreateResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='principalCreateResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='principalCreateResponse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalCreateResponse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.legalEntityId is not None:
            namespaceprefix_ = self.legalEntityId_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityId>%s</%slegalEntityId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityId), input_name='legalEntityId')), namespaceprefix_ , eol_))
        if self.principal is not None:
            namespaceprefix_ = self.principal_nsprefix_ + ':' if (UseCapturedNS_ and self.principal_nsprefix_) else ''
            self.principal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='principal', pretty_print=pretty_print)
        if self.transactionId is not None:
            namespaceprefix_ = self.transactionId_nsprefix_ + ':' if (UseCapturedNS_ and self.transactionId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransactionId>%s</%stransactionId>%s' % (namespaceprefix_ , self.gds_format_integer(self.transactionId, input_name='transactionId'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityId')
            value_ = self.gds_validate_string(value_, node, 'legalEntityId')
            self.legalEntityId = value_
            self.legalEntityId_nsprefix_ = child_.prefix
            # validate type legalEntityIdType87
            self.validate_legalEntityIdType87(self.legalEntityId)
        elif nodeName_ == 'principal':
            obj_ = legalEntityPrincipalCreateResponseWithResponseFields.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.principal = obj_
            obj_.original_tagname_ = 'principal'
        elif nodeName_ == 'transactionId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'transactionId')
            ival_ = self.gds_validate_integer(ival_, node, 'transactionId')
            self.transactionId = ival_
            self.transactionId_nsprefix_ = child_.prefix
# end class principalCreateResponse


class principalDeleteResponse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, transactionId=None, legalEntityId=None, principalId=None, responseDescription=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.transactionId = transactionId
        self.transactionId_nsprefix_ = None
        self.legalEntityId = legalEntityId
        self.validate_legalEntityIdType88(self.legalEntityId)
        self.legalEntityId_nsprefix_ = None
        self.principalId = principalId
        self.principalId_nsprefix_ = None
        self.responseDescription = responseDescription
        self.validate_responseDescriptionType89(self.responseDescription)
        self.responseDescription_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, principalDeleteResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if principalDeleteResponse.subclass:
            return principalDeleteResponse.subclass(*args_, **kwargs_)
        else:
            return principalDeleteResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_transactionId(self):
        return self.transactionId
    def set_transactionId(self, transactionId):
        self.transactionId = transactionId
    def get_legalEntityId(self):
        return self.legalEntityId
    def set_legalEntityId(self, legalEntityId):
        self.legalEntityId = legalEntityId
    def get_principalId(self):
        return self.principalId
    def set_principalId(self, principalId):
        self.principalId = principalId
    def get_responseDescription(self):
        return self.responseDescription
    def set_responseDescription(self, responseDescription):
        self.responseDescription = responseDescription
    def validate_legalEntityIdType88(self, value):
        result = True
        # Validate type legalEntityIdType88, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on legalEntityIdType88' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on legalEntityIdType88' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_responseDescriptionType89(self, value):
        result = True
        # Validate type responseDescriptionType89, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on responseDescriptionType89' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on responseDescriptionType89' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.transactionId is not None or
            self.legalEntityId is not None or
            self.principalId is not None or
            self.responseDescription is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalDeleteResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('principalDeleteResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'principalDeleteResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='principalDeleteResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='principalDeleteResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='principalDeleteResponse'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='principalDeleteResponse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.transactionId is not None:
            namespaceprefix_ = self.transactionId_nsprefix_ + ':' if (UseCapturedNS_ and self.transactionId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransactionId>%s</%stransactionId>%s' % (namespaceprefix_ , self.gds_format_integer(self.transactionId, input_name='transactionId'), namespaceprefix_ , eol_))
        if self.legalEntityId is not None:
            namespaceprefix_ = self.legalEntityId_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityId>%s</%slegalEntityId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityId), input_name='legalEntityId')), namespaceprefix_ , eol_))
        if self.principalId is not None:
            namespaceprefix_ = self.principalId_nsprefix_ + ':' if (UseCapturedNS_ and self.principalId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprincipalId>%s</%sprincipalId>%s' % (namespaceprefix_ , self.gds_format_integer(self.principalId, input_name='principalId'), namespaceprefix_ , eol_))
        if self.responseDescription is not None:
            namespaceprefix_ = self.responseDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.responseDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sresponseDescription>%s</%sresponseDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.responseDescription), input_name='responseDescription')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'transactionId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'transactionId')
            ival_ = self.gds_validate_integer(ival_, node, 'transactionId')
            self.transactionId = ival_
            self.transactionId_nsprefix_ = child_.prefix
        elif nodeName_ == 'legalEntityId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityId')
            value_ = self.gds_validate_string(value_, node, 'legalEntityId')
            self.legalEntityId = value_
            self.legalEntityId_nsprefix_ = child_.prefix
            # validate type legalEntityIdType88
            self.validate_legalEntityIdType88(self.legalEntityId)
        elif nodeName_ == 'principalId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'principalId')
            ival_ = self.gds_validate_integer(ival_, node, 'principalId')
            self.principalId = ival_
            self.principalId_nsprefix_ = child_.prefix
        elif nodeName_ == 'responseDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'responseDescription')
            value_ = self.gds_validate_string(value_, node, 'responseDescription')
            self.responseDescription = value_
            self.responseDescription_nsprefix_ = child_.prefix
            # validate type responseDescriptionType89
            self.validate_responseDescriptionType89(self.responseDescription)
# end class principalDeleteResponse


class riskIndicatorsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, riskIndicator=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if riskIndicator is None:
            self.riskIndicator = []
        else:
            self.riskIndicator = riskIndicator
        self.riskIndicator_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, riskIndicatorsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if riskIndicatorsType.subclass:
            return riskIndicatorsType.subclass(*args_, **kwargs_)
        else:
            return riskIndicatorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_riskIndicator(self):
        return self.riskIndicator
    def set_riskIndicator(self, riskIndicator):
        self.riskIndicator = riskIndicator
    def add_riskIndicator(self, value):
        self.riskIndicator.append(value)
    def insert_riskIndicator_at(self, index, value):
        self.riskIndicator.insert(index, value)
    def replace_riskIndicator_at(self, index, value):
        self.riskIndicator[index] = value
    def hasContent_(self):
        if (
            self.riskIndicator
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='riskIndicatorsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('riskIndicatorsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'riskIndicatorsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='riskIndicatorsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='riskIndicatorsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='riskIndicatorsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='riskIndicatorsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for riskIndicator_ in self.riskIndicator:
            namespaceprefix_ = self.riskIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.riskIndicator_nsprefix_) else ''
            riskIndicator_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='riskIndicator', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'riskIndicator':
            obj_ = potentialRiskIndicator.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.riskIndicator.append(obj_)
            obj_.original_tagname_ = 'riskIndicator'
# end class riskIndicatorsType


class riskIndicatorsType18(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, riskIndicator=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if riskIndicator is None:
            self.riskIndicator = []
        else:
            self.riskIndicator = riskIndicator
        self.riskIndicator_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, riskIndicatorsType18)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if riskIndicatorsType18.subclass:
            return riskIndicatorsType18.subclass(*args_, **kwargs_)
        else:
            return riskIndicatorsType18(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_riskIndicator(self):
        return self.riskIndicator
    def set_riskIndicator(self, riskIndicator):
        self.riskIndicator = riskIndicator
    def add_riskIndicator(self, value):
        self.riskIndicator.append(value)
    def insert_riskIndicator_at(self, index, value):
        self.riskIndicator.insert(index, value)
    def replace_riskIndicator_at(self, index, value):
        self.riskIndicator[index] = value
    def hasContent_(self):
        if (
            self.riskIndicator
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='riskIndicatorsType18', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('riskIndicatorsType18')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'riskIndicatorsType18':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='riskIndicatorsType18')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='riskIndicatorsType18', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='riskIndicatorsType18'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='riskIndicatorsType18', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for riskIndicator_ in self.riskIndicator:
            namespaceprefix_ = self.riskIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.riskIndicator_nsprefix_) else ''
            riskIndicator_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='riskIndicator', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'riskIndicator':
            obj_ = potentialRiskIndicator.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.riskIndicator.append(obj_)
            obj_.original_tagname_ = 'riskIndicator'
# end class riskIndicatorsType18


class paypageCredentialsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, paypageCredential=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if paypageCredential is None:
            self.paypageCredential = []
        else:
            self.paypageCredential = paypageCredential
        self.paypageCredential_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, paypageCredentialsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if paypageCredentialsType.subclass:
            return paypageCredentialsType.subclass(*args_, **kwargs_)
        else:
            return paypageCredentialsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_paypageCredential(self):
        return self.paypageCredential
    def set_paypageCredential(self, paypageCredential):
        self.paypageCredential = paypageCredential
    def add_paypageCredential(self, value):
        self.paypageCredential.append(value)
    def insert_paypageCredential_at(self, index, value):
        self.paypageCredential.insert(index, value)
    def replace_paypageCredential_at(self, index, value):
        self.paypageCredential[index] = value
    def hasContent_(self):
        if (
            self.paypageCredential
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='paypageCredentialsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('paypageCredentialsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'paypageCredentialsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='paypageCredentialsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='paypageCredentialsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='paypageCredentialsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='paypageCredentialsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for paypageCredential_ in self.paypageCredential:
            namespaceprefix_ = self.paypageCredential_nsprefix_ + ':' if (UseCapturedNS_ and self.paypageCredential_nsprefix_) else ''
            paypageCredential_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='paypageCredential', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'paypageCredential':
            obj_ = paypageCredential.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.paypageCredential.append(obj_)
            obj_.original_tagname_ = 'paypageCredential'
# end class paypageCredentialsType


class paypageCredentialsType62(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, paypageCredential=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if paypageCredential is None:
            self.paypageCredential = []
        else:
            self.paypageCredential = paypageCredential
        self.paypageCredential_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, paypageCredentialsType62)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if paypageCredentialsType62.subclass:
            return paypageCredentialsType62.subclass(*args_, **kwargs_)
        else:
            return paypageCredentialsType62(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_paypageCredential(self):
        return self.paypageCredential
    def set_paypageCredential(self, paypageCredential):
        self.paypageCredential = paypageCredential
    def add_paypageCredential(self, value):
        self.paypageCredential.append(value)
    def insert_paypageCredential_at(self, index, value):
        self.paypageCredential.insert(index, value)
    def replace_paypageCredential_at(self, index, value):
        self.paypageCredential[index] = value
    def hasContent_(self):
        if (
            self.paypageCredential
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='paypageCredentialsType62', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('paypageCredentialsType62')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'paypageCredentialsType62':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='paypageCredentialsType62')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='paypageCredentialsType62', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='paypageCredentialsType62'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='paypageCredentialsType62', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for paypageCredential_ in self.paypageCredential:
            namespaceprefix_ = self.paypageCredential_nsprefix_ + ':' if (UseCapturedNS_ and self.paypageCredential_nsprefix_) else ''
            paypageCredential_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='paypageCredential', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'paypageCredential':
            obj_ = paypageCredential.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.paypageCredential.append(obj_)
            obj_.original_tagname_ = 'paypageCredential'
# end class paypageCredentialsType62


class errorsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, error=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if error is None:
            self.error = []
        else:
            self.error = error
        self.error_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, errorsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if errorsType.subclass:
            return errorsType.subclass(*args_, **kwargs_)
        else:
            return errorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_error(self):
        return self.error
    def set_error(self, error):
        self.error = error
    def add_error(self, value):
        self.error.append(value)
    def insert_error_at(self, index, value):
        self.error.insert(index, value)
    def replace_error_at(self, index, value):
        self.error[index] = value
    def hasContent_(self):
        if (
            self.error
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='errorsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('errorsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'errorsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='errorsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='errorsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='errorsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='errorsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for error_ in self.error:
            namespaceprefix_ = self.error_nsprefix_ + ':' if (UseCapturedNS_ and self.error_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%serror>%s</%serror>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(error_), input_name='error')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'error':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'error')
            value_ = self.gds_validate_string(value_, node, 'error')
            self.error.append(value_)
            self.error_nsprefix_ = child_.prefix
# end class errorsType


class approvedMccsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, approvedMcc=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if approvedMcc is None:
            self.approvedMcc = []
        else:
            self.approvedMcc = approvedMcc
        self.approvedMcc_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, approvedMccsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if approvedMccsType.subclass:
            return approvedMccsType.subclass(*args_, **kwargs_)
        else:
            return approvedMccsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_approvedMcc(self):
        return self.approvedMcc
    def set_approvedMcc(self, approvedMcc):
        self.approvedMcc = approvedMcc
    def add_approvedMcc(self, value):
        self.approvedMcc.append(value)
    def insert_approvedMcc_at(self, index, value):
        self.approvedMcc.insert(index, value)
    def replace_approvedMcc_at(self, index, value):
        self.approvedMcc[index] = value
    def hasContent_(self):
        if (
            self.approvedMcc
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='approvedMccsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('approvedMccsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'approvedMccsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='approvedMccsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='approvedMccsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='approvedMccsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='approvedMccsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for approvedMcc_ in self.approvedMcc:
            namespaceprefix_ = self.approvedMcc_nsprefix_ + ':' if (UseCapturedNS_ and self.approvedMcc_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sapprovedMcc>%s</%sapprovedMcc>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(approvedMcc_), input_name='approvedMcc')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'approvedMcc':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'approvedMcc')
            value_ = self.gds_validate_string(value_, node, 'approvedMcc')
            self.approvedMcc.append(value_)
            self.approvedMcc_nsprefix_ = child_.prefix
# end class approvedMccsType


class agreementsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, legalEntityAgreement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if legalEntityAgreement is None:
            self.legalEntityAgreement = []
        else:
            self.legalEntityAgreement = legalEntityAgreement
        self.legalEntityAgreement_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, agreementsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if agreementsType.subclass:
            return agreementsType.subclass(*args_, **kwargs_)
        else:
            return agreementsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_legalEntityAgreement(self):
        return self.legalEntityAgreement
    def set_legalEntityAgreement(self, legalEntityAgreement):
        self.legalEntityAgreement = legalEntityAgreement
    def add_legalEntityAgreement(self, value):
        self.legalEntityAgreement.append(value)
    def insert_legalEntityAgreement_at(self, index, value):
        self.legalEntityAgreement.insert(index, value)
    def replace_legalEntityAgreement_at(self, index, value):
        self.legalEntityAgreement[index] = value
    def hasContent_(self):
        if (
            self.legalEntityAgreement
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='agreementsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('agreementsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'agreementsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='agreementsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='agreementsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='agreementsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://payfac.vantivcnp.com/api/merchant/onboard"', name_='agreementsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for legalEntityAgreement_ in self.legalEntityAgreement:
            namespaceprefix_ = self.legalEntityAgreement_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityAgreement_nsprefix_) else ''
            legalEntityAgreement_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='legalEntityAgreement', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityAgreement':
            obj_ = legalEntityAgreement.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.legalEntityAgreement.append(obj_)
            obj_.original_tagname_ = 'legalEntityAgreement'
# end class agreementsType


class legalEntityResponse(response):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = response
    def __init__(self, transactionId=None, duplicate=None, legalEntityId=None, responseCode=None, responseDescription=None, originalLegalEntityId=None, originalLegalEntityStatus=None, backgroundCheckResults=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(legalEntityResponse, self).__init__(transactionId, extensiontype_,  **kwargs_)
        self.duplicate = _cast(bool, duplicate)
        self.duplicate_nsprefix_ = None
        self.legalEntityId = legalEntityId
        self.validate_legalEntityIdType(self.legalEntityId)
        self.legalEntityId_nsprefix_ = None
        self.responseCode = responseCode
        self.responseCode_nsprefix_ = None
        self.responseDescription = responseDescription
        self.validate_responseDescriptionType(self.responseDescription)
        self.responseDescription_nsprefix_ = None
        self.originalLegalEntityId = originalLegalEntityId
        self.validate_originalLegalEntityIdType(self.originalLegalEntityId)
        self.originalLegalEntityId_nsprefix_ = None
        self.originalLegalEntityStatus = originalLegalEntityStatus
        self.validate_originalLegalEntityStatusType(self.originalLegalEntityStatus)
        self.originalLegalEntityStatus_nsprefix_ = None
        self.backgroundCheckResults = backgroundCheckResults
        self.backgroundCheckResults_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityResponse.subclass:
            return legalEntityResponse.subclass(*args_, **kwargs_)
        else:
            return legalEntityResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_legalEntityId(self):
        return self.legalEntityId
    def set_legalEntityId(self, legalEntityId):
        self.legalEntityId = legalEntityId
    def get_responseCode(self):
        return self.responseCode
    def set_responseCode(self, responseCode):
        self.responseCode = responseCode
    def get_responseDescription(self):
        return self.responseDescription
    def set_responseDescription(self, responseDescription):
        self.responseDescription = responseDescription
    def get_originalLegalEntityId(self):
        return self.originalLegalEntityId
    def set_originalLegalEntityId(self, originalLegalEntityId):
        self.originalLegalEntityId = originalLegalEntityId
    def get_originalLegalEntityStatus(self):
        return self.originalLegalEntityStatus
    def set_originalLegalEntityStatus(self, originalLegalEntityStatus):
        self.originalLegalEntityStatus = originalLegalEntityStatus
    def get_backgroundCheckResults(self):
        return self.backgroundCheckResults
    def set_backgroundCheckResults(self, backgroundCheckResults):
        self.backgroundCheckResults = backgroundCheckResults
    def get_duplicate(self):
        return self.duplicate
    def set_duplicate(self, duplicate):
        self.duplicate = duplicate
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_legalEntityIdType(self, value):
        result = True
        # Validate type legalEntityIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on legalEntityIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on legalEntityIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_responseDescriptionType(self, value):
        result = True
        # Validate type responseDescriptionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on responseDescriptionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on responseDescriptionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_originalLegalEntityIdType(self, value):
        result = True
        # Validate type originalLegalEntityIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 19:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on originalLegalEntityIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on originalLegalEntityIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_originalLegalEntityStatusType(self, value):
        result = True
        # Validate type originalLegalEntityStatusType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on originalLegalEntityStatusType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on originalLegalEntityStatusType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.legalEntityId is not None or
            self.responseCode is not None or
            self.responseDescription is not None or
            self.originalLegalEntityId is not None or
            self.originalLegalEntityStatus is not None or
            self.backgroundCheckResults is not None or
            super(legalEntityResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='legalEntityResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityResponse'):
        super(legalEntityResponse, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityResponse')
        if self.duplicate is not None and 'duplicate' not in already_processed:
            already_processed.add('duplicate')
            outfile.write(' duplicate="%s"' % self.gds_format_boolean(self.duplicate, input_name='duplicate'))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='legalEntityResponse', fromsubclass_=False, pretty_print=True):
        super(legalEntityResponse, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.legalEntityId is not None:
            namespaceprefix_ = self.legalEntityId_nsprefix_ + ':' if (UseCapturedNS_ and self.legalEntityId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slegalEntityId>%s</%slegalEntityId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.legalEntityId), input_name='legalEntityId')), namespaceprefix_ , eol_))
        if self.responseCode is not None:
            namespaceprefix_ = self.responseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.responseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sresponseCode>%s</%sresponseCode>%s' % (namespaceprefix_ , self.gds_format_integer(self.responseCode, input_name='responseCode'), namespaceprefix_ , eol_))
        if self.responseDescription is not None:
            namespaceprefix_ = self.responseDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.responseDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sresponseDescription>%s</%sresponseDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.responseDescription), input_name='responseDescription')), namespaceprefix_ , eol_))
        if self.originalLegalEntityId is not None:
            namespaceprefix_ = self.originalLegalEntityId_nsprefix_ + ':' if (UseCapturedNS_ and self.originalLegalEntityId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalLegalEntityId>%s</%soriginalLegalEntityId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.originalLegalEntityId), input_name='originalLegalEntityId')), namespaceprefix_ , eol_))
        if self.originalLegalEntityStatus is not None:
            namespaceprefix_ = self.originalLegalEntityStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.originalLegalEntityStatus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soriginalLegalEntityStatus>%s</%soriginalLegalEntityStatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.originalLegalEntityStatus), input_name='originalLegalEntityStatus')), namespaceprefix_ , eol_))
        if self.backgroundCheckResults is not None:
            namespaceprefix_ = self.backgroundCheckResults_nsprefix_ + ':' if (UseCapturedNS_ and self.backgroundCheckResults_nsprefix_) else ''
            self.backgroundCheckResults.export(outfile, level, namespaceprefix_='tns:', namespacedef_='', name_='backgroundCheckResults', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('duplicate', node)
        if value is not None and 'duplicate' not in already_processed:
            already_processed.add('duplicate')
            if value in ('true', '1'):
                self.duplicate = True
            elif value in ('false', '0'):
                self.duplicate = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
        super(legalEntityResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'legalEntityId')
            value_ = self.gds_validate_string(value_, node, 'legalEntityId')
            self.legalEntityId = value_
            self.legalEntityId_nsprefix_ = child_.prefix
            # validate type legalEntityIdType
            self.validate_legalEntityIdType(self.legalEntityId)
        elif nodeName_ == 'responseCode' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'responseCode')
            ival_ = self.gds_validate_integer(ival_, node, 'responseCode')
            self.responseCode = ival_
            self.responseCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'responseDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'responseDescription')
            value_ = self.gds_validate_string(value_, node, 'responseDescription')
            self.responseDescription = value_
            self.responseDescription_nsprefix_ = child_.prefix
            # validate type responseDescriptionType
            self.validate_responseDescriptionType(self.responseDescription)
        elif nodeName_ == 'originalLegalEntityId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'originalLegalEntityId')
            value_ = self.gds_validate_string(value_, node, 'originalLegalEntityId')
            self.originalLegalEntityId = value_
            self.originalLegalEntityId_nsprefix_ = child_.prefix
            # validate type originalLegalEntityIdType
            self.validate_originalLegalEntityIdType(self.originalLegalEntityId)
        elif nodeName_ == 'originalLegalEntityStatus':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'originalLegalEntityStatus')
            value_ = self.gds_validate_string(value_, node, 'originalLegalEntityStatus')
            self.originalLegalEntityStatus = value_
            self.originalLegalEntityStatus_nsprefix_ = child_.prefix
            # validate type originalLegalEntityStatusType
            self.validate_originalLegalEntityStatusType(self.originalLegalEntityStatus)
        elif nodeName_ == 'backgroundCheckResults':
            obj_ = backgroundCheckResults.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.backgroundCheckResults = obj_
            obj_.original_tagname_ = 'backgroundCheckResults'
        super(legalEntityResponse, self).buildChildren(child_, node, nodeName_, True)
# end class legalEntityResponse


class legalEntityCreateResponse(legalEntityResponse):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = legalEntityResponse
    def __init__(self, transactionId=None, duplicate=None, legalEntityId=None, responseCode=None, responseDescription=None, originalLegalEntityId=None, originalLegalEntityStatus=None, backgroundCheckResults=None, principal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(legalEntityCreateResponse, self).__init__(transactionId, duplicate, legalEntityId, responseCode, responseDescription, originalLegalEntityId, originalLegalEntityStatus, backgroundCheckResults,  **kwargs_)
        self.principal = principal
        self.principal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityCreateResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityCreateResponse.subclass:
            return legalEntityCreateResponse.subclass(*args_, **kwargs_)
        else:
            return legalEntityCreateResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_principal(self):
        return self.principal
    def set_principal(self, principal):
        self.principal = principal
    def hasContent_(self):
        if (
            self.principal is not None or
            super(legalEntityCreateResponse, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='legalEntityCreateResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('legalEntityCreateResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'legalEntityCreateResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityCreateResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='legalEntityCreateResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='legalEntityCreateResponse'):
        super(legalEntityCreateResponse, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='legalEntityCreateResponse')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='legalEntityCreateResponse', fromsubclass_=False, pretty_print=True):
        super(legalEntityCreateResponse, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.principal is not None:
            namespaceprefix_ = self.principal_nsprefix_ + ':' if (UseCapturedNS_ and self.principal_nsprefix_) else ''
            self.principal.export(outfile, level, namespaceprefix_, namespacedef_='', name_='principal', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(legalEntityCreateResponse, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'principal':
            obj_ = legalEntityPrincipalCreateResponse.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.principal = obj_
            obj_.original_tagname_ = 'principal'
        super(legalEntityCreateResponse, self).buildChildren(child_, node, nodeName_, True)
# end class legalEntityCreateResponse


GDSClassesMapping = {
    'approvedMccResponse': approvedMccResponse,
    'backgroundCheckResults': backgroundCheckResults,
    'errorResponse': errorResponse,
    'legalEntityAgreementCreateRequest': legalEntityAgreementCreateRequest,
    'legalEntityAgreementCreateResponse': legalEntityAgreementCreateResponse,
    'legalEntityAgreementRetrievalResponse': legalEntityAgreementRetrievalResponse,
    'legalEntityCreateRequest': legalEntityCreateRequest,
    'legalEntityCreateResponse': legalEntityCreateResponse,
    'legalEntityPrincipalCreateRequest': legalEntityPrincipalCreateRequest,
    'legalEntityPrincipalCreateResponse': legalEntityPrincipalCreateResponse,
    'legalEntityPrincipalCreateResponseWithResponseFields': legalEntityPrincipalCreateResponseWithResponseFields,
    'legalEntityPrincipalDeleteResponse': legalEntityPrincipalDeleteResponse,
    'legalEntityResponse': legalEntityResponse,
    'legalEntityRetrievalResponse': legalEntityRetrievalResponse,
    'legalEntityUpdateRequest': legalEntityUpdateRequest,
    'principalCreateResponse': principalCreateResponse,
    'principalDeleteResponse': principalDeleteResponse,
    'response': response,
    'subMerchantAmexAcquiredFeature': subMerchantAmexAcquiredFeature,
    'subMerchantCreateRequest': subMerchantCreateRequest,
    'subMerchantCreateResponse': subMerchantCreateResponse,
    'subMerchantECheckFeature': subMerchantECheckFeature,
    'subMerchantFraudFeature': subMerchantFraudFeature,
    'subMerchantRetrievalResponse': subMerchantRetrievalResponse,
    'subMerchantUpdateRequest': subMerchantUpdateRequest,
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'approvedMccResponse'
        rootClass = approvedMccResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'approvedMccResponse'
        rootClass = approvedMccResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'approvedMccResponse'
        rootClass = approvedMccResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:http://payfac.vantivcnp.com/api/merchant/onboard')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'approvedMccResponse'
        rootClass = approvedMccResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from generatedClass import *\n\n')
        sys.stdout.write('import generatedClass as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

__all__ = [
    "address",
    "addressUpdatable",
    "agreementsType",
    "approvedMccResponse",
    "approvedMccsType",
    "backgroundCheckResults",
    "bankruptcyResult",
    "businessNameAddressPhoneAssociation",
    "businessResult",
    "businessScore",
    "businessToPrincipalAssociation",
    "businessVerificationIndicators",
    "businessVerificationResult",
    "errorResponse",
    "errorsType",
    "legalEntityAgreement",
    "legalEntityAgreementCreateRequest",
    "legalEntityAgreementCreateResponse",
    "legalEntityAgreementRetrievalResponse",
    "legalEntityBackgroundCheckFields",
    "legalEntityCreateRequest",
    "legalEntityCreateResponse",
    "legalEntityPrincipal",
    "legalEntityPrincipalCreateRequest",
    "legalEntityPrincipalCreateResponse",
    "legalEntityPrincipalCreateResponseWithResponseFields",
    "legalEntityPrincipalDeleteResponse",
    "legalEntityPrincipalUpdatable",
    "legalEntityResponse",
    "legalEntityRetrievalResponse",
    "legalEntityUpdateRequest",
    "lienResult",
    "nameAddressSsnAssociation",
    "nameAddressTaxIdAssociation",
    "paypageCredential",
    "paypageCredentialsType",
    "paypageCredentialsType62",
    "potentialRiskIndicator",
    "principalAddress",
    "principalBackgroundCheckFields",
    "principalCreateResponse",
    "principalDeleteResponse",
    "principalNameAddressPhoneAssociation",
    "principalResult",
    "principalScore",
    "principalVerificationIndicators",
    "principalVerificationResult",
    "response",
    "riskIndicatorsType",
    "riskIndicatorsType18",
    "subMerchantAmexAcquiredFeature",
    "subMerchantCreateRequest",
    "subMerchantCreateResponse",
    "subMerchantCredentials",
    "subMerchantECheckFeature",
    "subMerchantFraudFeature",
    "subMerchantFunding",
    "subMerchantPrimaryContact",
    "subMerchantPrimaryContactUpdatable",
    "subMerchantRetrievalResponse",
    "subMerchantUpdateRequest"
]
