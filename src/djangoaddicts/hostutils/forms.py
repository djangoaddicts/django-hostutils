from django import forms


class HostProcessFilterForm(forms.Form):
    """Form Class for filtering host processes"""

    status_choices = [(i, i) for i in ["running", "idle", "sleeping", "stopped", "zombie", "dead"]]
    status = forms.MultipleChoiceField(
        choices=status_choices,
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        required=False,
        label="Status",
    )
    created_at__gte = forms.DateTimeField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "datetime-local"}),
        required=False,
        label="Created After",
    )
    created_at__lte = forms.DateTimeField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "datetime-local"}),
        required=False,
        label="Created Before",
    )
