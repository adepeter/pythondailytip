# Generated by Django 3.2.4 on 2021-06-09 15:47

from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PythonTip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.PositiveBigIntegerField(unique=True, verbose_name='Tweet ID')),
                ('tip', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='Number of Tweet likes')),
                ('retweets', models.PositiveIntegerField(default=0, verbose_name='Number of retweets')),
                ('timestamp', models.DateTimeField()),
                ('published', models.BooleanField(default=True, help_text='Is tweet published?', verbose_name='Published')),
            ],
            options={
                'verbose_name': 'Tip',
                'ordering': ['-timestamp'],
                'get_latest_by': '-timestamp',
            },
        ),
        migrations.CreateModel(
            name='PythonTipHashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='#HashTag')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Hash Tag',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PythonTipLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Hyperlink',
            },
        ),
        migrations.CreateModel(
            name='PythonTipTweetUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField(unique=True, verbose_name='Tweet user ID')),
                ('username', models.CharField(db_index=True, max_length=255, verbose_name='Username')),
                ('display_name', models.CharField(max_length=255, verbose_name='Username')),
            ],
            options={
                'verbose_name': 'Tweet User',
            },
        ),
        migrations.CreateModel(
            name='TweeCrypt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_key', django_cryptography.fields.encrypt(models.CharField(max_length=25, verbose_name='Twitter API Consumer Key'))),
                ('consumer_secret', django_cryptography.fields.encrypt(models.CharField(max_length=50, verbose_name='Twitter API Consumer Secret'))),
                ('access_token', django_cryptography.fields.encrypt(models.TextField(max_length=50, verbose_name='Twitter API Consumer Key'))),
                ('access_token_secret', django_cryptography.fields.encrypt(models.TextField(max_length=50, verbose_name='Twitter API Access Token Secret'))),
            ],
            options={
                'verbose_name': 'Twitter API Config Key',
            },
        ),
        migrations.AddIndex(
            model_name='pythontiptweetuser',
            index=models.Index(fields=['user_id', 'username'], name='idx_id_username'),
        ),
        migrations.AddField(
            model_name='pythontiplink',
            name='tip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='twee.pythontip', verbose_name='Tip'),
        ),
        migrations.AddField(
            model_name='pythontip',
            name='hash_tags',
            field=models.ManyToManyField(blank=True, related_name='tips', to='twee.PythonTipHashTag'),
        ),
        migrations.AddField(
            model_name='pythontip',
            name='tweeted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tips', to='twee.pythontiptweetuser', verbose_name='Tweeted by'),
        ),
        migrations.AddConstraint(
            model_name='pythontiplink',
            constraint=models.UniqueConstraint(fields=('tip', 'url'), name='unique_links'),
        ),
    ]
