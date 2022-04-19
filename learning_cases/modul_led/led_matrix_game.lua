function callback( event )
end

-- 6 14 18 26
k=16
leds = Ledbar.new(29)
     leds:set(k, 0, 0.2, 0)
function main_program()
    roll, pitch, yaw = Sensors.orientation()
    
        if roll < -20 then
            kold=k
            k=k-1
        
        
        elseif roll > 20 then
            kold=k
            k=k+1
        
        
        elseif pitch < -20 then
           kold=k
            k=k-5
        
        
        elseif pitch > 20 then
          kold=k
            k=k+5
        end
        
        leds:set(k, 0, 0.2, 0)
        leds:set(kold, 0, 0, 0)
        Timer.callLater(0.3, function () main_program() end)
end

main_program()
