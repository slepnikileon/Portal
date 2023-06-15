from django.db import models



class Access(models.Model):

    LOCAL_CHOICES = [
        ('Облако', 'Облако'),
        ('Локально', 'Локально'),
    ]

    LEVEL_LICENCES = [
        ('Первичка','Первичка'),
        ('Вторичка','Вторичка'),
        ('Третичка','Третичка'),
    ]

    EDRPOU = models.IntegerField('ЕДРПОУ')
    FullName = models.CharField('Полное название', max_length=255)
    Name = models.CharField('Краткое название', max_length=255, blank=True, null=True)
    Oblast = models.CharField('Область', max_length=255, blank=True, null=True)
    Localithation = models.CharField('Локализация', max_length=8, choices=LOCAL_CHOICES, blank=True, null=True)
    Level_medical_help = models.CharField('Уровень мед. помощи', choices=LEVEL_LICENCES, max_length=8, blank=True, null=True)
    License = models.IntegerField('Количество лицензий', blank=True, null=True)
    Contact = models.TextField('Контакты', blank=True, null=True)
    RDP_SQL_IP = models.CharField('RDP SQL IP', max_length=50, blank=True, null=True)
    RDP_SQL_Login = models.CharField('RDP SQL Login', max_length=50, blank=True, null=True)
    RDP_SQL_Password = models.CharField('RDP SQL Password', max_length=50, blank=True, null=True)
    SQL_Server_Password = models.CharField('SQL Server Password', max_length=50, blank=True, null=True)
    RDP_APP_IP = models.CharField('RDP APP IP', max_length=50, blank=True, null=True)
    RDP_APP_Login = models.CharField('RDP APP Login', max_length=50, blank=True, null=True)
    RDP_APP_Password = models.CharField('RDP APP Password', max_length=50, blank=True, null=True)
    EMCI_IP = models.CharField('EMCI IP', max_length=50, blank=True, null=True)
    EMCI_Port = models.CharField('EMCI Port', max_length=50, blank=True, null=True)
    EMCI_Login = models.CharField('EMCI Login', max_length=50, blank=True, null=True)
    EMCI_Password = models.CharField('EMCI Password', max_length=50, blank=True, null=True)
    Info = models.TextField('Info', blank=True, null=True)
    
    def __str__(self):
        return self.Name
