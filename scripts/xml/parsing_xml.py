import datetime
import json

import xmltodict

start_time = datetime.datetime.now()

file = f'case_2_input_data.xml'

with open(file) as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    json_data = json.dumps(data_dict, ensure_ascii=False, indent=4)

print(datetime.datetime.now() - start_time)
print(json_data)
