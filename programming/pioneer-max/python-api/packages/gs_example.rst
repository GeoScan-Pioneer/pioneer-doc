Пакет gs_example
==================
.. contents:: 
   :depth: 3

Описание
--------------

В данном пакете находятся базовые примеры работы с Пионер Макс

Состав пакета
---------------

Ноды
~~~~~~~~
    * board_test.py - пример получения бортовой информации
    * flight_test.py - пример управления автопилотом в локальных координатах
    * flight_global_test.py - пример управления автопилотом в глобальных координатах
    * led_test.py - пример управления светодиодами
    * logger_test.py - пример взаимодействия с логами
    * sensors_test.py - пример взаимодействия с бортовыми сенсорами
    * navigation_test.py - пример взаимодействия с системами навигации
    * cargo_test.py - пример взаимодействия с модулем магнитного захвата

Файлы запуска (launch)
~~~~~~~~~~~~~~~~~~~~~~~~
    * test_board.launch - пример запуска board_test
    * test_flight.launch - пример запуска flight_test
    * test_flight_global.launch - пример запуска flight_global_test
    * test_led.launch - пример запуска led_test
    * test_sensors.launch - пример запуска sensors_test
    * test_navigation.launch - пример запуска navigation_test

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
