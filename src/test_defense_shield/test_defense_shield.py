from test_defense_shield.alert import serial
from . import __version__

def main():
    print("Main routine in the driver")
    alert = serial.Serial()
    print(alert.run())
    print(__version__)
