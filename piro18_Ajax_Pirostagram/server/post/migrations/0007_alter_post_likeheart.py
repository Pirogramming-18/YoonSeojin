# Generated by Django 4.1.5 on 2023-01-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0006_post_likeheart_alter_post_like"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likeHeart",
            field=models.TextField(
                default='<i class="fa-regular fa-heart" style="color:red"></i>'
            ),
        ),
    ]
