Объект ap | Управление автопилотом
----------------------------------

    .. function:: ap.push(Event)

        Добавить событие автопилоту (см. :ref:`outluaevent`).

        :param Event: номер события или название (например, ``Ev.COPTER_LANDED``).

        **Пример**

        .. code-block:: lua

            Ev.MCE_PREFLIGHT
            ap.push(Ev.MCE_PREFLIGHT)

    .. function:: ap.goToPoint(latitude, longitude, altitude)

         Для полёта с использованием GPS.

        :param latitude: задается широта в градусах, умноженных на :math:`10^{-7}`;
        :param longitude: задается долгота в градусах, умноженных на :math:`10^{-7}`;
        :param altitude: задается высота в метрах.

        **Пример**

        .. code-block:: lua

            ap.goToPoint(60.0859810, 30.4206500, 50)

    .. function:: ap.goToLocalPoint(x, y, z , time)

        Для полёта с использованием локальной системы координат.

        :param x: задается координата точки по оси `x`, в метрах;
        :param y: задается координата точки по оси `y`, в метрах;
        :param z: задается координата точки по оси `z`, в метрах;
        :param time: время, за которое коптер перейдет в следующую точку, в секундах. Если значение не указано, коптер стремится к точке с максимальной скоростью.

        **Пример**

        .. code-block:: lua

            ap.goToLocalPoint(1, 1, 1.2)
            -- или
            ap.goToLocalPoint(1, 1, 1.2, 10)

    .. function:: ap.updateYaw(angle)

        Установить рыскание.

        :param angle: угол в радианах.