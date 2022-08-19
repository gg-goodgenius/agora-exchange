import json

with open('case_2_input_data.json') as json_file:
    data = json.load(json_file)

for item in data['ГруппаНоменклатура']:
    url = item['Ссылка']
    parent = item['Родитель']
    name = item['Наименование']
    tag = item['ПометкаУдаления']

for item in data['ЕдиницыИзмерения']:
    units_of_measurement = item['ЕдиницыИзмерения']
    url = item['Ссылка']
    full_name = item['НаименованиеПолное']
    coefficient = item['Коэффициент']

for item in data['Номенклатура']:
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
