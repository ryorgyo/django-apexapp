# Generated by Django 4.1.7 on 2023-02-22 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apexapp.room')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Room_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apexapp.room')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('to_user', models.ManyToManyField(to='loginapp.user')),
            ],
        ),
    ]
