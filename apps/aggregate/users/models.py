from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as _UserManager
from django.db import models

from authentication.encryption import encryption_fields as custom_fields


class UserManager(_UserManager):
    def inactive(self):
        return self.filter(is_active=False)

    def active(self):
        return self.filter(is_active=False)


class User(AbstractUser):
    objects = UserManager()

    class UserStatus(models.TextChoices):
        ACTIVE = "active", "활성화"
        DORMANT = "dormant", "휴면"
        SUSPENSION = "suspension", "정지"

    class UserType(models.TextChoices):
        CUSTOMER = "customer", "고객"
        OWNER = "store_owner", "사장님"

    """
    AbstractUser를 상속받았기때문에 User에는 아래 7개 Field들이 이미 선언되어있다.

    username = models.CharField(max_length=150, unique=True,)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True,)
    date_joined = models.DateTimeField(default=timezone.now)
    """

    user_type = models.CharField(help_text="고객 유형", default=UserType.CUSTOMER, max_length=16, choices=UserType.choices)
    phone = models.CharField(max_length=64, blank=True, help_text="전화번호")
    name_kor = models.CharField(max_length=64, help_text="회원 성함(한국어)")
    registration_number = custom_fields.EncryptedField(
        max_length=custom_fields.encrypt_max_length(16),
        help_text="주민등록번호",
        blank=True,
    )

    class Meta:
        db_table = "user"


class StoreOwner(User):
    @property
    def has_multi_store(self) -> bool:
        """
        상점 여러개 소유한 사장님인가?
        """

        return True

    class Meta:
        proxy = True


class Customer(User):
    @property
    def is_init_user(self) -> bool:
        """
        아직 첫 주문을 완료하지 않은 고객인가?
        """
        return False

    class Meta:
        proxy = True


class HModel(models.Model):
    aa = models.CharField(max_length=64, default="qqqqq", help_text="help_text")

    class Meta:
        db_table = "h_model"