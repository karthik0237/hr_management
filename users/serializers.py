from rest_framework.serializers import ModelSerializer, ValidationError

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




        if attrs.get('name', None):
            name = attrs.get('name')
            attrs['name_uc'] = str(name).upper()
        return super().validate(attrs)



class StateSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.State
        fields = '__all__'
        read_only_fields = BaseUserSerializer.Meta.fields_read_only + ['name_uc']
    
    def validate(self, attrs):

        if attrs.get('name', None):
            name = attrs.get('name')
            attrs['name_uc'] = str(name).upper()
        return super().validate(attrs)

    

class CitySerializer(BaseUserSerializer):
    
    class Meta:
        model = models.City
        fields = '__all__'
        read_only_fields = BaseUserSerializer.Meta.fields_read_only + ['name_uc']
    
    def validate(self, attrs):

        if attrs.get('name', None):
            name = attrs.get('name')
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

        # email validation
        email = attrs.get('email')
        valid_email = is_valid_email(email)
        if valid_email == False:
            raise ValidationError(detail = 'please enter valid email')
        

        # mobile number validation
        mobile = attrs.get('mobile')
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
        valid_ifsc = is_valid_ifsc(ifsc)
        if valid_ifsc == False:
            raise ValidationError(detail = 'invalid IFSC code. Only uppercase letters and numbers allowed')
        
        # pan_card validation
        pan_card = attrs.get('pan_card')
        valid_pan_card = is_valid_pan_card(pan_card)
        if valid_pan_card == False:
            raise ValidationError(detail = 'invalid PAN. Only uppercase letters and numbers allowed')
        

        #bank acoount number validation
        bankaccount_no = attrs.get("bankaccount_no")
        valid_bankaccount_no = is_valid_bankaccount_no("bankaccount_no")
        if valid_bankaccount_no == False:
            raise ValidationError(detail= 'invalid')

        return super().validate(attrs)
        



class FamilyMembersSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.FamilyMembers
        fields = '__all__'

    def validate(self, attrs):

        # relationship validation
        relationship = attrs.get('relationship')
        valid_string = is_valid_string(relationship)
        if valid_string == False:
            raise ValidationError(detail = 'invalid format. Only letters are allowed')
        
        # email validation
        email = attrs.get('email')
        valid_email = is_valid_email(email)
        if valid_email == False:
            raise ValidationError(detail = 'please enter valid email')
        
        # mobile number validation
        mobile = attrs.get('mobile')
        valid_mobile = is_valid_mobile(mobile)
        if valid_mobile == False:
            raise ValidationError(detail = 'please enter valid mobile number')

        return super().validate(attrs)



class EducationDetailsSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.EducationDetails
        fields = '__all__'


    def validate(self, attrs):
        return super().validate(attrs)

class UserExperienceSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserExperience
        fields = '__all__'


class UserGroupSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserGroup
        fields = '__all__'




