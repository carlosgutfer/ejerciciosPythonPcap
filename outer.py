def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())
 Devuelve el valor que hay dentro de la función inner que está dentro de la función