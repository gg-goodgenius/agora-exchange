import datetime
import json

import ruamel.yaml

start_time = datetime.datetime.now()

file = f'case_2_input_data.yml'

yaml = ruamel.yaml.YAML(typ='safe')
with open(file, 'r') as file:
    data = yaml.load(file)

print(datetime.datetime.now() - start_time)
print(json.dumps(data, ensure_ascii=False, indent=4))
