
import six
from crontab import CronTab


def update_cron_command(command, period="daily"):

    """update backend jobs"""

    cron = CronTab(user=True)
    cron.remove_all()
    job = cron.new(command=command)
    if period == "hourly":
        job.minute.on(0)
        job.hour.during(0, 23)
    elif period == "weekly":
        job.minute.on(0)
        job.hour.on(0)
        job.dow.on(1)
    else:
        job.minute.on(0)
        job.hour.on(0)
    job.enable()
    cron.write()
    return cron.render()