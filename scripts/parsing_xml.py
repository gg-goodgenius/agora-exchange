from bs4 import BeautifulSoup

file = open('case_2_input_big_data.xml', 'r')
xml_file = file.read()

soup = BeautifulSoup(xml_file, 'xml')

for item in soup.find_all("ГруппаНоменклатура"):
    print(f"Группа Номенклатура\n"
          f"Ссылка - {item.findNext('Ссылка').text}\n"
          f"Родитель - {item.findNext('Родитель').text}\n"
          f"Наименование - {item.findNext('Наименование').text}\n"
          f"Пометка Удаления - {item.findNext('ПометкаУдаления').text}")
    print('-----------------------------------------------')

for item in soup.find_all("ЕдиницыИзмерения"):
    print(f"Единицы Измерения\n"
          f"Наименование - {item.findNext('Наименование').text}\n"
          f"Ссылка - {item.findNext('Ссылка').text}\n"
          f"Наименование Полное - {item.findNext('НаименованиеПолное').text}\n"
          f"Коэффициент - {item.findNext('Коэффициент').text}")
    print('-----------------------------------------------')

for item in soup.find_all("Номенклатура"):
    print(f"Номенклатура\n"
          f"Ссылка - {item.findNext('Ссылка').text}\n"
          f"Родитель - {item.findNext('Родитель').text}\n"
          f"Пометка Удаления - {item.findNext('ПометкаУдаления').text}\n"
          f"Артикул - {item.findNext('Артикул').text}\n"
          f"Наименование - {item.findNext('Наименование').text}\n"
          f"Ставка НДС - {item.findNext('СтавкаНДС').text}\n"
          f"Описание - {item.findNext('Описание').text}\n"
          f"Единица Хранения Остатков - {item.findNext('ЕдиницаХраненияОстатков').text}\n"
          f"Вести Учет По Характеристикам - {item.findNext('ВестиУчетПоХарактеристикам')}\n"
          f"ТипНоменклатуры - {item.findNext('ТипНоменклатуры').text}\n"
          f"Штрихкод - {item.findNext('Штрихкод').text}\n"
          f"Файл - {item.findNext('Файл').text}\n"
          f"Путь - {item.findNext('Путь').text}\n"
          f"Основное - {item.findNext('Основное').text}\n"
          )
    print('-----------------------------------------------')
