# micropython-easytime
适用于 micropython 的时间设置与管理模块，可以较为方便地设置、获取或同步时间

### 代码示例
```python
from libs.easytime import EasyTime

# time_zone 为时区
et = EasyTime(time_zone=8, datetime=(2023, 1, 1, 6, 0, 0, 0, 0))

# 获取当前时间
print(et.time())
# (2023, 1, 1, 6, 0, 0, 0, 226)

# 设置当前时间
print(et.time((2023, 1, 1, 6, 1, 0, 0, 0)))
# None

# 设置当前年份
print(et.year(2022))
# None

# 获取当前年份
print(et.year())
# 2023

# 获取当前月份
print(et.month())
# 1

# 其他的详见源码，以此类推，此处不再举例
# 从 NTP 时间服务器同步时间（请先连接网络）
# et.sync()
```

### 注意事项
- 时间同步需要连接网络，在硬件允许的情况下，您可以使用 `micropython-easynetwork` 连接无线网络，也可以用其他的方式。
- [https://github.com/funnygeeker/micropython-easynetwork](https://github.com/funnygeeker/micropython-easynetwork)

### 参考资料
Github - PyClock：[https://github.com/01studio-lab/pyClock](https://github.com/01studio-lab/pyClock)

MicroPython - Docs：[https://docs.micropython.org/en/latest/library/pyb.RTC.html](https://docs.micropython.org/en/latest/library/pyb.RTC.html)

### 其他
感谢各位大佬对开源做出的贡献！

交流QQ群：[748103265](https://jq.qq.com/?_wv=1027&k=I74bKifU)