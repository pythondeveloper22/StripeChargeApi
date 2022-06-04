from django.views.generic.base import TemplateView
from django.conf import settings
import stripe
from django.shortcuts import render
from django.http import HttpResponse

stripe.api_key = "sk_test_3I7qOec3y13GfLfElxBjzqdy00FdKlQxKb"
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

#
def charge(request):
    if request.method == 'POST':
        print(request.POST)
        amount=50
        customer = stripe.Customer.create(
            # email='customer@example.com',
            email=request.POST['stripeEmail'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer= customer.id,
            amount=amount,
            currency='usd',
            description='Django Charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')


