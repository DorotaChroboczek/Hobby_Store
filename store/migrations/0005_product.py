# Generated by Django 3.1.7 on 2021-03-27 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_unitofmeasurement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.PositiveSmallIntegerField(verbose_name='Package size')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('availability', models.IntegerField()),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.unitofmeasurement')),
                ('meta_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.metaproduct')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
