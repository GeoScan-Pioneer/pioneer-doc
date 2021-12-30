Настройка сети
========================

Изменение настроек Wi-Fi точки доступа
---------------------------------------
1. Введите в терминале:
   
.. code-block:: bash

   sudo nano /etc/hostapd/hostapd.conf

Вы увидите список настроек сети:

.. image:: ../const/media/network/hostapd.png
   :alt: Похоже, картинка не загрузилась :c 
   :align: center
   :scale: 65%

2. Для изменения имени Wi-Fi точки доступа поменяйте значение параметра **ssid**

3. Для изменения пароля Wi-FI поменяйте значение параметра **wpa_passphrase**
   
.. hint:: По умолчанию имя точки - **Geoscan**, пароль - **geoscan123**

5. После внесения изменений, нажмите *Ctrl+X*, затем *Y* и *Enter*
6. Перезапустите Raspberry Pi 
   
.. code-block:: bash

   sudo reboot

Подключение коптера к внешней Wi-Fi сети
------------------------------------------

Для подключения коптера к существующей Wi-Fi сети потребуется подключиться к коптеру любым удобным способом,
кроме его Wi-Fi точки доступа (по умолчанию Geoscan)

Это может быть как подключение клавиатуры и монитора (с помощью microHDMI-кабеля),
так и подключение коптера к любой сети по ethernet-кабелю, для использования с помощью ssh.

Подробнее об использовании коптера, подключенного по ethernet:
:doc:`ethernet`

.. Процещуру включения HDMI нужно описать на отдельной странице (из-за измененного uboot) и сделать ссылку сюда

Теперь, с помощью методов работы с коптером, описанных выше, можно приступать к подключению к другой Wi-Fi сети.

1. Поочерёдно введите в терминале следующие команды:
   
.. code-block:: bash

   sudo systemctl disable config-wlan
   sudo systemctl stop isc-dhcp-server
   sudo systemctl disable isc-dhcp-server
   sudo systemctl stop hosatpd
   sudo systemctl disable hostapd
   sudo systemctl enable NetworkManager
   sudo systemctl start NetworkManager

После этого сервисы, отвечающие за точку доступа коптера, отключатся, и включится утилита NetworkManager.

Для работы с утилитой NetworkManger используется команда **nmcli**.
Все действия с сетью рекомендуется выполнять от имени администратора **sudo**

2. Выведем список доступных Wi-Fi сетей:

.. code-block:: bash

    nmcli device wifi list

3. Подключаемся к Wi-Fi сети:

.. code-block:: bash

    nmcli device wifi connect "<ssid сети (имя)>" password <пароль> name "<имя для взаимодействия>>"

Пример для подключения к wifi сети Geoscan с паролем geoscan123:

.. code-block:: bash

    nmcli device wifi connect "Geoscan" password geoscan123 name "geowifi"

Имя geowifi будет использоваться при работе с сетью в дальнейшем с помощью nmcli

Например для того, чтобы отключиться от сети, потребуется ввести команду: 

.. code-block:: bash

    nmcli con down geowifi
