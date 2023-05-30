# Generated by Django 4.0.3 on 2023-05-30 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('view_count', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('seller', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_question', to=settings.AUTH_USER_MODEL)),
                ('voter', models.ManyToManyField(related_name='voter_question', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='voter',
        ),
        migrations.RenameModel(
            old_name='QuestionCount',
            new_name='ProductCount',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='comment',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_answer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='voter',
            field=models.ManyToManyField(related_name='voter_answer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productcount',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product'),
        ),
    ]
