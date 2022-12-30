from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from multipage_form.views import MultipageFormView
from .forms import LoremForm

class LoremFormView(MultipageFormView):
    template_name = 'stage1.html'
    form_class = LoremForm
    success_url = reverse_lazy("lorem:thank_you")

    def form_valid(self, form):
        next_form_class = form.get_next_form_class()
        if next_form_class == '':
            html = render_to_string(
                'emails/email.html',
                {
                    'content': form.cleaned_data.get('textarea_field')
                }
            )

            email = form.cleaned_data.get('email')

            if email:
                send_mail(
                    'Lorem ipsum',
                    'Lorem ipsum dolor sit amet...',
                    'info@openscoring.io',
                    [
                        email
                    ],
                    fail_silently=False,
                    html_message=html,
                )

        return super().form_valid(form)

class LoremThankYouView(TemplateView):
    template_name = 'thank_you.html'
