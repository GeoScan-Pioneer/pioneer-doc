Объект camera | Управление камерой
==================================

Для понимания работы рекомендуется ознакомиться с примером: :doc:`examples/camera_record`

Запрос захвата:

.. code:: lua

    camera.requestMakeShot()

Проверка ответа на ранее сделанный запрос:

.. code:: lua

    result = camera.checkRequestShot()

Возможные ответы:

 - -1 - Ответ не получен.
 - 0 - Команда выполнена успешно.
 - 1 - Команда не выполнена.

.. code:: lua

    camera.requestRecordStart() - запрос на старт записи.
    camera.requestRecordStop() - запрос на остановку записи.

.. code:: lua

    camera.checkRequestRecord() - проверка состояния связи.(получение ответа от устройства)