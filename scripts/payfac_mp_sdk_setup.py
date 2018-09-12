#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

import os
import sys
import tempfile

import six

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, package_root)

from payfacMPSdk import utils


def ask_user():
    attrs = [
        'username',
        'password',
        'merchant_id',
        'proxy',
        'printXml',
        'neuterXml'
    ]
    attr_dict = {
        'username': '',
        'password': '',
        'merchant_id': '',
        'url': '',
        'proxy': '',
        'printXml': 'n',
        'neuterXml': 'n'
    }
    attr_valid_dict = {

        'neuterXml': {
            'y': True,
            'n': False,
        },
        'printXml': {
            'y': True,
            'n': False,
        }
    }
    attr_des_dict = {
        'username': 'Please input your presenter user name: ',
        'password': 'Please input your presenter password: ',
        'merchant_id': 'Please input your merchantId: ',
        'proxy': 'If you want to using https proxy, please input your proxy server address. Must start with "https://"',
        'printXml': 'Do you want to print xml in console? y for Yes, n for No.',
        'neuterXml': 'Do you want to hide sensitive data in printed xml? y for Yes, n for No.'
    }
    print(CC.bpurple('"Welcome to the Merchant Provisioner PayFac Python SDK"'))
    print('''    Please enter values for the following settings
    (just press Enter to accept a default value, if one is given in brackets).''')

    for attr in attrs:
        while True:
            print(gene_prompt(attr, attr_dict, attr_valid_dict, attr_des_dict))
            if six.PY3:
                x = input('')
            else:
                x = raw_input('')
            if not x:
                x = attr_dict[attr]
            if attr in attr_valid_dict:
                if x.lower() in attr_valid_dict[attr]:
                    x = attr_valid_dict[attr][x.lower()]
                else:
                    print('Invalid input for "%s" = "%s"' % (attr, x))
                    continue
            attr_dict[attr] = x
            break
    environmentConfig(attr_dict)
    conf = utils.Configuration()
    for k in attr_dict:
        setattr(conf, k, attr_dict[k])
    print(CC.bgreen('Configurations have saved at: %s ' % conf.save()))
    print(CC.bpurple('Successful!'))


def environmentConfig(attr_dict):
    Environment = {
        "SANDBOX": 'https://www.testvantivcnp.com/sandbox/payfac',
        "PRELIVE": 'https://payfac.vantivprelive.com',
        "POSTLIVE": 'https://services.vantivpostlive.com',
        "PRODUCTION": 'https://services.vantivcnp.com',
        "OTHER": 'You will be asked for all the values',
    }
    badInput = False
    continueTakeInput = True

    while continueTakeInput:
        if badInput: print("====== Invalid choice enetered ==========")
        print("Please choose an environment from the following list (example: 'prelive'): ");
        for env in Environment:
            print(env, Environment[env])
        userInput = raw_input('')
        if (userInput in Environment) and (userInput != 'OTHER'):
            attr_dict['url'] = Environment[userInput]
            continueTakeInput = False
        elif (userInput == 'OTHER'):
            print(
                "Please input the URL for online transactions (ex: https://www.testvantivcnp.com/sandbox/communicator/online): ");
            userInput = raw_input('')
            attr_dict['url'] = userInput
            continueTakeInput = False
        else:
            continueTakeInput = True
            badInput = True


def gene_prompt(attr, attr_dict, attr_valid_dict, attr_des_dict):
    if attr_dict[attr]:
        if attr in attr_valid_dict:
            option_str = CC.bcyan('Please select from following options:\n')
            for k in attr_valid_dict[attr]:
                _opt = attr_valid_dict[attr][k]
                if isinstance(_opt, bool):
                    _opt = 'True' if _opt else 'False'
                option_str += '%s - %s\n' % (CC.bgreen(k), CC.byellow(_opt))

            prompt = '\n%s\n%s%s [%s]: ' % \
                     (CC.bcyan(attr_des_dict[attr]), option_str, CC.bred(attr), CC.bgreen(attr_dict[attr]))
        else:
            prompt = '\n%s\n%s [%s]: ' % (CC.bcyan(attr_des_dict[attr]), CC.bred(attr), attr_dict[attr])
    else:
        prompt = '\n%s\n%s: ' % (CC.bcyan(attr_des_dict[attr]), CC.bred(attr))
    return prompt


# noinspection PyClassHasNoInit
class CC:
    # RESET
    COLOR_OFF = '\033[0m'  # TEXT RESET

    # REGULAR COLORS
    BLACK = '\033[0;30m'  # BLACK
    RED = '\033[0;31m'  # RED
    GREEN = '\033[0;32m'  # GREEN
    YELLOW = '\033[0;33m'  # YELLOW
    BLUE = '\033[0;34m'  # BLUE
    PURPLE = '\033[0;35m'  # PURPLE
    CYAN = '\033[0;36m'  # CYAN
    WHITE = '\033[0;37m'  # WHITE

    # BOLD
    BBLACK = '\033[1;30m'  # BLACK
    BRED = '\033[1;31m'  # RED
    BGREEN = '\033[1;32m'  # GREEN
    BYELLOW = '\033[1;33m'  # YELLOW
    BBLUE = '\033[1;34m'  # BLUE
    BPURPLE = '\033[1;35m'  # PURPLE
    BCYAN = '\033[1;36m'  # CYAN
    BWHITE = '\033[1;37m'  # WHITE

    # UNDERLINE
    UBLACK = '\033[4;30m'  # BLACK
    URED = '\033[4;31m'  # RED
    UGREEN = '\033[4;32m'  # GREEN
    UYELLOW = '\033[4;33m'  # YELLOW
    UBLUE = '\033[4;34m'  # BLUE
    UPURPLE = '\033[4;35m'  # PURPLE
    UCYAN = '\033[4;36m'  # CYAN
    UWHITE = '\033[4;37m'  # WHITE

    @classmethod
    def black(cls, _str):
        return cls.BLACK + _str + cls.COLOR_OFF

    @classmethod
    def red(cls, _str):
        return cls.RED + _str + cls.COLOR_OFF

    @classmethod
    def green(cls, _str):
        return cls.GREEN + _str + cls.COLOR_OFF

    @classmethod
    def yellow(cls, _str):
        return cls.YELLOW + _str + cls.COLOR_OFF

    @classmethod
    def blue(cls, _str):
        return cls.BLUE + _str + cls.COLOR_OFF

    @classmethod
    def purple(cls, _str):
        return cls.PURPLE + _str + cls.COLOR_OFF

    @classmethod
    def cyan(cls, _str):
        return cls.CYAN + _str + cls.COLOR_OFF

    @classmethod
    def white(cls, _str):
        return cls.WHITE + _str + cls.COLOR_OFF

    @classmethod
    def ublack(cls, _str):
        return cls.UBLACK + _str + cls.COLOR_OFF

    @classmethod
    def ured(cls, _str):
        return cls.URED + _str + cls.COLOR_OFF

    @classmethod
    def ugreen(cls, _str):
        return cls.UGREEN + _str + cls.COLOR_OFF

    @classmethod
    def uyellow(cls, _str):
        return cls.UYELLOW + _str + cls.COLOR_OFF

    @classmethod
    def ublue(cls, _str):
        return cls.UBLUE + _str + cls.COLOR_OFF

    @classmethod
    def upurple(cls, _str):
        return cls.UPURPLE + _str + cls.COLOR_OFF

    @classmethod
    def ucyan(cls, _str):
        return cls.UCYAN + _str + cls.COLOR_OFF

    @classmethod
    def uwhite(cls, _str):
        return cls.UWHITE + _str + cls.COLOR_OFF

    @classmethod
    def bblack(cls, _str):
        return cls.BBLACK + _str + cls.COLOR_OFF

    @classmethod
    def bred(cls, _str):
        return cls.BRED + _str + cls.COLOR_OFF

    @classmethod
    def bgreen(cls, _str):
        return cls.BGREEN + _str + cls.COLOR_OFF

    @classmethod
    def byellow(cls, _str):
        return cls.BYELLOW + _str + cls.COLOR_OFF

    @classmethod
    def bblue(cls, _str):
        return cls.BBLUE + _str + cls.COLOR_OFF

    @classmethod
    def bpurple(cls, _str):
        return cls.BPURPLE + _str + cls.COLOR_OFF

    @classmethod
    def bcyan(cls, _str):
        return cls.BCYAN + _str + cls.COLOR_OFF

    @classmethod
    def bwhite(cls, _str):
        return cls.BWHITE + _str + cls.COLOR_OFF


def main(argv=sys.argv):
    ask_user()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
