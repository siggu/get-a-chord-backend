from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 이 부분을 추가합니다.
    path('search_results/', views.search, name='search_videos'),  # 검색 결과 보여주는 URL 패턴
    path('play/<str:video_id>/', views.play, name='play'),  # 비디오 재생 URL 패턴
]
