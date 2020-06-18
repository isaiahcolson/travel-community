class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_lenght=100)
    review = models.CharField(max_length=300)
    rating = models.IntegerField()

    