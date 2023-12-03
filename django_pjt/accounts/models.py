from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter

# Create your models here.
class User(AbstractUser):
    예금 = '예금'
    적금 = '적금'
    FINANCIAL_CHOICES = [
        (예금, '예금'),
        (적금, '적금'),
    ]
    name = models.TextField(blank=False)    # 이름
    age = models.IntegerField(blank=True, null=True)    # 나이
    money = models.IntegerField(blank=True, null=True)  # 보유자산
    saving_possible_money = models.IntegerField(blank=True, null=True)  # 매달 저축 가능 금액
    saving_possible_period = models.IntegerField(blank=True, null=True)  # 추가: 저축 가능 기간
    financial_type = models.CharField(max_length=2, choices=FINANCIAL_CHOICES, blank=True, default=None, ) # 추가: 예적금 중 희망 
    mbti = models.CharField(max_length=4, blank=True, null=True)  # 추가: MBTI
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True)
    
    
    # # superuser fields
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # USERNAME_FIELD = 'username'

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
    
    # Saves a new `User` instance using information provided in the
    # signup form.

        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        email = data.get("email")
        username = data.get("username")
        name = data.get("name")
        age = data.get("age")
        money = data.get("money")
        saving_possible_money = data.get("saving_possible_money")
        saving_possible_period = data.get("saving_possible_period")
        financial_type = data.get("financial_type")
        mbti = data.get("mbti")
        financial_products = data.get("financial_products")
        
        user_username(user, username)
        if email:
            user_email(user, "email", email)
        if name:
            user_field(user, "name", name)
        if age:
            user.age = age
        if money:
            user.money = money
        if saving_possible_money:
            user.saving_possible_money = saving_possible_money
        if saving_possible_period:
            user.saving_possible_period = saving_possible_period
        if financial_type:
            user.financial_type = financial_type
        if mbti:
            user.mbti = mbti
        if financial_products:
            user_field(user, "financial_products", financial_products)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user    
    
