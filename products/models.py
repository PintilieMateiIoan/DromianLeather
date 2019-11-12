from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone
from sortedm2m.fields import SortedManyToManyField

@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50, default="0 lei")
    pub_date = models.DateTimeField('date published')
    related = SortedManyToManyField('self', blank=True)
    img_path = models.ImageField(upload_to="products/media/products/images/")
    img_description = models.CharField(max_length=200)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def __str__(self):
        return self.name
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
