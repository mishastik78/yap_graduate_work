# Generated by Django 4.1.7 on 2023-03-09 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promo', '0009_bulkpromocreate_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bulkpromocreate',
            options={'ordering': ('-created',), 'verbose_name': 'promo code generator', 'verbose_name_plural': 'promo codes generator'},
        ),
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ('-created',), 'verbose_name': 'activation log', 'verbose_name_plural': 'activations log'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='productpromocode',
            options={'verbose_name': 'related product', 'verbose_name_plural': 'related products'},
        ),
        migrations.AlterModelOptions(
            name='promocode',
            options={'ordering': ('-created',), 'verbose_name': 'promo', 'verbose_name_plural': 'promos'},
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bulks', to=settings.AUTH_USER_MODEL, verbose_name='creator'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='creation_done',
            field=models.BooleanField(default=False, verbose_name='creation completed'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='discount value'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='discount_type',
            field=models.CharField(choices=[('fixed_price', 'fixed price'), ('percentage_discount', 'percentage discount'), ('fixed_discount', 'fixed discount')], max_length=30, verbose_name='discount type'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='expired',
            field=models.DateTimeField(blank=True, null=True, verbose_name='valid to'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='minimal_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='minimum check amount to apply'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='promos_bulk', through='promo.ProductPromoCode', to='promo.product', verbose_name='promo assign to products'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='start_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='bulkpromocreate',
            name='url_download',
            field=models.URLField(blank=True, null=True, verbose_name='download csv link'),
        ),
        migrations.AlterField(
            model_name='history',
            name='applied_user_id',
            field=models.UUIDField(verbose_name='code is activated by (UUID id)'),
        ),
        migrations.AlterField(
            model_name='history',
            name='billing_info',
            field=models.TextField(blank=True, null=True, verbose_name='info from billing service'),
        ),
        migrations.AlterField(
            model_name='history',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='history',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='amount of the applied discount'),
        ),
        migrations.AlterField(
            model_name='history',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='history',
            name='promocode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='history', to='promo.promocode', verbose_name='activated promo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='product description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='product name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='product price'),
        ),
        migrations.AlterField(
            model_name='productpromocode',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='productpromocode',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='productpromocode',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promo.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='activates_left',
            field=models.PositiveIntegerField(blank=True, help_text='leave blank for autofill', verbose_name='number of activations left'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='activates_possible',
            field=models.PositiveIntegerField(default=1, verbose_name='number of possible activations'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='code',
            field=models.CharField(blank=True, db_index=True, help_text='leave blank for autofill', max_length=50, unique=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='codes', to=settings.AUTH_USER_MODEL, verbose_name='creator'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='discount value'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='discount_type',
            field=models.CharField(choices=[('fixed_price', 'fixed price'), ('percentage_discount', 'percentage discount'), ('fixed_discount', 'fixed discount')], max_length=30, verbose_name='discount type'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='expired',
            field=models.DateTimeField(blank=True, null=True, verbose_name='valid to'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='promo code is active'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='minimal_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='minimum check amount to apply'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='promos', through='promo.ProductPromoCode', to='promo.product', verbose_name='promo assign to products'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='start_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='valid from'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='promocode',
            name='user_id',
            field=models.UUIDField(blank=True, null=True, verbose_name='promo assign to user (UUID id)'),
        ),
    ]
