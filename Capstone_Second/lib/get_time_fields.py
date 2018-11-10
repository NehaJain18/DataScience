# -*- coding: utf-8 -*-


# -- ==identifier== --
def get_time_fields(x):
    import pandas as pd
    utc = pd.datetime.utcfromtimestamp(x)
    result = {'year': utc.year, 'month' : utc.month,'day': utc.day, 'weekday': utc.weekday(), 'hour': utc.hour}
    return pd.Series(result)

# -- ==identifier== --