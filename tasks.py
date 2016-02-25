from invoke import run, task


@task
def deploy_develop_to_develop():
    run('gondor deploy develop develop')


@task
def deploy_master_to_develop():
    run('gondor deploy develop master')


@task
def deploy_production():
    run('gondor deploy primary master')


@task
def update_develop_db():
    run('gondor manage develop database:copy primary')


@task
def update_local_db():
    run('dropdb -h localhost djangocon2015; createdb -h localhost djangocon2015 && gondor sqldump primary | ./manage.py dbshell')
