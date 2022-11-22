Перемещение по точкам в локальной системе координат.
====================================================

.. code:: lua

    local boardNumber = boardNumber
    local unpack = table.unpack
    local points = {
            {-0.6, 0.3, 0.2},
            {0.6, 0.3,  0.2},
            {0, 0, 0.5},
            {0.6, -0.3, 0.2}
    }

    local curr_point = 1

    local function nextPoint()
        if(#points >= curr_point) then
            ap.goToLocalPoint(unpack(points[curr_point]))
            curr_point = curr_point + 1
        else
            ap.push(Ev.MCE_LANDING)
        end
    end

    function callback(event)
        if(event == Ev.TAKEOFF_COMPLETE) then
            nextPoint()
        end
        if(event == Ev.POINT_REACHED) then
            nextPoint()
        end
    end


    local leds = Ledbar.new(1)
    local blink = 0
    leds:set(0,1,1,1)
    timerBlink = Timer.new(1, function ()
            if(blink == 1) then
                blink = 0
            else
                blink = 1
            end
            leds:set(0, blink, 0, 0)
    end)
    timerBlink:start()
    ap.push(Ev.MCE_PREFLIGHT)
    Timer.callLater(1, function() ap.push(Ev.MCE_TAKEOFF) end)

