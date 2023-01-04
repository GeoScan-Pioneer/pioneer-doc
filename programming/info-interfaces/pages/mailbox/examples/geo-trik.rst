Передача сообщений между Пионером и Триком
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: examples/geo-trik.png
    :align: center
    :width: 600

Контроллер Тик переведен в режим точки доступа с помощью `WEB-интерфейса <https://help.trikset.com/trik/web-interface>`__, а
квадрокоптер Пионер Мини переведен в режим клиента и подключен к WI-FI сети Трика так же с
помощью своего `WEB-интерфейса <../../../../instructions/pioneer-mini/settings/esp_webinterface.html>`__.

В настройках контроллера Трик (меню Взаимодействие) установлен бортномер 01 и указан его IP адрес:

.. raw:: html

    <div style="width:100%; display:flex; justify-content: space-evenly;">
    <img src="../../../../_images/geo-trik_main_interaction.png" style="max-width:200px">
    <img src="../../../../_images/geo-trik_interaction_settings.png" style="max-width:200px">
    </div>

.. image:: examples/geo-trik_interaction_settings.png
    :align: center
    :width: 0

.. image:: examples/geo-trik_main_interaction.png
    :align: center
    :width: 0

Код для квадрокоптера на Lua:

.. code:: lua

    function callback(event)
    end

    mailbox.connect("192.168.0.100", 8889)
    sleep(0.1)

    data,_,_,_,_ = Sensors.range();
    mailbox.send(1, data);

Код для контроллера Трик на JS:

.. code:: javascript

    var main = function() {
        var msg = mailbox.receive()
        print("Received message: " + msg)
    }