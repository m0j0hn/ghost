#!/usr/bin/python
import random

ADDRESSES = ['mkdbscrEwzz1TEP9uHUkY5yVtPPBj7Bemq2',
             'm24BdlawfalT3SLdj1ndlajfIIdan93pazt',
             'mAPlua4s6lUsAh4bsaleiJLISv72Jslckaw']

deposited = False

def get_new_address():
    return random.choice(ADDRESSES)

def getreceivedbyaddress(address):
    if deposited:
        return 0
    deposited = True
    return 10

def send_bitcoins(address,amount):
    return True