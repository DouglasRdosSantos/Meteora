# Generated by Django 5.1.2 on 2024-11-01 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meteora', '0002_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='Produtos/%Y/%m/%d/'),
        ),
    ]
