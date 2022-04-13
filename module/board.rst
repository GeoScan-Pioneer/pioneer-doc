Плата подключения дополнительных модулей
========================================

Плата-адаптер используется для подключения дополнительной полезной нагрузки к «Пионеру».

Плата крепится на нижнюю часть квадрокоптера вместо крышки отсека аккумулятора при помощи стоек и винтов М3. При установке ориентируйте плату так, чтобы стрелка находилась снизу и указывала в ту же сторону, что и стрелка на основной плате квадрокоптера.
Сверху на плате расположены два разъема. Используйте их для подключения адаптера к плате автопилота с помощью шлейфов, идущих в комплекте. На нижней поверхности расположены два разъема для подключения модулей. Модули подключаются "насквозь" через плату.

.. raw:: html

   <div style="position: relative; padding-bottom: 50%; overflow: hidden; margin-bottom:30px;margin-left: 0px;margin-right: 0px;">
        <iframe src="https://www.youtube.com/embed/jfZ0vFYUGKA" allowfullscreen="" style="position: absolute; width:100%; height: 100%;" frameborder="0"></iframe>
   </div>

.. warning:: Обратите внимание, шлейфы подключения имеют разное количество пинов (10 и 12). Убедитесь, что Вы подключаете шлейф в соответствующий разъём!

Плата адаптер 4.0
~~~~~~~~~~~~~~~~~

.. image:: /_static/images/modules_board_v4.png
    :align: center

**Особенности версии 4.0:**

* Встроенный модуль дальномера
* Встроенный модуль оптического позиционирования
* Возможность подключения камеры OpenMV
* Разъём подключения модуля камеры для работы с FPV-комплектом

Плата адаптер 2.0
~~~~~~~~~~~~~~~~~

.. image:: /_static/images/modules_board_v2.png
    :align: center

**Особенности версии 2.0:**

* Встроенный модуль дальномера
* Разъём подключения модуля камеры для работы с FPV-комплектом


 
Платы расширения оснащены лазерным дальномером. Он позволяет точно определять высоту над уровнем пола в пределах 0 - 4 м. Дальномер активируется в режиме удержания высоты. При этом «Пионер» будет сохранять одинаковое расстояние от поверхности, даже если она неровная. Пролетая над препятствием или впадиной, квадрокоптер будет менять высоту. Если закрыть датчик рукой или другим предметом, «Пионер» будет набирать высоту до тех пор, пока расстояние до препятствия не вернется к прежнему значению, или пока квадрокоптер не упрется в потолок.

.. warning:: Перед использованием платы-адаптера убедитесь, что на модуле оптического позиционирования и дальномере нет заводской плёнки!


Пример 1
~~~~~~~~

Данные с дальномера можно считывать и использовать для управления квадрокоптером. В качестве примера приведена программа, меняющая цвет светодиодов на "Пионере" в зависимости от расстояния до земли. Используйте Pioneer Station, чтобы  `загрузить программу`_ на "Пионер".

.. note::
    Дальномер неактивен в режиме полета по GPS. Если программа не работает, откройте вкладку "`параметры автопилота`_ " в Pioneer Station и выберите набор параметров "LPS" или "OPT". Также можно вручную поменять значение параметра BoardPioneer_modules_gnss на 0,0.

.. _загрузить программу: ../programming/pioneer_station/pioneer_station_upload.html 
.. _параметры автопилота: ../settings/autopilot_parameters.html
.. _OpenMV IDE: https://github.com/openmv/openmv-ide/releases/


::

    -- https://learnxinyminutes.com/docs/ru-ru/lua-ru/ ссылка для быстрого ознакомления с основами языка LUA
    -- упрощаем вызов функции получения расстояния с лазерного дальномера
    local range = Sensors.range
    -- количество светодиодов на основной плате пионера
    local ledNumber = 4
    -- создание порта управления светодиодами
    local leds = Ledbar.new(ledNumber)

    -- функция смены цвета светодиодов
    local function changeColor(red, green, blue)
	    -- меняет поочередно цвета каждого из 4-х светодиодов
        for i = 0, ledNumber - 1, 1 do
            leds:set(i, red, green, blue)
        end
    end

    function callback(event)
    end

    -- создаем таймер, который будет каждую десятую секунды считывать расстояние до пола
    timerRangeRead = Timer.new(0.1, function ()
        -- считываем показания в метрах с лазерного дальномера (он идет 1-м в списке) подключенного датчика расстояния
        distance = range()
        r, g, b = 0, 0, 0
        -- при превышении допустимого расстояния лазерного дальномера датчик выдает константу 8.19 м
        if (distance >= 8.19) then
            -- в таком случае светодиоды загораются красным
            r = 1
        else
            -- меняем яркость светодиодов в зависимости от расстояния (~1.5 - максимальное расстояние для лазерного дальномера на плате адаптере)
            g = math.abs(distance / 1.5)
        end
        -- меняем цвет светодиодов на посчитанные значения
        changeColor(r, g, b)
    end)
    -- запускаем таймер
    timerRangeRead:start()

Пример 2
~~~~~~~~

Пример демонстрирует, как реализовать взаимодействие камеры OpenMV c модулем захвата груза при помощи платы подключения дополнительных модулей версии 4.0. В данном скрипте электромагнит, расположенный на модуле захвата, отпускает груз при попадании маркера в объектив камеры.

Подключите программируемую камеру OpenMV и модуль захвата груза к плате подключения дополнительных модулей. Не забудьте зафиксировать оба модуля с помощью винтов и стоек.

Используйте Pioneer Station, чтобы  `загрузить программу`_ на "Пионер". Для загрузки программы на камеру OpenMV воспользуйтесь `OpenMV IDE`_ предварительно скачав версию для своей OC.

**Скрипт для автопилота:**

::

    local unpack = table.unpack -- импортируем функцию для распаковки массивов
    local ledNumber = 4 -- количество светодиодов
    local leds = Ledbar.new(ledNumber) -- инициализация объекта управления светодиодами
    local height = 1 --высота полета коптера
    local rc = Sensors.rc
    local magneto = Gpio.new(Gpio.C, 3, Gpio.OUTPUT)

    local uartNum = 4 -- номер Uart интерфейса (USART4)
    local baudRate = 9600 -- скорость передачи данных
    local dataBits = 8
    local stopBits = 1
    local parity = Uart.PARITY_NONE
    local uart = Uart.new(uartNum, baudRate, parity, stopBits) -- создание протокола обмена

    local colors = {
            {1, 0, 0}, -- (1) красный
            {1, 1, 1}, -- (2) белый
            {0, 1, 0}, -- (3) зеленый
            {1, 1, 0}, -- (4) желтый
            {1, 0, 1}, -- (5) фиолетовый
            {0, 0, 1}, -- (6) синий
            {0, 0, 0}  -- (7) черный/отключение светодиодов
    }

    -- переключение цвета светодиодов
    local function changeColor(color)
        -- проходим в цикле по всем светодиодам с 0 по 3
        for i=0, ledNumber - 1, 1 do
            leds:set(i, unpack(color))
        end
    end 


    -- обработка событий
    function callback(event)
        --if event == Ev.TAKEOFF_COMPLETE then
        --    changeColor(colors[3]) -- зеленый
            -- Timer.callLater(5, function () ap.push(Ev.MCE_LANDING) end)
        --end
        if event == Ev.COPTER_LANDED then
            ap.push(Ev.ENGINES_DISARM)
            changeColor(colors[7]) -- выключаем светодиоды
        end
    end

    function getc()
        while uart:bytesToRead() == 0 do
        end
        return uart:read(1)
    end

    function ord(chr, signed)
        local specifier = "B"
        if signed then specifier = "b" end
        return string.unpack(specifier, chr)
    end

    function getData() -- функция приёма пакета данных
        while true do -- ждём приёма начала пакета
            if (ord(getc()) == 0xBB) then break end
        end
        local ledstate = ord(getc())
        local dx = ord(getc(), true)
        local dy = ord(getc(), true)
        ord(getc()) -- принять конец пакета
        
        return ledstate, dx, dy
    end


    local takerFunction = function () -- функция для периодического чтения данных из UART
        local ledstate, dx, dy = getData()
        
        if (ledstate == 0) then
            changeColor(colors[1]) -- красный - не найден
            magneto:set()
        else
            changeColor(colors[3]) -- зелёный - найден
            magneto:reset()
        end
    end

    markerTimer = Timer.new(0.01, function () takerFunction() end)
    magneto:set()
    markerTimer:start()

**Скрипт для OpenMV:**

:: 

    import sensor, image, time, math, pyb
    from pyb import UART, LED

    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    screen_w = 160
    screen_h = 120
    sensor.set_framesize(sensor.QQVGA)
    sensor.skip_frames(30)
    sensor.set_auto_gain(False)
    sensor.set_auto_whitebal(False)

    uart = UART(3)
    uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000)


    track_id = 3 # qr код, за которым следим, и о котором передаём информацию на квадрокоптер


    clock = time.clock()

    def sendPacket(ledState, dx, dy):
        uart.writechar(0xBB) # packet begin byte
        uart.writechar(ledState)
        uart.writechar(dx.to_bytes(1, 'big')[0])
        uart.writechar(dy.to_bytes(1, 'big')[0])
        #uart.writechar(crc) # no crc now
        uart.writechar(0xFF) # packet end byte

    while(True):
        clock.tick()
        img = sensor.snapshot()
        apriltag_array = img.find_apriltags()
        found = False
        if len(apriltag_array) == 0:
            pass
        else:
            found = True
            for tag in apriltag_array:
                img.draw_rectangle(tag.rect(), color = (255, 0, 0))
                img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
                #red_led.off()
                #green_led.on()
                print_args = (tag.id(), (180 * tag.rotation())/math.pi)
                print("Tag Number", str(tag.id()))
                dx = int(tag.cx() - screen_w/2)
                dy = int(tag.cy() - screen_h/2)
                print("dx=" + str(dx) + ", dy=" + str(dy))
                #if (tag.id() == track_id):
                    #found = True
                    #sendPacket(1, dx, dy)
                sendPacket(1, dx, dy)
        if not found:
            sendPacket(0, 0, 0) # send info, no qr code found
    print(clock.fps())

Прошивка платы расширения
~~~~~~~~~~~~~~~~~~~~~~~~~

Для обновления прошивки платы расширения выполните следующие действия:

1.	Скачайте актуальную прошивку для модуля расширения. Актуальные версии прошивок можно найти в разделе :doc:`../downloads/software-d`

2.	Загрузите плату расширения в режиме "бутлоадера". Для этого модуль должен быть установлен на пионер и подключён к плате автопилота с помощью шлейфов, идущих в комплетке. 

3.	Удерживая нажатой кнопку **"Старт"** на базовой плате, подключите её с помощью USB-кабеля к ПК. При этом зелёный и красный светодиоды, расположенные на плате расширения, будут гореть постоянно как и все светодиоды на плате автопилота. (Обе платы перейдут в режим прошивки).

4.	В PioneerStation перейдите в раздел обновления прошивки и выберите устройство **PioneerAdapter**. Нажмите **"Далее"**

.. image:: /_static/images/fw_adapter.png
	:align: center 

5.	В качестве источника, выберите вариант обновления "Из файла" и укажите путь к ранее скачанному файлу. Нажмите **"Прошить"** и дождитесь окончания прошивки.




