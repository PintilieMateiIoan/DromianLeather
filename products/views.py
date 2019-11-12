from django.views import generic
from django.utils import timezone

from .models import Product

class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'latest_product_list'

    def get_queryset(self):
        return Product.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_queryset(self):
        return Product.objects.filter(pub_date__lte=timezone.now())
