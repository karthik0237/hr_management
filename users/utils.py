import re
import users.serializers


def is_valid_string(string):
   pass
    



def is_valid_email(string):

    valid = re.fullmatch(r'\b[A-Za-z0-9._%$+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9$+-]{2,7}\b', string)

    if valid == None:
     return False
    return True