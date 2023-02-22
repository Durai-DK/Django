from django.db import models


class StoreDetails(models.Model):
    Store_Name = models.CharField(max_length=250)
    APX_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.APX_Name


class RatingReview(models.Model):
    store = models.ForeignKey(StoreDetails,on_delete=models.CASCADE)
    views = models.IntegerField()
    date = models.DateField()
    ratings = models.IntegerField()

    def __str__(self):
        return '{} {} {} {}'.format(self.store,self.date,self.views,self.ratings)