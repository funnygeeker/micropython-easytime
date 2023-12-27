[简体中文 (Chinese)](./README.ZH-CN.md)
# micropython-easytime

A time management module for `micropython` that allows for easy setting, retrieving, and synchronizing of time.

### Code Example
```python
from lib.easytime import EasyTime

et = EasyTime(time_zone=8, datetime=(2023, 1, 1, 6, 0, 0, 0, 0))

# Get the current time
print(et.time())
# (2023, 1, 1, 6, 0, 0, 0, 226)

# Set the current time
print(et.time((2023, 1, 1, 6, 1, 0, 0, 0)))
# None

# Set the current year
print(et.year(2022))
# None

# Get the current year
print(et.year())
# 2023

# Get the current month
print(et.month())
# 1

# For more details, please refer to the source code. This is just an example.
# Synchronize time from NTP time server (Please connect to the network first)
# et.sync()
```

### Notes
- Time synchronization requires a network connection. You can use `micropython-easynetwork` to connect to a wireless network or use other methods.
- [https://github.com/funnygeeker/micropython-easynetwork](https://github.com/funnygeeker/micropython-easynetwork)

### References
Github - PyClock: [https://github.com/01studio-lab/pyClock](https://github.com/01studio-lab/pyClock)

MicroPython - Docs: [https://docs.micropython.org/en/latest/library/pyb.RTC.html](https://docs.micropython.org/en/latest/library/pyb.RTC.html)