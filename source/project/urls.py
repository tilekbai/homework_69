from django.contrib import admin
from django.urls import path

from api_app_1.views import (
    json_echo_view, 
    get_token_view,
    add_view,
    subtract_view,
    multiply_view,
    divide_view,
)

from webapp.views import (
    IndexView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView),
    path('test/', json_echo_view),
    path('test/coocki/', get_token_view),
    path('add/', add_view),
    path('subtract/', subtract_view),
    path('multiply/', multiply_view),
    path('divide/', divide_view),    
]
