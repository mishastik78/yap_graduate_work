# Generated by Django 4.1.7 on 2023-03-09 11:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0006_alter_promocode_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkPromoCreate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('creation_done', models.BooleanField(default=False, verbose_name='Создание завершено')),
                ('url_download', models.URLField(blank=True, null=True, verbose_name='Ссылка для скачивания csv')),
            ],
            options={
                'verbose_name': 'Генератор промокодов',
                'verbose_name_plural': 'Генератор промокодов',
                'db_table': 'content"."bulk_creation',
                'ordering': ('-created',),
            },
        ),
    ]
