from django.db import models


# Creates model of University Campus
class UniversityCampus(models.Model):
    campusName = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campusId = models.IntegerField(default="", blank=True, null=False)


    #Creates model manager
    object = models.Manager()


    #Displays the object output values in the form of a string
    def __str__(self):
        display_campus = '{0.campusName}'
        return display_campus.format(self)

    #Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"