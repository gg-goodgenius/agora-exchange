from django.db import models
from django.contrib.auth.models import User

class Exchange(models.Model):
    sendler = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exchange_sendelr')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exchange_recipient')

    def __str__(self) -> str:
        return f"{self.sendler} - {self.recipient}"

class UpdateData(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE, related_name='updates')
    resultid = models.CharField(max_length=1000)
    finish = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.resultid}"


class MappingClass(models.Model):
    TYPES_DATA = (
        (0, 'xml'),
        (1, 'json'),
        (2, 'yaml'),
        (3, 'xls'),
    )
    name_class = models.CharField(max_length=255)
    name_data = models.CharField(max_length=255)
    type_data = models.IntegerField(default=0, choices=TYPES_DATA)

    def __str__(self) -> str:
        return f"{self.name_class}"

class MappingField(models.Model):
    name_field = models.CharField(max_length=255)
    name_data = models.CharField(max_length=255)
    mapping_class = models.ForeignKey(MappingClass, null=True, on_delete=models.SET_NULL, related_name='fields')

    def __str__(self) -> str:
        return f"{self.mapping_class} - {self.name_field}"