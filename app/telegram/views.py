import requests
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MessageParams
from .serializers import MessageParamsSerializer


# Create your views here.
class MessageParamsView(APIView):
    def get(self, request):

        request_data = request.data
        params = MessageParams.objects.get()

        # если запрос без данных, отправляю данные для автозаполнения полей фронта
        if not request_data:
            return Response({'saved_params': MessageParamsSerializer(params).data})

        # иначе получаем данные
        member_id, message = request_data['member_id'], request_data['message']

        # В тз не описано, по какому принципу проверять member_id
        # По идее в бд приложения должен быть этот юзер и его id, тогда просто проверяем и все
        # Пока для вида проверка на наличие данных, получаемых сервером

        if not member_id:
            return Response({'status': 404})

        # если member id есть, то по api телеграма отправляю от лица бота сообщение
        requests.get(
            f'https://api.telegram.org/bot{params.bot_token}/sendMessage?chat_id={params.chat_id}&text={message}')

        return Response({'status': 200})

    def post(self, request):

        request_data = request.data
        token, chat_id = request_data['token'], request_data['chat_id']

        # токен или chat id не заполнены
        if not token or not chat_id:
            return Response({'status': 401})

        # иначе обновляем данные бд
        MessageParams.objects.all().delete()
        params = MessageParams(bot_token=token, chat_id=chat_id)
        params.save()

        return Response({'status': 200})
