'''
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 27-06-2020
DESCRIPTION: Formulario HTML5, haciendo uso de Bulma y Web.py.
'''

import web

urls = [
    '/','mvc.controllers.formulario.Formulario' 
] # COLOCAMOS LA RUTA

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()