# Generated by Django 3.1.7 on 2021-02-25 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patrimoine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_closed', models.DateTimeField(blank=True, null=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimoine.building')),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_equip_checked', models.BooleanField(default=False)),
                ('is_meeting_done', models.BooleanField(default=False)),
                ('percentage_of_compliteness', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Created', 'Created'), ('In process', 'In process'), ('Done', 'Done')], default='Created', max_length=20)),
                ('case', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cases.case')),
            ],
        ),
        migrations.CreateModel(
            name='Verification_LocationEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_checked', models.BooleanField(default=False)),
                ('location_equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimoine.locationequipment')),
                ('verification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.verification')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Created', 'Created'), ('In process', 'In process'), ('Done', 'Done')], default='Created', max_length=20)),
                ('meeting_date', models.DateTimeField(blank=True, null=True)),
                ('verification', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cases.verification')),
            ],
        ),
    ]
