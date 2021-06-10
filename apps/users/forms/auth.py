from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm


class AuthenticationForm(BaseAuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(AuthenticationForm, self).__init__(request=None, *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-solid h-auto p-6 rounded-lg',
                'placeholder': '%s' % field.title(),
                'autocomplete': 'off'
            })
