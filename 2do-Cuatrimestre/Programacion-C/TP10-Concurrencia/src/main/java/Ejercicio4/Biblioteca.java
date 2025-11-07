package Ejercicio4;

import java.util.Hashtable;

public class Biblioteca
{
    private Hashtable<Integer, Libro> libros;

    public Biblioteca()
    {
        this.libros = new Hashtable<Integer, Libro>();
    }
    public void agregarLibro(Libro libro)
    {
        this.libros.put(libro.getIdLibro(), libro);
        System.out.println("Se ha donado el libro: " + libro.getIdLibro());
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
        System.out.println("Libro con id = "+ idLibro +" encontrado");
        return libroBuscado;
    }

    public synchronized void devolverLibro(Libro libro)
    {
        this.libros.put(libro.getIdLibro(), libro);
        notifyAll();
    }

    public int tamanio()
    {
        return this.libros.size();
    }
    public void mostrarLibros()
    {
        for (Libro libro : this.libros.values())
        {
            System.out.println("ID: " + libro.getIdLibro() + ", Título: " + libro.getTitulo());
        }
    }
    public Libro getLibro(int idLibro)
    {
        return this.libros.get(idLibro);
    }
}
