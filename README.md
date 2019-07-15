Flasky
# ProjetoComidasVeganas
Aplicação comida vegana


# Instruções para execução

```
git clone https://github.com/edusantana/disk-bode
cd disk-bode
python3 -m venv venv
source venv/bin/activate
pip install flask flask-bootstrap flask-moment flask-wtf flask-sqlalchemy flask-migrate
```

Agora vamos adicionar valores ao banco de dados:

```python
flask shell
from app import db
db.create_all()

titulo = Comida(titulo= "colocamos o titulo da comida")
foto = Comida(foto= "colocamos o link da imagem")
preco = Comida(preco="colocamos o preco da comida")

db.session.add(titulo)
db.session.add(foto)
db.session.add(preco)
db.session.commit
# CTRL+D para sair
exit()
```

E executar a aplicação

```
export FLASK_APP=app.py
flask run -p 8080
```

# Sobre o livro

```
git clone https://github.com/miguelgrinberg/flasky.git
cd flasky
git checkout -f 4c
cd ..
```

# faz o de voces

```
git clone https://github.com/JessiLari/ProjetoComidasVeganas
cd ProjetoComidasVeganas

python3 -m venv venv
source venv/bin/activate
```
