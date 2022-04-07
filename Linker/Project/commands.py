# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import click

from Linker import app, db
from Linker.models import Message,UsersData


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
@click.option('--count', default=30, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""
    from faker import Faker
    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('Created %d fake messages.' % count)

@app.cli.command()
def adduser():
    click.echo('请输入用户名')
    username = input()
    click.echo('请输入密码')
    password = input()
    click.echo('输入邮箱')
    email = input()
    User1 = UsersData(
        username = username,
        password = password,
        email = email
    )
    db.session.add(User1)
    db.session.commit()
    click.echo('Created %s succeeded'% User1.username)

@app.cli.command()
def da():
    db.drop_all()
    click.echo('finish')

@app.cli.command()
def ca():
    db.create_all()
    click.echo('finish')