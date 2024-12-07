import serial

def read_serial_data(port, baud_rate, timeout=1):
    """
    Reads data from the specified serial port and displays it.
    Matches Tera Term configuration.
    """
    try:
        # Configure the serial port
        with serial.Serial(
            port=port,
            baudrate=baud_rate,
            bytesize=serial.EIGHTBITS,  # 8 data bits
            parity=serial.PARITY_NONE,  # No parity
            stopbits=serial.STOPBITS_ONE,  # 1 stop bit
            timeout=timeout,  # Timeout for reading
            xonxoff=False,  # No software flow control
            rtscts=False,  # No hardware (RTS/CTS) flow control
        ) as ser:
            print(f"Connected to {port} at {baud_rate} baud.")

            while True:
                # Read and decode data
                data = ser.read(ser.in_waiting or 1)  # Read available data
                if data:
                    print(data.decode('latin-1', errors='ignore'), end='')  # Decode and print
    except serial.SerialException as e:
        print(f"Serial port error: {e}")
    except KeyboardInterrupt:
        print("Serial reading stopped by user.")

if __name__ == "__main__":
    # Update port to match Tera Term configuration
    read_serial_data(port="/dev/tty.usbserial-A5XK3RJT", baud_rate=115200)
