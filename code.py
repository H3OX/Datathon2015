import json
import numpy as np
import datetime
import joblib

path = 'train.json'
ds = []

start = datetime.datetime.now()
print('Data writing started')
with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        data = json.loads(line)
        id = data['id']
        employment = data['employment']['name']
        ename = data['employer']['name']
        billing_type = data['billing_type']['name']
        prof1 = data['specializations'][0]['profarea_id']
        premium = data['premium']
        schedule = data['schedule']['name']
        msg = data['allow_messages']
        adr = data['address']
        city = np.nan
        if adr:
            city = adr['city']
        experience = data['experience']['name']
        target_from = data['salary']['from']
        target_to = data['salary']['to']
        ds.append([id, employment, ename, billing_type, prof1, premium, schedule, msg, city, experience, target_from, target_to])
end = datetime.datetime.now()
joblib.dump(ds, 'dataset.pkl')
print(f'Writing finished in {start-end} seconds.')
