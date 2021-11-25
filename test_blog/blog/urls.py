 from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
 
urlpatterns = [
    path('<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
]