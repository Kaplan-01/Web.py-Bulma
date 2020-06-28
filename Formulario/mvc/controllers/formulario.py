'''
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 27-06-2020
DESCRIPTION: Formulario HTML5, haciendo uso de Bulma y Web.py.
'''

import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/")

class Formulario():
    
    def GET(self):
        try:
            return render.formulario() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.
