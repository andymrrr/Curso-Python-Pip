import requests

def get_category():

    solicitud = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(solicitud.status_code)
    categorias = solicitud.json()

    for categoria in categorias:
        print(categoria['name'])
