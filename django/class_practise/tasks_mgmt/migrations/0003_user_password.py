from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks_mgmt", "0002_user_task_created_at_task_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(blank=True, default="", max_length=128),
        ),
    ]
