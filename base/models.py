from django.db import models

class DailyRecord(models.Model):
      date = models.DateField(unique=True)
      MedActual = models.PositiveIntegerField(blank=True, null=True)
      SurgActual = models.PositiveIntegerField(blank=True, null=True)
      MedPredict = models.FloatField(blank=True, null=True)
      SurgPredict = models.FloatField(blank=True, null=True)
      MedTCI = models.PositiveIntegerField(blank=True, null=True)
      SurgTCI = models.PositiveIntegerField(blank=True, null=True)
      
      def __unicode__(self):
            return u"Record for %s" % (self.date)
