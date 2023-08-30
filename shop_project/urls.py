"""
URL configuration for shop_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.shortcuts import render
from .sitemaps import StaticViewSitemap,ProductViewSitemap
from django.contrib.sitemaps.views import sitemap
from os import getenv
sitemaps = {
    'static':StaticViewSitemap,
    'product':ProductViewSitemap
}

urlpatterns = [
    path(getenv('ADMIN_URL'), admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('robots.txt',lambda r:render(r,'robots.txt',content_type="text/plain")),
     path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+i18n_patterns(
    path('',include('customer.urls')),
    path('',include('payment.urls')),
    path('',include('shop.urls')),
)


