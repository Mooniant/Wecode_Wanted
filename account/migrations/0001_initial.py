# Generated by Django 3.1.2 on 2020-10-07 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('education', models.CharField(max_length=20, null=True)),
                ('company', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=10, null=True)),
                ('end_date', models.CharField(max_length=10, null=True)),
                ('company_name', models.CharField(max_length=10, null=True)),
                ('department', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'careers',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=10, null=True)),
                ('end_date', models.CharField(max_length=10, null=True)),
                ('college_name', models.CharField(max_length=10, null=True)),
                ('major', models.CharField(max_length=10, null=True)),
                ('contents', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'educations',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_url', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.career')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.education')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
            options={
                'db_table': 'resumes',
            },
        ),
        migrations.CreateModel(
            name='Application_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reusme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.resume')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
            options={
                'db_table': 'application_status',
            },
        ),
    ]