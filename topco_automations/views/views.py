"""
horilla_automation/views/views.py
"""

from django import forms
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse

from horilla.decorators import login_required, permission_required
from topco_automations.methods.methods import generate_choices
from topco_automations.methods.serialize import serialize_form
from topco_automations.models import MailAutomation


@login_required
def get_to_field(request):
    """
    This method is to render `mail to` fields
    """
    model_path = request.GET["model"]
    to_fields, mail_details_choice, model_class = generate_choices(model_path)

    class InstantModelForm(forms.ModelForm):
        """
        InstantModelForm
        """

        class Meta:
            model = model_class
            fields = "__all__"

    serialized_form = serialize_form(InstantModelForm(), "automation_multiple_")

    return JsonResponse(
        {
            "choices": to_fields,
            "mail_details_choice": mail_details_choice,
            "serialized_form": serialized_form,
        }
    )


@login_required
@permission_required("horilla_automation")
def delete_automation(request, pk):
    """
    Automation delete view
    """
    try:
        MailAutomation.objects.get(id=pk).delete()
        messages.success(request, "Automation deleted")
    except Exception as e:
        print(e)
        messages.error(request, "Something went wrong")
    return redirect(reverse("mail-automations"))
