import uuid
from enum import Enum

from django.db import models
from django.contrib.auth.models import AbstractUser,Group






class DesignationChoice(Enum):

    INTERN = 'Intern'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    LEAD = 'Lead'
    EXECUTIVE = 'Executive'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    

class GenderChoice(Enum):

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
class MaritalStatusChoice(Enum):

    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls) # an iterable containing (human readable names, actual values) tuples 
    

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
        return tuple((i.name, i.value) for i in cls)
    
    
    




# Create your models here.
class BaseUserModel(models.Model):

    created_at = models.DateTimeField(auto_now_add = True, blank = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default  = True)

    class Meta:
        abstract = True


class Department(BaseUserModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())    
    name = models.CharField(max_length = 32, null = False, unique = True,db_index = True)
  # department_head = models.IntegerField(default = null)



class Country(BaseUserModel):

    name = models.CharField(max_length = 32, unique = True, null = False, db_index = True)
    name_uc = models.CharField(max_length = 32, unique = True, null = False )


class State(BaseUserModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    name = models.CharField(max_length = 32, null = False)
    name_uc = models.CharField(max_length = 32, null = False )
    country =  models.ForeignKey(Country,on_delete = models.PROTECT)


class City(BaseUserModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    name = models.CharField(max_length = 32, null = False)
    name_uc = models.CharField(max_length = 32, null = False )
    state = models.ForeignKey(State, on_delete = models.PROTECT)
    country = models.ForeignKey(Country, on_delete = models.PROTECT)
    latitude = models.CharField(max_length = 32, null = True)
    longitude = models.CharField(max_length = 32, null = True)


class User(BaseUserModel, AbstractUser):

    name = models.CharField(null = False, max_length = 32)
    # username
    # password
    designation = models.CharField(choices =  DesignationChoice.choices, max_length = 32, db_index = True)
    employee_id = models.CharField(max_length = 16, null = False,unique = True,db_index = True)
    department = models.ForeignKey(Department, on_delete = models.PROTECT, null = True)
    # date_joined
    picture = models.ImageField(upload_to = "profile", null = True)
    # mobile no validation required
    mobile = models.CharField(max_length = 16, null = False, unique = True)
    # email validation required
    email = models.CharField(max_length = 60, unique = True, null = False, db_index = True)
    dob = models.DateField(null = True)

    door_no = models.CharField(max_length = 32)
    street = models.CharField(max_length = 64)
    locality = models.CharField(max_length = 32)
    city = models.ForeignKey(City, on_delete = models.PROTECT, null = True)

    gender = models.CharField(choices = GenderChoice.choices, max_length = 12, null = False)
    #reporting_to = models.ForeignKey('self', on_delete = models.PROTECT)
    passport_no = models.CharField(max_length = 16, null = True, unique = True)
    nationality = models.CharField(max_length = 32,null = True)

    marital_status = models.CharField(choices =  MaritalStatusChoice.choices, max_length = 16, null = True)
    no_of_children = models.IntegerField(null = True)
    # groups
    blood_group = models.CharField(choices = BloodGroupChoice.choices, max_length = 12, null = True)
    social_id_no = models.CharField(max_length = 16,unique = True,null = True)






class UserBankdetails(BaseUserModel):
    
    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    user = models.ForeignKey(User, on_delete = models.PROTECT, null  = False, db_index = True)
    bank_name = models.CharField(max_length = 32, null = False)
    ifsc = models.CharField(max_length = 16,null = False)
    base_branch = models.CharField(max_length = 32,null = True)
    pan_card = models.CharField(max_length = 16, null = True)
    is_company_issued = models.BooleanField(default = False, db_index = True)



class FamilyMembers(BaseUserModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    user = models.ForeignKey(User, on_delete = models.PROTECT, db_index = True)
    name = models.CharField(max_length = 32, null = False)
    relationship = models.CharField(max_length = 32, null = True, default = None)
    mobile = models.CharField(max_length = 12, null = False)
    email = models.EmailField(null = True)
    dob = models.DateTimeField(null = True)
    is_emergency_contact = models.BooleanField(default = True)


class EducationDetails(BaseUserModel):

    id  = models.UUIDField(primary_key = True, editable = False, default =  uuid.uuid4())
    user = models.ForeignKey(User, on_delete = models.PROTECT,db_index = True)
    start_date = models.DateField(null = False)
    end_date = models.DateField(null = True)
    institute_name = models.CharField(max_length = 128, default = None)
    percentage = models.FloatField(null = False)
    course = models.CharField(max_length = 64, null = False)
    level = models.CharField(max_length = 32, null = True, default = None)


class UserExperience(BaseUserModel):
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




class UserGroup(BaseUserModel):

    name = models.CharField(max_length = 32, unique = True,db_index = True)


    def save(self,*args,**kwargs):

       # get or create group with name, returns tuple(Group_object,true/false)
        group, created = Group.objects.get_or_create(name = self.name)
        return super().save(*args,**kwargs)
    








    





    