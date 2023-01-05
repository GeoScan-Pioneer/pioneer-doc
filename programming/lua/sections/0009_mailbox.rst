Объект mailbox | Беспроводная передача сообщений
------------------------------------------------

    .. function:: mailbox.connect(ip, port)

        Инициализация подключения к устройству с заданным адресом и портом

        :param ip: str - ip адрес устройства назначения
        :param port: num - порт устройства назначения, рекомендуется использовать 8889

        **Пример**

            .. code:: lua

                hull, message = mailbox.connect("192.168.0.100", 8889)


    .. function:: mailbox.hasMessages()

        Проверяет, есть ли пришедшие сообщения

        :return: bool - есть ли пришедшие сообщения

        **Пример**

            .. code:: lua

                has_mes = mailbox.hasMessages()


    .. function:: mailbox.myHullNumber()

        Возвращает текущий бортномер устройства

        :return: num - бортномер устройства

        **Пример**

            .. code:: lua

                my_hull = mailbox.myHullNumber()


    .. function:: mailbox.receive(blocking)

        Считывание одного байта

        :param blocking: true|false - блокирование выполнения программы, при true ожидает получения сообщения, при false - возвращает сообщение из буфера или -1, если сообщений нет.
        :return: hull - бортномер отправителя, message - сообщение

        **Пример**

            .. code:: lua

                hull, message = mailbox.receive(true)


    .. function:: mailbox.send(hull, message)

        Отправка сообщения

        :param hull: num - бортномер устройства, которому отправляется сообщение, если hull < 0, то сообщение отправится всем известным устроствам
        :param message: num|str - сообщение для отправки

        **Пример**

            .. code:: lua

                mailbox.send(42, "Hello Username")
                mailbox.send(-1, "Hello World")


    .. function:: mailbox.setHullNumber(hull)

        Устанавливает новый бортномер для устройства, перезаписывается параметр Trik_hullNum

        :param hull: num - новый бортномер

        **Пример**

            .. code:: lua

                mailbox.setHullNumber(12)


    **Дополнительные примеры программ** можно посмотреть на странице с `описанием протокола mailbox <../../programming/info-interfaces/pages/mailbox/mailbox.html#id4>`__