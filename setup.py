# -*- coding: utf-8 -*-
import sys

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
    version='13',
    description='Worldpay payfac SDK',
    author='Worldpay',
    author_email='SDKSupport@vantiv.com',
    url='https://developer.vantiv.com/community/ecommerce',
    packages=['payfacsdk', 'scripts'],
    install_requires=[
        'PyXB==1.2.5',
        'paramiko>=1.14.0',
        'requests>=2.13.0',
        'six>=1.10.0',
        'xmltodict>=0.10.2',
        'unittest2>=1.1.0',
        'mock'
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

.. _`Vantiv eCommerce`: https://developer.vantiv.com/community/ecommerce

About Vantiv eCommerce
----------------------
`Vantiv eCommerce`_ powers the payment processing engines for leading companies that sell directly to consumers through  internet retail, direct response marketing (TV, radio and telephone), and online services. Vantiv eCommerce is the leading authority in card-not-present (CNP) commerce, transaction processing and merchant services.


About this SDK
--------------
The Vantiv eCommerce Python Chargeback SDK is a Python implementation of the `Vantiv eCommerce`_ Chargeback API. This SDK was created to make it as easy as possible to manage your chargebacks using Vantiv eCommerce API. This SDK utilizes the HTTPS protocol to securely connect to Vantiv eCommerce. Using the SDK requires coordination with the Vantiv eCommerce team in order to be provided with credentials for accessing our systems.

Each Python SDK release supports all of the functionality present in the associated Vantiv eCommerce Chargeback API version (e.g., SDK v2.1.0 supports Vantiv eCommerce Chargeback API v2.1). Please see the Chargeback API reference guide to get more details on what the Vantiv eCommerce chargeback engine supports.

This SDK was implemented to support the Python programming language and was created by Vantiv eCommerce. Its intended use is for online and batch transaction processing utilizing your account on the Vantiv eCommerce payments engine.

See LICENSE file for details on using this software.

Please contact `Vantiv eCommerce`_ to receive valid merchant credentials in order to run tests successfully or if you require assistance in any way.  We are reachable at sdksupport@Vantiv.com

Dependencies
------------
* pyxb v1.2.5 : http://pyxb.sourceforge.net/
* paramiko v1.14.0: http://www.paramiko.org/
* requests v2.13.0: http://docs.python-requests.org/en/master/
* six v1.10.0: https://github.com/benjaminp/six
* xmltodict 0.10.2: https://github.com/martinblech/xmltodict

Setup
-----
* Run cnp_chargeback_sdk_setup and answer the questions.

.. code:: bash

   cnp_chargeback_sdk_setup

EXAMPLE
-------
Using dict
..........
.. code-block:: python

    #Example for Chargeback SDK
    from __future__ import print_function, unicode_literals

    from cnpsdk import *

    # Initial Configuration object. If you have saved configuration in '.vantiv_chargeback_sdk.conf' at system environment
    # variable: CHARGEBACK_SDK_CONFIG or user home directory, the saved configuration will be automatically load.
    conf = utils.Configuration()

    # Configuration need following attributes for chargeback requests:
    # user = ''
    # password = ''
    # merchantId = ''
    # url = 'https://www.testvantivcnp.com/sandbox/communicator/online'
    # proxy = ''

    # Retrieving information about a chargeback by caseId:
    response = chargeback_retrieval.get_chargeback_by_case_id(xxxx)
    response = chargeback_retrieval.get_chargebacks_by_date("2018-01-01)

    # Update chargeback case
    chargeback_update.represent_case(xxxx, "Note on activity: represented case!")
    chargeback_update.assign_case_to_user(xxxx, "userId", "Note on activity: assigned case to user!")

    # Upload and manage documents to support chargeback case
    chargeback_docuemnt.upload_document(xxxx, "invoice.pdf")
    response = chargeback_docuemnt.list_documents(xxxx)

''',
)
