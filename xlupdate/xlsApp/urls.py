from django.urls import path, include
from rest_framework.routers import DefaultRouter
from xlsApp.views import update_database

# router = DefaultRouter()
# router.register(r'update_database', StudDetailViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('update_database/', update_database, name='update_database'),
]
