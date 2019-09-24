import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from firstapp.models import AccessRecord, Websites, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):

    for entry in range(n):

        # get the topic for the entry
        top = add_topics()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new web page entry
        website = Websites.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that websites
        acc_rec = AccessRecord.objects.get_or_create(name=website, date=fake_date)[0]


if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating complete")

