from celery import shared_task
from bs4 import BeautifulSoup
from core.models import MappingField, MappingClass

@shared_task
def exchange(type_data: str, data: str) -> object:
    """ Конвертция данных """
    result = []
    soup = BeautifulSoup(data, 'xml')
    mclss = MappingClass.objects.all()
    # print(soup)
    for mcls in mclss:
        # print(mcls)
        # print(mcls.name_data)
        for item in soup.find_all(mcls.name_data):
            flds = mcls.fields.all()
            # print(flds)
            fields_result = []
            for fld in flds:
                # print(fld)
                # print(fld.name_data)
                value = item.findNext(fld.name_data)
                if value:
                    fields_result.append(dict.fromkeys([fld.name_field], value.text))
            result.append({
                'object': mcls.name_class,
                'fields': fields_result
            })
            # print(result)
    return result