from django.db import models

class DailyRecord(models.Model):
      date = models.DateField(blank=True, unique=True)
      predictionTotal = models.FloatField(blank=True)
      surgicalAdmissions = models.PositiveIntegerField(blank=True)
      medicalAdmissions = models.PositiveIntegerField(blank=True)
      surgicalTCI = models.PositiveIntegerField(blank=True)
      medicalTCI = models.PositiveIntegerField(blank=True)
      
      def __unicode__(self):
            return u"Record for $s" % (self.date)
