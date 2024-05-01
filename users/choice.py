

from enum import Enum



class DesignationType(Enum):

    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    Middle = 'Middle'

    @classmethod
    def choices(cls):
        return tuple(i.value for i in cls)
    

class GenderType(Enum):

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    @classmethod
    def choices(cls):
        return tuple(i.value for i in cls)
    
class MaritalStatus(Enum):

    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'

    @classmethod
    def choices(cls):
        return tuple(i.value for i in cls)
    

class BloodGroupType(Enum):

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
    
    
    




    


