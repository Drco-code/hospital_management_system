import django_filters

from billing.models import Billing

class BillingFilter(django_filters.FilterSet):

    class Meta:
        models = Billing
        fields = {
            "total_amount": ['lte', 'gte'],
            "payment_date": ['lte', 'gte']
        }