# import re
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#
#
# def check(email):
#     if (re.search(regex, email)):
#         print("Valid Email")
#     else:
#         print("Invalid Email")
#
#
# email = "ankitrai326@gmail.com"
#
#
# check(email)
#
# email2 = "my.ownsite@ourearth.org"
# check(email2)
#
# email3 = "ankitrai326.com"
# check(email3)

from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', 'shera.rashiduulu@gmail.com', ['shera.rashiduulu@gmail.com'], fail_silently=False, )