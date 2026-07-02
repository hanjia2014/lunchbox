d = 0

def on_servos_run(p0: number, p1: number):
    servos.P0.run(p0)
    servos.P1.run(p1)
    
def on_button_pressed_a():
    # servos.P0.run(0)
    # servos.P1.run(0)
    on_servos_run(0, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global d
    d = sonar.ping(DigitalPin.P3, DigitalPin.P2, PingUnit.CENTIMETERS)
    if d > 0 and d < 50:
        # servos.P0.run(0)
        # servos.P1.run(0)
        on_servos_run(0, 0)
        basic.pause(100)
        # servos.P0.run(70)
        # servos.P1.run(0 - 70)
        on_servos_run(70, 0 - 70)
        basic.pause(400)
        # servos.P0.run(70)
        # servos.P1.run(0 - 70)
        on_servos_run(70, 0 - 70)
        basic.pause(400)
    else:
        servos.P0.run(70)
        servos.P1.run(0 - 70)
    basic.pause(50)
basic.forever(on_forever)
