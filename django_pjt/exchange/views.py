# converter/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests, datetime
from .serializers import *
from datetime import datetime, timedelta


@api_view(['GET'])
def convert_currency(request):
    today = datetime.now()			# 현재 날짜 추출
    print(today)
    # 평일이면서 11시 이전인 경우
    if 0 <= today.weekday() <= 4 and today.hour < 11:
        # 월요일이면 전주 금요일로 설정, 그렇지 않으면 어제로 설정
        yesterday = today - timedelta(days=1) if today.weekday() != 0 else today - timedelta(days=3)

    # 주말인 경우
    elif today.weekday() == 5 or today.weekday() == 6 :
        # 토요일이나 일요일이면 어제나 엊그제 중에 금요일로 설정
        yesterday = today - timedelta(days=1) if today.weekday() == 5 else today - timedelta(days=2)
    # 11시 이후되면 그냥 가져오기
    else :
        yesterday = today 
        
    api_key = 'TRLP98UbzQOqhFAAdzuA6gqLSfHOwrHF'
    date = yesterday.strftime('%Y%m%d')
    print(date)
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

    params = {
        'authkey': api_key,
        'searchdate': date,
        'data': 'AP01'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    serializer = CurrencyConversionListSerializer(data, many=True)
    
    return Response(serializer.data)