from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        '''Returns the brand name'''
        return self.name

class Kind(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        '''Returns the kind name'''
        return self.name

class Product(models.Model):
    brand = models.ForeignKey(Brand)
    name = models.CharField(max_length=20)
    kinds = models.ManyToManyField(Kind)
    
    def __str__(self):
        '''Returns the brand, name and kind of the product'''
        return  "{0} {1} {2}".format(self.brand, self.name, ' '.join([kind.name for kind in self.kinds.all()]))