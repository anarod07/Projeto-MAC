rota para página de artistas
@app.route('/artistas')
def artistas():
    return render_template("artistas.html")

#rota para página de discos
@app.route('/discos')
def discos():
    return render_template("discos.html")

#rota para página de login
@app.route('/login')
def login():
    return render_template("login.html")

#rota para página de quem somos
@app.route('/sobre-nós')
def sobre():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
