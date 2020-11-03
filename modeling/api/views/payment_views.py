from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

class KakaoPay(APIView):
    # 카카오 페이 결제 준비 단계
    def post(self, request):
        url = "https://kapi.kakao.com"
        headers = {
            'Authorization': "KakaoAK " + "19ec65168ecd5968e1f8e5eca0a3ea3c",
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        params = {
            'cid': "TC0ONETIME",
            'partner_order_id': 'partner_order_id',
            'partner_user_id': 'partner_user_id',
            'item_name': '초코파이',
            'quantity': 1,
            'total_amount': 2200,
            'vat_amount': 200,
            'tax_free_amount': 0,
            # 결제 성공했을때
            'approval_url': 'http://localhost:8080/kakaopay/approve/',
            # 실패했을때
            'fail_url': 'http://localhost:8080/fail/',
            # 결제취소했을때
            'cancel_url': 'http://localhost:8080/cancel/',
        }
        response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
        response = json.loads(response.text)
        return Response(response)

class KakaoPayApprove(APIView):
    # 카카오 페이 결제 승인
    def post(self, request):
        url = "https://kapi.kakao.com"
        headers = {
            'Authorization': "KakaoAK " + "19ec65168ecd5968e1f8e5eca0a3ea3c",
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        params = {
            'cid': "TC0ONETIME",
            'tid': "T2824892672097674277",
            'partner_order_id': 'partner_order_id',
            'partner_user_id': 'partner_user_id',
            'pg_token': '070d996c2b76c8fc45cc'
        }
        response = requests.post(url+"/v1/payment/approve", params=params, headers=headers)
        response = json.loads(response.text)
        return Response(response)