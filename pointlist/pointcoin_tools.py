__author__ = 'ben'

import os
import json
from subprocess import Popen, PIPE
from pointlist.models import PointcoinAddress
from os import chdir, getcwd

PASSWORD = 'ILovePoints'
def get_new_address():
    '''
    This function gets a vanity address associated with the master wallet
    :return: new address
    '''
    lastdir = getcwd()
    chdir('/home/ubuntu/pointlist/pointlist')
    process = Popen(['./pointctl', '--wallet', 'walletpassphrase', PASSWORD], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    process = Popen(['./pointctl', '--wallet', 'getnewaddress'], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    chdir(lastdir)
    return output.strip()

def check_balance(address):
    '''
    This function takes in an address and returns the balance of that address
    :param address:
    :return: balance
    '''
    lastdir = getcwd()
    chdir('/home/ubuntu/pointlist/pointlist')
    process = Popen(['./pointctl', '--wallet', 'walletpassphrase', PASSWORD], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    process = Popen(['./pointctl', '--wallet', 'listreceivedbyaddress'], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    chdir(lastdir)
    return get_balance(output, address)

def get_balance(output, address):
    '''
    This function takes in the output from listreceievedbyaddress
    and an address to check the balance of and gets the balance
    :param output:
    :param address:
    :return:
    '''
    data = json.loads(output)
    for line in data:
        if line['address'] == address:
            return line['amount']
    return 0

def update_last_balance(address):
    '''
    This function updates the last_balance field of the passed in address
    :param address:
    :return:
    '''
    addr = PointcoinAddress.objects.get(address=address)
    addr.last_balance = check_balance(address)
    return True

def spend(amount, toAddress, fromAddress):
    '''
    This function spends the amount of pointcoin specified using
    transactions in the fromAddress to the toAddress
    :param amount:
    :param toAddress:
    :param fromAddress:
    :return: true if successful
    '''
    address = PointcoinAddress.objects.get(address=fromAddress)
    if address.current_amount < amount:
        print 'Not Successful, not enough funds'
        return False
    lastdir = getcwd()
    chdir('/home/ubuntu/pointlist/pointlist')
    # Logging into the wallet
    process = Popen(['./pointctl', '--wallet', 'walletpassphrase', PASSWORD], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    # Spending the pointcoin!
    process = Popen(['./pointctl', '--wallet', 'sendfrom', '\"\"',
                    '\"' + toAddress + '\"', amount], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    chdir(lastdir)
    if len(output) == 64 and ':' not in output:
        address.current_amount = address.current_amount - amount
        address.save()
        return True
    return False