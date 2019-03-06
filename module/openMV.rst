Программируемая камера OpenMV
=============================

.. image:: /_static/images/openmv_module.png
	:align: center

OpenMV - это программируемая камера. Она может самостоятельно обрабатывать видео поток и посылать команды управления на "Пионер".

Для установки камеры на квадрокоптер сначала установите модуль OpenMV. Закрепите его на 4 винта М3 и подключите оба разъема. Сама камера крепится к модулю на два 8-пиновых разъема. Для дополнительной надежности можно соединить платы камеры и модуля через две стойки с винтами.

Пример
----------

Модуль OpenMV взаимодействует с базовой платой "Пионера" через интерфейс UART. Для его настройки нужно написать две отдельных программы для квадрокоптера и камеры.
Для настройки соединения на "Пионере" используйте следующий код:

::

  -- инициализируем Uart интерфейс
  local uartNum = 4 -- номер Uart интерфейса (USART4)
  local baudRate = 9600 -- скорость передачи данных
  local stopBits = 1
  local parity = Uart.PARITY_NONE
  local uart = Uart.new(uartNum, baudRate, parity, stopBits)    


Теперь нужно настроить протокол обмена на самой камере. Для этого `скачайте и запустите OpenMV IDE`_ для своей ОС. Подключите камеру к компьютеру кабелем micro-USB и нажмите кнопку "Соединить" в левом нижнем углу OpenMV IDE. Теперь написанный в текстовом поле код можно загружать непосредственно в камеру, нажав кнопку "запустить" в левом нижнем углу.

Код для инициализации интерфейса  UART на камере:

.. _скачайте и запустите OpenMV IDE: https://github.com/openmv/openmv-ide/releases/

::

 uart = UART(3)
 uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000)


Протокол обмена между камерой и "Пионером" создан.

Ниже - пример программы, которая меняет яркость свечения светодиодов на "Пионере" в зависимости от яркости картинки, принимаемой камерой OpenMV. 
В коде обеих программ (для "Пионера" и OpenMV) уже содержатся блоки создания UART интерфейса.

Код для "Пионера"

::

 -- https://learnxinyminutes.com/docs/ru-ru/lua-ru/ ссылка для быстрого ознакомления с основами языка LUA
 -- количество светодиодов на основной плате пионера
 local ledNumber = 4
 -- создание порта управления светодиодами
 local leds = Ledbar.new(ledNumber)

 -- функция, изменяющая цвет 4-х RGB светодиодов на основной плате пионера
 local function changeColor(red, green, blue)
    for i=0, ledNumber - 1, 1 do
        leds:set(i, red, green, blue)
    end
 end

 -- функция, которая меняет цвет светодиодов на красный и выключает таймер
 local function emergency()
    takePhotoTimer:stop()
    -- так как после остановки таймера его функция выполнится еще раз, то меняем цвета светодиодов на красный через секунду
    Timer.callLater(1, function () changeColor(1, 0, 0) end)
 end

 -- определяем функцию анализа возникающих событий в системе
 function callback(event)
    -- проверка, низкое ли напряжение на аккумуляторе
    if (event == Ev.LOW_VOLTAGE2) then
        emergency()
    end
 end

 changeColor(1, 0, 0) -- red

 -- инициализируем Uart интерфейс
 local uartNum = 4 -- номер Uart интерфейса (USART4)
 local baudRate = 9600 -- скорость передачи данных
 local dataBits = 8
 local stopBits = 1
 local parity = Uart.PARITY_NONE
 local uart = Uart.new(uartNum, baudRate, parity, stopBits) -- создание протокола обмена

 changeColor(1, 0, 1) --purple

 local N = 10
 local i = 7
 local strUnpack = string.unpack
 function getData() -- функция приёма байта данных
    i = i + 1
    if (i == N + 1) then i = 0 end
    buf = uart:read(uart:bytesToRead()) or '0'
    if (#buf == 0) then buf = '\0' end
    leds:set(1, 0, i/N, 0.5 - 0.5*i/10)
    if (strUnpack ~= nil) then
        local b = strUnpack("B", buf)
        return b -- примерно должно так работать
    else
        return 20
    end
 end


 local takerFunction = function () -- функция для периодического чтения данных из UART
  local intensity = getData() / 100.0
  changeColor(intensity, intensity, intensity)
 end
 local interval = 0.1
 getMeasureTimer = Timer.new(interval, takerFunction) -- таймер для создания фото
 getMeasureTimer:start()


 changeColor(1, 0.2, 0) -- orange


Код для OpenMV

::

 # Hello World Example
 #
 # Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!
 
 from pyb import UART, LED

 import sensor, lcd, image, time, utime

 ledBlue = LED(2)
 ledGreen = LED(3)

 ledBlue.on()
 sensor.reset()                      # Reset and initialize the sensor.
 sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
 sensor.set_framesize(sensor.LCD)   # Set frame size to QVGA (320x240)
 sensor.skip_frames(100)     # Wait for settings take effect.
 clock = time.clock()                # Create a clock object to track the FPS.
 lcd.init()
 #lcd.set_backlight(True)
 ledBlue.off()

 #Init uart

 uart = UART(3)
 uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000) # init with given parameters

 M_LED_COUNT = 10
 led_counter = M_LED_COUNT
 led_mode = 0
 while(True):
    clock.tick()                    # Update the FPS clock.
    clk = utime.ticks_ms()
    img = sensor.snapshot()         # Take a picture and return the image.
    #print(clock.fps())              # Note: OpenMV Cam runs about half as fast when connected
                                    # to the IDE. The FPS should increase once disconnected.

    for r in img.find_rects(threshold = 40000):
        img.draw_rectangle(r.x(), r.y(), r.w(), r.h(), (255, 0, 0))
        for p in r.corners():
            img.draw_circle(p[0], p[1], 5, color = (0, 255, 0))
        print(r)

    lcd.display(img)

    print(img.get_histogram().get_statistics().l_mean())
    uart.writechar(img.get_histogram().get_statistics().l_mean())
    led_counter = led_counter - 1
    if (led_counter == 0):
        if (led_mode == 0):
            ledGreen.on()
        else:
            ledGreen.off()
        led_mode = 1 - led_mode
        led_counter = M_LED_COUNT
    while (clk + 100 > utime.ticks_ms()):
        pass


Используя Pioneer Station и OpenMV IDE, `загрузите`_ соответствующие программы на квадрокоптер и модуль камеры. Подключите аккумулятор к "Пионеру" и запустите выполнение программы. Протестируйте ее работу, направляя камеру на объекты с различной яркостью.

.. _загрузите: ../programming/pioneer_station/pioneer_station_upload.html





