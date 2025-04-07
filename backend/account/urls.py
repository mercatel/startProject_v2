from django.urls import path

from account.views import AccountList, AccountCreate, MyAccountDetail

urlpatterns = [
    path('account-list/', AccountList.as_view()),
    path('account-create/', AccountCreate.as_view()),
    path('account-my/', MyAccountDetail.as_view())
]
