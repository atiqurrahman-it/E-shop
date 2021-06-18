from django.db import models

from django.utils.html import mark_safe


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_all_category():
        return Category.objects.all()

    def __str__(self):
        return self.title

    # admin panel a model er name set
    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    main_img = models.ImageField(upload_to='Products')
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    sort_description = models.CharField(default='', null=True, max_length=265, verbose_name='sort_description')
    details_Description = models.TextField(verbose_name='details_Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_date']

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="70px" />' % self.main_img.url)

    image_tag.short_description = 'Image'

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryId(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

