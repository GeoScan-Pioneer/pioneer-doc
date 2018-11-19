Программируемая камера OpenMV
=============================

.. image:: /_static/images/openmv_module.png
	:align: center

Программируемая камера OpenMV позволяет обрабатывать видео поток на борту "Пионера" и осуществлять автономную навигацию по визуальным признакам.

Для установки камеры на квадрокоптер необходимо сначала установить модуль OpenMV. Крепление модуля на 4 винта М3 с подключением двух  разъемов. Затем, на установленный модуль крепится сама камера на два 8-пиновых разъема. Для дополнительной надежности можно использовать две стойки с винтами для соединения плат камеры и модуля.

 
Модуль OpenMV взаимодействует с базовой платой "Пионера" посредством интерфейса UART. При этом для квадрокоптера и камеры необходимо написать две отдельных программы с соответствующими командами, которые структурируют взаимодействие.
Для настройки соединения на "Пионере" используйте следующий код

::

  -- инициализируем Uart интерфейс
  local uartNum = 4 -- номер Uart интерфейса (USART4)
  local baudRate = 9600 -- скорость передачи данных
  local stopBits = 1
  local parity = Uart.PARITY_NONE
  local uart = Uart.new(uartNum, baudRate, parity, stopBits)    



Также необходимо указать протокол обмена на самой камере. Для этого `скачайте и запустите OpenMV IDE`_. Подключите камеру к компьютеру кабелем micro-USB и нажмите кнопку "Соединить" в левом нижнем углу OpenMV IDE. Теперь написанный в текстовом поле код можно загружать непосредственно в камеру, нажав кнопку "запустить" в левом нижнем углу.

Код для инициализации интерфейса  UART на камере

.. _скачайте и запустите OpenMV IDE: http://github.com/openmv/openmv-ide/releases/download/v2.0.0/openmv-ide-windows-2.0.0.exe

::

 uart = UART(3)[font=monospace][/font]
 uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000)



Протокол обмена между камерой и "Пионером" создан.



Далее приводится пример программ, меняющий яркость свечения светодиодов на "Пионере" в зависимости от яркости картинки, принимаемой камерой OpenMV. 
В коде обеих программ (для "Пионера" и OpenMV) уже содержатся блоки создания UART интерфейса.

код для "Пионера"

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

 --changeColor(1, 0.4, 0) --yellow

 local N = 10
 local i = 7
 local strUnpack = string.unpack
 function getData() -- функция приёма байта данных
    --uart:write('abc', 3)
    --return 50
    --return uart:read(1) or 0
    i = i + 1
    if (i == N + 1) then i = 0 end
    buf = uart:read(uart:bytesToRead()) or '0'
    if (#buf == 0) then buf = '\0' end
    --buf = '0'
    leds:set(1, 0, i/N, 0.5 - 0.5*i/10)
    --local chr = buf[#buf]
    if (strUnpack ~= nil) then
        local b = strUnpack("B", buf)
        return b -- примерно должно так работать
    else
        return 20
    end
    --string.byte(buf)
    --return #buf
    --return string.byte(string.sub(buf, -1)) or 0
    --return string.byte(buf) or 0
 end


 local takerFunction = function () -- функция для периодического чтения данных из UART
  local intensity = getData() / 100.0
  changeColor(intensity, intensity, intensity)
 end
 local interval = 0.1
 getMeasureTimer = Timer.new(interval, takerFunction) -- таймер для создания фото
 getMeasureTimer:start()


 changeColor(1, 0.2, 0) -- orange


Код для openmv

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





Используя Pioneer Station и OpenMV IDE, `загрузите`_ соответсвующие программы на квадрокоптер и модуль камеры. Подключите аккумулятор к "Пионеру" и запустите выполнение программы. Протестируйте ее работу, направляя камеру на объекты с различной яркостью.

.. _загрузите: ../programming/pioneer_station/pioneer_station_upload.html





