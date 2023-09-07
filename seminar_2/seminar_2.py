from flask import Flask, redirect, session, render_template, url_for, request

app = Flask(__name__)
app.secret_key = '37c6e1b6c4721d8c99867277b54872270df9838eeef833a28c67ac2f23906f03'


@app.route('/', methods=['GET', 'POST'])
def main():
    context = {
        'title': 'Главная страница',
    }
    if 'name' in session:
        context['name'] = session['name']
        return render_template('main.html', **context)
    else:
        return redirect(url_for('form'))



@app.route('/task_1')
def task_1():
    context = {
        'title': 'Задача №1',
        'task': ['Создать страницу, на которой будет форма для ввода имени и электронной почты',
                 'При отправке которой будет создан cookie файл с данными пользователя',
                 'Также будет произведено перенаправление на страницу приветствия, где будет \
                 отображаться имя пользователя.',
                 'На странице приветствия должна быть кнопка "Выйти"'
                 'При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление \
                 на страницу ввода имени и электронной почты.']
    }
    return render_template('task-1.html', **context)


@app.route('/form/', methods=['GET', 'POST'])
def form():
    context = {
        'title': 'Форма для POST запроса',
    }

    if request.method == 'POST':
        session['name'] = request.form.get('name') or 'NoName'
        session['email'] = request.form.get('email') or 'NoEmail'
        return redirect(url_for('main'))
    return render_template('form.html', **context)


@app.route('/logout/')
def logout():
    session.pop('name', None)
    session.pop('mail', None)
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
