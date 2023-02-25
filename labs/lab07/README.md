## Вывод url-адресов из scrapy
Запрос со стороны атакуемого:
![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab07/source_url.jpg)


Вывод на стороне атакующего:
![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab07/hacker_url.jpg)

## Из данного дампа трафика мы увидели, что передовался конфиг роутера

Передовался конфиг
![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab07/tftp-config.jpg)
```
! Last configuration change at 20:55:45 UTC Fri Mar 3 2017 by weberjoh
! NVRAM config last updated at 21:02:36 UTC Fri Mar 3 2017 by weberjoh
! NVRAM config last updated at 21:02:36 UTC Fri Mar 3 2017 by weberjoh
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
service password-encryption
!
hostname CCNP-LAB-R2
!
boot-start-marker
boot-end-marker
!
!
enable secret 5 $1$Z.9j$Nvobsx9NvJzqtRLQqR.9b0
!
aaa new-model
!
!
aaa group server radius foobar
 server name blubb

!
aaa authentication login default group radius local-case
aaa authentication login johndoe group foobar local-case none
!
!
!
!
!
aaa session-id common
!
clock timezone UTC 1 0
clock summer-time UTC recurring last Sun Mar 2:00 last Sun Oct 3:00
!
dot11 syslog
ip source-route
!
!
ip cef
!
ip dhcp excluded-address 192.168.10.1 192.168.10.10
ip dhcp excluded-address 192.168.20.1 192.168.20.10
ip dhcp excluded-address 192.168.30.1 192.168.30.10
!
ip dhcp pool VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1 
 dns-server 192.168.120.22 
 domain-name webernetz.net
 option 42 ip 46.4.88.180 212.227.54.68 37.120.191.245 
 option 150 ip 192.168.110.10 
!
ip dhcp pool VLAN20
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1 
 dns-server 192.168.120.22 
 option 42 ip 46.4.88.180 212.227.54.68 37.120.191.245 
 option 150 ip 192.168.110.10 
 domain-name webernetz.net
!
ip dhcp pool VLAN30
 network 192.168.30.0 255.255.255.0
 default-router 192.168.30.1 
 dns-server 192.168.120.22 
 domain-name webernetz.net
 option 42 ip 46.4.88.180 212.227.54.68 37.120.191.245 
 option 150 ip 192.168.110.10 
!
!
ip domain name webernetz.net
ip name-server 2003:51:6012:120::A08:53
ipv6 unicast-routing
ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
!
!
!
!
voice-card 0
!
crypto pki token default removal timeout 0
!
crypto pki trustpoint TP-self-signed-1253431187
 enrollment selfsigned
 subject-name cn=IOS-Self-Signed-Certificate-1253431187
 revocation-check none
 rsakeypair TP-self-signediAzyAO-1253431187
!
!
crypto pki certificate chain TP-self-signed-1253431187
 certificate self-signed 01 nvram:IOS-Self-Sig#2.cer
!
!
license udi pid CISCO2811 sn FCZ115171R6
archive
 path tftp://192.168.110.10/$h-$t
 write-memory
username weberjoh privilege 15 secret 5 $1$kI2F$Sz18KSQV/D/QJpbpIGpH10
!
redundancy
!
!
ip ssh version 2
! 
!
!
!
!
!
!
!
interface FastEthernet0/0
 no ip address
 shutdown
 duplex auto
 speed auto
!
interface FastEthernet0/1
 no ip address
 duplex auto
 speed auto
!
interface FastEthernet0/1.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ip verify unicast source reachable-via rx
 ipv6 address 2003:51:6012:122::1/64
 ipv6 rip CCNPv6 enable
!
interface FastEthernet0/1.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ip verify unicast source reachable-via rx
!
interface FastEthernet0/1.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ip verify unicast source reachable-via rx
!
interface FastEthernet0/1.121
 encapsulation dot1Q 121
 ip address 192.168.121.2 255.255.255.0
 ip verify unicast source reachable-via rx allow-default
 ipv6 address 2003:51:6012:121::2/64
 ipv6 rip CCNPv6 enable
!
interface Serial0/0/0
 no ip address
 shutdown
 no fair-queue
 clock rate 2000000
!
interface Serial0/0/1
 no ip address
 shutdown
 clock rate 2000000
!
router rip
 version 2
 network 192.168.10.0
 network 192.168.20.0
 network 192.168.30.0
 network 192.168.121.0
!
ip forward-protocol nd
no ip http server
ip http secure-server
!
!
!
ip sla 260720081
 icmip-echo 2A01:488:42:1000:50ED:8588:8A:C570
ip sla schedule 260720081 life forever start-time now
ip sla 260720082
 dns blog.webernetz.net name-server 192.168.120.22
ip sla schedule 260720082 life forever start-time now
ip sla 260720083
 icmp-jitter 192.168.120.1
ip sla schedule 260720083 life forever start-time now
ip sla 260720084
 udp-jitter 192.168.121.254 65535
ip sla schedule 260720084 life forever start-time now
ip sla 260720085
 udp-jitter 192.168.121.253 65534
ip sla schedule 260720085 life forever start-time now
logging 192.168.120.10
access-list 1 permit 192.168.0.0 0.0.255.255 log
access-list 1 deny   any log
ipv6 router rip CCNPv6
 timers 10 30 10 20
!
!
!
!
!
snmp-server community n5rAD1ig314IqfioYBWw RO
snmp-server ifindex persist
snmp-server contact Johannes Weber
!
!
!
radius server blubb
 address ipv6 2001:DB8::1812 auth-port 1812 acct-port 1813
!
!
ipv6 access-list vty-access
 permit ipv6 2003:51:6012::/48 any log
 deny ipv6 any any log
!
control-plane
!
!
!
!
mgcp profile default
!
!
!
!
!
!

line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 access-class 1 in
 exec-timeout 0 0
 privilege level 15
 ipv6 access-class vty-access in
 transport input ssh
line vty 5 15
 access-class 1 in
 ipv6 access-class vty-access in
 transport input all
!
scheduler allocate 20000 1000
ntp update-calendar
ntp server ipv6 2.de.pool.ntp.org
ntp server ipv6 2.pool.ntp.org
ntp server ntp1.webernetz.net prefer
ntp server ntp2.webernetz.net prefer
end
```
