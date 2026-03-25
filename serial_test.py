import serial
import time

print("Opening serial connection...")
ser = serial.Serial('/dev/ttyUSB0',
	115200,
	timeout=1,
	dsrdtr=False,
	rtscts=False
	)

print("Waiting for ESP32 to boot...")

# Critical: disable DTR/RTS AFTER opening
ser.setDTR(False)
ser.setRTS(False)

time.sleep(2) # allow ESP32 to reset after connection, enough time to fully boot

ser.reset_input_buffer()
ser.reset_output_buffer()

print("Sending ON")
ser.write(b'ON\n')
ser.flush()

time.sleep(3)

print("Sending OFF")
ser.write(b'OFF\n')
ser.flush()

ser.close()

print("Done")
