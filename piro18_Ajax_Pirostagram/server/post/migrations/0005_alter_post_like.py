# Generated by Django 4.1.5 on 2023-01-25 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0004_comment_deleted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="like",
            field=models.TextField(
                default='<i class="fa-solid fa-heart style="color:red"></i>'
            ),
        ),
    ]