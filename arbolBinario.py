class Nodo():
    #Creacion del objeto NODO
    def __init__(self, dato):

        self.dato = dato
        self.derecha = None
        self.izquierda = None

class Arbol():
    #Creacion del objeto Arbol
    def __init__(self):

        self.root = None
    
    #Variables privadas
    #Metodo para agregar un nodo al arbol
    def _add(self,nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._add(nodo.izquierda, dato)
        elif dato > nodo.dato:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._add(nodo.derecha, dato)
        else:
            print(f'El elemento {dato} ya estaba en el arbol.')

    #Metodo para imprimir en recorrido inorden
    def _inorden(self,nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(nodo.dato, end=' ')
            self._inorden(nodo.derecha)
    
    #Metodo para imprimir en recorrido preorden
    def _preorden(self,nodo):
        if nodo is not None:
            print(nodo.dato, end=' ')
            self._preorden(nodo.izquierda)
            self._preorden(nodo.derecha)
    
    #Metodo para imprimir en recorrido postorden
    def _postorden(self, nodo):
        if nodo is not None:
            self._postorden(nodo.izquierda)
            self._postorden(nodo.derecha)
            print(nodo.dato, end=' ')
        
    #Metodo para conocer el ancentro
    def _ancestro(self,nodo,busqueda):
        if nodo is None:
            return False
        elif nodo.dato == busqueda:
            return True
        elif (self._ancestro(nodo.izquierda, busqueda) or self._ancestro(nodo.derecha,busqueda)):
            print(nodo.dato)

    #Metodo para mostrar la RAIZ del arbol
    def _head(self,nodo):
        if nodo is not None:
            print(f'El nodo raiz del arbol es {nodo.dato}')
        else:
            print('El arbol no contiene ninguna raiz, por lo tanto esta vacio!')

    #Metodo de busqueda
    def _search(self,nodo,busqueda):
        if nodo is None:
            return None
        elif nodo.dato == busqueda:
            return nodo
        elif busqueda < nodo.dato:
            return self._search(nodo.izquierda, busqueda)
        elif busqueda > nodo.dato:
            return self._search(nodo.derecha, busqueda)

    #Metodo GET para el hijo derecho
    def _getRightChild(self, nodo, dato):
        if nodo.derecha is None:
            return None
        elif dato == nodo.dato:
            return print('El hijo derecho es: ', nodo.derecha.dato) 
        elif dato > nodo.dato:
            self._getRightChild(nodo.derecha, dato)
        else:
            print('no tiene hijo derecho')
    
    #Metodo GET para el hijo izquierdo
    def _getLeftChild(self, nodo, dato):
        if nodo.izquierda is None:
            return print('no tiene descendiente izquierdo')
        elif dato == nodo.dato:
            return print('El hijo izquierdo es: ',nodo.izquierda.dato) 
        elif dato < nodo.dato:
            self._getLeftChild(nodo.izquierda,dato)
        else:
            print('no tiene hijo izquierdo')

    #Variables publicas

    def add(self, dato):
        if not self.root:
            self.root = Nodo(dato)
        else:
            self._add(self.root, dato)

    def inorden(self):
        print('Imprimiendo árbol inorden: ')
        self._inorden(self.root)
        print('')

    def preorden(self):
        print('Imprimiendo árbol preorden: ')
        self._preorden(self.root)
        print('')
    
    def postoden(self):
        print('Imprimiendo árbol postorden: ')
        self._postorden(self.root)
        print('')
    
    def getRightChild(self, dato):
        self._getRightChild(self.root, dato)
    
    def getLeftChild(self,dato):
        self._getLeftChild(self.root, dato)

    def buscar(self,busqueda):
        return self._search(self.root, busqueda)

    def ancestro (self,busqueda):
        self._ancestro(self.root,busqueda)
    
    def head(self):
        self._head(self.root)

