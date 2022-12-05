import serial
import time
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1) # port may vary
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("Enter Value: ") 
    value = write_read(num)
    print(value) 
