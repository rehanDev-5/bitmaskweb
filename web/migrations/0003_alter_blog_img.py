# Generated by Django 4.1 on 2022-09-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_blog_img_alter_blog_category_alter_blog_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.FileField(default='none', upload_to='blogs/'),
        ),
    ]
