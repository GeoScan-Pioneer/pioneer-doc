Объект GPIO | Управление пинами
===============================

.. class:: Gpio

    .. method:: new(Port, Pin, Mode)

        Cоздать GPIO на порте с настройками.

        :param Port: Gpio.A; Gpio.B; ... Gpio.E;
        :param Pin: номер пина на порте;
        :param Mode: Gpio.INPUT, Gpio.Output, Gpio.ALTFU.

    .. method:: read(self)

        Получить значение.

    .. method:: set(self)

        Установить значение в 1.

    .. method:: reset(self)

        Установить значение в 0.

    .. method:: write(self, value)

        :param value: установить значение.

    .. method:: setFunction(self, num)

        Задать номер альтернативной функции.

**Пример**

.. code-block:: lua

    local pin_name = Gpio.new(Gpio.A, 1, Gpio.OUTPUT)
    pin_name:read() -- получить значение
    pin_name:set() -- установить значение 1
    pin_name:reset() -- установить значение 0
    pin_name:write(true) -- установить значение true
    pin_name:setFunction(1) -- задать номер альтернативной функции