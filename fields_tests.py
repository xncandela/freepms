
import os
import django
from freepms import settings

from django.apps import apps
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freepms.settings")
django.setup()

app='master'
modelname='Country'


model = apps.get_model(f'{app}.{modelname.lower()}')

for field in model._meta.get_fields():
    if 'reverse_related' in f'{type(field)}':
        continue

    print(field.name,field.is_relation,field.many_to_many,field.many_to_one)
    if field.is_relation:
        a=field.related_model
        print(field.related_model)