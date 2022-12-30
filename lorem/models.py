from django.db import models
from multipage_form.models import MultipageModel

class Lorem(MultipageModel):
    text_field = models.CharField(max_length=20, blank=True)
    date_field = models.DateField(blank=True, null=True)
    time_field = models.TimeField(blank=True, null=True)
    textarea_field = models.TextField(blank=True)

    SELECT_CHOICE_A = 'A'
    SELECT_CHOICE_B = 'B'
    SELECT_CHOICES = [
        (SELECT_CHOICE_A, '(A) Lorem ipsum'),
        (SELECT_CHOICE_B, '(B) Dolor sit'),
    ]

    select_field = models.CharField(
        max_length=1,
        choices=SELECT_CHOICES,
        default=SELECT_CHOICE_A,
        help_text='Lorem ipsum dolor sit amet...'
    )

    checkbox_field = models.BooleanField(default=False)
    radio_field = models.BooleanField(default=False)

    radio2_field = models.BooleanField(default=False)

    number_field = models.IntegerField(default=0)
    email = models.EmailField(max_length=255, null=True)
