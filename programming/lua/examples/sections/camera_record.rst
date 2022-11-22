Фото и запись видео
===================

.. code:: lua

    -- Количество светодиодов
    local ledNumber = 4
    local leds = Ledbar.new(ledNumber)
    -- Функция для смены цвета светодиодов
    local function changeColor(color)
        for i=0, ledNumber - 1, 1 do
            leds:set(i, table.unpack(color))
        end
    end

    -- Таблицы цветов
    local colors = {
        {0, 0, 0}, -- Чёрный (светодиоды не горят)
        {1, 0, 0}, -- Красный
        {0, 1, 0}, -- Зелёный
        {1, 1, 1}, -- Белый
    }

    -- Сделать снимок
    local function makeShot()
        changeColor(colors[2]) -- Красный цвет светодиодов
        camera.requestMakeShot() -- Отправить запрос на снимок
        -- Ждём, пока придёт ответ
        while camera.checkRequestShot() == -1 do  -- 0 успешно, 1 ошибка, -1 ответ не пришёл
        end
        changeColor(colors[1]) -- Выключаем светодиоды
    end

    -- Запись видео
    local function record()
        changeColor(colors[3]) -- Зелёный цвет светодиодов
        camera.requestRecordStart() -- Отправить запрос на запись видео
        -- Ждём подтверждения
        while camera.checkRequestRecord() == -1 do
        end
        -- Ждём 10 секунд, чтобы получилось 10-секундное видео
        sleep(10)
        camera.requestRecordStop() -- Отправить запрос на остановку видео
        -- Ждём подтверждения
        while camera.checkRequestRecord() == -1 do
        end
        changeColor(colors[1]) -- Выключаем светодиоды
    end

    -- ОСНОВНAЯ ПРОГРАММА
    makeShot() -- сделать снимок
    sleep(2) -- ждём 2 секунды
    record() -- записывать видео


