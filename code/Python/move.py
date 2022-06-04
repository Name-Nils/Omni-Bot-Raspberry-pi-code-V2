import serial


ser = serial.Serial(
    port='/dev/ttyACM0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


def send(data):
    ser.write((str(data) + "\n").encode("utf-8"))

last_string = ""
def move_str(string_):
    global last_string
    if (last_string != string_):
        print (string_ + "\n")
        ser.write((string_ + "\n").encode("utf-8"))
    last_string = string_


