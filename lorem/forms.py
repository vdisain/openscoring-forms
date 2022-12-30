from django.core.exceptions import ValidationError
from django.forms import RadioSelect, Textarea
from multipage_form.forms import MultipageForm, ChildForm
from .models import Lorem

class LoremForm(MultipageForm):
    model = Lorem
    starting_form = "Stage1Form"

    class Stage1Form(ChildForm):
        template_name = "stage1.html"
        required_fields = [
            "text_field", 
            #"date_field", 
            #"time_field", 
            "textarea_field"
        ]
        #next_form_class = "Stage2Form"

        class Meta:
            fields = [
                "text_field", 
                "date_field", 
                "time_field",
                "textarea_field", 
                "radio_field",
            ]
            widgets = {
                "textarea_field": Textarea(
                    attrs={
                        "placeholder": "Lorem ipsum ...", 
                    },
                )
            }

        def get_next_form_class(self):
            if self.instance.radio_field:
                return "Stage2bForm"
            return "Stage2Form"

    class Stage2Form(ChildForm):
        template_name = "stage2.html"
        required_fields = "__all__"

        class Meta:
            fields = ["select_field", "number_field", "email", "checkbox_field"]

    class Stage2bForm(ChildForm):
        template_name = "stage2b.html"
        required_fields = "__all__"

        class Meta:
            fields = [
                "radio2_field"
            ]
            widgets = {
                "radio2_field": RadioSelect(choices=[
                    (True, "Yes"), 
                    (False, "No")
                ])
            }

        def clean_radio2_field(self):
            radio2 = self.cleaned_data.get("radio2_field")
            if radio2 != True:
                raise ValidationError("Should be Yes.")
            return radio2
