Пакет gs_navigation
========================
.. contents:: 
   :depth: 3


Описание
----------------
Данный пакет предоставляет инструменты для работы с системами позиционирования

Состав пакета
-------------------------
Классы
~~~~~~~~
* GlobalNavigation (приватный)
* LocalNavigation (приватный)
* OpticalFlow (приватный)
* NavigationManager

Описание классов
-------------------------------
GlobalNavigation
~~~~~~~~~~~~~~~~~
Класс взаимодействия с глобальной системой навигации

Инициализация
""""""""""""""""""""""""""""""""""""""""""""
.. class:: GlobalNavigation

.. py:class:: gn = GlobalNavigation(alive, navSystem)

    :аргументы: alive, navSystem - сервисы
    :return: объект класса GlobalNavigation

    Cоздаёт объект класса GlobalNavigaton.

Доступные поля класса
""""""""""""""""""""""""""""""""""""""""
* name - str
* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __nav_service - rospy.ServiceProxy: gs_interfaces.srv.NavigationSystem
* __global_position - gs_interfaces.msg.PointGPS
* __satellites - gs_interfaces.msg.SatellitesGPS
* __global_status - std_msgs.msg.Int8
* __global_position_subscriber - rospy.Subscriber: gs_interfaces.msg.PointGPS
* __satellites_subscriber - rospy.Subscriber: gs_interfaces.msg.SatellitesGPS
* __global_status_subscriber - rospy.Subscriber: std_msgs.msg.Int8


Описание методов
"""""""""""""""""""""""""""""""

.. py:classmethod:: position()

    :аргументы: None
    :return: gs_interfaces/PointGPS

    Получить глобальные GPS координаты


.. py:classmethod:: satellites()

    :аргументы: None
    :return: gs_interfaces/SatellitesGPS

    Получить количество спутников


.. py:classmethod:: status()

    :аргументы: None
    :return: std_msgs/Int8

    Получить статус системы позиционирования


Используемые топики
"""""""""""""""""""""""""""""""""""""

* geoscan/navigation/global/position (gs_interfaces/PointGPS)
* geoscan/navigation/satellites (gs_interfaces/SatellitesGPS)
* geoscan/navigation/global/status (std_msgs/Int8)

LocalNavigation
~~~~~~~~~~~~~~~~
Класс взаимодействия с локальной системой навигации

Инициализация
""""""""""""""""""""""""""""""""""""""""""""
.. class:: LocalNavigation

.. py:class:: ln = LocalNavigation(alive, navSystem)

    :аргументы: alive, navSystem - сервисы
    :return: объект класса LocalNavigation

    Cоздаёт объект класса LocalNavigaton.

Доступные поля класса
""""""""""""""""""""""""""""""""""""""""
* name - str
* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __nav_service - rospy.ServiceProxy: gs_interfaces.srv.NavigationSystem
* __local_position - geometry_msgs.msg.Point
* __local_velocity - geometry_msgs.msg.Point
* __local_yaw - int
* __local_position_subscriber - rospy.Subscriber: geometry_msgs.msg.Point
* __local_velocity_subscriber - rospy.Subscriber: geometry_msgs.msg.Point
* __local_yaw_subscriber - rospy.Subscriber: std_msgs.msg.Float32

Описание методов
"""""""""""""""""""""""""""""""

.. py:classmethod:: position()

    :аргументы: None
    :return: geometry_msgs/Point

    Получить LPS координаты


.. py:classmethod:: velocity()

    :аргументы: None
    :return: geometry_msgs/Point

    Возвращает скорость коптера возвращаемую LPS (vx,vy,vz)


.. py:classmethod:: yaw()

    :аргументы: None
    :return: std_msgs/Float32

    Возвращает угол поворота в системе LPS

Использование топики
"""""""""""""""""""""""""""""""""""""""
* geoscan/navigation/local/position (geometry_msgs/Point)
* geoscan/navigation/local/velocity (geometry_msgs/Point)
* geoscan/navigation/local/yaw (std_msgs/Float32)


OpticalFlow
~~~~~~~~~~~~
Класс взаимодействия с модулем оптического потока (OPT)

Инициализация
""""""""""""""""""""""""""""""""""""""""""""
.. class:: OpticalFlow

.. py:class:: opt = OpticalFlow(alive, navSystem)

    :аргументы: alive, navSystem - сервисы
    :return: объект класса OpticalFlow

    Cоздаёт объект класса LocalNavigaton.

Доступные поля класса
""""""""""""""""""""""""""""""""""""""""
* name - str
* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __nav_service - rospy.ServiceProxy: gs_interfaces.srv.NavigationSystem
* __opt_velocity - gs_interfaces.msg.OptVelocity
* __opt_velocity_subscriber - rospy.Subscriber: gs_interfaces.msg.OptVelocity

Описание методов
"""""""""""""""""""""""""""""""

.. py:classmethod:: velocity()

    :аргументы: None
    :return: gs_interfaces/OptVelocity

    Получить информацию с модуля оптического потока (OPT)

Используемые топики
"""""""""""""""""""""""""""""""""""""""
* geoscan/navigation/opt/velocity (gs_interfaces/OptVelocity)


NavigationManager
~~~~~~~~~~~~~~~~~~
Класс взаимодействия с информацией, получаемой от систем позиционирования

Инициализация
""""""""""""""""""""""""""
Без параметров

Доступные поля класса
""""""""""""""""""""""""""""""""""""""""
* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __nav_service - rospy.ServiceProxy: gs_interfaces.srv.NavigationSystem
* __set_nav_service - rospy.ServiceProxy: gs_interfaces.srv.SetNavigationSystem
* gps - GlobalNavigation
* lps - LocalNavigation
* opt - OpticalFlow

Описание методов
"""""""""""""""""""""""""""""""

.. py:classmethod:: getSystem()

    :аргументы: None
    :return: gs_interfaces/NavigationSystem

    Получить текущую систему позиционирования

.. py:classmethod:: setSystem()

    :аргументы: system - название системы позиционирования (OPT, GPS, LPS)
    :return: gs_interfaces/NavigationSystem

    Установить систему позиционирования

Используемые сервисы
"""""""""""""""""""""""""""""""""""""""
* geoscan/alive (gs_interfaces/Live)
* geoscan/navigation/get_system (gs_interfaces/NavigationSystem)
* geoscan/navigation/set_system (gs_interfaces/SetNavigationSystem)


Необходимые пакеты
-----------------------------------
**ROS:**
* gs_interfaces
* gs_core
* geometry_msgs
* std_msgs

Примечание
--------------------
Все классы в данном пакете могут быть использованы только при запущеной ноде ros_plaz_node.py из пакета gs_core
