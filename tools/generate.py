from __future__ import absolute_import, division, print_function
import os
import sys

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)

from payfacMPSdk import utils
version = utils.Configuration().VERSION
xsd_name = 'merchant-onboard-api-v%s.xsd' % version

print('Generate module fields using pyxb')
xsd_abs_path = os.path.join(package_root, "schema", xsd_name)
print(xsd_abs_path)
ns = "xmlns:\"http://payfac.vantivcnp.com/api/merchant/onboard\""
os.system('generateDS.py --namespacedef=%s -o generatedClass.py %s' %(ns,xsd_abs_path))

print('Copy generatedClass.py and to package')
gen_field_py_abs_path = os.path.join(package_root, 'tools', 'generatedClass.py')
target_field_py_abs_path = os.path.join(package_root, 'payfacMPSdk', 'generatedClass.py')
os.system('mv %s %s' % (gen_field_py_abs_path, target_field_py_abs_path))

