import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fake_users.settings')

import django
django.setup()

from user_app.models import User
from faker import Faker

fake = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fake.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake.email()

        #making new entries into the db
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]
        #using the get or create function produces a tuple and we only want the first part which is the object that is created


if __name__ == '__main__':
    print("Populating DB...")
    populate(20)
    print("Done.")
