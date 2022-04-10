import flask

app = flask.Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['EXPLAIN_TEMPLATE_LOADING'] = True


@app.route("/profile")
def get_profile():
    context ={
                'name': "Margareth Foster",
                'email': "margareth.foster@gmail.com",
                'role': "admin"
    }

    

    return flask.render_template("views/profile.html", context=context)


@app.route("/produto")
def get_products():
    context = [
            {
              "id": 1, 
              "name": "John Maddog Hall", 
              "desc": "Estoque unidade MADDOG", 
              "qtde": 1221, 
              "price": 13.50
            },
            {
                 "id": 1, 
                 "name": "Ada Lovelace", 
                 "desc": "Estoque unidade LOVELACE ", 
                 "qtde": 2341, 
                 "price": 23.50
            },
            {
                 "id": 1, 
                 "name": "Grace Hopper", 
                 "desc": "Estoque HOPPER", 
                 "qtde": 1242, 
                 "price": 34.50
            },

    ]

    return flask.render_template("views/product.html", context=context)


@app.route("/")
def get_teste():

    context = {
        "results": [ 
            {"name": "Usuários", "icon": "fas fa-user-circle fa-2x", "total": 8},
            {"name": "Valor do Estoque", "icon": "fas fa-dollar-sign fa-2x", "total": 200352},
            {"name": "Produtos", "icon": "fas fa-gift fa-2x", "total" : 8282},
        ],
        "table" : [
            {
              "id": 1, 
              "name": "John Maddog Hall", 
              "desc": "Estoque unidade MADDOG", 
              "qtde": 1221, 
              "price": 13.50
            },
            {
                 "id": 1, 
                 "name": "Ada Lovelace", 
                 "desc": "Estoque unidade LOVELACE ", 
                 "qtde": 2341, 
                 "price": 23.50
            },
            {
                 "id": 1, 
                 "name": "Grace Hopper", 
                 "desc": "Estoque HOPPER", 
                 "qtde": 1242, 
                 "price": 34.50
            },
            {
                 "id": 1, 
                 "name": "Linus Torvalds", 
                 "desc": "Estoque TORVALDS", 
                 "qtde": 4442, 
                 "price": 12.50
            },
        ]

    }


    return flask.render_template("views/index.html", context=context)




