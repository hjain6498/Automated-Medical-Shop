#Runs on Raspberry Pi
#Uses Camera module of Raspberry Pi to get medicine data from qr-code. 

from subprocess import Popen, PIPE
import subprocess

cmd=['zbarcam', '--prescale=640x480', '--nodisplay']
cmd1=['zbarcam', '--prescale=640x480']

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
for line in iter(p.stdout.readline, b''):
    qrc=line.decode()
    lst=qrc.split(' ')
    print('Patient Name:',lst[0].split(':')[1],lst[1])
    print('Date of Prescription:',lst[2])
	print('List of Medicines:')
    for med in range(3, len(lst)):
        print('Medicine Id:', lst[med])

p.stdout.close()
p.wait()