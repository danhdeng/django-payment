import stripe

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView 
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from .models import Shopping

# Create your views here.

stripe.api_key=settings.STRIPE_SECRET_KEY

class ShoppingLandingPageView(TemplateView):
    print(settings.STRIPE_PUBLIC_KEY)
    template_name="landing.html"
    def get_context_data(self, **kwargs):
        product=Shopping.objects.get(name="test product")
        context=super(ShoppingLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
        })
        return context
    
class ShoppingSuccessPageView(TemplateView):
    template_name="success.html"

class ShoppingCancelPageView(TemplateView):
    template_name="cancel.html"


class CreateCheckoutSessionsView(View):
    def post(self, request, *args, **kwargs):
        product_id=self.kwargs["pk"]
        product =Shopping.objects.get(id=product_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
          line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })