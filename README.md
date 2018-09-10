[![Build Status](https://travis-ci.org/Vantiv/payfac-mp-sdk-python.svg?branch=13.x)](https://travis-ci.org/Vantiv/payfac-mp-sdk-python)
[![codecov](https://codecov.io/gh/Vantiv/payfac-mp-sdk-python/branch/13.x/graph/badge.svg)](https://codecov.io/gh/Vantiv/payfac-mp-sdk-python)
![Github All Releases](https://img.shields.io/github/downloads/vantiv/payfac-mp-sdk-python/total.svg)
[![GitHub](https://img.shields.io/github/license/vantiv/payfac-mp-sdk-python.svg)](https://github.com/Vantiv/payfac-mp-sdk-python/13.x/LICENSE) 
[![GitHub issues](https://img.shields.io/github/issues/vantiv/payfac-mp-sdk-python.svg)](https://github.com/Vantiv/payfac-mp-sdk-python/issues)

# payfac-mp-sdk-python

The PayFac Merchant Provisioner SDK is a Java implementation of the [Worldpay](https://developer.vantiv.com/community/ecommerce) PayFac Merchant Provisioner API. This SDK was created to make it as easy as possible to perform operations that allows you to create and update Legal Entities and Sub-merchants, as well as retrieve information about existing Legal Entities and Sub-merchants in near real-time. This SDK utilizes the HTTPS protocol to securely connect to Worldpay. Using the SDK requires coordination with the Vantiv eCommerce team in order to be provided with credentials for accessing our systems.

Each Python SDK release supports all of the functionality present in the associated PayFac Merchant Provisioner API version (e.g., SDK v13.0.0 supports API v13.0.0). Please see our [documentation](https://developer.vantiv.com/community/ecommerce/pages/documentation) for PayFac Merchant Provisioner API to get more details on what operations are supported.

This SDK is implemented to support the Python programming language and is created by Worldpay. Its intended use is for PayFac API operations with Worldpay.


## Getting Started

These instructions will help you get started with using the SDK.

### Dependencies

* [pyxb v1.2.5](http://pyxb.sourceforge.net/)
* [paramiko v1.14.0](http://www.paramiko.org/)
* [requests v2.13.0](http://docs.python-requests.org/en/master/)
* [six v1.10.0](https://github.com/benjaminp/six)
* [xmltodict 0.10.2](https://github.com/martinblech/xmltodict)



### Setup

1. To download and install:

#### Using pip 
```
pip install Cnppayfac-mpSdk
```

#### Without Pip

```
# Clone repo
git clone https://github.com/Vantiv/payfac-mp-sdk-python.git
# Cd to repo
cd payfac-mp-sdk-python
# Checkout latest branch 13.x
git checkout 13.x
# Run the setup file
python setup.py install
```

2. setup configurations
```
payfac-mp_sdk_setup
```

### Configuration
List of configuration parameters along with their values can be found [here](https://gist.github.com/VantivSDK/8b7dd606230ec65b36eba457df4443de).


## Usage example

```python
#Example for PayFac MP SDK
from __future__ import print_function, unicode_literals

from payfacMpSdk import *

# Initial Configuration object. If you have saved configuration in '.vantiv_payfac-mp_sdk.conf' at system environment
# variable: payfac-mp_SDK_CONFIG or user home directory, the saved configuration will be automatically load.
conf = utils.Configuration()

# Configuration need following attributes for payfac-mp requests:
# user = ''
# password = ''
# merchantId = ''
# url = 'https://www.testvantivcnp.com/sandbox/communicator/online'
# proxy = ''

# Retrieving information about a payfac-mp by caseId:
response = payfac-mp_retrieval.get_payfac-mp_by_case_id(xxxx)
response = payfac-mp_retrieval.get_payfac-mps_by_date("2018-01-01)

# Update payfac-mp case
payfac-mp_update.represent_case(xxxx, "Note on activity: represented case!")
payfac-mp_update.assign_case_to_user(xxxx, "userId", "Note on activity: assigned case to user!")

# Upload and manage documents to support payfac-mp case
payfac-mp_docuemnt.upload_document(xxxx, "invoice.pdf")
response = payfac-mp_docuemnt.list_documents(xxxx)

```

## Versioning
For the versions available, see the [tags on this repository](https://github.com/vantiv/payfac-mp-sdk-python/tags). 

## Changelog
For the list of changes, check out the [changelog](https://github.com/Vantiv/payfac-mp-sdk-python/blob/13.x/CHANGELOG.md)

## Authors

* [**Ajjunesh Raju**](https://github.com/ayush17agarwal)
* [**Chen Chang**](https://github.com/cc6980312)

See also the list of [contributors](https://github.com/vantiv/payfac-mp-sdk-python/contributors) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Vantiv/payfac-mp-sdk-python/blob/13.x/LICENSE.md) file for details

## Examples
More examples can be found in [Functional and Unit Tests](https://github.com/Vantiv/payfac-mp-sdk-python/tree/13.x/src/test/java/com/mp/sdk)

## Support
Please contact [Vantiv eCommerce](https://developer.vantiv.com/community/ecommerce) to receive valid merchant credentials in order to run tests successfully or if you require assistance in any way.  Support can also be reached at sdksupport@Vantiv.com
