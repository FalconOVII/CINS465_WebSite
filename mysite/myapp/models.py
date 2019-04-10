from django.db import models
# from django.core.urlresolvers import reverse

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=250)
    category = models.CharField(max_length=500)
    description = models.CharField(max_length=250)
    recipe_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.recipe_title + ' - ' + self.category

class Mix(models.Model):
    mix_title = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredients = models.CharField(max_length=250)
    directions = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.mix_title

'''
class Suggestion(models.Model):
    suggestion_field = models.CharField(max_length=250)

    def __str__(self):
        return self.suggestion_field

class LiquorType(models.Model):
    beers = models.CharField(max_length=250)
    wines = models.CharField(max_length=250)
    mix_drinks = models.CharField(max_lenth=250)

class Beer(models.Model):
    beer_type = models.CharField(max_lenth=250)
    beer_style = models.CharField(max_length=250)
    beer_title = models.CharField(max_length=250)
    beer_brewer = models.CharField(max_length=250)
    beer_country = models.CharField(max_length=250)
    beer_acohol_content = models.CharField(max_length=250)
    beer_description = models.CharField(max_length=250)

class Wine(models.Model):
    wine_type = models.CharField(max_lenth=250)
    wine_style = models.CharField(max_length=250)
    wine_title = models.CharField(max_length=250)
    wine_brewer = models.CharField(max_length=250)
    wine_country = models.CharField(max_length=250)
    wine_acohol_content = models.CharField(max_length=250)
    wine_description = models.CharField(max_length=250)

'''