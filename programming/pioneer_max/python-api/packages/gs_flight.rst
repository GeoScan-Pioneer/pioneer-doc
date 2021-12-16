Пакет gs_flight
===================
.. contents:: 
   :depth: 3

Описание
--------------

Данный пакет предоставляет инструменты для взаимодействия с автопилотом.

Состав пакета
-----------------

Классы
~~~~~~~~
* FlightController
* CallbackEvent

Описание классов
-----------------------------

FlightController
~~~~~~~~~~~~~~~~~
Класс взаимодействия с автопилотом

Создание объекта класса
""""""""""""""""""""""""""""""""""""""""""""
.. class:: FlightController

.. py:class:: fc = FlightController(callback)

    :аргументы: callback-функция
    :return: объект класса FlightController

    Cоздаёт объект класса FlightController.

Доступные поля класса
""""""""""""""""""""""""""""""""""""""""

* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __event_service - rospy.ServiceProxy: gs_interfaces.srv.Event
* __yaw_service - rospy.ServiceProxy: gs_interfaces.srv.Yaw
* __local_position_service- rospy.ServiceProxy: gs_interfaces.srv.Position
* __global_position_service - rospy.ServiceProxy: gs_interfaces.srv.PositionGPS
* __callback_event - rospy.Subscriber: std_msgs.msg.Int32

Описание методов
"""""""""""""""""""""""""""""""

.. py:classmethod:: goToLocalPoint()

    :аргументы: x,y,z,time - координаты в локальной системе позиционирования, время полёта в точку
    :return: bool

    Приказывает автопилоту лететь в локальные координаты, x - координата точки по оси x, в метрах , y - координата точки по оси y, в метрах, z- координата точки по оси z, в метрах, time - время, за которое коптер перейдет в следующую точку, в секундах. Если значение не указано, коптер стремится к точке с максимальной скоростью

.. py:classmethod:: goToPoint()

    :аргументы: latitude,longitude,altitude 
    :return: bool

    Приказывает автопилоту лететь в GPS координаты, latitude – задается широта в градусах, умноженных на 10^(-7), longitude – задается долгота в градусах, умноженных на 10^(−7), altitude – задается высота в метрах

.. py:classmethod:: updateYaw()

    :аргументы: angle - угол поворота в радианах
    :return: bool

    Устанавливает рыскание


.. py:classmethod:: preflight()

    :аргументы: нет
    :return: bool

    Приказывает автопилоту выполнить предвзлётную подготовку


.. py:classmethod:: takeoff()

    :аргументы: нет
    :return: bool

    Приказывает автопилоту выполнить взлёт


.. py:classmethod:: landing()

    :аргументы: нет
    :return: bool

    Приказывает автопилоту произвести посадку


.. py:classmethod:: disarm()

    :аргументы: нет
    :return: bool

    Приказывает автопилоту заглушить двигатели

Используемые сервисы ROS
"""""""""""""""""""""""""""""""
* geoscan/alive (gs_interfaces/Live)
* geoscan/flight/set_event (gs_interfaces/Event)
* geoscan/flight/set_yaw (gs_interfaces/Yaw)
* geoscan/flight/set_local_position (gs_interfaces/Position)
* geoscan/flight/set_global_position (gs_interfaces/PositionGPS)

Используемые топики ROS
"""""""""""""""""""""""""""""""
* geoscan/flight/callback_event (std_msgs/Int32)

CallbackEvent
~~~~~~~~~~~~~~
Энумератор событий автопилота 

Доступные значения
""""""""""""""""""""""

* ALL - пустое событие
* COPTER_LANDED - приземлился
* LOW_VOLTAGE1 - низкий заряд АКБ, но заряда хватит, чтобы вернуться домой
* LOW_VOLTAGE2 - низкий заряд АКБ, начата экстренная посадка
* POINT_REACHED - точка достигнута
* POINT_DECELERATION - близко к заданной точке
* TAKEOFF_COMPLETE - взлет выполнен
* ENGINES_STARTED - двигатели запущены
* SHOCK - сильный удар, возможна потеря управления


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

    * gs_interfaces
    * gs_core
    * std_msgs
    * geometry_msgs

Примечание
-----------------------------

Все классы в данном пакете могут быть использованы только при запущеной ноде ros_plaz_node.py из пакета gs_core