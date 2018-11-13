Модуль LED
==========


.. image:: /_static/images/led_module.png
	:align: center


Модуль LED представляет собой плату с 25-ю программируемыми светодиодами, которая крепится к плате расширения снизу. Подключение через разъем X2 комплектным шлейфом.

Блок светодиодов может использоваться для подсветки или индикации событий в зависимости от заданной программы. 

В качестве примера приведена программа, случайно меняющая цвет блока светодиодов каждую секунду. Чтобы `загрузить программу на "Пионер"`_, воспользуйтесь Pioneer Station. 

.. _загрузить программу на "Пионер": ../programming/pioneer_station/pioneer_station_upload.html



::

 -- количество светодиодов на основной плате пионера(4) + на модуле LED (25)
 local ledNumber = 29
 -- создание порта управления светодиодами
 local leds = Ledbar.new(ledNumber)

 -- функция, изменяющая цвет RGB светодиодов 
 local function changeColor(red, green, blue)
    for i=0, ledNumber - 1, 1 do
        leds:set(i, red, green, blue)
    end
 end

 -- функция, которая выключает светодиоды и таймер timerRandomLED
 local function emergency()
    timerRandomLED:stop()
    -- так как после остановки таймера его функция выполнится еще раз, то выключаем светодиоды через секунду
    Timer.callLater(1, function () changeColor(0, 0, 0) end)
 end

 function callback(event)
    -- проверка, низкое ли напряжение на аккумуляторе
    if (event == Ev.LOW_VOLTAGE2) then
        emergency()
    end
 end

 -- создание таймера, который каждую секунду меняет цвет всех светодиодов на случайный
 timerRandomLED = Timer.new(1, function ()
    changeColor(math.random(), math.random(), math.random())
 end)
 -- запуск созданного таймера
 timerRandomLED:start()

