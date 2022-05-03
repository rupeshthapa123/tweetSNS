from django.urls import path

from .views import ( 
    tweet_detail_view, tweet_list_view,
)

urlpatterns = [
    path('',tweet_list_view),
    path('<int:tweet_id>/', tweet_detail_view)
]