from celery import shared_task
from bs4 import BeautifulSoup
from core.models import MappingField, MappingClass

@shared_task(ignore_result=False)
def exchange(type_data: str, data: str) -> object:
    """ Конвертция данных """
    if type_data == 'xml':
        soup = BeautifulSoup(data, 'xml')
        mclss = MappingClass.objects.all()
        result = []
        for mcls in mclss:
            for item in soup.find_all(mcls.name_data):
                flds = mcls.fields.all()
                fields_result = []
                for fld in flds:
                    value = item.findNext(fld.name_data)
                    if value:
                        fields_result.append(dict.fromkeys([fld.name_field], value.text))
                result.append({
                    'object': mcls.name_class,
                    'fields': fields_result
                })
        return result