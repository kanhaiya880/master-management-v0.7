# Generated by Django 4.2.1 on 2023-05-21 15:33

import datetime
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0014_alter_userprofile_ans_1_alter_userprofile_ans_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='ans_3',
            field=models.TextField(max_length=1055, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='ans_4',
            field=models.TextField(max_length=1055, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='ans_5',
            field=models.TextField(max_length=1055, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='ans_6',
            field=models.TextField(max_length=1055, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='ans_7',
            field=models.TextField(max_length=1055, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='ans_8',
            field=models.TextField(max_length=1055, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='ans_9',
            field=models.TextField(max_length=1055, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='ans_question1',
            field=models.CharField(default='empty', max_length=255),
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='ans_question2',
            field=models.CharField(default='empty', max_length=255),
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='business_name',
            field=models.CharField(max_length=70, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='confirmeduserprofile',
            name='ans_1',
            field=models.TextField(max_length=1055, null='True'),
        ),
        migrations.AlterField(
            model_name='confirmeduserprofile',
            name='ans_2',
            field=models.TextField(max_length=1055, null='True'),
        ),
    ]
