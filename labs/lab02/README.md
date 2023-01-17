Настройка бзопасности

Схема сети:

![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab02/schem.jpg)

Основные настройки маршрутизаторов:

<b>
R1(config)# hostname R1

R1(config)# interface g0/0/0

R1(config-if)# ip address 10.1.1.1 255.255.255.0

R1(config-if)# no shutdown

R1(config)# interface g0/0/1

R1(config-if)# ip address 192.168.1.1 255.255.255.0

R1(config-if)# no shutdown

</b>

Настроил OSPF:

<b>
R1(config)# router ospf 1

R1(config-router)# network 192.168.1.0 0.0.0.255 area 0

R1(config-router)# network 10.1.1.0 0.0.0.3 area 0

R2(config)# router ospf 1

R2(config-router)# network 10.1.1.0 0.0.0.3 area 0

R2(config-router)# network 10.2.2.0 0.0.0.3 area 0

R3(config)# router ospf 1

R3(config-router)# network 10.2.2.0 0.0.0.3 area 0

R3(config-router)# network 192.168.3.0 0.0.0.255 area 0

</b>

Базовые настройки безопасности:

<b>
enable  

configure terminal 

service password-encryption  

security passwords min-length 10  

enable algorithm-type scrypt secret cisco12345 

ip domain name netsec.com  

username user01 algorithm-type scrypt secret user01pass  

username admin privilege 15 algorithm-type scrypt secret adminpasswd 

banner motd " Unauthorized access is strictly prohibited! "  

line con 0  

 exec-timeout 5 0  

login local  

 logging synchronous  

line aux 0

 exec-timeout 5 0

login local

line vty 0 4

 exec-timeout 5 0

 privilege level 15

transport input ssh

 login local

crypto key generate rsa general-keys modulus 1024

ip ssh time-out 90

ip ssh authentication-retries 2

ip ssh version 2

</b>

Затем создал пользователя с командами только show:

<b>
R1# configure terminal

R1(config)# parser view admin2

R1(config-view)# secret admin2pass

R1(config-view)# commands exec include all show

R1(config-view)# end
</b>

Создал пользователя только с определенными коммандами show:

<b>
R1(config)# parser view tech

R1(config-view)# secret techpasswd

R1(config-view)# commands exec include show version

R1(config-view)# commands exec include show interfaces

R1(config-view)# commands exec include show ip interface brief

R1(config-view)# commands exec include show parser view

R1(config-view)# end
</b>

На роутере R3 запустил автоматические настройки безопасности:

<b>
	R3# auto secure
</b>