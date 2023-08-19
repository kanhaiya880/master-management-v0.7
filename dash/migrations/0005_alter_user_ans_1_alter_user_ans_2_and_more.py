# Generated by Django 4.2 on 2023-05-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0004_user_ans_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ans_1',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='ans_2',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='ans_choices',
            field=models.CharField(choices=[('Follow up', 'Follow up'), ('Hold up', 'Hold up'), ('Canceled', 'Canceled')], default='nothing', max_length=50),
        ),
    ]