import pandas as pd
import sys
import xlrd
import numpy as np
import time
from datetime import date,datetime

def compare_time(time1,time2):


    s_time = time.mktime(time.strptime(time1,'%Y-%m-%d'))
    if len(time2) > 11:
        e_time = time.mktime(time.strptime(time2,'%Y-%m-%d %H:%M:%S'))
    else:
        e_time = time.mktime(time.strptime(time2, '%Y-%m-%d'))

    result =int(s_time) - int(e_time)
    return result

def nat_check(nat):
    return nat == np.datetime64('NaT')

def main():
    file = sys.argv[1]
    date_time = sys.argv[2]
    print(file)
    print(date)
    content = xlrd.open_workbook(filename=file, encoding_override='gbk')
    df = pd.read_excel(content)
    map = {}
    for ind, row in df.iterrows():
        print(ind)
        # print(row[0], row[1], row[2])
        code = row[1]
        change_date = row[3]
        if str(code) == 'NaT':
            break
        if compare_time(str(date_time), str(change_date)) > 0:
            if row[4] == u'纳入':
                # print('纳入')
                map[code] = row
            else:
                # print('剔除')
                map.pop(code)
        else:
            print(123)
    # print(len(map))

    my_df = pd.DataFrame.from_dict(map, orient='index')

    # print(my_df)
    my_df.to_excel('./output'+date_time+'.xls')



if __name__ == "__main__":
    main()