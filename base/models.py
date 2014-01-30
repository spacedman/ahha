from django.db import models

class DailyRecord(models.Model):
      date = models.DateField(unique=True)
      predictionTotal = models.FloatField(blank=True, null=True)
      surgicalAdmissions = models.PositiveIntegerField(blank=True, null=True)
      medicalAdmissions = models.PositiveIntegerField(blank=True, null=True)
      surgicalTCI = models.PositiveIntegerField(blank=True, null=True)
      medicalTCI = models.PositiveIntegerField(blank=True, null=True)
      
      def __unicode__(self):
            return u"Record for %s" % (self.date)
