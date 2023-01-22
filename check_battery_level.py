import subprocess  # To install packages
import platform  # Check operating system
import importlib.util

spec = importlib.util.find_spec("psutil")
if spec is None:
    subprocess.run(["pip", "install", "psutil"])

# psutil package used to check battery level
import psutil

# Check battery level
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

print("\nOperation system: " + platform.system())

if not plugged:
    print(f'Battery percent: {percent}')
else:
    print('Computer is running on AC power')
