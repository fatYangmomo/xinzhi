# Generated by Django 2.1 on 2018-07-13 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialReport',
            fields=[
                ('stock_code', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='股份代码')),
                ('stock_name', models.CharField(max_length=50, verbose_name='股份名称')),
                ('report_date', models.CharField(max_length=10, null=True, verbose_name='报告日期')),
                ('capital', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='总股本')),
                ('business_receipts', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='营业收入')),
                ('profits', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='净利润')),
                ('business_ratio', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='营业收入增长率')),
                ('profits_ratio', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='净利润增长率')),
                ('share_asset', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='每股净资产')),
                ('asset_ratio', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='净资产收益率')),
                ('share_profit', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='每股收益')),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='当前价格')),
                ('shiying_ratio', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='市盈率')),
                ('shijing_ratio', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='市净率')),
                ('plate', models.CharField(max_length=10, null=True, verbose_name='所属板块')),
                ('closing_price', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='收盘价')),
                ('front_close', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='前收盘')),
            ],
            options={
                'verbose_name': 'financial_report',
                'db_table': 'financial_report',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=32, verbose_name='组合名称')),
            ],
            options={
                'verbose_name': 'group',
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_code', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='股份代码')),
                ('stock_name', models.CharField(max_length=50, verbose_name='股份名称')),
                ('plate', models.CharField(max_length=10, null=True, verbose_name='所属板块')),
            ],
            options={
                'verbose_name': 'stock',
                'db_table': 'stock',
            },
        ),
        migrations.AddField(
            model_name='financialreport',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Group'),
        ),
    ]
