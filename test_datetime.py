# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta
from test_map_reduce import str2int
def to_timestamp(dt_str, tz_str):
    ts_user = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    m = re.match(r'(UTC)(\+|-)(\d+):(\d+)',tz_str)
    print(m.groups())
    if m.group(2) == '+':
        h = str2int(m.group(3))
    else:
        h = -str2int(m.group(3))
    print(h)
    ts_addzone = ts_user.replace(tzinfo=timezone(timedelta(hours=h)))
    print(ts_addzone)
    return ts_addzone.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')