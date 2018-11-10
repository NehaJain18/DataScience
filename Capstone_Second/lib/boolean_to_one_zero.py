# -*- coding: utf-8 -*-


# -- ==identifier== --
# change boolean variables into 1/0 number
def boolean_to_one_zero(df, col, value, bool_value):
    if bool_value:
        df.loc[df[col] == value, col] = 1
        df[col].fillna(0,inplace=True)
    else:
        df.loc[df[col] == value, col] = 0
        df[col].fillna(1,inplace=True)
    df[col] = df[col].astype(int)

# -- ==identifier== --