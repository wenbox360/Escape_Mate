import serial
from time import sleep

#Simple demo game
def game():
    while True:
        ser = serial.Serial ("/dev/ttyAMA0", 9600)    #Open port with baud rate
        received_data = ser.read()              #read serial port
        sleep(0.03)
        data_left = ser.inWaiting()             #check for remaining byte
        received_data += ser.read(data_left)
        print (received_data)                   #print received data
        ser.write(received_data)                #transmit data serially 


        LED1_status = received_data[0]
        LED2_status = received_data[1]
        LED3_status = received_data[2]
        LED4_status = received_data[3]
        LED5_status = received_data[4]

        if LED1_status == '4' and LED2_status == '3' and LED3_status == '5' and LED4_status == '1' and LED5_status == '2':  
            return True 