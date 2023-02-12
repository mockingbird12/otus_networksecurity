# ARP-spoofing


На атакуемом смотрим arp-таблицу:
```
arp -v
```
![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab05/before.jpg)

Затем на атакущем мы изменям main.py вводим туда данные об атакуемом.
Запускаем через python3 main.py

Снова смотрим arp-таблицу на атакуемом:

![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab05/after.jpg)
Из нее мы видим, что mac-адрес шлюза изменился на mac атакующего.

Чтобы трафик проходил через атакующего, на нем нужно прописать
```
systemctl -w net.ipv4.ip_forward=1
```
Но на атакуемом возникнет дублирование пакетов, т.к. ему будет отвечать и роутер и атакующий.