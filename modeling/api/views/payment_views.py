from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import ProgramPaymentSerialiezr
import requests
import json
from ..models import ProgramRecord
front_site = 'https://k3c202.p.ssafy.io/'
class KakaoPay(APIView):
    # 카카오 페이 결제 준비 단계
    def post(self, request):
        program_id = request.POST.get('program_id')
        price_id = request.POST.get('price_id')
        print(program_id,price_id,'----')
        print(front_site)
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
            'approval_url': '{}kakaopay/approve/?program={}&price={}'
                .format(front_site,program_id, price_id),
            # 실패했을때
            'fail_url': f'{front_site}fail/',
            # 결제취소했을때
            'cancel_url': f'{front_site}cancel/',
        }
        print(params,'params')
        response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
        print(response,'response')
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

        serializer = ProgramPaymentSerialiezr(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                programpayment = serializer.save(
                    client_id = request.user.client.first().id,
                    program_id = request.POST.get('program_id'),
                    price_id = request.POST.get('price_id')
                )
                ProgramRecord.objects.create(
                    program = programpayment.program,
                    programprice = programpayment.price,
                    client = programpayment.client,
                    max_online_count = programpayment.price.online_count,
                    max_offline_count = programpayment.price.offline_count
                )
                return Response(response, status=status.HTTP_201_CREATED)
        except:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)