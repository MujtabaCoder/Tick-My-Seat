# Generated by Django 4.2.8 on 2024-02-17 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cinema',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.cinema'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.format'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.language'),
        ),
    ]