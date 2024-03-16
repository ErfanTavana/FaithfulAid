from django.db import models


# ایجاد مدل نیازمندان
class Needy(models.Model):
    GENDER_CHOICES = (
        ('مرد', 'مرد'),
        ('زن', 'زن'),
    )

    MARITAL_STATUS_CHOICES = (
        ('مجرد', 'مجرد'),
        ('متاهل', 'متاهل'),
        ('بیوه', 'بیوه'),
        ('مطلقه', 'مطلقه'),
    )

    RELIGION_CHOICES = (
        ('تشیع', 'تشیع'),
        ('تسنن', 'تسنن'),
    )

    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام خانوادگی')
    father_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام پدر')
    national_code = models.CharField(max_length=10, blank=True, null=True, verbose_name='کد ملی')
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER_CHOICES, verbose_name='جنسیت')
    family_members_count = models.PositiveIntegerField(blank=True, null=True, verbose_name='تعداد اعضا')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='شماره تماس')
    referrer_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='نام و نام خانوادگی معرف', )
    marital_status = models.CharField(max_length=15, blank=True, null=True, choices=MARITAL_STATUS_CHOICES,
                                      verbose_name='وضعیت تاهل')
    religion = models.CharField(max_length=15, blank=True, null=True, choices=RELIGION_CHOICES, verbose_name='مذهب')
    job = models.CharField(max_length=100, blank=True, null=True, verbose_name='شغل')
    coverage = models.CharField(max_length=100, blank=True, null=True, verbose_name='تحت پوشش')
    street_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='نام خیابان')
    route_code = models.IntegerField(default=0, blank=True, null=True, verbose_name='کد مسیر')
    address = models.TextField(blank=True, null=True, verbose_name='آدرس دقیق')

    def __str__(self):
        return f'{self.name} {self.last_name}'
