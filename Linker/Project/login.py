from flask import render_template,request,flash,redirect,url_for,session
from Linker import app,db
from Linker.forms import UsersForm
from Linker import bootstrap
from Linker.models import UsersData 


@app.route('/login',methods=['GET','POST'])
def login():
    form = UsersForm()
    if session['logged_in']:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            query_register = request.form.get('register')
            query_logon = request.form.get('logon')
            query_database = UsersData.query.get(username)
            if query_logon:
                if query_database:
                    if password == query_database.password:
                        flash('登录成功')
                        session['logged_in'] = True
                        return redirect(url_for('index'))
                    else:
                        flash('密码错误')
                else:
                    flash('用户不存在')

            if query_register:
                query_database = UsersData.query.get(username)
                if query_database:
                    flash('用户名已存在')
                else:
                    users = UsersData(
                        username = username,
                        password = password,
                        email = '222'
                    )
                    db.session.add(users)
                    db.session.commit()
                    flash('注册成功')
        return render_template('login.html',form=form)


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))