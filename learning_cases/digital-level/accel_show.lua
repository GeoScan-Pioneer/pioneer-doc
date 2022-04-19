-- Test programm accelerometer show

-- ���������� ����������� �� �������� ����� �������(4) + �� ������ LED (25)
local ledNumber = 29
-- �������� ����� ���������� ������������
local leds = Ledbar.new(ledNumber)
local offset = 4

local pitchLED = 2 -- ��������� ���������� "���������" ���������� �� X
local rollLED = 2 -- ��������� ���������� "���������" ���������� �� Y

local function showAccel()
    leds:set(pitchLED*5 + rollLED + offset, 0, 0, 0)


    roll, pitch = Sensors.orientation() 
    rollLED = math.floor(roll/10)
    pitchLED = math.floor(pitch/10)
    
    if rollLED > 2 then
        rollLED = 2
    end
    
    if rollLED < -2 then
        rollLED = -2
    end
    
    if pitchLED > 2 then
        pitchLED = 2
    end
    
    if pitchLED < -2 then
        pitchLED = -2
    end
    
    rollLED = rollLED + 2
    pitchLED = pitchLED + 2
    
    leds:set(pitchLED*5 + rollLED + offset, 0, 1, 0)
    
end

local function test()
    leds:set(pitchLED*5 + rollLED + offset, 0, 0, 0)

    pitchLED = pitchLED + 1
    rollLED = rollLED + 1
    
    if rollLED == 5 then
        rollLED = 0
    end
    
    if pitchLED == 5 then
        pitchLED = 0
    end
    
    
    leds:set(pitchLED*5 + rollLED + offset, 0, 1, 0)
    
end


-- �������� �������, ������� ������ ������� ������ ���� ���� ����������� �� ���������
timerRandomLED = Timer.new(1, function ()
   test()
end)
-- ������ ���������� �������
timerRandomLED:start()

