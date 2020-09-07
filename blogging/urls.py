from django.urls import path, include
from rest_framework import routers
from blogging.views import stub_view, list_view, detail_view
import blogging.views

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]

router = routers.DefaultRouter()
router.register(r'users', blogging.views.UserViewSet)
router.register(r'groups', blogging.views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
