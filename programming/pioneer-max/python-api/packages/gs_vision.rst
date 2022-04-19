Пакет gs_vision
====================
.. contents:: 
   :depth: 3

Описание
-------------

Данный пакет предоставляет готовые инструменты распознавания различных меток

Состав пакета
-----------------

Ноды
~~~~~~~~
    * apriltag_node.py
    * aruco_node.py
    * qrcode_node.py

Файлы запуска (launch)
~~~~~~~~~~~~~~~~~~~~~~~~
    * apriltag_test.launch - пример запуска apriltag_node
    * aruco_test.launch - пример запуска aruco_node
    * qrcode_test.launch - пример запуска qrcode_node

Типы сообщений
~~~~~~~~~~~~~~
    * QR.msg
    * ArUco.msg
    * Apriltag.msg
    * QR_array.msg
    * ArUco_array.msg
    * Apriltag_array.msg

Описание нод
-----------------------------
restart.py
~~~~~~~~~~~~~~
При выполнении перезапускает базовую плату Пионер

Необходимые пакеты
-----------------------------

**Python:**

    * gs_board
    * gs_flight
    * gs_module
    * gs_logger
    * gs_sensors
    * gs_navigation

**ROS:**

    * gs_core
    * gs_interfaces

Использование
-----------------------------

*Для работы всех (кроме cargo_test.py) требуется запущенная ros_plaz_node из пакета gs_core*

.. code-block:: ros
    :caption: Запуск ros_plaz_node с помощью утилиты rospioneer (перед запуском примеров в отдельном окне терминала)

    rospioneer start

.. code-block:: ros
    :caption: Запуск примера управления светодиодами напрямую

    rosrun gs_example led_test.py --screen

.. code-block:: ros
    :caption: Запуск примера управления светодиодами с помощью лаунч файла

    roslaunch gs_example test_led.launch --screen

.. hint:: Параметр "--screen" отвечает за вывод отладочной информации в консоль
