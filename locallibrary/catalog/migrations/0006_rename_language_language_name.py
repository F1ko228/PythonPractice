# Generated by Django 4.2.7 on 2023-11-20 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_language_alter_book_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='language',
            new_name='name',
        ),
    ]
