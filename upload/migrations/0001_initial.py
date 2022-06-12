# Generated by Django 4.0.5 on 2022-06-12 17:19

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', django_fsm.FSMField(choices=[('PENDING', 'PENDING'), ('PROCESSING', 'PROCESSING'), ('COMPLETED', 'COMPLETED')], default='pending', max_length=50, protected=True)),
            ],
        ),
    ]
