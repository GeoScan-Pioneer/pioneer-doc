Пакет gs_sensors
=====================================
.. contents:: 
   :depth: 3

Описание
----------------
Пакет gs_sensors представлены инструменты для получение данных с сенсоров

.. warning:: Все классы в данном пакете могут быть использованы только при запущеной ноде ros_plaz_node.py из пакета gs_core

Состав пакета
-------------------------

Классы
~~~~~~~

* SensorManager

Ноды
~~~~~~~

* ultraconis_node

Описание классов
-------------------------------

SensorManager
~~~~~~~~~~~~~~~~~~~~

Класс менеджера бортовой информации.

.. important:: Данный класс является оберткой для сервисов и топиков ROS.

.. contents::
   :local:

.. highlight:: python

Создание объекта класса
""""""""""""""""""""""""""""""""""""""""""""

.. class:: SensorManager

.. py:class:: board = SensorManager()

    :аргументы: нет
    :return: объект класса SensorManager

    Cоздаёт объект класса SensorManager.

Доступные поля класса
""""""""""""""""""""""""""""""""""""""""

    * error_number - float
    * __battery_state - gs_interfaces.msg.SimpleBatteryState
    * __gyro - geometry_msgs.msg.Point
    * __accel - geometry_msgs.msg.Point
    * __orientation - gs_interfaces.msg.Orientation
    * __altitude - float
    * __mag - geometry_msgs.msg.Point
    * __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
    * __gyro_subscriber - rospy.Subscriber: geometry_msgs.msg.Point
    * __accel_subscriber - rospy.Subscriber: geometry_msgs.msg.Point
    * __orientation_subscriber - rospy.Subscriber: gs_interfaces.msg.Orientation
    * __altitude_subscriber - rospy.Subscriber: std_msgs.msg.Float32
    * __mag_subscriber - rospy.Subscriber: geometry_msgs.msg.Point
    * __power_subscriber - rospy.Subscriber: gs_interfaces.msg.SimpleBatteryState

Описание методов
"""""""""""""""""""""""""""""""

.. py:classmethod:: gyro()

    :аргументы: нет
    :return: gx, gy, gz

    Возвращает данные c гироскопа.

.. py:classmethod:: accel()

    :аргументы: нет
    :return: ax, ay, az

    Возвращает данные c акселерометра.

.. py:classmethod:: orientation()

    :аргументы: нет
    :return: roll, pitch, azimuth

    Возвращает данные положения.

.. py:classmethod:: altitude()

    :аргументы: нет
    :return: float

    Возвращает данные высоты по барометру.

.. py:classmethod:: mag()

    :аргументы: нет
    :return: mx, my, mz

    Возвращает данные с магнитометра.

.. py:classmethod:: power()

    :аргументы: нет
    :return: charge, seconds

    Возвращает заряд АКБ.

Используемые сервисы ROS
"""""""""""""""""""""""""""""""""""""""""""

 * geoscan/alive (gs_interfaces/Live)

Используемые топики ROS
"""""""""""""""""""""""""""""""""""""""""
 * geoscan/sensors/gyro (geometry_msgs/Point)
 * geoscan/sensors/accel (geometry_msgs/Point)
 * geoscan/sensors/orientation (gs_interfaces/Orientation)
 * geoscan/sensors/altitude (std_msgs/Float32)
 * geoscan/sensors/mag (geometry_msgs/Point)
 * geoscan/battery_state (gs_interfaces/SimpleBatteryState)

Описание нод
-------------------
ultraconis_node
~~~~~~~~~~~~~~~
Нода ультразвукового датчика HC-SR04

**Параметры:**

* trig - номер GPIO порта, соответствующий TRIG

* echo - номер GPIO порта, соответствующий ECHO

**Топики:**

* ultrasonic_sensor/trig_<номер TRIG порта>_echo_<номер ECHO порта> (std_msgs/Float32)

Необходимые пакеты
-----------------------------

**Python:**

    * RPi.GPIO

**ROS:**

    * gs_core
    * gs_interfaces
    * std_msgs
    * geometry_msgs

Примечание
-----------------------------

Все классы в данном пакете могут быть использованы только при запущеной ноде ros_plaz_node.py из пакета gs_core
