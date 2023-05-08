from django.apps import apps

from master.models import App,Model


def load_apps():
    for key, value in apps.all_models.items():
        keys = ['admin', 'contenttypes', 'auth', 'sessions']
        if value.__len__() > 0 and key not in keys:
            app ,new = App.objects.get_or_create(name=key)
            for model in apps.all_models[key]:

                mm = apps.all_models[key][model]

                Model.objects.get_or_create(app=app ,model=mm._meta.label.split('.')[1])