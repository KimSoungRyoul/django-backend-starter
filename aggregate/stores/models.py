from django.db import models


# Create your models here.
class Store(models.Model):
    class StoreType(models.TextChoices):
        FOOD = "food", "배달음식"
        GROCERY = "grocery", "식료품/가공식품"
        PET_FOOD = "pet_food", "반려동물음식"

    name = models.CharField(max_length=128, help_text="음식점 가게명")
    owner = models.ForeignKey(to="users.User", on_delete=models.CASCADE, null=True)
    tel_num = models.CharField(max_length=16, help_text="음식점 연락처")
    created_at = models.DateTimeField(auto_now_add=True)
    store_type = models.CharField(choices=StoreType.choices, help_text="상점 유형", max_length=32)

    class Meta:
        db_table = "store"
