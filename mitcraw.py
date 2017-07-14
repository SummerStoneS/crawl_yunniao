from yunniao import get_response, get_details, get_quote, get_vehicle
from time import sleep
from dump import Processing
import time

while 1:
    try:
        result_list = get_response()
    except:
        sleep(200)
        continue
    dump_data = Processing()
    for task in result_list:
        task_id = task['task_id']
        if dump_data.find_exist(task_id=task_id):
            break                                           # 如果task_id存在，则直接等下一次刷新
        else:
            try:
                details = get_details(task_id)               # 如果订单结束报价，就get不到什么了。。。
                task['quote'] = get_quote(details)
                task['vehicle'] = get_vehicle(details)
            except:
                task['vehicle'] = 'over time'
                task['quote'] = 'over time'
            task['capture_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            dump_data.insert(task)
            print(task_id)
    sleep(200)                                                # 休息200秒再爬