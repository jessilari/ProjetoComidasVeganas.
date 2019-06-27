import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, StringField
from wtforms.validators import DataRequired, NumberRange
#from wtforms.fields.html5 import IntegerField
from wtforms.widgets.html5 import NumberInput
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Comida(db.Model):
    titulo =  db.Column(db.String(50), unique=True, primary_key=True)
    foto = db.Column(db.String(128), unique=True)
    preco = db.Column(db.Float)

@app.route('/', methods=['GET'])
def comidas():
    comidas=Comida.query.all()
    return render_template('comidas.html', comidas=comidas)

class Cadastro(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    foto = StringField('Foto', validators=[DataRequired()])
    preco = FloatField('Preco', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
    
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastrar():
    comidas=Comida.query.all()
    form = Cadastro()
    if form.validate_on_submit():
        p = Comida(titulo=form.titulo.data, foto=form.foto.data, preco=form.preco.data)
        db.session.add(p)
        db.session.commit()
        flash("Nova comida cadastrada")
    else:
        print("Erro")
    return render_template('cadastro.html', comidas=comidas, form=form)
    