from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic

from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        profile = Profile(user=result)
        if commit:
            profile.save()
        return result
