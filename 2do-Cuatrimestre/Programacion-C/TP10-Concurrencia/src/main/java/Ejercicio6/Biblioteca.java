package Ejercicio6;

import java.util.Hashtable;

public class Biblioteca
{
    private static final int MAXLIBROS = 10;
    private Hashtable<Integer, Libro> libros;
    private Hashtable<Integer, Revista> revistas;

    public Biblioteca()
    {
        this.libros = new Hashtable<Integer, Libro>();
        this.revistas = new Hashtable<Integer, Revista>();
    }

    public void agregarLibro(Libro libro)
    {
        this.libros.put(libro.getIdLibro(), libro);
    }

    public void agregarRevista(Revista revista)
    {
        this.revistas.put(revista.getIdrevista(), revista);
    }

    public Libro obtenerLibro(int idLibro)
    {
        synchronized (this.libros)
        {
            Libro libroBuscado = null;
            while ((libroBuscado = this.libros.get(idLibro)) == null)
            {
                System.out.println("Libro con id = " + idLibro + " NO encontrado");
                try
                {
                    this.libros.wait();
                } catch (InterruptedException e)
                {
                    e.printStackTrace();
                }
            }
            this.libros.remove(idLibro);
            System.out.println(">>Libro con id = " + idLibro + " encontrado");
            System.out.println("Se saco el libro con id = " + libroBuscado.getIdLibro() + " a la biblioteca, hay un total de " + this.libros.size() + " libros.");
            this.libros.notifyAll();
            return libroBuscado;
        }
    }

    public void donarLibro(Libro libro)
    {
        synchronized (this.libros)
        {
            while (this.libros.size() >= MAXLIBROS)
            {
                System.out.println("Biblioteca llena. Esperando para donar el libro con id = " + libro.getIdLibro());
                try
                {
                    this.libros.wait();
                } catch (InterruptedException e)
                {
                    e.printStackTrace();
                }
            }
            System.out.println("Se ingreso el libro con id = " + libro.getIdLibro() + " a la biblioteca.");
            this.libros.put(libro.getIdLibro(), libro);
            this.libros.notifyAll();
        }
    }

    public void devolverLibro(Libro libro)
    {
        synchronized (this.libros)
        {
            this.libros.put(libro.getIdLibro(), libro);
            System.out.println("<<Se devolvió el libro con id = " + libro.getIdLibro() + " a la biblioteca, hay un total de " + this.libros.size() + " libros.");
            this.libros.notifyAll();
        }
    }

    public Revista obtenerRevista(int idRevista)
    {
        synchronized (this.revistas)
        {
            Revista revistaBuscada = null;
            while ((revistaBuscada = this.revistas.get(idRevista)) == null)
            {
                System.out.println("Revista con id = " + idRevista + " NO encontrado");
                try
                {
                    this.revistas.wait();
                } catch (InterruptedException e)
                {
                    e.printStackTrace();
                }
            }
            this.revistas.remove(idRevista);
            System.out.println(">>Revista con id = " + idRevista + " encontrado");
            System.out.println("Se saco la revista con id = " + revistaBuscada.getIdrevista() + " a la biblioteca, hay un total de " + this.revistas.size() + " revistas.");
            this.revistas.notifyAll();
            return revistaBuscada;
        }
    }

    public void devolverRevista(Revista revista)
    {
        synchronized (this.revistas)
        {
            this.revistas.put(revista.getIdrevista(), revista);
            System.out.println("<<Se devolvió la revista con id = " + revista.getIdrevista() + " a la biblioteca, hay un total de " + this.revistas.size() + " revistas.");
            this.revistas.notifyAll();
        }
    }

    public int tamanioLibros()
    {
        return this.libros.size();
    }
    public int tamanioRevistas()
    {
        return this.revistas.size();
    }
}
