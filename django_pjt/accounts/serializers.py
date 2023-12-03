from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import User
from dj_rest_auth.serializers import UserDetailsSerializer

class CustomRegisterSerializer(RegisterSerializer):
    # 회원가입 시 추가로 필요한 필드들을 모두 정의
    # 나머지 필드들은 RegisterSerizalizer 에 있음
    name = serializers.CharField(required=True, max_length=255)  # 유저이름으로 사용
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    saving_possible_money = serializers.IntegerField(required=False)   # 매달 저축 가능 금액으로 사용
    saving_possible_period = serializers.IntegerField(required=False)
    financial_type = serializers.CharField(required=False, max_length=2)
    # mbti = serializers.CharField(required=False, max_length=4)
    financial_products = serializers.ListField(child=serializers.CharField(), required=False)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('name', ''),
            'age': self.validated_data.get('age', ''),
            'money': self.validated_data.get('money', ''),
            'saving_possible_money': self.validated_data.get('saving_possible_money', ''),
            'saving_possible_period': self.validated_data.get('saving_possible_period', ''),
            'financial_type': self.validated_data.get('financial_type', ''),
            # 'mbti': self.validated_data.get('mbti', ''),
            'financial_products': self.validated_data.get('financial_products', ''),
        }
        
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        # 필요없는 것은 지운다. 에러 굳이 띄우지 않을 거라 지우나 내가 살림
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
                )
        user.save()
        self.custom_signup(request, user)
        # 이메일 딱히 쓰지 않을것이기 때문에 지움
        # setup_user_email(request, user, [])
        return user
      

class UserProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['age', 'money', 'saving_possible_money', 'saving_possible_period', 'financial_type']



class UserFinancialEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['financial_products']

class UserFinancialMBTIEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mbti']


from django.contrib.auth import authenticate, get_user_model
UserModel = get_user_model()

class CustomUserDetailsSerializer(UserDetailsSerializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    saving_possible_money = serializers.IntegerField(required=False)
    saving_possible_period = serializers.IntegerField(required=False)
    mbti = serializers.CharField(required=False, max_length=4)
    financial_type = serializers.CharField(required=False, max_length=2)
    financial_products = serializers.ListField(child=serializers.CharField(), required=False)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # financial_products를 리스트에서 쉼표로 구분된 문자열로 변환
        representation['financial_products'] = ''.join(map(str, instance.financial_products)) if instance.financial_products else ''
        
        return representation

    
    class Meta(UserDetailsSerializer.Meta):
        extra_fields = []
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
            
        if hasattr(UserModel, 'name'):
            extra_fields.append('name')

        if hasattr(UserModel, 'age'):
            extra_fields.append('age')

        if hasattr(UserModel, 'money'):
            extra_fields.append('money')

        if hasattr(UserModel, 'saving_possible_money'):
            extra_fields.append('saving_possible_money')
            
        if hasattr(UserModel, 'saving_possible_period'):
            extra_fields.append('saving_possible_period')
            
        if hasattr(UserModel, 'mbti'):
            extra_fields.append('mbti')
            
        if hasattr(UserModel, 'financial_type'):
            extra_fields.append('financial_type')

        if hasattr(UserModel, 'financial_products'):
            extra_fields.append('financial_products')
            
        model = UserModel
        fields = ('pk', *extra_fields)
