Передача данных по Mailbox
==========================

Прием сообщения
---------------

.. code:: lua

    function callback(event)
    end

    hull, msg = mailbox.receive(true)

    if(msg == "a") then
        ap.push(Ev.MCE_PREFLIGHT)
    end


Отправка сообщения
---------------

.. code:: lua

    function callback(event)
    end

    mailbox.connect("192.168.0.100", 8889)
    sleep(0.1)

    data,_,_,_,_ = Sensors.range();
    mailbox.send(42, data);

Предполагается, что бортномер устройства известен. Бортномер устанавливается соответсвующей функцией
API и является уникальным идентификатором устройства в сети почтовых ящиков. Однако первое соединение устройств производится функцией connect()
по IP адресу и порту.