from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

class KakaoPay(APIView):
    def post(self, request):
        url = "https://kapi.kakao.com"
        headers = {
            'Authorization': "KakaoAK " + "19ec65168ecd5968e1f8e5eca0a3ea3c",
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        params = {
            'cid': "TC0ONETIME",
            'partner_order_id': '1001',
            'partner_user_id': 'dongsik',
            'item_name': '초코파이',
            'quantity': 1,
            'total_amount': 2200,
            'vat_amount': 200,
            'tax_free_amount': 0,
            # 결제 성공했을때
            'approval_url': 'http://localhost:8080',
            # 실패했을때
            'fail_url': 'http://localhost:8080',
            # 결제취소했을때
            'cancel_url': 'http://localhost:8080',
        }
        response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
        response = json.loads(response.text)
        return Response(response) 