# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import exchange

class ExchangeView(APIView):
    ''' Обмен '''
    # permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        ''' GET '''
        try:
            # проверить обновления по токену и передать в celery
            pass
        except Exception:
            return Response({
                'result': False
            })
    def post(self, request, *args, **kwargs):
        ''' POST '''
        try:
            # вытащить тип данных и данные передать в celery
            pass
        except Exception:
            return Response({
                'result': False
            })
