from __future__ import absolute_import, division, print_function
import os
import sys

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)

from payfacsdk import utils

version = utils.Configuration().VERSION
xsd_name = 'merchant-onboard-api-v%s.xsd' % version

# xsd_name = 'merchant-onboard-api-v13.xsd'
print('Generate module fields using pyxb')
xsd_abs_path =  os.path.join(package_root, "schema", xsd_name)
print(xsd_abs_path)
os.system('pyxbgen --schema-location %s --module fields_payfac' %xsd_abs_path)

print('Copy fields_payfac.py to package')
gen_field_py_abs_path = os.path.join(package_root, 'tools', 'fields_payfac.py')
target_field_py_abs_path = os.path.join(package_root, 'payfacsdk', 'fields_payfac.py')
os.system('mv %s %s' % (gen_field_py_abs_path, target_field_py_abs_path))



