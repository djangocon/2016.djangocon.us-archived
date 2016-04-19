from invoke import run, task


@task
def create_feature_flags(production=False):
    """Creates/updates feature flags and switches."""

    instance = 'primary' if production else 'staging'
    run('ec run --instance {instance} web -- python manage.py flag double_blind_reviews --create --superuser'.format(instance=instance))
    run('ec run --instance {instance} web -- python manage.py switch homepage_sponsorship_list off --create'.format(instance=instance))


@task
def deploy(production=False):
    """Deploy code to staging or primary (production)."""

    instance = 'primary' if production else 'staging'
    run('ec deploy --instance {instance}'.format(instance=instance))


@task
def migrate(production=False):
    """Migrate staging or primary (production) database."""

    instance = 'primary' if production else 'staging'
    run('ec run --instance {instance} web -- python manage.py migrate'.format(instance=instance))


@task
def push():
    """Push development and master branches to github."""

    run('git push origin development')
    run('git push origin master')


@task
def restart(production=False):
    """Restart staging or primary (production) database."""

    instance = 'primary' if production else 'staging'
    run('ec services restart --instance {instance} web'.format(instance=instance))


@task
def update_local_db(production=False):
    """Copy production database to local machine (for testing only)."""

    instance = 'primary' if production else 'staging'
    run('dropdb -h localhost djangocon2016; createdb -h localhost djangocon2016 && ec run --instance {instance} db -- pg_dump --no-owner --no-acl | ./manage.py dbshell'.format(instance=instance))
