from base.horilla_company_manager import HorillaCompanyManager

class EmployeeManagerExcludingAdmins(HorillaCompanyManager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.exclude(employee_user_id__is_superuser=True)

    def include_admins(self):
        return super().get_queryset()
