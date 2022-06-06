import logging
from functools import reduce

# import numpy
import pandas

import records

log = logging.getLogger("merge")
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)


def unique(l: list) -> list:
    u = []
    for e in l:
        if e not in u:
            u.append(e)
    return list(u)


df1 = pandas.DataFrame(records.r1)
df2 = pandas.DataFrame(records.r2)
df3 = pandas.DataFrame(records.r3)
df_list = [df1, df2, df3]
df_keys = {
    0: ["ID", "SERIAL"],
    1: ["HOST_NM"],
    2: ["HOST_NM", "SERIAL"],
}
target_columns = ["HOST_NM", "SERIAL", "IP_ADDRESS"]
df = reduce(lambda left, right: pandas.merge(
    left, right, on=["HOST_NM"], how="outer"), df_list)
log.debug(df)

# Replace null and empty strings with numpy.NaN
# df = df.replace(r"^\s*$", numpy.NaN, regex=True)
df = df.mask(df == '')
log.debug(f'\n\n{df}')
