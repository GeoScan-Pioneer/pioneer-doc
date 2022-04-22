Пакет gs_core
==============
.. contents:: 
   :depth: 3

Описание
----------

В данном пакете находятся необходимые основные ноды для корректной работы Geoscan Pioneer Max

Состав пакета
---------------------

Ноды
~~~~~~~~
   * ros_plaz_node - основная нода, связь с базовой платой Пионер

Файлы запуска (launch)
~~~~~~~~~~~~~~~~~~~~~~~~
   
    * pioneer.launch - запуск системы
  
Python скрипты
~~~~~~~~~~~~~~~
   
    * restart.py - перезапуск базовой платы Пионер

Описание нод
-----------------

ros_plaz_node
~~~~~~~~~~~~~~
Нода связи по протоколу plazlink между полетным контроллером Geoscan Pioneer и микрокомпьютером

**Параметры:**

* port *(String)* - название UART порта, в который подключена базовая плата Пионер (по умолчанию: /dev/ttyS0), обязательный параметр

**Сервисы:**

* geoscan/alive (gs_interfaces/Live) - возвращает статус соединения
* geoscan/get_log (gs_interfaces/Log) - возвращает лог
* geoscan/flight/set_event (gs_interfaces/Event) - приказывает автопилоту выполнить Event
* geoscan/flight/set_yaw (gs_interfaces/Yaw) - приказывает автоплоту выполнить рысканье
* geoscan/flight/set_local_position (gs_interfaces/Position) - приказывает автопилоту выполнить перемещение в локальных координатах
* geoscan/flight/set_global_position (gs_interfaces/PositionGPS) - приказывает автопилоту выполнить перемещение в глобальных координатах
* geoscan/led/board/set (gs_interfaces/Led) - управление светодиодами на плате Geoscan Pioneer
* geoscan/led/module/set (gs_interfaces/Led) - управление светодиодами на LED модуле
* geoscan/board/get_info (gs_interfaces/Info) - возвращает бортовой номер
* geoscan/board/get_time (gs_interfaces/Time) - возвращает время с момента включения коптера
* geoscan/board/get_uptime (gs_interfaces/Time) - возвращает время запуска для системы навигации
* geoscan/board/get_flight_time (gs_interfaces/Time) - возвращает время с начала полета
* geoscan/board/get_parameters (gs_interface/ParametersList) - возварщает параметры АП
* geoscan/board/set_parameters (gs_interface/SetParametersList) - устанавливает параметры АП
* geoscan/board/restart (std_srvs/Empty) - перезагружает базовую Плату Пионер
* geoscan/navigation/get_system (gs_interfaces/NavigationSystem) - возвращает текущую систему позиционирования
* geoscan/navigation/set_system (gs_interfaces/SetNavigationSystem) - устанавливает систему позиционирования

**Топики:**

* geoscan/log (std_msgs/String) - последнее сообщение лога
* geoscan/battery_state (gs_interfaces/SimpleBatteryState) - состояние АКБ
* geoscan/navigation/local/position (geometry_msgs/Point) - локальные координаты в ситеме LPS
* geoscan/navigation/local/yaw (std_msgs/Float32) - угол поворота в системе LPS
* geoscan/navigation/local/velocity (geometry_msgs/Point) - скорость коптера возвращаемая LPS
* geoscan/navigation/global/position (gs_interfaces/PointGPS) - глобальные координаты GPS
* geoscan/navigation/global/status (std_msgs/Int8) - статус GPS модуля
* geoscan/navigation/satellites (gs_interfaces/SatellitesGPS)- количество спутников
* geoscan/navigation/opt/velocity (gs_interfaces/OptVelocity) - данные с модуля оптического потока (OPT)
* geoscan/flight/callback_event (std_msgs/Int32) - события вытопилота
* geoscan/sensors/gyro (geometry_msgs/Point) - данные c гироскопа
* geoscan/sensors/accel (geometry_msgs/Point) - данные c акселерометра
* geoscan/sensors/orientation (gs_interfaces/Orientation) - данные положения
* geoscan/sensors/altitude (std_msgs/Float32) - данные высоты по барометр
* geoscan/sensors/mag (geometry_msgs/Point) - данные магнитометра

Описание Python скриптов
-----------------------------
restart.py
~~~~~~~~~~~~~~
При выполнении перезапускает базовую плату Пионер

Необходимые пакеты
-----------------------------

**Python:**

  * PySerial

**ROS:**

  * gs_interfaces 
  * geometry_msgs
  * std_msgs
  * std_srvs

Использование
-----------------------------

.. code-block::
    :caption: Установка порта подключения базовой платы Пионер на /dev/ttyS0

    rosparam set ros_plaz_node/port /dev/ttyS0

.. code-block::
    :caption: Запуск ros_plaz_node

    rosrun gs_core ros_plaz_node.py