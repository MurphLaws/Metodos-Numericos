# Metodo de las potencias

Los siguientes archivos son implementaciones del **Método de la Potencia** y **Método de la potencia inversa** en Python.

## Requisitos

Para la ejecucion de cada programa es necesario contar con **Python 3.7.3**; con la libreria 
**Numpy**, que agrega mayor soporte para trabajar con vectores y matrices, y con la libreria **Scipy**, que permite utilizar funciones para determinar la factorizacion LU o la inversa de una determinada matriz.

### 1. Metodo de La Potencia

Para ejecutar el archivo _potencias.py_, que corresponde a la implementacion del Computer Problem 4(a). Este archivo utiliza las distintas funciones sugeridas en el problema, para hallar el valor propio dominante y el vector propio asociado a ese valor para la matriz A y el el vector incial x:

``` 
    | 6 5 -5 |      | -1 |
A = | 2 6 -2 |, x = |  1 |
    | 2 5 -1 |      |  1 |
```
Los metodos utilizados son

<br />
<br />

**maxNoZero(v**) para retornar el mayor valor de un arreglo distinto de cero. Se usa para determinar la funcion phi utilizada en el metodo.  
```python
def maxNoZero(v):
    return max([x for x in v if x !=0])
```
<br />
<br />


**normaInfinito(v)** para determinar la norma infinito de un vector, es decir el valor absoluto del mayor elemento del arreglo.
```python
def normaInfinito(v):
    maxv: float
    maxv = v[0]
    for i in range(0, len(v)):
        if abs(v[i]) >= maxv:
            maxv = abs(v[i])
    return maxv
```

<br />
<br />


**normalizarVector(v)** para dividir todos los elementos de un arreglo por la norma infinito de este.
```python
def normalizarVector(v):
    w = [0]*len(v)
    for i in range(0, len(v)):
        w[i] = v[i] / normaInfinito(v)
    return w
```

<br />
<br />


**productoMatrizVector(m, v)** para multiplicar una matriz por un vector.
```python
def productoMatrizVector(m, v):
    rows = len(m)
    w = [0]*rows
    suma = 0
    for j in range(rows):
        mi = m[j]
        for i in range(len(v)):
            suma += mi[i]*v[i]
        w[j], suma = suma, 0

    return w
```
<br />
<br />


Y por ultimo, **metodoPotencias(A, x, M,)**, que utiliza todos los metodos vistos anteriormente y que recibe: una matriz A, a la que se le calculara su valor propio dominante y el vector asociado a este; un vector inicial x y un numero de iteraciones M.

```python
def metodoPotencias(A, x, M,):
    y = []
    r:  float
    r0: float
    i: int
    for i in range(0, M):
        print(i, ":")
        print("y =", y)
        print("x =", x)
        r0 = maxNoZero(x)
        y = productoMatrizVector(A, x)
        x = y
        r = maxNoZero(x)/r0
        x = normalizarVector(y)
        print("r =", r)

```
Para recrear los resultados obtenidos en Ejemplo 1, es necesaio invocar este metodo seleccionando A, x y M de la siguiente manera:

```
    | 6 5 -5 |      | -1 |
A = | 2 6 -2 |, x = |  1 |, M=28
    | 2 5 -1 |      |  1 |
    
```

### 2. Metodo de La Potencia Inversa

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo


## Authors

**Nicolas Lasso** - [MurphLaws](https://github.com/MurphLaws)



