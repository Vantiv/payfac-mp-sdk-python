# -*- coding: utf-8 -*-
import sys
from setuptools import setup

# Require Python 2.7.9 or higher or Python 3.4 or higher
if (sys.version_info[:3] < (2, 7, 9)) or ((sys.version_info[0] == 3) and sys.version_info[:2] < (3, 4)):
    raise ValueError('''PyXB requires:
  Python2 version 2.7.9 or later; or
  Python3 version 3.4 or later
(You have %s.)''' % (sys.version,))

setup(
    name='PayfacMpSDK',
    version='13.0.0',
    description='Worldpay payfac SDK',
    author='Worldpay',
    author_email='SDKSupport@vantiv.com',
    url='https://developer.vantiv.com/community/ecommerce',
    packages=['payfacMPSdk', 'scripts'],
    install_requires=[
        'paramiko>=1.14.0',
        'requests>=2.13.0',
        'six>=1.10.0',
        'xmlschema>=1.0.3',
        'generateDS>=2.29.24',
        'unittest2>=1.1.0',
        'python-dateutil>=2.7.3',
        'mock', 'lxml'
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'payfac_mp_sdk_setup = scripts.payfac_mp_sdk_setup:main',
        ],
    },
    long_description='''Worldpay Python Payfac SDK
=====================================================

.. _`WorldPay eCommerce`: https://developer.vantiv.com/community/ecommerce

About WorldPay eCommerce
----------------------
`WorldPay eCommerce`_ powers the payment processing engines for leading companies that sell directly to consumers through  internet retail, direct response marketing (TV, radio and telephone), and online services. WorldPay eCommerce is the leading authority in card-not-present (CNP) commerce, transaction processing and merchant services.


About this SDK
--------------
The WorldPay Python PayFac SDK is a Python implementation of the `WorldPay eCommerce`_ PayFac API. This SDK was created to make it as easy as possible to manage your PayFac using WorldPay eCommerce API. This SDK utilizes the HTTPS protocol to securely connect to WorldPay eCommerce. Using the SDK requires coordination with the WorldPay eCommerce team in order to be provided with credentials for accessing our systems.

Each Python SDK release supports all of the functionality present in the associated WorldPay eCommerce PayFac API version (e.g., SDK v2.1.0 supports WorldPay eCommerce PayFac API v2.1). Please see the PayFac API reference guide to get more details on what the WorldPay eCommerce PayFac engine supports.

This SDK was implemented to support the Python programming language and was created by WorldPay eCommerce. Its intended use is for online and batch transaction processing utilizing your account on the WorldPay eCommerce payments engine.

See LICENSE file for details on using this software.

Please contact `WorldPay eCommerce`_ to receive valid merchant credentials in order to run test successfully or if you require assistance in any way.  We are reachable at sdksupport@Vantiv.com

Dependencies
------------
* pyxb v1.2.5 : http://pyxb.sourceforge.net/
* paramiko v1.14.0: http://www.paramiko.org/
* requests v2.13.0: http://docs.python-requests.org/en/master/
* six v1.10.0: https://github.com/benjaminp/six
* xmltodict 0.10.2: https://github.com/martinblech/xmltodict

Setup
-----
* Run payfac_mp_sdk_setup and answer the questions.

.. code:: bash

   payfac_mp_sdk_setup

EXAMPLE
-------
Using dict
..........
.. code-block:: python

    #Example for PayFac SDK
    from __future__ import print_function, unicode_literals

    from cnpsdk import *

    # Initial Configuration object. If you have saved configuration in '.payfac_mp_sdk.conf' at system environment
    # variable: PAYFAC_SDK_CONFIG or user home directory, the saved configuration will be automatically load.
    conf = utils.Configuration()

    # Configuration need following attributes for PayFac requests:
    # user = ''
    # password = ''
    # merchantId = ''
    # url = 'https://www.testvantivcnp.com/sandbox/communicator/online'
    # proxy = ''

    # Retrieving information about a LegalEntity by legalentityID:
    response = payfac_legalEntity.get_by_legalEntityId(legalentityId)

    # Update a LegalEntity
    request = "......(some request)"
    response = payfac_legalEntity.put_by_legalEntityId(legalentityId, request)

    # Create a LegalEntity
    request = "......(some request)"
    response = payfac_legalEntity.post_by_legalEntity(request)

''',
)
