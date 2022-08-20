from celery import shared_task

@shared_task
def exchange(type: str, data: str) -> object:
    """ Конвертция данных """
    from bs4 import BeautifulSoup

    data = open('case_2_input_big_data.xml', 'r')
    xml_file = file.read()

    soup = BeautifulSoup(xml_file, 'xml')

    for item in soup.find_all("ГруппаНоменклатура"):
        url = item.findNext('Ссылка').text
        parent = item.findNext('Родитель').text
        name = item.findNext('Наименование').text
        tag = item.findNext('ПометкаУдаления').text

    for item in soup.find_all("ЕдиницыИзмерения"):
        url = item.findNext('Ссылка').text
        name = item.findNext('Наименование').text
        full_name = item.findNext('НаименованиеПолное').text
        coefficient = item.findNext('Коэффициент').text

    for item in soup.find_all("Номенклатура"):
        url = item.findNext('Ссылка').text
        parent = item.findNext('Родитель').text
        name = item.findNext('Наименование').text
        tag = item.findNext('ПометкаУдаления').text
        article = item.findNext('Артикул').text
        nds = item.findNext('СтавкаНДС').text
        description = item.findNext('Описание').text
        storage_unit = item.findNext('ЕдиницаХраненияОстатков').text
        characteristic = item.findNext('ВестиУчетПоХарактеристикам')
        type = item.findNext('ТипНоменклатуры').text
        barcode = item.findNext('Штрихкод').text
        file = item.findNext('Файл').text
        path = item.findNext('Путь').text
        general = item.findNext('Основное').text
    