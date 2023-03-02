# Author: funnygeeker（稽术宅）
# Github: https://github.com/funnygeeker/micropython-easytime
import time as _time
from machine import RTC


class EasyTime:
    def __init__(self, time_zone: int = 8, datetime: tuple = None,
                 host: str = 'time3.cloud.tencent.com', delay: int = 1000, retry: int = 3):
        """
        Args:
            time_zone: 时区
            datetime: 初始日期
            host: NTP 时间服务器的 IP 地址或域名
            delay: 获取时间失败后的间隔时间，单位：毫秒
            retry: 获取时间失败后的最大重试次数
        """
        import ntptime
        self.rtc = RTC()
        if datetime:
            self.rtc.init(datetime)
        self.host = host
        self.delay = delay
        self.retry = retry
        self.ntptime = ntptime
        self.time_zone = time_zone

    def _time(self, num: int, index: int):
        """
        [私有函数] 获取或设置具体时间
        Args:
            num: 具体数值
            index: 需要设置数据的索引
        """
        if num is None:
            return self.rtc.datetime()[index]
        else:
            time = list(self.rtc.datetime())
            time[index] = num
            return self.rtc.datetime(time)

    def year(self, time: int = None):
        """
        获取或设置年
        """
        return self._time(time, 0)

    def month(self, time: int = None):
        """
        获取或设置月
        """
        return self._time(time, 1)

    def day(self, time: int = None):
        """
        获取或设置日
        """
        return self._time(time, 2)

    def weekday(self, time: int = None):
        """
        获取或设置星期
        """
        return self._time(time, 3)

    def hour(self, time: int = None):
        """
        获取或设置时
        """
        return self._time(time, 4)

    def minute(self, time: int = None):
        """
        获取或设置分
        """
        return self._time(time, 5)

    def second(self, time: int = None):
        """
        获取或设置秒
        """
        return self._time(time, 6)

    def subsecond(self, time: int = None):
        """
        获取或设置亚秒
        """
        return self._time(time, 7)

    def time(self, time: tuple = None):
        """
        获取或设置时间
        """
        if time is None:
            return self.rtc.datetime()
        else:
            return self.rtc.datetime(time)

    def sync(self) -> bool:
        """
        与 NTP 服务器同步时间
        """
        self.ntptime.host = self.host
        # 设置NTP时区，中国在 UTC +8 时区计算方式： 3155673600 - 8*3600 = 3155644800
        self.ntptime.NTP_DELTA = 3155673600 - self.time_zone * 3600
        for i in range(self.retry):  # 最多尝试获取 self.retry 次
            try:
                self.ntptime.settime()  # 获取网络时间
                return True
            except Exception as error:
                print("[ERROR] Can not get time, Trying again({}/ {})\n{}".format(i+1, self.retry, error))
            _time.sleep_ms(self.delay)
        print("[ERROR] Can not get time, Maybe the network is not connected!")
        return False
