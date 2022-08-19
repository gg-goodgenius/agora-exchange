import ruamel.yaml

file = f'case_2_input_data.yml'

yaml = ruamel.yaml.YAML(typ='safe')
with open(file, 'r') as file:
    data = yaml.load(file)

for item in data[0]['ГруппаНоменклатура']:
    url = item['Ссылка']
    parent = item['Родитель']
    name = item['Наименование']
    tag = item['ПометкаУдаления']

for item in data[1]['ЕдиницыИзмерения']:
    units_of_measurement = item['ЕдиницыИзмерения']
    url = item['Ссылка']
    full_name = item['НаименованиеПолное']
    coefficient = item['Коэффициент']

for item in data[2]['Номенклатура']:
    url = item['Ссылка']
    parent = item['Родитель']
    tag = item['ПометкаУдаления']
    article = item['Артикул']
    name = item['Наименование']
    nds = item['СтавкаНДС']
    description = item['Описание']
    storage_unit = item['ЕдиницаХраненияОстатков']
    characteristic = item['ВестиУчетПоХарактеристикам']
    type = item['ТипНоменклатуры']
    barcode = item['Штрихкод']
    file = item['Файл']
    path = item['Путь']
    general = item['Основное']
