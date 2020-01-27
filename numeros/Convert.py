""" Modulo de numeros arabigos y romanos """

__docformat__ = "restructuredtext"  
class numerosConvert:
    _DIC_ROMANOS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    _LISTA_VALORES = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    _LISTA_ROMANOS = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    def __init__(self):
        ''' Clase para convertir entre numeros romanos y arabigos '''
        pass

    def romano_a_arabigo(self, numeroRomano):
        """ romano_a_arabigo  
        ======
        funcion que recibe un numero romano y regresa un arabigo \n
        Parametros: \n
            * :param p:numeroRomano 
            """
        # inicializamos nuestro resultado
        resultado = 0

        # por cada numero en el str recibido hago una iteracion
        for romanoIndex in range(0, len(numeroRomano)):

            # si mi indice de busqueda es el 0 ó el valor en:
            # busco en la posision n el numero romano,
            # busco su valor en mi diccionaro de romanos
            # si el valor es menor o igual al valor -1 del mismo
            # esto para validar su jerarquia
            if romanoIndex == 0 or self._DIC_ROMANOS[numeroRomano[romanoIndex]] <= self._DIC_ROMANOS[numeroRomano[romanoIndex - 1]]:
                # a mi resultado le sumo el valor en del indice n de mi numero romano en mi diccionario
                resultado += self._DIC_ROMANOS[numeroRomano[romanoIndex]]
            else:
                # a mi resultado le sumo el valor de mi numero que esta en el indice rel recivido - 2 y lo multiplico por el valor en del indice n de mi numero romano en mi diccionario
                # de esta manera evito duplicidad del valor
                resultado += self._DIC_ROMANOS[numeroRomano[romanoIndex]] - 2 * self._DIC_ROMANOS[numeroRomano[romanoIndex - 1]]
        return resultado
    
    def arabigo_a_romano(self, numeroArabigo):
        ''' funcion que recibe un numero arabigo y regresa un numero romano '''
        resultado = ''

        # recorro el tamano de mi lista de valores
        for valorIndex in range(len(self._LISTA_VALORES)):
            # mientras el valor de mi numero recibido sea mayor
            # o igual al que se encuentra en mi indice de la lista
            while numeroArabigo >= self._LISTA_VALORES[valorIndex]:
                # 
                numeroArabigo -= self._LISTA_VALORES[valorIndex]
                resultado += self._LISTA_ROMANOS[valorIndex]
        return resultado