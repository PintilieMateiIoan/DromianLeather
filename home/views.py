from django.views import generic
from django.utils import timezone

from products.models import Product

class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'latest_product'

    def get_queryset(self):
        return Product.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:1]
