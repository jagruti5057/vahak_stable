import random
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings

def send_otp_via_email(email):
    subject = 'Your account verification email'
    otp = random.randint(1000, 9999)
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email ])
    return otp

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def send_otp(phone):
    if phone:
        key = random.randint(1000, 9999)    
        print(key)
        return key
    else:
        return False
                    
def updateuserfields(model,obj,instance,obj2,updatefield):
    li = list(obj2.split(","))
    if updatefield =='routes':
        for current_genre in instance.routes.all():
            instance.routes.remove(current_genre)
    else:
        for current_genre in instance.role.all():
            instance.role.remove(current_genre)
# Repopulate genres into instance.
    for route in li:
        user_obj = model.objects.get(pk=instance.id)
        if updatefield == 'routes':
            data_obj = obj.objects.get(id=route)
            user_obj.routes.add(data_obj.id)   
        else:
             data_obj = obj.objects.get(name=route)
             user_obj.role.add(data_obj.id)           
    return user_obj