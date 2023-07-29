import time
import serial

ser = serial.Serial(
	'/dev/tty.usbmodem0x80000001',
	115200,
)

def _exec(command = '#', timeout = 3):
	ser.write((command + '\n').encode())
	ser.flush()

	time.sleep(timeout)
	out = ''

	# out = ser.read_all()
	while ser.inWaiting() > 0:
	    out += ser.read().decode('utf8')

	return out

def extract_name(output: str):
	last_part = output.split("# name: ")[-1]
	return last_part.split("\r\n")[0]

_exec('#', timeout=0)
diff = _exec('diff', timeout=5)
name = extract_name(diff)

if not name:
	print("ERROR: Cant dump diff, please try again")
	exit()

open(f"presets/bnf/{name}.txt", "w").write(diff)

ser.write(b'exit\n')
ser.close()