Линукс сервисы Пионер Макс
----------------------------

Для каждого из веб инструментов работы с Пионер Макс существуют по два linux-сервиса - для ethernet и wlan0 подключения.

Сервисы запускаются автоматически при старте Raspberry, если интерфейс wlan0 или eth отключён, то сервисы для него выключаются.

.. warning:: Все действия с сервисами требуется выполнять от имени администратора с помощью sudo

.. code-block:: bash
    :caption: Включить сервис

    sudo systemctl start <название сервиса>  

.. code-block:: bash
    :caption: Выключить сервис

    sudo systemctl stop <название сервиса>  

.. code-block:: bash
    :caption: Перезагрузить работающий сервис

    sudo systemctl restart <название сервиса>

.. code-block:: bash
    :caption: Включить автозапуск сервиса при старте Raspberry

    sudo systemctl enable <название сервиса>  

.. code-block:: bash
    :caption: Выключить автозапуск сервиса при старте Raspberry

    sudo systemctl disable <название сервиса>  

.. csv-table:: Названия сервисов
   :header: "Утилита", "wlan0", "eth"
   :widths: 15, 20, 20

    "Butterfly","wlan-butterfly","eth-butterfly"
    "Code-OSS","code-server-wlan","code-server-eth"
    "WebMenu","web-wlan-menu","web-eth-menu"
    "MissionControl","mission-control-wlan","mission-control-eth"


Пример использования:

.. code-block:: bash
    :caption: Перезапустить сервис buttefly для интерфейса wlan0

    sudo systemctl restart wlan-butterfly
