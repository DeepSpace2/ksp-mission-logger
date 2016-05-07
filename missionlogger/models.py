from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


class Vessel(models.Model):
    created_at = models.DateField(editable=False)
    updated_at = models.DateField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('missionlogger:mission-add')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now().date()
        self.updated_at = timezone.now().date()
        return super().save(*args, **kwargs)


class Mission(models.Model):
    created_at = models.DateField(editable=False)
    updated_at = models.DateField()
    title = models.CharField(max_length=256, null=False, blank=False)
    vessel = models.ForeignKey(to=Vessel, related_name='vessels')
    status = models.IntegerField(choices=((1, 'In progress'),
                                          (2, 'Success'),
                                          (3, 'Partial success'),
                                          (4, 'Failure')))
    details = models.TextField()

    def get_class(self):
        if self.status == 1:
            return 'inprogress'
        if self.status == 2:
            return 'success'
        if self.status == 3:
            return 'partial'
        return 'failure'

    def __str__(self):
        return '{} - {} - {}'.format(self.title, self.vessel, self.get_status_display())

    def get_absolute_url(self):
        return reverse('missionlogger:index')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now().date()
        self.updated_at = timezone.now().date()
        return super().save(*args, **kwargs)




