# from .models import CommonUser
# from django.contrib.auth.password_validation import validate_password
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import CommonUser

class UserRegistrationSerializer(RegisterSerializer):
    
    # class Meta:
    #     model = CommonUser
    #     fields = ['username', 'email', 'password', 'phone']
    #     extra_kwargs = {
    #         'password': {
    #             'write_only':True
    #         }
    #     }
    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=40)
    def get_cleaned_data(self):
        return {
            'name' : self.validated_data.get('name', ''),
            'email' : self.validated_data.get('email', ''),
            'password' : self.validated_data.get('password', ''),
            'phone' : self.validated_data.get('phone', ''),
        }
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()

        user = adapter.save_user(request, user, self, commit=False)
        
        password = self.validated_data['password1']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonUser
        fields = ('email', 'last_login', 'date_joined', 'is_staff')
        
class UserIdPostSerializer(serializers.Serializer):
    token = serializers.CharField()