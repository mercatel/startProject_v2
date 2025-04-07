from rest_framework import serializers

from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    username = serializers.CharField(write_only=True)
    lastname = serializers.CharField(required=True)
    firstname = serializers.CharField(required=True)

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "email",
            "lastname",
            "firstname",
            "patronymic",
            "is_staff",
            "is_superuser",
        ]
