import pandas as pd
from clean import get_source_data


def day_time(datetime_str):

    if 0 <= datetime_str.hour < 6:
        x = '0点-5点'
    elif 6 <= datetime_str.hour < 12:
        x = '6点-11点'
    elif 12 <= datetime_str.hour < 18:
        x = '12点-17点'
    else:
        x = '18点-23点'
    return x


def is_week(datetime_str):

    if 0 <= datetime_str.weekday() <=4:
        x = '工作日'
    else:
        x = '非工作日'
    return x


def get_specific_time(data):
    data.capture_time = pd.to_datetime(data.capture_time)
    data['day'] = data.capture_time.apply(lambda x: x.day)
    data['time'] = data.capture_time.apply(day_time)
    data['is_weekday'] = data.capture_time.apply(is_week)
    return data
if __name__ == '__main__':
    # data = pd.read_csv('yunniao.csv', index_col=0, parse_dates=True, encoding='gbk')
    source_data = get_source_data()
    data = get_specific_time(source_data)
    a = pd.pivot_table(data, values='task_id', index=['day', 'is_weekday'], columns=['time'], aggfunc='count', margins=True)
    a.to_csv('pivot_table.csv', index=True)