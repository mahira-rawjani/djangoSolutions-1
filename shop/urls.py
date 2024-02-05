from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage),
    path('shopAll/', views.shop_all),
    path('product/<int:pk>', views.product, name='product'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)