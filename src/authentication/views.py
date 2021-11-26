# Create your views here.
from django import views
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class DashboardView(views.generic.TemplateView):
    template_name = 'dashboard.html'
