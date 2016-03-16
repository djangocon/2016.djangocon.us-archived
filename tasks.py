from invoke import run, task


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
def update_local_db():
    """Copy production database to local machine (testing only)."""

    # run('dropdb -h localhost djangocon2015; createdb -h localhost djangocon2015 && gondor sqldump primary | ./manage.py dbshell')
    run('ec run db -- pg_dump --no-owner --no-acl > dump.sql')
