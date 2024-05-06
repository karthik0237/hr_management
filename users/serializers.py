from rest_framework.serializers import ModelSerializer, ValidationError

from users import models
from users.utils import is_valid_email, is_valid_string



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
        
        

        return super().validate(attrs)
    
   



class UserBankdetailsSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserBankdetails
        fields = '__all__'


class FamilyMembersSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.FamilyMembers
        fields = '__all__'



class EducationDetailsSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.EducationDetails
        fields = '__all__'


class UserExperienceSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserExperience
        fields = '__all__'


class UserGroupSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserGroup
        fields = '__all__'




