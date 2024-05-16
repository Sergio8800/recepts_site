from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

# from . import views
from .views import *

if settings.DEBUG:
    urlpatterns = [
        path('', index_start_app, name='index_start_app'),

        path('cat/add/', category_form, name='category_form'),
        path('product/add/', product_form, name='product_form'),

        path('login/', LoginUser.as_view(), name='loginform'),
        path('register/', RegisterUser.as_view(), name='register'),
        path('logout/', logout_user, name='logout'),

        path('product/del/<int:product_id>/', deleteView, name='deleteView'),


        path('product/<int:product_id>/', product_form_update, name='product_form_update'),
        # name='product' на прямую связана get_absolute_url


    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)