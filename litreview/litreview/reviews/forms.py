from django import forms


class createTicket(forms.Form):
    title = forms.CharField(label="Titre")
    description = forms.CharField(label="Description")
    image = forms.ImageField(label="Image")


class createCritical(forms.Form):
    title = forms.CharField(label="Titre")
    available_notes = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    note = forms.ChoiceField(choices=available_notes, widget=forms.RadioSelect, label="Note")
    description = forms.CharField(label="Commentaire")


class searchUser(forms.Form):
    search = forms.CharField(label=False)


class UnfollowUserButton(forms.Form):
    user_to_follow = forms.CharField(widget=forms.HiddenInput())
