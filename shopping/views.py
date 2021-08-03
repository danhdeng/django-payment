import stripe

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView 
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.

stripe.api_key=settings.STRIPE_SECRET_KEY

class ShoppingLandingPageView(TemplateView):
    template_name="landing.html"
    
class ShoppingSuccessPageView(TemplateView):
    template_name="success.html"

class ShoppingCancelPageView(TemplateView):
    template_name="cancel.html"


class CreateCheckoutSessionsView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN ='http://localhost:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=[
              'card',
            ],
          line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': shopping.price,
                        'product_data': {
                            'name': shopping.name,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return redirect(checkout_session.url, code=303)