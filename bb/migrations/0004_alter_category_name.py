# Generated by Django 4.0.3 on 2022-03-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb', '0003_alter_author_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('tanks', 'tanks'), ('hills', 'hills'), ('dd', 'dd'), ('merchants', 'merchants'), ('guildmasters', 'guildmasters'), ('questgivers', 'questgivers'), ('blacksmiths', 'blacksmiths'), ('tanners', 'tanners'), ('zelievars', 'zelievars'), ('spellmasters', 'spellmasters')], default='tanks', max_length=25, unique=True, verbose_name='Category'),
        ),
    ]
