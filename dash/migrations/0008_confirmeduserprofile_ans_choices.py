# Generated by Django 4.2.1 on 2023-05-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_confirmeduserprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmeduserprofile',
            name='ans_choices',
            field=models.CharField(choices=[('Follow up', 'Follow up'), ('Hold up', 'Hold up'), ('Canceled', 'Canceled')], default='nothing', max_length=50),
        ),
    ]
