import json
from math import log
def transform_json(line, border):
    dict_data = json.loads(line)
    if dict_data['salary'][border] is not None:
        result_line = '{} '.format(log(float(dict_data['salary'][border])))
    else:
        return 0
    result_line = result_line + '|{} {}'.format('billing_type', dict_data['billing_type']['id'])
    result_line = result_line + '|{} {}'.format('accept_handicapped', dict_data['accept_handicapped'])
    if dict_data['key_skills']:
        result_line = result_line + '|key_skills '
        for elem in dict_data['key_skills']:
            result_line = result_line + '{} '.format(elem['name'].encode('utf8').decode().replace(' ', '_').replace(':', ''))
        
    result_line = result_line + '|employment {}'.format(dict_data['employment']['id'])
    result_line = result_line + '|archived {}'.format(dict_data['archived'])
    if 'id' in dict_data['employer']:
        result_line = result_line + '|employer {}'.format(dict_data['employer']['id'])
    result_line = result_line + '|response_letter_required {}'.format(dict_data['response_letter_required'])
    result_line = result_line + '|type {}'.format(dict_data['type']['id'])
    if dict_data['specializations']:
        result_line = result_line + '|specializations '
        for elem in dict_data['specializations']:
            result_line = result_line + '{} '.format(elem['id'])
    result_line = result_line + '|premium {}'.format(dict_data['premium'])
    result_line = result_line + '|schedule {}'.format(dict_data['schedule']['id'])
    result_line = result_line + '|billing_type {}'.format(dict_data['billing_type']['id'])
    if dict_data['department']:
        result_line = result_line + '|department {}'.format(dict_data['department']['id'])
    if dict_data['address']:
        if 'city' in dict_data:
            result_line = result_line + '|address {}'.format(dict_data['address']['city'].encode('utf8').replace(':', ''))
    result_line = result_line + '|name ' + dict_data['name'].encode('utf8').decode().replace(':', '')
    result_line = result_line + '|area {}'.format(dict_data['area']['id'])
    result_line = result_line + '|experience {}'.format(dict_data['experience']['id'])
    result_line = result_line + '|description ' + dict_data['description'].encode('utf8').decode().replace(':', '').replace('\n', ' ')
    
    return result_line