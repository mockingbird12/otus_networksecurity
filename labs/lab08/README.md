[Мониторинг состояния сети  помощью Python]

На атакуемом смотрим arp-таблицу:
```
arp -v
```
![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab08/arp_before_attack.jpg)

Запускаем скрипт python3 main.py на атакуемом.

Запускаем arp_spoof на атакующем.

![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab08/arp_spoof.jpg)

Смотрим на атакуемом arp-таблицу:

![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab08/arp_after_attack.jpg)

Вывод скрипта атакуемого:

![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab08/arp_spoof_detector.jpg)

Проверяем письмо в ящике:

![alt-текст](https://github.com/mockingbird12/otus_networksecurity/blob/main/labs/lab08/mail_receive.jpg)
