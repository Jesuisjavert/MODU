from django.shortcuts import render
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class KakaoLogin(SocialLoginView):
    '''
    카카오 로그인

    ---
    
    
    '''
    adapter_class = KakaoOAuth2Adapter   
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test(request):
    print(request.user)
    return Response({'data': True})