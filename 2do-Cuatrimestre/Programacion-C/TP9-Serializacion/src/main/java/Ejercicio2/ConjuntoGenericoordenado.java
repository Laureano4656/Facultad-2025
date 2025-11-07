package Ejercicio2;

import java.io.Serializable;
import java.util.TreeSet;

public class ConjuntoGenericoordenado<E extends Comparable & Serializable>
{
    private TreeSet<E> elementos;
    private long serialVersionUID;

    void agregarElemento(E elemento)
    {
        elementos.add(elemento);
    }
    public int cantidadElementos()
    {
        return elementos.size();
    }
    public void eliminarElemento(E elemento)
    {
        elementos.remove(elemento);
    }

}
