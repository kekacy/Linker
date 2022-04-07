# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import flash, redirect, url_for, render_template, request, session
from Linker import app, db
from Linker.forms import HelloForm,UsersForm
from Linker.models import Message,UsersData


@app.route('/index')
@app.route('/', methods=['GET', 'POST'])
def index():
    form = UsersForm()
    if 'logged_in' not in session:
        session['logged_in'] = False
        return redirect(url_for('login'))
    form2 = HelloForm()
    if session['logged_in']:
        if form2.validate_on_submit():
            name = form2.name.data
            body = form2.body.data
            message = Message(body=body, name=name)
            db.session.add(message)
            db.session.commit()
            flash('Your message have been sent to the world!')
            return redirect(url_for('index'))
        messages = Message.query.order_by(Message.timestamp.desc()).all()
        return render_template('index.html', form=form2, messages=messages)
    else:
        return redirect(url_for('login'))


@app.route('/motor')
def motor():
    form = UsersForm()
    if 'logged_in' not in session:
        session['logged_in'] = False
    if session['logged_in']:
        return render_template('motor.html')
    else:
        return redirect(url_for('index'))


@app.route('/server')
def server():
    form = UsersForm()
    if 'logged_in' not in session:
        session['logged_in'] = False
    if session['logged_in']:
        return render_template('servo.html')
    else:
        return redirect(url_for('index'))


@app.route('/others')
def other():
    form = UsersForm()
    if 'logged_in' not in session:
        session['logged_in'] = False
    if session['logged_in']:
        return render_template('other.html')
    else:
        return redirect(url_for('index'))


