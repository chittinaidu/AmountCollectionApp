"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from django.urls import path,re_path
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,\
 DeleteView
from main.views import user_register,home_view,logout_view
from main.models import DonateAmount,PandaguluType,Contact,Payment
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('logout/', logout_view),
    path('admin/', admin.site.urls),
    path('', home_view),
    path('register/', user_register),
    path('index/',TemplateView.as_view(template_name="main/index.html")),
    path('DonateAmount/',login_required(ListView.as_view(
        model=DonateAmount,
    
    
     ))),
    path('donateamount_create/',login_required(CreateView.as_view(
    model=DonateAmount,
    fields="__all__",
    #fields=["NAME","AMOUNT","TYPE","DATE","USER"],
    success_url="/DonateAmount/",

    ))),
    re_path('donateamount_update/(?P<pk>[0-9]+)',login_required(UpdateView.as_view(
        model=DonateAmount,
        fields=["name","amount","type","date","user"],
        success_url="/DonateAmount",
        template_name="main/donateamount_update_form.html"
        ))),
    re_path('donateamount_delete/(?P<pk>[0-9]+)',login_required(DeleteView.as_view(
        model=DonateAmount,
        success_url="/DonateAmount",
        #template_name="main/donateamount_confirm_delete_form.html"
        ))),

    re_path('donateamount_payment/(?P<pk>[0-9]+)',login_required(CreateView.as_view(
        model=Payment,
        ))),

    #path('donateamount_payment/(?P<pk>[0-9]+)',login_required(CreateView.as_view(
     #   model=DonateAmount,
      # ))),
    
    path('PandaguluType/', login_required(ListView.as_view(
        model=PandaguluType,
        ))),

    path('Contact/',login_required(ListView.as_view(
        model=Contact,
        ))),
    
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
