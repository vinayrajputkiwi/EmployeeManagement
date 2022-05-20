# Generated by Django 4.0.4 on 2022-05-20 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='checkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='registeremp',
            fields=[
                ('checkin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.checkin')),
                ('identification_type', models.CharField(choices=[('ADHAAR', 'ADHAAR'), ('PANCARD', 'PANCARD'), ('OTHER', 'OTHER')], max_length=100)),
                ('identification', models.CharField(max_length=100, unique=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=50)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(choices=[('Twoheeler', 'Twowheeler'), ('FourWheeler', 'FourWheeler')], max_length=100)),
                ('vehicle_name', models.CharField(choices=[('Bike', 'Bike'), ('MahindraThar', 'MahindraThar'), ('MahindraXUV700', 'MahindraXUV700'), ('Tata Nexon', 'Tata Nexon'), ('Hyundai Creta', 'Hyundai Creta')], max_length=100)),
            ],
            bases=('app.checkin',),
        ),
    ]