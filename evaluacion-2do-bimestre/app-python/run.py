"""
"""

def listar_medidores():
    import requests 
    """ """
    print("Listar medidores")
    r = requests.get("http://127.0.0.1:8070/api/medidores/", auth=('fjsaca', '123456'))
    print(r.content, "\n")

def crear_medidor():
    """ """
    import requests 
    print("crear medidor")
    r = requests.post('http://127.0.0.1:8070/api/medidores/', data = {'marca':'http://127.0.0.1:8070/api/marcas/1/', 'costoMedidor':'11.0', 'origen':'Ecuador', 'cliente': 'http://127.0.0.1:8070/api/clientes/1/', 'direccion': 'Loja', 'parroquia': 'Sucre' }, auth=('fjsaca', '123456'))
    print(r.content)

def editar_medidor():
    """ """
    import requests 
    print("editar medidor")
    r = requests.put('http://127.0.0.1:8070/api/medidores/2/', data = {'marca':'http://127.0.0.1:8070/api/marcas/1/', 'costoMedidor':'15.0', 'origen':'Ecuador', 'cliente': 'http://127.0.0.1:8070/api/clientes/1/', 'direccion': 'Loja', 'parroquia': 'Sucre' }, auth=('fjsaca', '123456'))
    print(r.content)

def eliminar_medidor():
    """ """
    print("eliminar medidor")
    import requests 
    r = requests.delete('http://127.0.0.1:8070/api/medidores/2/', auth=('fjsaca', '123456'))
    print("Eliminado")
    


if __name__ == '__main__':
    bandera = True
    
    while(bandera):
        print("""Opciones:\n
                1) Listar Medidores\n
                2) Crear Medidor\n
                3) Editar Medidor\n
                4) Eliminar Medidor\n""")

        opcion = int(input("Ingrese opción  :"))

        if opcion==1:
            listar_medidores()
        elif opcion==2:
            crear_medidor()
        elif opcion==3:
            editar_medidor()
        elif opcion==4:
            eliminar_medidor()
        elif opcion<1 and opcion>4:
            print("opción invalida")

        continuar = input("Ingrese la letra Y para continuar :")

        if continuar != "Y":
            bandera = False
            

