from django.db import models

class Suggestion(models.Model):
    suggestion_field = models.CharField(max_length=240)

    def __str__(self):
        return self.suggestion_field