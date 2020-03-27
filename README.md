# Metodo de las potencias

Los siguientes archivos son implementaciones del **Método de la Potencia** y **Método de la potencia inversa** en Python.

## Requisitos

Para la ejecucion de cada programa es necesario contar con **Python 3.7.3**; con la libreria **Numpy**, que agrega mayor soporte para trabajar con vectores y matrices, y con la libreria **Scipy**, que permite utilizar funciones para determinar la factorizacion LU o la inversa de una determinada matriz.


### 1. Ejemplo 1

Se crea el archivo _potenciasEjemplo.py_, que corresponde a la implementacion del Computer Problem 1. Para este problema es necesario implementar el algoritmo del metodo de las potencias con el fin de observar el comportamiento de una matriz. Recordemos que este metodo se usa para determinar el valor propio dominante de una matriz, junto con su respectivo vector propio. Ahora, tenemos una matriz A y un vector inicial x tal que:

``` 
    | 6 5 -5 |      |  1 |
A = | 2 6 -2 |, x = |  2 |
    | 2 5 -1 |      |  3 |
```
El ejercicio pide que se ejecute el algoritmo con 100 iteraciones. Al hacerlo, se observa que alrededor de la iteracion numero 25 tanto el valor propio como el vector propio demuestran un aparente convergencia. Esto se aprecia en la siguiente imagen:

![1.1](https://github.com/MurphLaws/metodo-de-la-potencias/blob/master/Problema1/1.1.png)

Leugo, al observar las iteraciones finales del algoritmo, tanto el valor propio domiante como el vector incian una convergencia hacia valores distintos a los anteriores:

![1.2](https://github.com/MurphLaws/metodo-de-la-potencias/blob/master/Problema1/1.2.png)

Por ultimo, se corre el programa pero con 200 iteraciones, comprobando asi cuales son los valores finales que toman el valor y vector propios de la matriz:

![1.3](https://github.com/MurphLaws/metodo-de-la-potencias/blob/master/Problema1/1.3.png)

La explicacion de comportamiento se amplia en el pdf adjunto al archivo.

### 4. Metodo de La Potencia

Se crea el archivo _potencias.py_, que corresponde a la implementacion del Computer Problem 5.1.4(a). Este archivo utiliza las distintas funciones sugeridas en el problema, para hallar el valor propio dominante y el vector propio asociado a ese valor para la matriz A y el el vector incial x:

``` 
    | 6 5 -5 |      | -1 |
A = | 2 6 -2 |, x = |  1 |
    | 2 5 -1 |      |  1 |
```
Los metodos utilizados son:





**maxNoZero(v**) para retornar el mayor valor de un arreglo distinto de cero. Se usa para determinar la funcion phi utilizada en el metodo.  
```python
def maxNoZero(v):
    return max([x for x in v if x !=0])
```




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






**normalizarVector(v)** para dividir todos los elementos de un arreglo por la norma infinito de este.
```python
def normalizarVector(v):
    w = [0]*len(v)
    for i in range(0, len(v)):
        w[i] = v[i] / normaInfinito(v)
    return w
```



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
Para recrear los resultados obtenidos en Ejemplo 1, es necesario invocar este metodo seleccionando A, x y M de la siguiente manera:

```
    [[6, 5, -5],     
A =  [2, 6, -2],  x = [-1, 1 ,1], M=29
     [2, 5, -1]]    
    
                        
                        
```

La ejecucion resultante se puede ver en la siguiente imagen:
![4](https://github.com/MurphLaws/metodo-de-la-potencias/blob/master/Problema4/4.png)

### 5. Metodo de La Potencia Inverso

Se crea el archivo _potenciasInversas.py_, que corresponde a la implementacion del Computer Problem 5.1.5(a). Este archivo utiliza las mismos metodos usados en el problema anterior, la diferencia es que con este metodo se busca hallar el menor valor propio  y el vector propio asociado a ese valor para una matriz A con un vector inicial x. Ademas, este metodo utiliza la factorizacion LU de la matriz en su funcion principal:


```python
def metodoPotenciasInverso(A, x, M,):
    y = []
    r:  float
    r0: float
    i: int
    (P, L, U) = sla.lu(A)
    UInversa = sla.inv(U)
    LInversa = sla.inv(L)
    for i in range(0, M):
        print(i, ":")
        print("x =", np.around(x, 5))
        r0 = x[0]
        x = productoMatrizVector(UInversa, productoMatrizVector(LInversa, x))
        r = x[0]/r0
        x = normalizarVector(x)
        print("r =", r)

```

Para recrear los resultados obtenidos en Ejemplo 2, es necesario invocar este metodo seleccionando A, x y M de la siguiente manera:

```
    [[6, 5, -5],     
A =  [2, 6, -2],  x = [-3, 7 ,13], M=12
     [2, 5, -1]]   
    
```
La ejecucion resultante se puede ver en la siguiente imagen:
![5](https://github.com/MurphLaws/metodo-de-la-potencias/blob/master/Problema5/5.png)

## Autor

**Nicolas Lasso** - [MurphLaws](https://github.com/MurphLaws)



