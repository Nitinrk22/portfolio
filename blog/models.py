from django.db import models


class Blog(models.Model):
    Chars = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='BlogImages/')

    def __str__(self):
        return self.Chars

    def pub_date_format(self):
        return self.pub_date.strftime("%d %B %Y")

    def summary(self):
        return self.body[:150]
