Управление квадрокоптером с контроллера Трик
============================================


Необходимое оборудование
------------------------

Для тестирования работы протокола Mailbox не обязательно иметь реальный контроллер Трик, так как среда разработки TrikStudio
имеет встроенный симулятор, который поддерживает передачу данных по Mailbox, поэтому, список необходимого оборудования и ПО
выглядит следующим образом:

#. `TrikStudio. <https://trikset.com/downloads#trikstudio>`__
#. `PioneerStation. <https://dl.geoscan.aero/pioneer/upload/GCS/GEOSCAN_Pioneer_Station.exe>`__
#. `Квадрокоптер Геоскан Пионер Мини. <https://www.geoscan.aero/ru/products/pioneer/mini>`__
#. `Контроллер Трик (опционально). <https://trikset.com/prices>`__



Подготовка к работе
-------------------

#. Ознакомиться с `описанием протокола mailbox <../../programming/info-interfaces/pages/mailbox/mailbox.html>`__,
#. Ознакомиться с `описанием api объекта mailbox. <../../programming/lua/sections/0009_mailbox.html>`__
#. Произвести настройку оборудования в соответсвии с выбранными устройствами `по инструкциям <../../programming/info-interfaces/pages/mailbox/mailbox.html#id3>`__


.. note::
    Если у вас нет контроллера Трик и вы используете симуляцию в TrikStudio, то в LUA коде при подключении
    ( ф-я ``mailbox.connect()`` ) будет использоваться IP адрес вашего компьютера.

Основные сведения по работе с протоколом Mailbox
------------------------------------------------

Для понимания работы проекта следует ознакомиться с `документацией по протоколу mailbox, <../../programming/info-interfaces/pages/mailbox/mailbox.html>`__
а также с `описанием api объекта mailbox. <../../programming/lua/sections/0009_mailbox.html>`__


Код для квадрокоптера на Lua
----------------------------

.. code:: lua

    -- Simplification and caching table.unpack calls
    local unpack = table.unpack

    -- Base pcb number of RGB LEDs
    local ledNumber = 4
    -- RGB LED control port initialize
    local leds = Ledbar.new(ledNumber)

    -- Function changes color on all LEDs
    local function changeColor(color)
        -- Changing color on each LED one after another
        for i=0, ledNumber - 1, 1 do
            leds:set(i, unpack(color))
        end
    end

    -- Table of colors in RGB form for changeColor function
    local colors = {
            {1, 0, 0}, -- r
            {0, 1, 0}, -- g
            {0, 0, 1}, -- b
            {1, 1, 1}, -- w
    }


    -- Event processing function called automatically by autopilot
    function callback(event)

    end

    function lshift(x, by)
      return x * 2 ^ by
    end

    function rshift(x, by)
      return math.floor(x / 2 ^ by)
    end

    function BitAND(a,b)
        local p,c=1,0
        while a>0 and b>0 do
            local ra,rb=a%2,b%2
            if ra+rb>1 then c=c+p end
            a,b,p=(a-ra)/2,(b-rb)/2,p*2
        end
        return c
    end

    mailbox.setHullNumber(45);

    changeColor(colors[lshift(1, 2)]);

    -- example of message 0b 001 00000

    while(true)
    do
        hull, msg = mailbox.receive(true);

        cmd = rshift(BitAND(tonumber(msg), 224), 5);

        if(msg=="0") then
            changeColor({0,0,0});
            break;
        end;

        if(cmd == 1) then
            local r = rshift(BitAND(tonumber(msg), 4), 2);
            local g = rshift(BitAND(tonumber(msg), 2), 1);
            local b = BitAND(tonumber(msg), 1);
            changeColor({r,g,b});
        end
        if(cmd == 2) then
            local val = BitAND(tonumber(msg), 3);

            if(val == 0) then
                data,_,_,_,_ = Sensors.range();
                mailbox.send(hull, data);
            end
            if(val == 1) then
                data = Sensors.altitude();
                mailbox.send(hull, data);
            end
            if(val == 2) then
                roll,pitch,yaw = Sensors.orientation();
                mailbox.send(hull, math.floor(roll));
                mailbox.send(hull, math.floor(pitch));
                mailbox.send(hull, math.floor(yaw));
            end
            if(val == 3) then
                gx,gy,gz = Sensors.gyro();
                mailbox.send(hull, math.floor(gx));
                mailbox.send(hull, math.floor(gy));
                mailbox.send(hull, math.floor(gz));
            end
        end
        if(cmd == 3) then
            local val = BitAND(tonumber(msg), 7);
            if(val == 0) then
                ap.push(Ev.MCE_PREFLIGHT);
            end
            if(val == 4) then
                ap.push(Ev.ENGINES_DISARM);
            end
        end
    end



Код для контроллера Трик
------------------------

.. code:: javascript

    // глобальная переменаая-флаг состояния работы программы
    var stop = false;

    // callback функция, вызываемая, при нажатии на любую кнопку контроллера
    // принимает code - код кнопки, и value - значение
    // (1 - нажатие, 0 - отпускание, 2 - зажатие)
    var keys_handler = function(code, value){
        switch(code){
            case KeysEnum.Up:
                code = 1;
                if(value == 1)	Menu.pointer_l--;
                break;
            case KeysEnum.Left:
                code = 2;
                break;
            case KeysEnum.Down:
                code = 3;
                if(value == 1)	Menu.pointer_l++;
                break;
            case KeysEnum.Power:
                code = 4;
                break;
            case KeysEnum.Esc:
                code = 5;
                if (Menu.deph != 0 && value == 1){
                    Menu.deph--;
                    Menu.pointer_l = Menu.pointer_h;
                }
                break;
            case KeysEnum.Right:
                code = 6;
                break;
            case KeysEnum.Enter:
                code = 7;
                if(value == 1)	menu_enter_handler();
                break;
        }

        if(code != 7)	draw_menu();
    }

    var Menu = {
        // главные заголовки меню
        heads: ["RGB LEDS", "SENSORS", "FLYING", "EXIT"],
        // второй уровень меню, каждый элемент массива соответствует главным заголовкам
        lables: [
            ["|-Red", "|-Green", "|-Blue"],
            ["|-Distance", "|-Altitude", "|-Orientation", "|-Gyro"],
            ["|-Arm", "|-Takeoff", "|-Go forward", "|-Go backward", "|-Go left", "|-Go right", "|-Land", "|-Disarm"],
            ["|-Sure exit?"]
        ],
        // действия при нажатии на каждый заголовок второго уровня
        actions: [
            [
                function() {Menu.colors[0] = !Menu.colors[0]; mailbox.send( 45, (1<<5) + Menu.convert_color_to_int() )},
                function() {Menu.colors[1] = !Menu.colors[1]; mailbox.send( 45, (1<<5) + Menu.convert_color_to_int() )},
                function() {Menu.colors[2] = !Menu.colors[2]; mailbox.send( 45, (1<<5) + Menu.convert_color_to_int() )},
            ],
            [
                function() {mailbox.send( 45, (2<<5) + 0); process_dst_parser()},
                function() {mailbox.send( 45, (2<<5) + 1); process_alt_parser()},
                function() {mailbox.send( 45, (2<<5) + 2); process_orientation_parser()},
                function() {mailbox.send( 45, (2<<5) + 3); process_accel_parser()},
            ],
            [
                function() {mailbox.send( 45, (3<<5) + 0)},
                function() {mailbox.send( 45, (3<<5) + 1)},
                function() {mailbox.send( 45, (3<<5) + 2)},
                function() {mailbox.send( 45, (3<<5) + 3)},
                function() {mailbox.send( 45, (3<<5) + 4)},
                function() {mailbox.send( 45, (3<<5) + 5)},
                function() {mailbox.send( 45, (3<<5) + 6)},
                function() {mailbox.send( 45, (3<<5) + 7)},
            ],
            [
                function() {mailbox.send(45, 0); stop=true;}
            ]

        ],
        // указатель текущего уровня погружения в меню (0 - заголовки первого уровня, 1 - второго)
        deph: 0,
        // расстояние в пикселях между элементами меню
        space_y: 20,
        // текущее положение курсора на заголовках первого уровня
        pointer_h: 0,
        // текущее положение курсора на заголовках второго уровня
        pointer_l: 0,
        // состояния RGB светодиодов соответственно
        colors: [false,false,false],
        convert_color_to_int: function(){
            return ((Menu.colors[0]<<2) + (Menu.colors[1]<<1) + (Menu.colors[2]<<0))
        }
    }

    // отрисовка меню
    var draw_menu = function(){
        brick.display().clear()

        if(Menu.deph == 0){
            if(Menu.pointer_l < 0)	Menu.pointer_l = 0;
            if(Menu.pointer_l > Menu.heads.length-1)	Menu.pointer_l = Menu.heads.length-1;

            for (var i=0; i<Menu.heads.length; i++){
                brick.display().addLabel(Menu.heads[i], 25, (i+1)*Menu.space_y)
            }
        }
        else {
            if(Menu.pointer_l < 0)	Menu.pointer_l = 0;
            if(Menu.pointer_l > Menu.lables[Menu.pointer_h].length-1)	Menu.pointer_l = Menu.lables[Menu.pointer_h].length-1;

            for (var i=0; i<Menu.lables[Menu.pointer_h].length; i++){
                brick.display().addLabel(Menu.lables[Menu.pointer_h][i], 25, (i+1)*Menu.space_y)
            }
        }

        brick.display().addLabel("->", 0, (Menu.pointer_l+1)*Menu.space_y)

        brick.display().redraw()
    }

    //обработка нажатия на Enter, вызывается внутри keys_handler
    var menu_enter_handler = function() {
        if(Menu.deph == 0){
            Menu.pointer_h = Menu.pointer_l;
            Menu.pointer_l = 0;
            Menu.deph++;
        }
        else {
            Menu.actions[Menu.pointer_h][Menu.pointer_l]();
        }
        draw_menu()
    }

    // выводит всплывающее окно с показаниями датчиков (ответ от квадрокоптера)
    // принимает массив с именами показаний, которые ожидаются
    var process_sensors_parser = function(names) {
        brick.display().clear();
        for(var j=0; j < names.length; j++){
            msg = mailbox.receive();
            brick.display().addLabel(names[j] + Math.round(Number(msg)*100)/100, 25, 70 + (j+1)*20)
        }
        brick.display().redraw();
        script.wait(2000);
        draw_menu();
    }

    var process_dst_parser = function() {
        var names = ["Distance: "]
        process_sensors_parser(names);
    }

    var process_alt_parser = function() {
        var names = ["Altitude: "]
        process_sensors_parser(names);
    }

    var process_orientation_parser = function() {
        var names = ["Roll: ", "Pitch: ", "Azimuth: "]
        process_sensors_parser(names);
    }

    var process_accel_parser = function() {
        var names = ["Gx: ", "Gy: ", "Gz: "]
        process_sensors_parser(names);
    }

    var main = function() {
        brick.keys().buttonPressed.connect(keys_handler)
        draw_menu()

        // УКАЖИТЕ ПРАВИЛЬНЫЙ IP КВАДРОКОПТЕРА В ВАШЕЙ СЕТИ
        // если точкой доступа является сам квадрокоптера, ip удрес будет 192.168.4.1
        mailbox.connect("192.168.43.182", 8889)
        script.wait(1000)
        print('Connection should be done')

        // пустой бесконечный цикл с одной лишь командой задержки
        // поскольку все нажатия и команды обрабатываются как callback-функции
        while(!stop){
            script.wait(10)
        }
    }
