# Generated by Django 3.1.7 on 2021-03-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_productpromotion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Overcategory',
                'verbose_name_plural': 'Overcategories',
            },
        ),
    ]
