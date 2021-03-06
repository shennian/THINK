from flask import Flask, render_template, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    msg = TextField('Leave a Message', validators=[Required()])
    submit = SubmitField('submit')
    

app = Flask(__name__)
bootstrap = Bootstrap(app)


msgs = []
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        msg = form.msg.data
        flash('new message')
        msgs.append(msg)
    return render_template('index.html', form=form, msgs=msgs)
    
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
    
    
    
    
    
    
    
