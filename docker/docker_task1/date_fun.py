import sys
from time import sleep
from datetime import datetime


while True:
    sys.stderr.write(f"{datetime.today()}\n")
    sleep(1)
