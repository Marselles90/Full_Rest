"""
Register some views
# https://www.django-rest-framework.org/api-guide/routers/

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('category', views.CategoryViewSet)
router.register('news', views.NewsViewSet)

urlpatterns = router.urls
"""

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('book', views.BookViewSet)
router.register('author', views.AuthorViewSet)

urlpatterns = router.urls
