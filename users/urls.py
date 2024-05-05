from django.urls import path

from users.views import router as userrouter


urlpatterns = [

]

urlpatterns += userrouter.urls