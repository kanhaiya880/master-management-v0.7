# Generated by Django 4.2.1 on 2023-05-21 12:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0012_alter_userprofile_ans_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='ans_question',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ans_3',
            field=models.TextField(default='empty', max_length=1055),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ans_4',
            field=models.TextField(default='empty', max_length=1055),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ans_5',
            field=models.TextField(default='empty', max_length=1055),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ans_6',
            field=models.TextField(default='empty', max_length=1055),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ans_7',
            field=models.TextField(default='empty', max_length=1055),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ans_8',
            field=models.TextField(default='empty', max_length=1055),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ans_9',
            field=models.TextField(default='empty', max_length=1055),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ans_question1',
            field=models.CharField(default='empty', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ans_question2',
            field=models.CharField(default='empty', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='business_name',
            field=models.CharField(default='empty', max_length=70),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ans_1',
            field=models.TextField(default='empty', max_length=1055),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ans_2',
            field=models.TextField(default='empty', max_length=1055),
        ),
    ]
