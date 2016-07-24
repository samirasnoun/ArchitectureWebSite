"""
# class ContactForm(forms.ModelForm):
#     confirm_email = forms.EmailField(
#         label="Confirm email",
#         required=True,
#     )

#     class Meta:
#         model = Contact

#     def __init__(self, *args, **kwargs):
#         if kwargs.get(’instance’):
#             email = kwargs[’instance’].email
#             kwargs.setdefault(’initial’, {})[’confirm_email’] = email
    
#         return super(ContactForm, self).__init__(*args, **kwargs)
"""

send_mail('Feedback from your site, topic: %s' % topic,message, sender,['samir.asnoun@gmail.com'])