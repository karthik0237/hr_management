from rest_framework.serializers import ModelSerializer, ValidationError
from django.contrib.auth.hashers import make_password

from users import models
from users.utils import *



class BaseUserSerializer(ModelSerializer):

    class Meta:
        fields = ['id','created_at','updated_at','is_active']
        fields_read_only = ['id','created_at','updated_at']



class DepartmentSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.Department
        fields = '__all__'



class CountrySerializer(BaseUserSerializer):
    
    class Meta:
        model = models.Country
        fields = '__all__'
        read_only_fields = BaseUserSerializer.Meta.fields_read_only + ['name_uc']

    def validate(self, attrs):

        is_updated = bool(self.instance)


        name = attrs.get('name', None)
        if is_valid_string('name') == None:
            raise ValidationError("invalid input. Only letters and spaces are allowed")
        
        if name != None:
            attrs['name_uc'] = str(name).upper()

        return super().validate(attrs)



class StateSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.State
        fields = '__all__'
        read_only_fields = BaseUserSerializer.Meta.fields_read_only + ['name_uc']
    
    def validate(self, attrs):

        name = attrs.get('name', None)
        if is_valid_string('name') == None:
            raise ValidationError("invalid input. Only letters and spaces are allowed")
        
        if name != None:
            attrs['name_uc'] = str(name).upper()
        return super().validate(attrs)

    

class CitySerializer(BaseUserSerializer):
    
    class Meta:
        model = models.City
        fields = '__all__'
        read_only_fields = BaseUserSerializer.Meta.fields_read_only + ['name_uc']
    
    def validate(self, attrs):

        name = attrs.get('name', None)
        if is_valid_string('name') == None:
            raise ValidationError("invalid input. Only letters and spaces are allowed")
        
        if name != None:
            attrs['name_uc'] = str(name).upper()
        return super().validate(attrs)



class UserSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.User
        fields = BaseUserSerializer.Meta.fields +  ['name','username','password','employee_id',\
                                                    'designation','picture','date_joined','department',\
                                                    'mobile','email','dob','door_no','street','locality',\
                                                    'city','gender','reporting_to','passport_no',\
                                                    'nationality','marital_status','no_of_children',\
                                                    'blood_group','groups','social_id_no','user_permissions']


    def validate(self, attrs):

        is_update = bool(self.instance)


        # password validation
        password = attrs['password'] #getting value of key - password 

        if password is not None:
            attrs['password']  = make_password(password)#hashing password
            return super().validate(attrs)

        # email validation
        email = attrs.get('email')
        if email != None:
            valid_email = is_valid_email(email)
            if valid_email == False:
                raise ValidationError(detail = 'please enter valid email')
        

        # mobile number validation
        mobile = attrs.get('mobile')
        if mobile != None:
            valid_mobile = is_valid_mobile(mobile)
            if valid_mobile == False:
                raise ValidationError(detail = 'please enter valid mobile number')
        
        

        return super().validate(attrs)
    
   



class UserBankdetailsSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserBankdetails
        fields = '__all__'


    def validate(self, attrs):

        is_update = bool(self.instance)

        # ifsc validation
        ifsc = attrs.get('ifsc')
        if ifsc != None:
            valid_ifsc = is_valid_ifsc(ifsc)
            if valid_ifsc == False:
                raise ValidationError(detail = 'invalid IFSC code. Only uppercase letters and numbers allowed')
        
        # pan_card validation
        pan_card = attrs.get('pan_card')
        if pan_card != None:
            valid_pan_card = is_valid_pan_card(pan_card)
            if valid_pan_card == False:
                raise ValidationError(detail = 'invalid PAN. Only uppercase letters and numbers allowed')
        

        # bank acoount number validation
        bankaccount_no = attrs.get("bankaccount_no")
        if bankaccount_no != None:
            valid_bankaccount_no = is_valid_bankaccount_no(bankaccount_no)
            if valid_bankaccount_no == False:
                raise ValidationError(detail= 'invalid')

        return super().validate(attrs)
        



class FamilyMembersSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.FamilyMembers
        fields = '__all__'

    def validate(self, attrs):
        is_update = bool(self.instance)

        # relationship validation
        relationship = attrs.get('relationship')
        if relationship != None:
            valid_string = is_valid_string(relationship)
            if valid_string == False:
                raise ValidationError(detail = 'invalid input')
        
        # email validation
        email = attrs.get('email')
        if email != None:
            valid_email = is_valid_email(email)
            if valid_email == False:
                raise ValidationError(detail = 'please enter valid email')
        
        # mobile number validation
        mobile = attrs.get('mobile')
        if mobile != None:
            valid_mobile = is_valid_mobile(mobile)
            if valid_mobile == False:
                raise ValidationError(detail = 'please enter valid mobile number')

        return super().validate(attrs)



class EducationDetailsSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.EducationDetails
        fields = '__all__'


    def validate(self, attrs):

        is_update = bool(self.instance)

        # startdate and enddate comparision
        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")

        if (end_date and start_date) != None:
            if end_date < start_date:
                raise ValidationError(detail = "start date must be less than end date")

        # percentage validation
        percentage = attrs.get("percentage")
        if percentage != None:
            if percentage < 0.0 or percentage > 100.0:
                raise ValidationError(detail = "percentage should be between 0.0 and 100.0")


        return super().validate(attrs)

class UserExperienceSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserExperience
        fields = '__all__'

    def validate(self, attrs):

        is_update = bool(self.instance)

        # start and end datetime validation
        start_datetime = attrs.get("start_datetime")
        end_datetime = attrs.get("end_datetime")

        if (end_datetime and start_datetime) != None:
            if end_datetime < start_datetime:
                raise ValidationError(detail = "start date must be less than end date")



        return super().validate(attrs)


class UserGroupSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserGroup
        fields = '__all__'




