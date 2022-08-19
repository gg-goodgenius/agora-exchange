import json

with open('case_2_input_data.json') as json_file:
    data = json.load(json_file)

for item in data['ГруппаНоменклатура']:
    url = item['Ссылка']
    parent = item['Родитель']
    name = item['Наименование']
    tag = item['ПометкаУдаления']

for item in data['ЕдиницыИзмерения']:
    url = item['Наименование']
    name = item['Ссылка']
    full_name = item['НаименованиеПолное']
    coefficient = item['Коэффициент']

for item in data['Номенклатура']:
    url = item['Ссылка']
    parent = item['Родитель']
    name = item['Наименование']
    tag = item['ПометкаУдаления']
    article = item['Артикул']
    nds = item['СтавкаНДС']
    description = item['Описание']
    storage_unit = item['ЕдиницаХраненияОстатков']
    characteristic = item['ВестиУчетПоХарактеристикам']
    type = item['ТипНоменклатуры']
    barcode = item['Штрихкод']
    file = item['Файл']
    path = item['Путь']
    general = item['Основное']
