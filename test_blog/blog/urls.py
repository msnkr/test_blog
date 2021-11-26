from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from .views import PostDeleteView, PostListView, PostDetailView, PostCreateView, PostUpdateView
 
urlpatterns = [
    path('<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'), 
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)