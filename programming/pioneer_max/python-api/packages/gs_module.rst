Пакет gs_module
====================================
.. contents:: 
   :depth: 3

Описание
----------------

Пакет gs_module предоставляет классы для управления внешними модулями такими как:
 * Светодиоды на базовой плате Пионер
 * LED модуль Пионер
 * Модуль магнитного захвата Пионер Макс

.. warning:: Все классы, кроме CargoController, могут быть использованы только при запущеной ноде ros_plaz_node.py из пакета gs_core

Состав пакета
-------------------------

Классы
~~~~~~~~~~~~~~~~
* BoardLedController
* ModuleLedController
* CargoController

Описание классов
-------------------------------

BoardLedController
~~~~~~~~~~~~~~~~~~~~~~~~~~

Класс для управления светодиодами на базовой плате Пионера. 

.. important:: Данный класс является оберткой для сервисов ROS.

.. contents::
   :local:

.. highlight:: python

Создание объекта класса
""""""""""""""""""""""""""""""""""""""""""""

.. class:: BoardLedController

.. py:class:: boardLed = BoardLedController()

     :аргументы: нет
     :return: объект класса BoardLedController

     Cоздаёт объект класса BoardLedController.

Описание методов
"""""""""""""""""""""""""""""""

.. py:classmethod:: changeColor(i, r, g, b)

      :аргументы: *i* - номер светодиода на базовой плате, принимает значение от 0 до 3;
               *r*, *g*, *b* — каналы по управлению красным, зелёным и синим свечением светодиода, принимает значения от 0.0 до 255.0 - интенсивность соответствующего канала.
      :return: нет

      Метод управления одним светодиодом на базовой плате Пионера.

.. py:classmethod:: changeAllColor(r, g, b)

      :аргументы: *r*, *g*, *b* — каналы по управлению красным, зелёным и синим свечением светодиода, принимает значения от 0.0 до 255.0 - интенсивность соответствующего канала.
      :return: нет

      Метод управления всеми светодиодами на базовой плате Пионера.

Используемые сервисы ROS
"""""""""""""""""""""""""""""""""""""""""""

 * geoscan/alive (gs_interfaces/Live)
 * geoscan/led/board/set (gs_interfaces/Led)

ModuleLedController
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Класс для управления светодидами на `LED модуле <https://pioneer-doc.readthedocs.io/ru/master/module/led.html>`__.

.. important:: Данный класс является оберткой для сервисов ROS.

.. contents::
   :local:

.. highlight:: python

Создание объекта класса
""""""""""""""""""""""""""""""""""""""""""""

.. class:: ModuleLedController

.. py:class:: moduleLed = ModuleLedController()

     :аргументы: нет
     :return: объект класса ModuleLedController

     Cоздаёт объект класса ModuleLedController.

Доступные поля класса
""""""""""""""""""""""""""""""""""""""""

    * __leds - list: std_msgs.msg.ColorRGBA
    * __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
    * __led_service - rospy.ServiceProxy: gs_interfaces.srv.Led

Описание методов
"""""""""""""""""""""""""""""""

.. py:classmethod:: changeColor(i, r, g, b)

      :аргументы: *i* - номер светодиода на LED модуле, принимает значение от 0 до 24;
               *r*, *g*, *b* — каналы по управлению красным, зелёным и синим свечением светодиода, принимает значения от 0.0 до 255.0 - интенсивность соответствующего канала.
      :return: нет

      Метод управления одним светодиодом на LED модуле.

.. py:classmethod:: changeAllColor(r, g, b)

      :аргументы: *r*, *g*, *b* — каналы по управлению красным, зелёным и синим свечением светодиодов, принимает значения от 0.0 до 255.0 - интенсивность соответствующего канала.
      :return: нет

      Метод управления всеми светодиодами на LED модуле.

Используемые сервисы ROS
"""""""""""""""""""""""""""""""""""""""""""

 * geoscan/alive (gs_interfaces/Live)
 * geoscan/led/module/set (gs_interfaces/Led)

Класс CargoController
~~~~~~~~~~~~~~~~~~~~~~~

Класс для управления модулем магнитного захвата Пионер Макс. 

.. warning:: Магнитный захват использует GPIO17 и GPIO18

.. contents::
   :local:

.. highlight:: python

Создание объекта класса
""""""""""""""""""""""""""""""""""""""""""""

.. class:: CargoController

.. py:class:: cargo = CargoController()

     :аргументы: нет
     :return: объект класса CargoController

     Cоздаёт объект класса CargoController.

Описание методов
"""""""""""""""""""""""""""""""

.. py:classmethod:: on()

      :аргументы: нет
      :return: нет

      Включает магнит на модуле.

.. py:classmethod:: off()

      :аргументы: нет
      :return: нет

      Выключает магнит на модуле.

.. py:classmethod:: changeColor(r=0, g=0, b=0, n=0)

      :аргументы: *n* - номер светодиода на модуле захвата, принимает значение от 0 до 24;
               *r*, *g*, *b* — каналы по управлению красным, зелёным и синим свечением светодиода, принимает значения от 0.0 до 255.0 - интенсивность соответствующего канала.
      :return: нет

      Метод управления одним светодиодом на модуле захвата.

.. py:classmethod:: changeAllColor(r=0, g=0, b=0)

      :аргументы: *r*, *g*, *b* — каналы по управлению красным, зелёным и синим свечением светодиодов, принимает значения от 0.0 до 255.0 - интенсивность соответствующего канала.
      :return: нет

      Метод управления всеми светодиодами на модуле захвата.

Необходимые пакеты
-----------------------------

**Python:**

    * RPi.GPIO
    * json
    * socket

**ROS:**

    * gs_core
    * gs_interfaces
    * std_msgs

Примечание
-----------------------------

Все классы, кроме CargoController, могут быть использованы только при запущеной ноде ros_plaz_node.py из пакета gs_core
