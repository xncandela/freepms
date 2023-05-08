from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'
    attrs = {'class': 'form-control'}

    def format_value(self, value):

        if value:
            if isinstance(value, str):
                retorno = value
            else:
                retorno = value.isoformat()
        else:
            retorno = None
        return retorno

class DateTimeInput(forms.DateInput):
    input_type = 'datetime-local'
    format = '%Y-%m-%d %H:%M'
    attrs = {'class': 'form-control'}

    def format_value(self, value):

        if value:
            if isinstance(value, str):
                retorno = value
            else:
                retorno = value.isoformat()
        else:
            retorno = None
        return retorno

class TimeInput(forms.DateInput):
    input_type = 'time'
    format = 'hh:mm'
    attrs = {'class': 'form-control'}

    def format_value(self, value):

        if value:
            if isinstance(value, str):
                retorno = value
            else:
                retorno = value.strftime('%H:%M')
        else:
            retorno = None
        return retorno
