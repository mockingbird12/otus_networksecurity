Административные роли

Схема сети:

![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab01/admin_roles.jpg)

Настроил ip-адреса на маршрутизаторах:

<b>R1(config)# interface g0/0/0

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

Настроил AAA и создал ползователя которому разрешены команды show, conf t, debug:

<b>
R1# configure terminal

R1(config)# parser view admin1

R1(config-view)# secret admin1pass

R1(config-view)# commands exec include all show

R1(config-view)# commands exec include all config terminal

R1(config-view)# commands exec include all debug

R1(config-view)# end
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
