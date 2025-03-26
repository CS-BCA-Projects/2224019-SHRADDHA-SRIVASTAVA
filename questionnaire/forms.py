from django import forms

class QuestionnaireForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name")
    age = forms.IntegerField(min_value=1, max_value=150, label="Age")
    duration = forms.CharField(max_length=10, label="Menstruation Duration")
    flow = forms.ChoiceField(choices=[
        ('Light', 'Light'),
        ('Moderate', 'Moderate'),
        ('Heavy', 'Heavy')
    ], label="Menstrual Flow")
    skin_type = forms.ChoiceField(choices=[
        ('Dry', 'Dry'),
        ('Oily', 'Oily'),
        ('Combination', 'Combination'),
        ('Sensitive', 'Sensitive'),
        ('Normal', 'Normal')
    ], label="Skin Type")
    itchiness = forms.ChoiceField(choices=[
        ('None', 'None'),
        ('Mild', 'Mild'),
        ('Severe', 'Severe')
    ], label="Itchiness")



# from django import forms

# class QuestionnaireForm(forms.Form):
#     MENSTRUAL_FLOW_CHOICES = [("Light", "Light"), ("Moderate", "Moderate"), ("Heavy", "Heavy")]
#     SKIN_TYPE_CHOICES = [("Dry", "Dry"), ("Oily", "Oily"), ("Combination", "Combination"), ("Sensitive", "Sensitive"), ("Normal", "Normal")]
#     ITCHINESS_CHOICES = [("None", "None"), ("Mild", "Mild"), ("Severe", "Severe")]

#     menstruation_duration = forms.IntegerField(label="Menstruation Duration (Days)", min_value=1)
#     menstrual_flow = forms.ChoiceField(label="Menstrual Flow", choices=MENSTRUAL_FLOW_CHOICES)
#     skin_type = forms.ChoiceField(label="Skin Type", choices=SKIN_TYPE_CHOICES)
#     itchiness = forms.ChoiceField(label="Itchiness Level", choices=ITCHINESS_CHOICES)

