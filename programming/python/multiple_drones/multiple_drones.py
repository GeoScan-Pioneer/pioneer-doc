import keyboard
from pioneer_sdk import Pioneer

coord_x = float(0)
coord_y = float(0)
coord_z = float(1)
yaw = float(0)

increment = float(0.1)
yaw_increment = float(0.1)

def arm(event):
    pioneer_mini1.arm()
    pioneer_mini2.arm()

def disarm(event):
    pioneer_mini1.disarm()
    pioneer_mini2.disarm()

def takeoff(event):
    pioneer_mini1.takeoff()
    pioneer_mini2.takeoff()

def land(event):
    pioneer_mini1.land()
    pioneer_mini2.land()

def forward(event):
    global coord_y
    coord_y += increment
    pioneer_mini1.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)
    pioneer_mini2.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)

def backward(event):
    global coord_y
    coord_y -= increment
    pioneer_mini1.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)
    pioneer_mini2.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)

def right(event):
    global coord_x
    coord_x += increment
    pioneer_mini1.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)
    pioneer_mini2.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)

def left(event):
    global coord_x
    coord_x -= increment
    pioneer_mini1.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)
    pioneer_mini2.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)

def up(event):
    global coord_z
    coord_z += increment
    pioneer_mini1.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)
    pioneer_mini2.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)

def down(event):
    global coord_z
    coord_z -= increment
    pioneer_mini1.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)
    pioneer_mini2.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)

def turn_right(event):
    global yaw
    yaw += yaw_increment
    pioneer_mini1.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)
    pioneer_mini2.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)

def turn_left(event):
    global yaw
    yaw -= yaw_increment
    pioneer_mini1.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)
    pioneer_mini2.go_to_local_point(x=coord_x, y=coord_y, z=coord_z, yaw=yaw)



if __name__ == '__main__':
    pioneer_mini1 = Pioneer(pioneer_ip='192.168.147.141') # Укажите IP вашего дрона
    pioneer_mini2 = Pioneer(pioneer_ip='192.168.147.10') # Укажите IP вашего дрона
    keyboard.on_press_key('1', arm)
    keyboard.on_press_key('2', disarm)
    keyboard.on_press_key('3', takeoff)
    keyboard.on_press_key('4', land)
    keyboard.on_press_key('w', forward)
    keyboard.on_press_key('s', backward)
    keyboard.on_press_key('d', right)
    keyboard.on_press_key('a', left)
    keyboard.on_press_key('space', up)
    keyboard.on_press_key('shift', down)
    keyboard.on_press_key('e', turn_right)
    keyboard.on_press_key('q', turn_left)
    while True:
        if keyboard.is_pressed('esc'):
            pioneer_mini1.land()
            pioneer_mini2.land()
            exit(0)
