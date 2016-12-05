# gbl_curso
Practicas de curso de Python



# Clase 1
  
### Emular Sets
Crear una clase para representar y manipular un Set (conjunto). La clase Set debe proveer las siguientes operaciones:


✓ Agregar un elemento al Set.  
✓ Remover un elemento del Set.  
✓ Diferencia entre un Set y otro Set.  
✓ Intersección entre un Set y otro Set.  
✓ Un método que determine si un Set está incluído en otro Set. Es decir, si todos los elementos de un Set pertenecen al otro Set.  
✓ Diferencia simétrica entre un Set y otro Set.  
✓ Producto cartesiano entre un Set y otro Set.
- Conjunto potencia de un Set.  


✓ Nota: recuerda que un Set no permite elementos duplicados, solo mantiene elementos únicos.
✓ Se puede definir un Set y sus elementos al momento de crear una instancia de la clase, como se muestra a continuación:
Set([1,2,3,4,5,6,1,4])
✓No usar el tipo 'set' ya incluído en el lenguaje en su implementación.  






### Cálculo Matricial  
Crear una clase que permita representar una matriz de cualquier orden o forma (n x n, n x m).
También debe permitir realizar las siguientes operaciones con matrices.


- Suma de matrices
- Producto de un escalar por una matriz
- Producto de matrices
- Traspuesta de una matriz
- Determinante de la matriz
- Matriz adjunta
- Matriz inversa


Agregar métodos adicionales:


- Un método para obtener una filas de una matriz. No devolver filas repetidas.
Por ejemplo, se puede indicar que se desean la filas 1, 3, 8 de una matriz de 20 x 10.


- Un método para obtener una columnas de una matriz. No devolver columnas repetidas.
Por ejemplo, se puede indicar que se desean las columnas 2, 4, 10 de una matriz de 20 x 10.


- Un método para obtener una parte de la matriz a partir de una columna cualquiera.
Por ejemplo de una matriz de 10 x 10, se quiere obtener la matriz de 10 x 2 a partir de la columna 5.


- Un método para mostrar en pantalla la matriz, en forma de matriz.


Se puede definir una matriz de 3 x 6 al momento de instanciar la clase como se muestra a continuación:
Matrix([[1,2,3,4,5,6],
	[10,11,12,13,14,15],
	[-1,-2,-3,-4,-5,-6]])


Referencia de Cálculo Matricial:
http://matematicasbachiller.com/videos/2-bachillerato/introduccion-al-algebra-de-lo-lineal/01-calculo-matricial-6
