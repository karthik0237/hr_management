import re
import users.serializers


def is_valid_string(string):
   valid = re.fullmatch(r'^([A-Za-z]{2,16} {0,})+$', string)

   if valid == None:
      return False
   return True
    



def is_valid_email(string):
    
    # r'' indicates raw string - treats \ as lietral, not as escape character

   valid = re.fullmatch(r'\b[A-Za-z0-9._%$+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9$+-]{2,7}\b', string)

   if valid == None:
      return False
   return True


def is_valid_mobile(string):

   match = re.fullmatch(r'^[\d+.\[\]() -]{5,24}$', string)

   if match == None:
      return False
   return True



def is_valid_ifsc(string):
    
    # r'' indicates raw string - treats '\' as lietral, not as escape character

   valid = re.fullmatch(r'^[A-Z]{4}0[0-9]{6}$', string)

   if valid == None:
     return False
   return True




def is_valid_pan_card(string):
    
    # r'' indicates raw string - treats \ as lietral, not as escape character

   valid = re.fullmatch(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', string)

   if valid == None:
     return False
   return True


def is_valid_bankaccount_no(string):

   valid = re.fullmatch(r'^[A-Z0-9 -]{2,35}$', string)

   if valid == None:
     return False
   return True



