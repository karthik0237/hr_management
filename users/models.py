from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default =True)

    class Meta:
        abstract = True


class Department(BaseModel):

    name = models.CharField(max_length=32, null=False, unique=True,db_index = True)
  # department_head = models.IntegerField()


class User(AbstractUser):
    name = models.CharField(null=False, max_length=32)



class UserBankdetails(BaseModel):
    
    user_id = models.ForeignKey(User, on_delete = models.PROTECT, null =False, db_index=True)
    bank_name = models.CharField(max_length=32, null = False)
    ifsc = models.CharField(max_length=16,null = False)
    base_branch = models.CharField(max_length=32,default = None)
    pan_card = models.CharField(max_length=16, default= None)
    is_company_issued = models.BooleanField(default=False, db_index = True)



class FamilyMembers(BaseModel):

    user_id = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True)
    name = models.CharField(max_length=32, null=False)
    relationship = models.CharField(max_length=32, default = None)
    mobile = models.CharField


    