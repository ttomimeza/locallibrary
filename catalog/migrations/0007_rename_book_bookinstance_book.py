# Generated by Django 4.2.1 on 2023-05-16 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_rename_genre_book_genre_rename_genre_genre_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='Book',
            new_name='book',
        ),
    ]