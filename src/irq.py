from machine import Pin

print("Entering irq.py")
led1 = Pin(16, Pin.OUT)
led2 = Pin(17, Pin.OUT)
p27 = Pin(27, Pin.IN)
count = 0

def setLed(pin):
    print(count)
    count += 1
    if (count % 2) == 0:
        led1.on()
        led2.off()
    else:
        led1.off()
        led2.on()

p27.irq(handler=setLed, trigger=Pin.IRQ_FALLING)
