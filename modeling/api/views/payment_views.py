from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

class KakaoPay(APIView):
    # 카카오 페이 결제 준비 단계
    def post(self, request):
        program_id = request.POST.get('program_id')
        price_id = request.POST.get('price_id')
        url = "https://kapi.kakao.com"
        headers = {
            'Authorization': "KakaoAK " + "19ec65168ecd5968e1f8e5eca0a3ea3c",
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        params = {
            'cid': "TC0ONETIME",
            'partner_order_id': 'partner_order_id',
            'partner_user_id': 'partner_user_id',
            'item_name': request.POST.get('item_name'),
            'quantity': 1,
            'total_amount': request.POST.get('total_amount'),
            'vat_amount': 0,
            'tax_free_amount': 0,
            # 결제 성공했을때
            'approval_url': 'http://localhost:8080/kakaopay/approve/?program={}&price={}'
                .format(program_id, price_id),
            # 실패했을때
            'fail_url': 'http://localhost:8080/fail/',
            # 결제취소했을때
            'cancel_url': 'http://localhost:8080/cancel/',
        }
        response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
        print(response.status_code==200)
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
            'tid': request.POST.get('tid'),
            'partner_order_id': 'partner_order_id',
            'partner_user_id': 'partner_user_id',
            'pg_token': request.POST.get('pg_token'),
        }
        response = requests.post(url+"/v1/payment/approve", params=params, headers=headers)
        response = json.loads(response.text)
        return Response(response)