package Ejercicio6;

public class Donador implements Runnable
{
    private String nombre;
    private Libro libroAdonar;
    private Biblioteca biblioteca;
    public Donador(String nombre,Biblioteca biblioteca, Libro libroAdonar)
    {
        this.nombre = nombre;
        this.libroAdonar = libroAdonar;
        this.biblioteca = biblioteca;
    }
    @Override
    public void run(){
        System.out.println(nombre + " va a intentar donar el libro: " + libroAdonar.getIdLibro());
        biblioteca.donarLibro(this.libroAdonar);

    }

}
