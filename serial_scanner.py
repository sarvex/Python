import sys

import serial


# A serial port-scanner for linux and windows platforms

# Author: Julio César Echeverri Marulanda
# e-mail: julio.em7@gmail.com
# blog:   blogdelingeniero1.wordpress.com

# You should have installed the PySerial module to use this method.

# You can install pyserial with the following line:      pip install pyserial


def ListAvailablePorts():
    # This function return a list containing the string names for Virtual Serial Ports
    # availables in the computer (this function works only for Windows & Linux Platforms but you can extend it)
    # if there isn't available ports, returns an empty List
    AvailablePorts = []
    platform = sys.platform
    if platform == 'linux':
        for i in range(0, 255):
            try:
                ser = serial.Serial(f'/dev/ttyUSB{str(i)}')
            except serial.serialutil.SerialException:
                pass
            else:
                AvailablePorts.append(f'/dev/ttyUSB{str(i)}')
                ser.close()
    elif platform == 'win32':
        for i in range(255):
            try:
                ser = serial.Serial(i, 9600)
            except serial.serialutil.SerialException:
                pass
            else:
                AvailablePorts.append(ser.portstr)
                ser.close()

    else:
        print('''This method was developed only for linux and windows
                the current platform isn't recognised''')
    if AvailablePorts:
        return AvailablePorts
    print("NO port in use")
    return 0

#  EXAMPLE OF HOW IT WORKS

#  if an Arduino is connected to the computer, the port will be show in the terminal
#  print ListAvailablePorts()
