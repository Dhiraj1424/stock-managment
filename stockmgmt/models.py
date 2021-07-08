from django.db import models

# Create your models here.
category_choice = (
    ('Furniture', 'Furniture'),
    ('IT Equipment', 'IT Equipment'),
    ('Phone', 'Phone'),
)


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    category = models.ForeignKey(
        Category,on_delete=models.CASCADE,blank=True)
    item_name = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    recive_quqntity = models.IntegerField(default=0, null=True)
    recive_by = models.CharField(max_length=20, null=True)
    issue_quqntity = models.IntegerField(default=0, null=True)
    issue_by = models.CharField(max_length=20, null=True)
    issue_to = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    created_by = models.CharField(max_length=20, null=True)
    reorder_level = models.IntegerField(default=0, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name+' ' + str(self.quantity)
