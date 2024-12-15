from flask import Flask
from database import init_db
from blueprints.disco_blueprint import disco_blueprint

app = Flask(_name_)

# Inicializando o banco de dados
init_db(app)

# Registrando o Blueprint
app.register_blueprint(disco_blueprint)

if _name_ == "_main_":
    app.run(debug=True)
