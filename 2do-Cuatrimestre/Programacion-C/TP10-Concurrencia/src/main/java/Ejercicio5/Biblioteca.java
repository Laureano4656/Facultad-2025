package Ejercicio5;

import java.util.Hashtable;

public class Biblioteca
{
    private static final int MAXLIBROS = 10;
    private Hashtable<Integer, Libro> libros;

    public Biblioteca()
    {
        this.libros = new Hashtable<Integer, Libro>();
    }
    public void agregarLibro(Libro libro)
    {
        this.libros.put(libro.getIdLibro(), libro);
    }

    public synchronized Libro obtenerLibro(int idLibro)
    {
        Libro libroBuscado = null;
        while ((libroBuscado = this.libros.get(idLibro) ) == null)
        {
            System.out.println("Libro con id = "+ idLibro +" NO encontrado");
            try
            {
                wait();
            }
            catch (InterruptedException e)
            {
                e.printStackTrace();
            }
        }
        this.libros.remove(idLibro);
        System.out.println(">>Libro con id = "+ idLibro +" encontrado");
        System.out.println("Se saco el libro con id = " + libroBuscado.getIdLibro() + " a la biblioteca, hay un total de " + this.libros.size() + " libros.");
        notifyAll();
        return libroBuscado;
    }

    public synchronized void donar(Libro libro)
    {
        while (this.libros.size() >= MAXLIBROS)
        {
            System.out.println("Biblioteca llena. Esperando para donar el libro con id = " + libro.getIdLibro());
            try
            {
                wait();
            }
            catch (InterruptedException e)
            {
                e.printStackTrace();
            }
        }
        System.out.println("Se ingreso el libro con id = " + libro.getIdLibro() + " a la biblioteca.");
        this.libros.put(libro.getIdLibro(), libro);
        notifyAll();
    }

    public synchronized void devolverLibro(Libro libro)
    {
        this.libros.put(libro.getIdLibro(), libro);
        System.out.println("<<Se devolvió el libro con id = " + libro.getIdLibro() + " a la biblioteca, hay un total de " + this.libros.size() + " libros.");
        notifyAll();
    }

    public int tamanio()
    {
        return this.libros.size();
    }

}
