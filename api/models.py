from django.db import models

class SaveData(models.Model):
    entry = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = 'Save Data'
        verbose_name = 'Save Data'
