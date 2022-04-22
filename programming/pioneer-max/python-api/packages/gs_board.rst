Пакет gs_board
===================================

.. contents:: 
   :depth: 3

Описание
----------
Пакет gs_board предоставляет классы взаимодействия с бортовой информацией

Класс BoardManager
------------------
Класс менеджера бортовой информации.

.. important:: Данный класс является оберткой для сервисов ROS.

.. contents::
   :local:

.. highlight:: python

Создание объекта класса
~~~~~~~~~~~~~~~~~~~~~~~

.. class:: BoardManager

.. py:class:: board = BoardManager()

    :аргументы: нет
    :return: объект класса BoardManager

    Cоздаёт объект класса BoardManager.

Доступные поля класса
~~~~~~~~~~~~~~~~~~~~~
    * __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
    * __restart - rospy.ServiceProxy: std_srvs.srv.Empty
    * __time_service - rospy.ServiceProxy: gs_interfaces.srv.Time
    * __uptime_service - rospy.ServiceProxy: gs_interfaces.srv.Time
    * __flight_time_service - rospy.ServiceProxy: gs_interfaces.srv.Time
    * __info_service - rospy.ServiceProxy: gs_interfaces.srv.Info
    * __get_parameters_service - rospy.ServiceProxy: gs_interfaces.srv.ParametersList
    * __set_parameters_service - rospy.ServiceProxy: gs_interfaces.srv.SetParametersList

Описание методов
~~~~~~~~~~~~~~~~

.. py:classmethod:: runStatus()

    :аргументы: нет
    :return: False, True

    Возвращает статус подключения Raspberry Pi к базовой плате Пионер.


.. py:classmethod:: boardNumber()

    :аргументы: нет
    :return: str

    Возвращает имя/номер базовой платы, параметр базовой платы *Board_number*.

.. py:classmethod:: time()

    :аргументы: нет
    :return: float

    Возвращает время с момента включения базовой платы (в мс)


.. py:classmethod:: uptime()

    :аргументы: нет
    :return: float

    Возвращает время с момента запуска системы навигации (в мс)


.. py:classmethod:: flightTime()

    :аргументы: нет
    :return: float

    Возвращает время с начала последнего полета (в мс)


.. py:classmethod:: restart()

    :аргументы: нет
    :return: нет

    Перезапуск базовой платы Пионера.


.. py:classmethod:: getParametrs()

    :аргументы: нет
    :return: dict

    Возвращает параметры АП.

.. py:classmethod:: setParametrs()

    :аргументы: params_dict - словарь параметров (название_параметра:значение_параметра)
    :return: bool

    Устанавливает параметры АП.

Используемые сервисы ROS    
~~~~~~~~~~~~~~~~~~~~~~~~
    * geoscan/alive (gs_interfaces/Live)
    * geoscan/board/restart (std_srvs/Empty)
    * geoscan/board/get_info (gs_interfaces/Info)
    * geoscan/board/get_time (gs_interfaces/Time)
    * geoscan/board/get_uptime (gs_interfaces/Time)
    * geoscan/board/get_flight_time (gs_interfaces/Time)
    * geoscan/board/get_parameters (gs_interfaces/ParametersList)
    * geoscan/board/set_parameters (gs_interfaces/SetParametersList) 

Необходимые пакеты
-----------------------------
**ROS:**
 
    * gs_interfaces
    * gs_core
    * std_srvs

Примечание
-----------------------------

*Для работы всех (кроме cargo_test.py) требуется запущенная ros_plaz_node из пакета gs_core*

.. code-block:: ros
    :caption: Запуск ros_plaz_node с помощью утилиты rospioneer (перед запуском примеров в отдельном окне терминала)

    rospioneer start

