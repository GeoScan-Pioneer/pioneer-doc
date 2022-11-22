Объект Sensors | Получение данных от датчиков
=============================================

Для получение данных от автопилота используется класс Sensors

.. class:: Sensors

    .. method:: lpsPosition()

        :return: x, y, z

    .. method:: lpsVelocity()

        :return: vx, vy, vz

    .. method:: lpsYaw()

        :return: yaw

    .. method:: orientation()

        Данные положения.

        :return: roll, pitch, azimuth

    .. method:: altitude()

        Данные высоты по барометру.

        :return: высота в метрах

    .. method:: range()

        Данные c датчиков расстояния.

        :return: Возвращает значения с датчика расстояния. Возвращает несколько значений.

    .. method:: accel()

        Данные c акселерометра.

        :return: ax, ay, az

    .. method:: gyro()

        Данные c гироскопа.

        :return: gx, gy, gz

    .. method:: rc()

        Данные c пульта управления.

        :return: channel1, channel2, channel3, channel4, channel5, channel6, channel7, channel8

**Примеры**

.. code:: lua

    local lpsPosition = Sensors.lpsPosition
    local lpsVelocity = Sensors.lpsVelocity
    local lpsYaw = Sensors.lpsYaw
    local orientation = Sensors.orientation
    local range = Sensors.range
    local accel = Sensors.accel
    local gyro = Sensors.gyro
    local rc = Sensors.rc

    lpsX, lpsY, lpsZ = lpsPosition()
    lpsVelX, lpsVelY, lpsVelZ = lpsVelocity()
    yaw = lpsYaw()

    roll, pitch, azimuth = orientation()

    range1, range2, _,_, range3 = range()

    ax, ay, az = accel()
    gx, gy, gz = gyro()
    aileron, _, _, _, _, _, _, ch8, = rc()