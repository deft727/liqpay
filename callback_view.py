from django.shortcuts import HttpResponse
from django.conf import settings
from liqpay import LiqPay
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):

    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('callback is valid', sign, flush=True)
        print('callback is not valid', sign, flush=True)
        response = liqpay.decode_data_from_str(data)
        print('callback data', response, flush=True)
        return HttpResponse()
