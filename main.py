def car_back():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.BACK, speed_LF)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.BACK, speed_LB)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.BACK, speed_RF)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.BACK, speed_RB)
def car_move_RF():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.FORWARD, speed_LF)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.FORWARD, 0)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.FORWARD, 0)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.FORWARD, speed_RB)
def drift_left():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.BACK, 0)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.BACK, speed_LB)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.BACK, 0)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.FORWARD, speed_RB)
def car_left():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.BACK, speed_LF)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.BACK, speed_LB)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.FORWARD, speed_RF)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.FORWARD, speed_RB)

def on_bluetooth_connected():
    global connect_flag, ble_val, color_num, speed_LF, speed_LB, speed_RF, speed_RB
    basic.show_icon(IconNames.HEART)
    connect_flag = 1
    while connect_flag == 1:
        ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        serial.write_string(ble_val)
        serial.write_line("")
        if ble_val == "a":
            car_forward()
        elif ble_val == "b":
            car_left()
        elif ble_val == "c":
            car_back()
        elif ble_val == "d":
            car_right()
        elif ble_val == "k":
            car_left_move()
        elif ble_val == "h":
            car_right_move()
        elif ble_val == "g":
            car_move_RF()
        elif ble_val == "i":
            car_move_RB()
        elif ble_val == "j":
            car_move_LB()
        elif ble_val == "l":
            car_move_LF()
        elif ble_val == "s":
            mecanumRobot.state(MotorState.STOP)
        elif ble_val == "t":
            mecanumRobot.set_led(LedCount.LEFT, LedState.ON)
            mecanumRobot.set_led(LedCount.RIGHT, LedState.ON)
        elif ble_val == "u":
            mecanumRobot.set_led(LedCount.LEFT, LedState.OFF)
            mecanumRobot.set_led(LedCount.RIGHT, LedState.OFF)
        elif ble_val == "e":
            drift_left()
        elif ble_val == "f":
            drift_right()
        elif ble_val == "m":
            if color_num < 9:
                color_num = color_num + 1
            showcolor()
        elif ble_val == "n":
            if color_num > 0:
                color_num = color_num - 1
            showcolor()
        elif ble_val == "o":
            strip.clear()
            strip.show()
        elif ble_val == "v":
            ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
            basic.pause(100)
            speed_LF = parse_float(ble_val)
            basic.pause(100)
            serial.write_number(speed_LF)
            serial.write_line("")
        elif ble_val == "w":
            ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
            basic.pause(100)
            speed_LB = parse_float(ble_val)
            basic.pause(100)
            serial.write_number(speed_LB)
            serial.write_line("")
        elif ble_val == "x":
            ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
            basic.pause(100)
            speed_RF = parse_float(ble_val)
            basic.pause(100)
            serial.write_number(speed_RF)
            serial.write_line("")
        elif ble_val == "y":
            ble_val = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
            basic.pause(100)
            speed_RB = parse_float(ble_val)
            basic.pause(100)
            serial.write_number(speed_RB)
            serial.write_line("")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def car_move_LB():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.BACK, speed_LF)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.FORWARD, 0)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.FORWARD, 0)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.BACK, speed_RB)
def showcolor():
    if color_num == 0:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    elif color_num == 1:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    elif color_num == 2:
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    elif color_num == 3:
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    elif color_num == 4:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    elif color_num == 5:
        strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    elif color_num == 6:
        strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
    elif color_num == 7:
        strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
    elif color_num == 8:
        strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
    strip.show()
def car_move_RB():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.BACK, 0)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.BACK, speed_LB)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.BACK, speed_RF)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.BACK, 0)
def tracking():
    if mecanumRobot.line_tracking(LT.LEFT) == 1 and mecanumRobot.line_tracking(LT.RIGHT) == 0:
        car_left()
    elif mecanumRobot.line_tracking(LT.LEFT) == 0 and mecanumRobot.line_tracking(LT.RIGHT) == 1:
        car_right()
    elif mecanumRobot.line_tracking(LT.LEFT) == 1 and mecanumRobot.line_tracking(LT.RIGHT) == 1:
        car_forward()
    else:
        mecanumRobot.state(MotorState.STOP)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SMALL_HEART)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def car_right_move():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.FORWARD, speed_LF)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.BACK, speed_LB)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.BACK, speed_RF)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.FORWARD, speed_RB)
def drift_right():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.BACK, 0)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.FORWARD, speed_LB)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.BACK, 0)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.BACK, speed_RB)
def follow():
    mecanumRobot.set_servo(90)
    basic.pause(500)
    if mecanumRobot.ultra() < 10:
        car_back()
    elif mecanumRobot.ultra() < 20:
        mecanumRobot.state(MotorState.STOP)
    elif mecanumRobot.ultra() < 40:
        car_forward()
    else:
        mecanumRobot.state(MotorState.STOP)
def car_move_LF():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.FORWARD, 0)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.FORWARD, speed_LB)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.FORWARD, speed_RF)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.FORWARD, 0)
def avoid():
    global distance, distance_l, distance_r
    distance = mecanumRobot.ultra()
    if distance < 20:
        mecanumRobot.state(MotorState.STOP)
        basic.pause(500)
        mecanumRobot.set_servo(180)
        basic.pause(500)
        distance_l = mecanumRobot.ultra()
        basic.pause(500)
        mecanumRobot.set_servo(10)
        basic.pause(500)
        distance_r = mecanumRobot.ultra()
        basic.pause(500)
        if distance_l > distance_r:
            car_left()
            basic.pause(300)
        else:
            car_right()
            basic.pause(300)
    else:
        basic.pause(500)
        car_forward()
        mecanumRobot.set_servo(90)
def car_forward():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.FORWARD, speed_LF)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.FORWARD, speed_LB)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.FORWARD, speed_RF)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.FORWARD, speed_RB)
def car_left_move():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.BACK, speed_LF)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.FORWARD, speed_LB)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.FORWARD, speed_RF)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.BACK, speed_RB)
def car_right():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.FORWARD, speed_LF)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.FORWARD, speed_LB)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.BACK, speed_RF)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.BACK, speed_RB)
distance_r = 0
distance_l = 0
distance = 0
ble_val = ""
connect_flag = 0
strip: neopixel.Strip = None
color_num = 0
speed_RF = 0
speed_RB = 0
speed_LF = 0
speed_LB = 0
serial.redirect_to_usb()
speed_LB = 75
speed_LF = 75
speed_RB = 75
speed_RF = 75
color_num = 0
strip = neopixel.create(DigitalPin.P8, 4, NeoPixelMode.RGB)
basic.show_icon(IconNames.HOUSE)

def on_forever():
    if ble_val == "p":
        tracking()
    elif ble_val == "q":
        follow()
    elif ble_val == "r":
        avoid()
    elif ble_val == "s":
        mecanumRobot.state(MotorState.STOP)
        mecanumRobot.set_servo(90)
basic.forever(on_forever)
