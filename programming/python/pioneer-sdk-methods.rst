Описание методов pioneer_sdk
============================

На данной странице разобраны методы библиотеки pioneer_sdk.
Примеры скриптов можно найти по `ссылке <https://github.com/geoscan/pioneer_sdk/tree/master/examples>`__.
Страница по настройке среды Pycharm: :doc:`python-sdk-main`


.. contents::
   :local:

..  tip:: Значения аргументов, представленных в описании метода являются стандартными, то есть если написано: led_control(led_id=255, r=0, g=0, b=0)
          то в программе его можно вызывать как led_control() - эквивалент надписи выше. Или например led_control(r=255) — тогда частично будут задействованы стандартные значения.

Pioneer
-------

Создание объекта класса:
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: Pioneer(name='pioneer', ip='192.168.4.1', mavlink_port=8001, connection_method=2, device='/dev/serial0', baud=115200, logger=True, log_connection=True)

**Аргументы:**
 - | *name* — имя используемое только для выведения логов в консоль; удобно назначать разные имена, при запуске нескольких дронов, чтобы знать с какого дрона пришло сообщение.
 - | *ip* - ip-адрес дрона.
 - | *mavlink_port* - порт для обмена MAVLink сообщениями.
 - | *connection_method* - 0 для подключения 'udpin'; 1 для подключения 'serial'; 2 для подключения 'udpout'.
 - | *device* - указание порта.
 - | *baud* - скорость передачи.
 - | *logger* - логи MAVLink сообщений. True - выводить в консоль; False - не выводить.
 - | *log_connection* - логи соединения. True - выводить в консоль; False - не выводить.

**Результат:** создание объект класса Pioneer.

Описание методов класса Pioneer:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:classmethod:: connected()

	**Аргументы:** Нет.

	**Результат:** Возвращает *False*, если соединение потеряно (в течении секунды нет сообщений от дрона), возвращает *True*, если соединение стабильное.


.. py:classmethod:: reboot_board()

	**Аргументы:** Нет.

	**Результат:** Перезагрузка дрона. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False*, если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: set_logger(value=True)

	**Аргументы:**

	- | *value* - принимает значения *True* или *False*

	**Результат:** Установка флага 'logger' в *True* или *False*.


.. py:classmethod:: set_log_connection(value=True)

	**Аргументы:**

	- | *value* - принимает значения *True* или *False*

	**Результат:** Установка флага 'log_connection' в *True* или *False*.


.. py:classmethod:: arm()

	**Аргументы:** Нет.

	**Результат:** Заводит моторы квадрокоптера. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False*, если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: disarm()

	**Аргументы:** Нет.

	**Результат:** Отключае моторы квадрокоптера. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False*, если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: takeoff()

	**Аргументы:** Явных аргументов нет, высота взлета задаётся параметром автопилота *Flight_com_takeoffAlt=x*, где x-высота взлета в метрах.

	**Результат:** Взлёт на высоту takeoffAlt. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False*, если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: land()

	**Аргументы:** Нет.

	**Результат:** Выполняет команду на посадку. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False*, если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: lua_script_upload(lua_source)

	**Аргументы:** 

	- | *lua_source* - путь до Lua-файла.

	**Результат:** Загрузка Lua-скрипта на дрон.


.. py:classmethod:: lua_script_control(state='Stop')

	**Аргументы:** 

	- | *state='Start'* - запуск скрипта, *state='Stop'* - остановка скрипта.

	**Результат:** Запуск/остановка Lua-скрипта. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False*, если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: led_control(led_id=255, r=0, g=0, b=0)

    **Аргументы:**

    - | *led_id* - номер светодиода для управления. (255 - все светодиоды; 0-3 — светодиоды от 1 до 4).
    - | *r*, *g*, *b* — каналы по управлению красным зелёным и синим свечением светодиода 0-255 - интенсивность соответствующего канала.

    **Результат:** Включение светодиодов. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False*, если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: go_to_local_point(x=None, y=None, z=None, yaw=None)

	**Аргументы:**

	- | *x*, *y*, *z* - координаты точки, в метрах.
	- | *yaw* - угол рысканья, задается в радианах.

	**Результат:** Отправка команды полёта в точку. Координаты указываются в **локальной системе координат**. Возвращает *True*, если команда отправлена успешно, *False* - если не удалось отправить или пришёл отказ.


.. py:classmethod:: go_to_local_point_body_fixed(x, y, z, yaw)

	**Аргументы:**

	- | *x*, *y*, *z* - координаты точки, в метрах.
	- | *yaw* - угол рысканья, задается в радианах.

	**Результат:** Отправка команды полёта в точку. Координаты указываются в **системе координат дрона**. Возвращает *True*, если команда отправлена успешно, *False* - если не удалось отправить или пришёл отказ.


.. py:classmethod:: set_manual_speed(vx, vy, vz, yaw_rate)

	**Аргументы:**

	- | *vx*, *vy*, *vz* - скорость в м/с.
	- | *yaw_rate* - скорость рад/с.

	**Результат:** Отправка команды полёта с заданной скоростью. Координаты указываются в **локальной системе координат**. Возвращает *True*, если команда отправлена успешно, *False* - если не удалось отправить или пришёл отказ. Команду *set_manual_speed* надо отправлять не один раз, а постоянно, пока необходимо лететь с заданной скоростью.


.. py:classmethod:: set_manual_speed_body_fixed(vx, vy, vz, yaw_rate)

	**Аргументы:**

	- | *vx*, *vy*, *vz* - скорость в м/с.
	- | *yaw_rate* - скорость рад/с.

	**Результат:** Отправка команды полёта с заданной скоростью. Координаты указываются в **системе координат дрона**. Возвращает *True*, если команда отправлена успешно, *False* - если не удалось отправить или пришёл отказ. Команду *set_manual_speed_body_fixed* надо отправлять не один раз, а постоянно, пока необходимо лететь с заданной скоростью.


.. py:classmethod:: point_reached()

	**Аргументы:** Нет

	**Результат:** Возвращает текущее состояние флага (True/False). Флаг устанавливается в *True* регулярно при достижении новой точки, и сбрасывается в *False* после каждого вызова функции point_reached() и после отправки go_to_local_point() или go_to_local_point_body_fixed().


.. py:classmethod:: get_local_position_lps(get_last_received=False)

	**Аргументы:** 

	- | *get_last_received* - если аргумент get_last_received=True, то возвращает значения [x, y, z] из последнего пришедшего сообщения. Возвращает *None*, если с дрона не было ни одного сообщения с координатами.

	**Результат:** Массив [x, y, z] с текущими координатами в локальной системе отсчёта. Возвращает *None*, если нет новых актуальных данных.



.. py:classmethod:: get_dist_sensor_data(get_last_received=False)

	**Аргументы:** 

	- | *get_last_received* - если аргумент get_last_received=True, то возвращает данные с дальномера из последнего пришедшего сообщения. Возвращает *None*, если с дрона не было ни одного сообщения с показаниями дальномера.

	**Результат:** Возвращает последние данные с дальномера (в метрах). Возвращает *None*, если нет новых актуальных данных.


.. py:classmethod:: get_optical_data(get_last_received=False)

	**Аргументы:** 

	- | *get_last_received* - если аргумент get_last_received=True, то возвращает словарь с данными из последнего пришедшего сообщения. Возвращает *None*, если с дрона не было ни одного сообщения с данными оптического потока.

	**Результат:** Возвращает словарь (dict), содержащий последнее данные с оптического потока. Возвращает *None*, если нет новых актуальных данных.


.. py:classmethod:: get_battery_status(get_last_received=False)

	**Аргументы:** 

	- | *get_last_received* - если аргумент get_last_received=True, то возвращает вольтаж батареи из последнего пришедшего сообщения. Возвращает *None*, если с дрона не было ни одного сообщения о состоянии батареи.

	**Результат:** Возвращает текущий вольтаж батареи. Возвращает *None*, если нет новых актуальных данных.


.. py:classmethod:: get_preflight_state()

	**Аргументы:** Нет.

	**Результат:** Возвращает словарь (dict) со значениями ошибок, возникших при preflight.


.. py:classmethod:: get_autopilot_state()

	**Аргументы:** Нет.

	**Результат:** Возвращает текущее состояние автопилота:('ROOT', 'DISARMED',	'IDLE',	'TEST_ACTUATION', 'TEST_PARACHUTE', 'TEST_ENGINE', 'PARACHUTE', 'WAIT_FOR_LANDING', 'LANDED', 'CATAPULT', 'PREFLIGHT', 'ARMED', 'TAKEOFF', 'WAIT_FOR_GPS', 'WIND_MEASURE', 'MISSION', 'ASCEND', 'DESCEND', 'RTL', 'UNCONDITIONAL_RTL', 'MANUAL_HEADING', 'MANUAL_ROLL', 'MANUAL_SPEED', 'LANDING', 'ON_DEMAND')


.. py:classmethod:: get_autopilot_version()

	**Аргументы:** Нет.

	**Результат:** Возвращает текущую версию автопилота.


.. py:classmethod:: send_rc_channels(channel_1=0xFF, channel_2=0xFF, channel_3=0xFF, channel_4=0xFF, channel_5=0xFF, channel_6=0xFF, channel_7=0xFF, channel_8=0xFF)

	**Аргументы:** *channel_1-8* - RC-каналы. 

	**Результат:** Отправка значений на каналы.


.. py:classmethod:: raspberry_poweroff()

	**Аргументы:** Нет.

	**Результат:** Выключение Raspbery Pi. Функция для базового пионера с модулем Raspbery Pi. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False* - если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: raspberry_reboot()

	**Аргументы:** Нет.

	**Результат:** Перезагрузка Raspbery Pi. Функция для базового пионера с модулем Raspbery Pi. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False* - если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: raspberry_start_capture(interval=0.1, total_images=0, sequence_number=0)

	**Аргументы:** Утверждаются.

	**Результат:** Начать запись видео на Raspbery Pi. Функция для базового пионера с модулем Raspbery Pi. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False* - если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: raspberry_stop_capture()

	**Аргументы:** Нет.

	**Результат:** Остановить запись видео на Raspbery Pi. Функция для базового пионера с модулем Raspbery Pi. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False* - если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.


.. py:classmethod:: raspberry_led_custom(mode=1, timer=0, color1=(0, 0, 0), color2=(0, 0, 0))

	**Аргументы:** Утверждаются.

	**Результат:** Включение светодиодов. Функция для базового пионера с модулем Raspbery Pi. Возвращает *True*, если результат 'ACCEPTED' или 'DENIED'. Возвращает *False* - если результат 'SEND_TIMEOUT', 'TEMPORARILY_REJECTED', 'UNSUPPORTED', 'FAILED', 'CANCELLED'. См. Pioneer.mav_result.

Pioneer.mav_result
------------------

 - | -1: 'SEND_TIMEOUT', 
 - |  0: 'ACCEPTED', 
 - |  1: 'TEMPORARILY_REJECTED', 
 - |  2: 'DENIED', 
 - |  3: 'UNSUPPORTED', 
 - |  4: 'FAILED', 
 - |  5: 'IN_PROGRESS', 
 - |  6: 'CANCELLED' }

Camera
------

Создание объекта класса:
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: Camera(timeout=0.5, ip='192.168.4.1', port=8888, video_buffer_size=65000, log_connection=True)

**Аргументы:**
 - | *timeout* — тайм-аут получения сообщения через сокет.
 - | *ip* - ip-адрес дрона.
 - | *port* - порт дрона для отправки изображения с камеры.
 - | *video_buffer_size* - размер буфера для считывания изображений.
 - | *log_connection* - логи соединения. *True* - выводить в консоль; *False* - не выводить.

**Результат:** создание объект класса Camera.

Описание методов класса Camera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:classmethod:: connect()

	**Аргументы:** Нет.

	**Результат:** Подключение к дрону для получения изображения.


.. py:classmethod:: disconnect()

	**Аргументы:** Нет.

	**Результат:** Отключиться от дрона.


.. py:classmethod:: get_frame()

	**Аргументы:** Нет.

	**Результат:** Получение изображения. Возвращает массив байтов в успешном случае. В противном случае возвращает *None*.	Если в процессе получения картинки выяснилось, что соединение потеряно, то происходит переподключение.


VideoStream
-----------

.. py:class:: VideoStream(logger=True)

Описание методов класса VideoStream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:classmethod:: start()

	**Аргументы:** Нет.

	**Результат:** Запуск потока видео. (Стрим запускается в отдельном потоке)


.. py:classmethod:: stop()

	**Аргументы:** Нет.

	**Результат:** Остановка потока видео.