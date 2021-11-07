import datos as dt

class Interpretacion:
    '''
    Clase para obtener información de un conjunto de Datos
    '''

    def __init__(self, datos):
        '''
        Constructor de la clase Interpretacion, que trabaja con los datos para dar una explicacion sencilla de la situacion actual.

        Argumentos:
            - datos: Lista de datos sobre los que se trabaja 
        '''
        self.contenedor_datos = list(datos)
 
    def leer_datos(self,fichero_leer):
        '''
        Metodo para leer y almacenar los datos de un fichero para trabajar con ellos
        '''
        lineas = []
        with open(fichero_leer, "r") as fichero:
            lineas = fichero.readlines()

        lineas.pop(0)
        for linea in lineas:
            aux = linea.split(",")
            fecha = aux[0]
            ccaa = aux[2]
            casos = int(aux[3])+int(aux[4])+int(aux[5])+int(aux[6])+int(aux[7])+int(aux[7])

            self.contenedor_datos.append(dt.Datos(fecha, ccaa, casos))
        

    def generar_interpretacion(self,com_auto,fecha):
        ''' Metodo para crear una interpretacion a partir del contenedor de datos 
        se puede filtrar dicha interpretacion por comunidad autonoma y
        fecha. Si no se desea contar con alguno de esos atributos, 
        se marca como cadena vacia "" '''
        indice = -1
        for i in range(0,len(self.contenedor_datos)):
            if self.contenedor_datos[i].com_autonoma == com_auto and self.contenedor_datos[i].fecha == fecha:
                indice = i
                break
        
        if indice >= 0:
            num_dias = 14
            total_casos = 0

            indice_inicio = max(indice-num_dias, 0)

            for i in range(indice_inicio, indice):
                total_casos = total_casos + self.contenedor_datos[i].num_casos

            if total_casos < 500:
                print("Vamos bien")
            else:
                print("No vamos bien")
        else:
            print("No se ha encontrado la comunidad autonoma o fecha indicadas")
                      