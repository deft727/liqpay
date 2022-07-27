from typing import NamedTuple, Any


class CreateSubscriptionTypes(NamedTuple):
    phone: int
    amount: int
    currency: str
    description: str
    order_id: int
    subscribe_date_start: str
    subscribe_periodicity: str
    card: str
    card_exp_month: str
    card_exp_year: str
    card_cvv: str


class UpdateSubscriptionTypes(NamedTuple):
    order_id: int
    amount: int
    currency: str
    description: str


class DeleteSubscriptionTypes(NamedTuple):
    order_id: int


class ResultSubscriptionData(NamedTuple):
    result: str
    status: bool
    err_description: Any
    order_id: int
