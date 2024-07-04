from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=225, blank=False, null=False)
    slug = models.SlugField(max_length=255, unique=True, blank=False, null=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.title

class Promotions(models.Model):
    description = models.CharField(max_length=225)
    discount = models.FloatField()
    def __str__(self) -> str:
        return self.description

class Product(models.Model):
    id = models.IntegerField(primary_key=True , auto_created=True)
    slug = models.SlugField(max_length=20, unique=True)
    title = models.CharField(max_length=225)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)
    type_of = models.CharField(max_length=255, blank=False)
    color = models.CharField(max_length=255, blank=False)
    shape = models.CharField(max_length=255, blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, related_name='products')
    promotions = models.ManyToManyField(Promotions, related_name='products' , blank=True, null=True)
    date_added = models.DateField()
    origin = models.CharField(max_length=255, blank=False)
    weight = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images')
   


