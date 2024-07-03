# Generated by Django 4.1.5 on 2023-01-31 18:56

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='fullname',
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(choices=[('WD', 'Windsor'), ('TO', 'Toronto'), ('CH', 'Chatham'), ('WL', 'WATERLOO')], default='CH', max_length=2),
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_items', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[(0, 'Cancelled order'), (1, 'Placed Order'), (2, 'Shipped Order'), (3, 'Delivered Order')], max_length=1)),
                ('last_updated', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.client')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='myapp1.item')),
            ],
        ),
    ]
