import time

import serial
import serial.tools.list_ports

port = None
ports = serial.tools.list_ports.comports()
for _port in ports:
  if "Betaflight" in _port.description:
    port = _port
    break


if not port:
  print(" >>> Port not found")
  exit()


ser = serial.Serial(
  port.device,
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

open(f"presets/bnf/{name}.txt", "w").write(f"""#$ TITLE: {name} defaults
#$ FIRMWARE_VERSION: 4.4
#$ CATEGORY: BNF
#$ STATUS: COMMUNITY
#$ KEYWORDS: defaults
#$ AUTHOR: gebeto


{diff}
""")

ser.write(b'exit\n')
ser.close()