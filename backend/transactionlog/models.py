from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    DATE_FMT = '%m-%d-%Y %I:%M %p'

    date = models.DateTimeField("date of purchase") # optional human readable name
    vendor = models.CharField(max_length=200) # temp, should be foreign key
    customer = models.CharField(max_length=200) # temp, should be fk
    purchase_total = models.DecimalField("purchase total", max_digits=6, decimal_places=2)
    snap = models.DecimalField("SNAP", max_digits=6, decimal_places=2, default=0)
    wicsenior = models.DecimalField("WIC/Senior", max_digits=6, decimal_places=2, default=0)
    match_snap = models.DecimalField("SNAP matching", max_digits=6, decimal_places=2, default=0)
    match_wicsenior = models.DecimalField("WIC/Senior matching", max_digits=6, decimal_places=2, default=0)
    cash_credit = models.DecimalField("cash/credit", max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        datestr = timezone.localtime(self.date).strftime(self.DATE_FMT)
        return f"{datestr} - {self.customer} @ {self.vendor} - ${self.purchase_total:,.2f}"
    
    #def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)