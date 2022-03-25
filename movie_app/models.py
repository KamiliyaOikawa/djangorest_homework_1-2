from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg, Sum


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    duration = models.DurationField(null=True, blank=True, verbose_name='Durations')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def reviews(self):
        review = Review.objects.filter(movie=self)
        return [{'text'} for i in review]

    @property
    def rating(self):
        count_reviews = self.reviews.count()
        sum = self.reviews.aggregate(Sum('stars'))['stars__sum']
        try:
            return round(sum / count_reviews, 1)
        except:
            return 0

        # p = 0
        #
        # for i in self.reviews.all():
        #     p += int(i.stars)
        # try:
        #     ans = p / self.reviews.all().count()
        #     return ans
        # except ZeroDivisionError:
        #     ans = p / 1
        #     return ans


class Review(models.Model):
    text = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name="reviews")
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)

    def __str__(self):
        return self.text
