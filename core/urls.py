from django.urls import path
from .views import SignupView, Index, PostDetailView, ArticleListView, PostDelete

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('t', Index.as_view()),
    path('author/add/', Index.as_view(), name='author-add'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('allpost', ArticleListView.as_view(),name = 'article-list'),
    path('delete/<slug:slug>/', PostDelete.as_view())
]
