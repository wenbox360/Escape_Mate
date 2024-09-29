import serial
import asyncio

# Simple async demo game
async def game():
    ser = serial.Serial("/dev/ttyAMA0", 9600)  # Open port with baud rate

    try:
        # Read serial port in a non-blocking way
        received_data = await asyncio.to_thread(ser.read, 6)  # Read 5 bytes
        await asyncio.sleep(0.03)  # Non-blocking sleep

        # Check for remaining bytes and append them
        data_left = await asyncio.to_thread(ser.inWaiting)
        if data_left > 0:
            received_data += await asyncio.to_thread(ser.read, data_left)  # Read remaining bytes

        # Ensure we have enough data
        if len(received_data) < 6:
            print("Error: Insufficient data received.")
            return False

        print(received_data)  # Print received data
        await asyncio.to_thread(ser.write, received_data)  # Transmit data serially

        # Evaluate LED statuses
        LED1_status = received_data[0]
        LED2_status = received_data[1]
        LED3_status = received_data[2]
        LED4_status = received_data[3]
        LED5_status = received_data[4]

        # Return result based on LED statuses
        return LED1_status == 1 and LED2_status == 1 and LED3_status == 1 and LED4_status == 1 and LED5_status == 1

    finally:
        ser.close()  # Ensure port is closed when done

