# -*- coding: utf8 -*-
from django import forms

from django.core.exceptions import ValidationError
from website.models import Contact
from localflavor.fr.forms import FRPhoneNumberField
from django.core.validators import validate_email
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS



class Contact2Form(ModelForm):
    
    def clean(self):
    	    cleaned_data = super(Contact2Form, self).clean()
    	    nameField = cleaned_data.get("nameField")
    	    firstNameField = cleaned_data.get("firstNameField")
    	    emailField = cleaned_data.get("emailField")
    	    phoneField = cleaned_data.get("phoneField")
    	    descField = cleaned_data.get("descField")

            if not nameField or len(nameField) < 2:
                msg_nameField = u"le nom doit contenir plus de 2 caracteres"
                self.add_error('nameField', msg_nameField)
        

            if not firstNameField or len(firstNameField) < 5:
                msg_firstNameField = u"le prenom doit contenir plus de 5 caracteres"
                self.add_error('firstNameField', msg_firstNameField)



            if not emailField or not '@' in emailField:    
                msg_emailField = u"le mail doit contenir @"
                self.add_error('emailField', msg_emailField)


            if not descField or len(descField) < 5:
                msg_descField = u"la descrition doit contenir plus de 5 caracteres"
                self.add_error('descField', msg_descField)

            if not phoneField or len(phoneField) < 10 :
                msg_phoneField = u"le numero de telephone doit contenir plus de 10 caracteres"
                self.add_error('phoneField', msg_phoneField)                

            

       
        
            return cleaned_data
    class Meta:
        model = Contact
        fields = ['nameField', 'firstNameField', 'descField', 'phoneField' ,   'emailField']
        error_messages = {

            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

        



TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)


class ContactFeedForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=False)
    
    def clean(self):
    	cleaned_data = super(ContactFeedForm, self).clean()
    	message = cleaned_data.get("message")
    	sender = cleaned_data.get("sender")
    	topic = cleaned_data.get("topic")

        if message and sender and topic:
            msg1 = u"Must put 1"
            msg2 = u"Must put 'help' 2"
            msg3 = u"Must put 'help' 3"
            self.add_error('message', msg1)
            self.add_error('sender', msg2)
            self.add_error('topic', msg3)

        return cleaned_data






class ContactForm(forms.Form):
    nameField = forms.CharField(label='Your nom', max_length=100)
    firstNameField = forms.CharField(label='Your prenom', max_length=100)
    emailField = forms.EmailField(required=True, validators=[validate_email])
    phoneField = FRPhoneNumberField()
    descField = forms.CharField(widget=forms.Textarea())
    def clean(self):
    	cleaned_data = super(ContactForm, self).clean()
    	nameField = cleaned_data.get("nameField")
    	firstNameField = cleaned_data.get("firstNameField")
    	emailField = cleaned_data.get("emailField")
    	phoneField = cleaned_data.get("phoneField")
    	descField = cleaned_data.get("descField")
        if len(nameField) < 5:
            msg_nameField = u"le nom doit contenir plus de 2 caracteres"
            self.add_error('nameField', msg_nameField)
        if len(firstNameField) < 5:
            msg_firstNameField = u"le prenom doit contenir plus de 2 caracteres"
            self.add_error('firstNameField', msg_firstNameField)
        if not '@' in emailField:    
            msg_emailField = u"le mail doit contenir @"
            self.add_error('emailField', msg_emailField)
        return cleaned_data





