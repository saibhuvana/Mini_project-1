# -*- coding: utf-8 -*-
"""Minor Project code

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BDzkI1gRwh7EqY3vp2duxyttBkTyTKUv
"""

import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
user_email = input("Enter an email address: ")
validate_email(user_email)