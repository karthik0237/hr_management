from django.db import models
from django.contrib.auth.models import AbstractUser,Group

# Create your models here.
class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default =True)

    class Meta:
        abstract = True


class Department(BaseModel):

    name = models.CharField(max_length=32, null=False, unique=True,db_index = True)
  # department_head = models.IntegerField(default = null)


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
    mobile = models.CharField(max_length=12, null = False)
    email = models.EmailField(default = None)
    dob = models.DateTimeField(default = None)
    is_emergency_contact = models.BooleanField(default = True)


class EducationalQualifications(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT,db_index=True)
    start_date = models.DateField(null = False)
    end_date = models.DateField(default = None)
    institute_name = models.CharField(max_length = 128, default=None)
    percentage = models.FloatField(null = False)
    course = models.CharField(max_length=64, null = False)
    level = models.CharField(default = None)


class UserExperience(BaseModel):
    user_id = models.ForeignKey(User, on_delete= models.PROTECT, db_index = True)
    title = models.CharField(max_length=64, null = False)
    place_of_work = models.CharField(max_length=50, null = False)
    start_datetime = models.DateField(default= None, db_index=True)
    end_datetime = models.DateField(null=False, db_index=True)
    skills = models.CharField(max_length=512, default= None)
    achievements = models.CharField(max_length= 512, default = None)


class Country(BaseModel):
    name = models.CharField(unique=True, null = False, db_index=True)


class State(BaseModel):
    name = models.CharField(max_length=32, null = False)
    country_id =  models.IntegerField(default=None)


class City(BaseModel):
    name = models.CharField(max_length=32, null = False)
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT)
    state_id = models.ForeignKey(State, on_delete = models.PROTECT)
    latitude = models.CharField(null=True)
    longitude = models.CharField(null=True)



class UserGroup(BaseModel):
    name = models.CharField(max_length=32, unique=True,db_index=True)

    def save(self,*args,**kwargs):
        '''
        get or create group with name
        '''
        group, created = Group.objects.get_or_create(name = self.name)
        return super().save(*args,**kwargs)
    








    





    