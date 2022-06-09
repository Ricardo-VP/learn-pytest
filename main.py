def suma(x, y):
    """
    Funcion que toma 2 argumentos y devuelve la suma de los mismos
    Args:
        x (int/float): Primer valor a sumar
        y (int/float): Segundo valor a sumar
    return: x+y
    """
    return x+y

def write(fpath, data_in):
    """"
    Funcion que escribe en un archivo
    Args:
        fpath: path absoluto del archivo
        data_in: informacion a escribir
    """
    with open(fpath, "w") as file_in:
        file_in.write(data_in)

class calculator:
    """
    Class calculator
    """
    def suma(x, y):
        """
        Funcion que toma 2 argumentos y devuelve la suma de los mismos
        Args:
            x (int/float): Primer valor a sumar
            y (int/float): Segundo valor a sumar
        return: x+y
        """
        return x+y
    