Объект UART | Управление UART
=============================

.. class:: Uart

    .. method:: new(num, rate, parity, stopBits)

        Cоздать Uart на порте с настройками.

        :param num: номер UART;
        :param rate: скорость;
        :param parity: Uart.PARITY_NONE, Uart.PARITY_EVEN, Uart.PARITY_ODD, необязательный параметр, по умолчанию Uart.PARITY_NONE;
        :param stopBits: Uart.ONE_STOP, Uart.TWO_STOP, необязательный параметр, по умолчанию Uart.ONE_STOP.

    .. method:: read(self, size)

        Прочитать ``size`` байт.

    .. method:: write(self, data, size)

        Записать данные (data) длиной (size).

    .. method:: bytesToRead(self)

        Количество данных доступных для чтения.

    .. method:: setBaudRate(self, rate)

        Установить скорость.

        :param rate: скорость uart.


**Пример**

.. code:: lua

    local uart = Uart.new(1, 115200)
    uart:read(10) -- прочитать 10 байт