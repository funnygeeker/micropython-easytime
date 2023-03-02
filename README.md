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

# 现在的以此类推，此处不再举例
# 从 NTP 时间服务器同步时间（请先连接网络）
# et.sync()
```