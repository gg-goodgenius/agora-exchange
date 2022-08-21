from celery.result import AsyncResult
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from core.tasks import exchange
from core.models import Exchange, UpdateData
from drf_yasg import openapi

class ExchangeView(APIView):
    ''' Обмен '''
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(responses={200: openapi.Response('JSON')})
    def get(self, request, *args, **kwargs):
        ''' Получение списка обновлений '''
        try:
            # проверить обновления по токену и передать в celery
            exch = Exchange.objects.filter(recipient = request.user).first()
            print(exch)
            #TODO: first fo deploy
            data = exch.updates.all().first()
            print(data)
            ares = AsyncResult(data.resultid)
            print(ares.state) 
            if ares.state != 'SUCCESS':
                result = None
            else:
                result = ares.get()
            return Response({
                'result': result
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
            data = fl.read().decode("UTF-8")
            # print(data)
            task = exchange.apply_async(args=[type_data, data])
            # print(task.get())
            # print(dir(task))
            # task.save()
            du = UpdateData(exchange=exch, resultid=task.task_id)
            du.save()
            return Response({
                'result':0 
            })
        except Exception as e:
            print(e)
            return Response({
                'result': False
            })
