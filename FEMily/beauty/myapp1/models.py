from django.db import models

class Specialist(models.Model):
    name = models.CharField(max_length=20, blank=False)
    father_name = models.CharField(max_length=35, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    phone = models.CharField(max_length=11)
    specialization = models.CharField(max_length=200, blank=False)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.second_name} {self.name} {self.father_name}'


class Client(models.Model):
    name = models.CharField(max_length=20, blank=False)
    father_name = models.CharField(max_length = 35, blank = False)
    second_name = models.CharField(max_length = 35, blank = False)
    phone = models.CharField(max_length=11)
    loyality_card = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.second_name} {self.name} {self.father_name}'


class Service(models.Model):
    title = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length = 200, blank = False)
    price = models.DecimalField(max_digits=5, decimal_places=2)



    def __str__(self):
        return f'{self.title}'

class Registration(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return f'{self.client}'


class Sale(models.Model):
    title = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=200, blank=False)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f'{self.title}'



class Reviews(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    messages = models.CharField(max_length=200, blank=False)


    def __str__(self):
        return f'{self.client_name}'