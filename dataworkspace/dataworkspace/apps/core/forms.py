from django import forms


class SupportForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='Your email address',
        widget=forms.EmailInput(attrs={'class': 'govuk-input'}),
    )
    message = forms.CharField(
        required=True,
        label='Description',
        widget=forms.Textarea(attrs={'class': 'govuk-textarea'}),
        help_text=(
            'If you want to provide feedback or a suggestion, describe it here. '
            'If you were having a problem, explain what you did, what happened and '
            'what you expected to happen.'
        ),
    )
