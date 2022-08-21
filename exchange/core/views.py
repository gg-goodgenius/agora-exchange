from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from core.tasks import exchange
from core.models import Exchange, UpdateData
from drf_yasg import openapi
import io 

class ExchangeView(APIView):
    ''' Обмен '''
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(responses={200: openapi.Response('JSON')})
    def get(self, request, *args, **kwargs):
        ''' Получение списка обновлений '''
        try:
            # проверить обновления по токену и передать в celery
            
            return Response({
                'result': 'GET'
            })
        except Exception:
            return Response({
                'result': False
            })

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('type', openapi.IN_QUERY, description="file type (xml, json, yaml)", type=openapi.TYPE_STRING),
        openapi.Parameter('file', openapi.IN_QUERY, description="file with data", type=openapi.TYPE_STRING),
    ], responses={200: openapi.Response('JSON')})
    def post(self, request, *args, **kwargs):
        ''' Создать обновления для маркетплейса '''
        try:
            # вытащить тип данных и данные передать в celery
            exch = Exchange.objects.filter(sendler = request.user).first()
            type_data = request.POST.get('type', 'xml')
            fl = request.FILES.getlist('file', None)
            fl = fl[0] if fl else None
            data = str(fl.read())
            task = exchange.apply_async(args=[type_data, data])
            print(task.backend)
            print(dir(task))
            # task.save()
            du = UpdateData(exchange=exch, taskid=task.task_id)
            du.save()
            return Response({
                'result':0 
            })
        except Exception as e:
            print(e)
            return Response({
                'result': False
            })
