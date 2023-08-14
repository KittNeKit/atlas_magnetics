import serial
import time

COM_PORT = 'COM/PORT'  # Replace with your COM port
BAUD_RATE = 9600

ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)


def measure_voltage(nplc):
    ser.write(f"VOLT:DC:NPLC {nplc}\n".encode())
    ser.write("READ?\n".encode())
    voltage = ser.readline().decode().strip()
    return float(voltage)


try:
    for nplc in [1, 5, 10]:
        while True:
            voltage = measure_voltage(nplc)
            print(f"Measured voltage (NPLC={nplc}): {voltage} V")
            time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")

finally:
    ser.close()
    print("Serial connection closed")
