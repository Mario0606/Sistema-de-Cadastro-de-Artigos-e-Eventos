# Generated by Django 2.2.5 on 2019-10-16 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Administrador.User')),
                ('matricule', models.IntegerField()),
            ],
            options={
                'db_table': 'students',
            },
            bases=('Administrador.user',),
        ),
    ]
