
from django.contrib import admin

# Register your models here.
from app.models import (Attendence, Contact, Enrollment, Gallary,
                        MembershipPlan, Trainer)

admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Enrollment)
admin.site.register(Gallary)
admin.site.register(Attendence)
