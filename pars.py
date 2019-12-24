import requests
import json
from datetime import datetime, timedelta


def parsing(t):
    File = list()
    a = t.strftime("%y-%m-%d %H:%M:%S")
    dt = datetime.strptime(a, "%y-%m-%d %H:%M:%S")
    dt = dt - timedelta(hours=4)
    b = datetime.now()
    datreq = b.strftime('%d.%m.%Y')
    data = {}

    req = requests.get(
        f'http://budget.gov.ru/epbs/registry/grants/data?filterminstartdate={datreq}&filterminsum=100000000&blocks=info&pageSize=1')
    test = json.loads(req.text)
    recordCount = test['recordCount']
    req_new = requests.get(
        f'http://budget.gov.ru/epbs/registry/grants/data?filterminstartdate={datreq}&filterminsum=100000000&blocks=info&pageSize={recordCount}')
    file = json.loads(req_new.text)
    for key in file['data']:
        time = key['info']['loaddate']
        time = datetime.strptime(time[2:19], "%y-%m-%d %H:%M:%S")
        if time > dt:
            data['Регистрационный номер'] = key['info']['regNum']
            data['Наименование вида соглашения'] = key['info']['mfName']
            data['Размер субсидии, бюджетных инвестиций, межбюджетного трансферта (средств)'] = key['info']['currencySum'] + ' рублей'
            data['Дата заключения соглашения'] = key['info']['startDate'][:10]
            data['Дата окончания срока действия соглашения'] = key['info']['endDate'][:10]
            data['Время добавления'] = time
            File.append(data)
            data = {}

    return File

