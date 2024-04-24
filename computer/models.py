from django.db import models


class ComputerBrand(models.Model):
    brand_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logos/', null=True, blank=True)

    def __str__(self):
        return self.brand_name


class ComputerSpecification(models.Model):
    generation = models.CharField(max_length=100)
    price_min = models.DecimalField(max_digits=10, decimal_places=2)
    price_max = models.DecimalField(max_digits=10, decimal_places=2)
    ram = models.IntegerField()
    brand = models.ForeignKey(ComputerBrand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.generation} - {self.brand.brand_name}"


class Computer(models.Model):
    computer_code = models.CharField(max_length=100, unique=True)
    computer = models.ForeignKey(ComputerSpecification, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_rate = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_rate
        super(Computer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.computer_code} - {self.computer.generation}"
