# Generated by Django 3.2.5 on 2021-07-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bestseller',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('flag', models.CharField(max_length=10)),
                ('url', models.TextField()),
                ('image', models.TextField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('summary', models.TextField()),
                ('category', models.CharField(choices=[('1', 'Novel_Poem'), ('170', 'Economic_Management'), ('1230', 'Home_Cook_Beauty'), ('1237', 'Religion_Mysticism'), ('517', 'Art_Culture'), ('76001', 'Reference_Book'), ('55890', 'Health_Hobby_Leisure'), ('987', 'Science'), ('74', 'History'), ('336', 'Self_Improvement'), ('1196', 'Travel'), ('55889', 'Essay'), ('656', 'Humanities')], max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('src', models.TextField()),
            ],
        ),
    ]