from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),
    url(r'^uimage/$', views.uimage, name='uimage'),   #add 의미는 uimage라는 이름을 넣으면 uimage를 반환하겠다는 뜻
]

urlpatterns += static(settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT)