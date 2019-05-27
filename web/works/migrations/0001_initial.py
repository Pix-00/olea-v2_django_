# Generated by Django 2.2.1 on 2019-05-27 12:57

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('wid', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('dep', models.IntegerField(choices=[(40, 'writing'), (50, 'reading'), (51, 'reading_eng'), (60, 'painting'), (70, 'post-production')])),
                ('role', models.CharField(max_length=20)),
                ('state', models.IntegerField(choices=[(-2, 'cancelled_f'), (-1, 'cancelled'), (0, 'normal'), (1, 'finished')], default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('timestamp',),
                'unique_together': {('project', 'dep', 'role')},
            },
        ),
        migrations.CreateModel(
            name='WorkFile',
            fields=[
                ('work', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='works.Work')),
                ('type_id', models.IntegerField(choices=[(0, 'none'), (10, 'folder'), (50, 'audio-flac'), (60, 'picture-png'), (70, 'video-mkv'), (71, 'video-mp4')])),
                ('fingerprint', models.BinaryField(max_length=32, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
        ),
    ]
