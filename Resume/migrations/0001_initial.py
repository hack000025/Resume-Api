# Generated by Django 3.1 on 2021-09-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('certificate_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Certificate_url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Certification',
                'db_table': 'user_Certification',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('college_name', models.CharField(max_length=90, primary_key=True, serialize=False)),
                ('stream', models.CharField(blank=True, max_length=50)),
                ('percentage', models.CharField(blank=True, max_length=50)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('Passout_Date', models.DateField()),
            ],
            options={
                'db_table': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('company_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ex_year_or_month', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Experience',
                'db_table': 'user_Experience',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('live_projects', models.BooleanField()),
                ('personal', models.BooleanField()),
                ('project_name', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('duration', models.CharField(blank=True, max_length=250)),
                ('langauges', models.CharField(blank=True, max_length=50)),
                ('role', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=550)),
                ('project_url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'db_table': 'user_Projects',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('Programming_lang', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Skills',
                'db_table': 'Skill',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(max_length=64)),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='Male', max_length=6)),
                ('phone', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=250, null=True)),
                ('country', models.CharField(blank=True, max_length=250, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('Certification', models.ManyToManyField(related_name='Certification', to='Resume.Certification')),
                ('Experinces', models.ManyToManyField(related_name='Experience', to='Resume.Experience')),
                ('Project', models.ManyToManyField(related_name='Project', to='Resume.Projects')),
                ('skills', models.ManyToManyField(related_name='Skills', to='Resume.Skills')),
            ],
            options={
                'db_table': 'Profile',
            },
        ),
    ]
