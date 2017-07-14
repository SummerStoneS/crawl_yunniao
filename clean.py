import pymongo
import pandas as pd


def get_collection():
    client = pymongo.MongoClient('192.168.3.109')
    client.test.authenticate = ('srf', 'chenbingxuan')
    db = client.mck
    return db.yunniao


def get_content(content):
    content = content.split('\n')
    return content


def get_vehicle_type(vehicle):
    type_all = []
    for request in vehicle:
        type = request['name']
        type_all.append(type)
        type = ','.join(type_all)
    return type


def get_source_data():
    collection = get_collection()
    yunniao = []
    id = []
    for record in collection.find():

        task_id = record['task_id']
        print(task_id)
        com_name = record['customer']['com_name']
        vehicle_type = get_vehicle_type(record['car_subsidy'])
        line_name = record['line_name']
        warehouse_loc = record['warehouse']['wh_addr_loc']
        distribution_area = record['distribution_area']
        content = get_content(record['content'])
        back_wh = content[2].split(',')[1]
        total_miles = content[3].split(',')[1]
        terminal_nums = content[3].split(',')[0]
        arrive_time = content[2].split(',')[0]
        finish_time = content[4].split(',')[0]
        total_time = content[4].split(',')[1]
        work_time = record['work_time']
        try:
            record['vehicle'] and record['capture_time']
        except:
            continue

        if record['vehicle'] != 'over time':
            cargo_type = record['vehicle']['content'][0]['content']
            vehicle_size = record['vehicle']['content'][1]['content']
            vehicle_weight = record['vehicle']['content'][2]['content']
            cargo_amount = record['vehicle']['content'][3]['content']
            driver_effort = record['vehicle']['content'][4]['content']
        else:
            cargo_type = None
            vehicle_size = None
            vehicle_weight = None
            cargo_amount = None
            driver_effort = None
        if record['quote']:
            quote = record['quote']
        else:
            quote = None
        capture_time = record['capture_time']
        new_record = [task_id,com_name,vehicle_type,line_name,warehouse_loc,distribution_area,back_wh,
                      total_miles,terminal_nums,arrive_time,finish_time,total_time,work_time,cargo_type,vehicle_size,
                      vehicle_weight,cargo_amount,driver_effort,quote,capture_time]
        id.append(task_id)
        yunniao.append(new_record)

    col_names = ['task_id','com_name','vehicle_type','line_name', 'warehouse_loc', 'distribution_area', 'back_wh',
                  'total_miles', 'terminal_nums', 'arrive_time', 'finish_time', 'total_time', 'work_time', 'cargo_type',
                 'vehicle_size','vehicle_weight', 'cargo_amount', 'driver_effort', 'quote','capture_time']
    yunniao = pd.DataFrame(yunniao, index=id, columns=col_names)
    yunniao.to_csv('C:\Serena921\\mckcrawl\\yunniao.csv', index=True, parse_dates=True)
    return yunniao
