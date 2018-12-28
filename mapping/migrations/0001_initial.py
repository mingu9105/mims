# Generated by Django 2.1.4 on 2018-12-28 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_unixdatetimefield.fields
import mapping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', django_unixdatetimefield.fields.UnixDateTimeField(auto_now_add=True, verbose_name='Request Date')),
                ('shooting_time', models.DateTimeField(auto_now=True, verbose_name='Shooting Date')),
                ('emr_file', models.FileField(blank=True, upload_to='', verbose_name='EMR File')),
                ('dicom_jpg_file', mapping.fields.ThumbnailImageField(upload_to='dicom_jpg/%Y/%m')),
                ('pacs_file', models.FileField(blank=True, upload_to='', verbose_name='PACS File')),
                ('progress', models.IntegerField(verbose_name='Viewing Progress')),
                ('examination_name', models.CharField(max_length=50, verbose_name='Examination Name')),
                ('examination_type', models.CharField(max_length=50, verbose_name='Examination Type')),
                ('examination_site', models.CharField(blank=True, max_length=50, verbose_name='Examination Site')),
                ('examination_regnum', models.IntegerField(unique=True, verbose_name='Examination Register Number')),
                ('patient_id', models.CharField(max_length=50, verbose_name='Patient ID')),
                ('requesterID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
