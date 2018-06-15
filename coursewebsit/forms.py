from django.contrib.auth.forms import PasswordResetForm as BasePasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class EmailValidationOnForgotPassword(BasePasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!")

        return email