from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


from account.models import Account
from account.serializers import AccountSerializer


class AccountList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]


class AccountCreate(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        request.data._mutable = True
        self.request.data["password"] = make_password(self.request.data["password"])
        return self.create(request, *args, **kwargs)


class MyAccountDetail(RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Account.objects.get(id=self.request.user.id)
