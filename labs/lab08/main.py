#!/usr/bin/env python
import scapy.all as scapy
import smtplib
import config

def get_mac(ip):
    ''' Get mac address by ip '''
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_req_broadcast = broadcast/arp_req
    resp_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]

    return resp_list[0][1].hwsrc


def send_alarm(email, password):
    print('Alarm!')
    print(email)
    print(password)
    message = 'ARP-attack!'
    server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
    server.set_debuglevel(1)
    server.ehlo(email)
    server.login(email, password)
    server.auth_plain()
    server.sendmail(email, email, message)
    server.quit()
    return 1

mail_send = 0
def process_sniffed_packet(packet):
   global mail_send
   if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
      try:
         real_mac = get_mac(packet[scapy.ARP].psrc)
         response_mac = packet[scapy.ARP].hwsrc
         if real_mac != response_mac and mail_send==0:
            print('ALARM! ARP-spoofing attack was detected!')
            mail_send = send_alarm(config.email_login,config.email_password)
      except IndexError:
         pass



def sniff(interface):
   scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

sniff(config.interface) 
