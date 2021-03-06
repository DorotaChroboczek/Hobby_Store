# Generated by Django 3.1.7 on 2021-03-27 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=800)),
                ('image', models.ImageField(upload_to='')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.subcategory')),
            ],
            options={
                'verbose_name': 'Meta Product',
                'verbose_name_plural': 'Meta Products',
            },
        ),
    ]
