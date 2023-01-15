from backend_api.views import MovieViewSet
from rest_framework.routers import DefaultRouter
from backend_api import views

router = DefaultRouter()
# Using the ModelViewSet by default provides the HTTP request methods of ‘get(), post(), delete(), put()’ through which the CRUD operations are performed.
router.register(r'movies', views.MovieViewSet, basename='movie')
urlpatterns = router.urls
