import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser,Group


from enum import Enum



class DesignationChoice(Enum):

    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    Middle = 'Middle'

    @classmethod
    def choices(cls):
        return tuple(i.value for i in cls)
    

class GenderChoice(Enum):

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    @classmethod
    def choices(cls):
        return tuple(i.value for i in cls)
    
class MaritalStatusChoice(Enum):

    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'

    @classmethod
    def choices(cls):
        return tuple(i.value for i in cls)
    

class BloodGroupChoice(Enum):

    O_POSITIVE = 'O Positive(O+)'
    A_POSITIVE = 'A Positive(A+)'
    B_POSITIVE = 'B Positive(O+)'
    AB_POSITIVE = 'AB Positive(AB+)'
    O_NEGATIVE = 'O Negative(O-)'
    A_NEGATIVE = 'A Negative(A-)'
    B_NEGATIVE = 'B Negative(B-)'
    AB_NEGATIVE = 'AB Negative(AB-)'


    # class method, accessed using class instance cls
    @classmethod
    def choices(cls):
        return tuple(i.value for i in cls)
    
    
    




# Create your models here.
class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default  = True)

    class Meta:
        abstract = True


class Department(BaseModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())    
    name = models.CharField(max_length = 32, null = False, unique = True,db_index = True)
  # department_head = models.IntegerField(default = null)



class Country(BaseModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    name = models.CharField(unique = True, null = False, db_index = True)


class State(BaseModel):
    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    name = models.CharField(max_length = 32, null = False)
    country =  models.ForeignKey(Country,on_delete = models.PROTECT)


class City(BaseModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    name = models.CharField(max_length = 32, null = False)
    state = models.ForeignKey(State, on_delete = models.PROTECT)
    country = models.ForeignKey(Country, on_delete = models.PROTECT)
    latitude = models.CharField(null = True)
    longitude = models.CharField(null = True)


class User(AbstractUser):

    name = models.CharField(null = False, max_length = 32)
    # username
    # password
    designation = models.CharField(choices =  DesignationChoice.choices, max_length = 32, db_index = True)
    employee_id = models.CharField(null = False,unique = True,db_index = True)
    department = models.ForeignKey(Department,on_delete = models.PROTECT)
    # date_joined
    picture = models.ImageField(upload_to = "profile", null = True)
    mobile = models.IntegerField(max_length = 16, null = False,unique = True)
    email = models.EmailField(unique = True,null = False,db_index = True)
    dob = models.DateField(null = True)

    door_no = models.CharField(max_length = 32)
    street = models.CharField(max_length = 64)
    locality = models.CharField(max_length = 32)
    city = models.ForeignKey(City, on_delete = models.PROTECT)

    gender = models.CharField(choices = GenderChoice.choices, null = False)
    reporting_to = models.ForeignKey('self',on_delete = models.PROTECT)
    passport_no = models.CharField(max_length = 16, null = True, unique = True)
    nationality = models.CharField(max_length = 32,null = True)

    marital_status = models.CharField(choices =  MaritalStatusChoice.choices, max_length = 16, null = True)
    no_of_children = models.IntegerField(null = True)
    # groups
    blood_group = models.CharField(choices = BloodGroupChoice.choices,max_length = 12, null = True)
    social_id_no = models.CharField(max_length = 16,unique = True,null = True)






class UserBankdetails(BaseModel):
    
    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    user = models.ForeignKey(User, on_delete = models.PROTECT, null  = False, db_index = True)
    bank_name = models.CharField(max_length = 32, null = False)
    ifsc = models.CharField(max_length = 16,null = False)
    base_branch = models.CharField(max_length = 32,null = True)
    pan_card = models.CharField(max_length = 16, null = True)
    is_company_issued = models.BooleanField(default = False, db_index = True)



class FamilyMembers(BaseModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    user = models.ForeignKey(User, on_delete = models.PROTECT, db_index = True)
    name = models.CharField(max_length = 32, null = False)
    relationship = models.CharField(max_length = 32, null = True, default = None)
    mobile = models.CharField(max_length = 12, null = False)
    email = models.EmailField(null = True)
    dob = models.DateTimeField(null = True)
    is_emergency_contact = models.BooleanField(default = True)


class EducationDetails(BaseModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    user = models.ForeignKey(User, on_delete = models.PROTECT,db_index = True)
    start_date = models.DateField(null = False)
    end_date = models.DateField(null = True)
    institute_name = models.CharField(max_length = 128, default = None)
    percentage = models.FloatField(null = False)
    course = models.CharField(max_length = 64, null = False)
    level = models.CharField(null = True, default = None)


class UserExperience(BaseModel):
    '''
    model for user experience
    '''
    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    user = models.ForeignKey(User, on_delete =  models.PROTECT, db_index = True)
    title = models.CharField(max_length = 64, null = False)
    place_of_work = models.CharField(max_length = 50, null = False)
    start_datetime = models.DateField(default =  None, db_index = True)
    end_datetime = models.DateField(null = False, db_index = True)
    skills = models.CharField(max_length = 512, null = True)
    achievements = models.CharField(max_length =  512,null = True)




class UserGroup(BaseModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    name = models.CharField(max_length = 32, unique = True,db_index = True)


    def save(self,*args,**kwargs):

       # get or create group with name, returns tuple(Group_object,true/false)
        group, created = Group.objects.get_or_create(name = self.name)
        return super().save(*args,**kwargs)
    








    





    