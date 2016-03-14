from invoke import run, task


@task
def deploy(production=False):
    instance = 'primary' if production else 'staging'
    run('ec deploy --instance {instance}'.format(instance=instance))
    run('ec run --instance {instance} web -- python manage.py migrate'.format(instance=instance))


@task
def migrate(production=False):
    instance = 'primary' if production else 'staging'
    run('ec run --instance {instance} web -- python manage.py migrate'.format(instance=instance))


@task
def update_local_db():
    # run('dropdb -h localhost djangocon2015; createdb -h localhost djangocon2015 && gondor sqldump primary | ./manage.py dbshell')
    run('ec run db -- pg_dump --no-owner --no-acl > dump.sql')
