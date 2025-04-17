from alert.serial import Serial

def main():
    print("Main routine in the driver")
    alert = Serial()
    print(alert.run())
