from django.conf import settings
from liqpay import LiqPay

from .subscription_types import CreateSubscriptionTypes, UpdateSubscriptionTypes,\
    DeleteSubscriptionTypes, ResultSubscriptionData


liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)


def create_liqpay_subscription(data: CreateSubscriptionTypes) -> ResultSubscriptionData:

    res = liqpay.api("request", {
        "action": "subscribe",
        "version": "3",
        "phone": data.phone,
        "amount": data.amount,
        "currency": data.currency,
        "description": data.description,
        "order_id": data.order_id,
        "subscribe": "1",
        "subscribe_date_start": data.subscribe_date_start,
        "subscribe_periodicity": data.subscribe_periodicity,
        "card": data.card,
        "card_exp_month": data.card_exp_month,
        "card_exp_year": data.card_exp_month,
        "card_cvv": data.card_cvv,
    })

    return ResultSubscriptionData(
        result=res.get('result'),
        status=True if res.get('subscribed') == 'subscribed' else False,
        err_description=res.get('err_description') if res.get('err_description') else False,
        order_id=res.get('order_id')
                                  )


def update_liqpay_subscription(data: UpdateSubscriptionTypes) -> ResultSubscriptionData:
    res = liqpay.api("request", {
            "action": "subscribe_update",
            "version": "3",
            "order_id": data.order_id,
            "amount": data.amount,
            "currency": data.currency,
            "description": data.description
            })
    return ResultSubscriptionData(
        result=res.get('result'),
        status=True if res.get('subscribed') == 'subscribed' else False,
        err_description=res.get('err_description') if res.get('err_description') else False,
        order_id=res.get('order_id')
    )


def unsubscribe_liqpay_subscription(data: DeleteSubscriptionTypes) -> ResultSubscriptionData:
    res = liqpay.api("request", {
        "action": "unsubscribe",
        "version": "3",
        "order_id": data.order_id

    })

    return ResultSubscriptionData(
        result=res.get('result'),
        status=True if res.get('subscribed') == 'subscribed' else False,
        err_description=res.get('err_description') if res.get('err_description') else False,
        order_id=res.get('order_id')
    )
