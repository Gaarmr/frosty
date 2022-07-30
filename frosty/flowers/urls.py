from django.urls import path
from .views import deals, feedback


urlpatterns = [
    path('deals/', deals.deal_lots_list, name='deal_lost_list'),
    path('feedback/', feedback.create_feedback, name='create_feedback'),
]
