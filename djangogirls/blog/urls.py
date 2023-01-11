#장고 함수 Path
from django.urls import path
#blog 애플리케이션에서 사용할 모든 뷰
from . import views

#post_list라는 view가 루트 url에 할당됨
#누군가 웹사이트에 들어오면 (뒤에 ''인) views.post_list를 보여줘라
#name은 url에 이름을 붙인 것으로 뷰를 식별
urlpatterns = [
    path('', views.post_list, name = 'post_list'),
]

