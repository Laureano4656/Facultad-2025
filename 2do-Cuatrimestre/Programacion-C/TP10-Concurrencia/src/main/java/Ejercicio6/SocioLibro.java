package Ejercicio6;

public class SocioLibro implements Runnable
{
    private String nombre;
    private Biblioteca biblioteca;


    public SocioLibro(String nombre, Biblioteca biblioteca)
    {
        this.nombre = nombre;
        this.biblioteca = biblioteca;
    }

    @Override
    public void run()
    {
        int idLibro = (int) (Math.random() * biblioteca.tamanioLibros()) + 1;
        System.out.println("El socio " + nombre + " quiere leer el libro de id  '" + idLibro + "'.");
        Libro libro = biblioteca.obtenerLibro(idLibro);
        int tiempoLectura = (int) (Math.random() * 5000) + 1000;
        System.out.println("El socio " + nombre + " está leyendo el libro con ID " + libro.getIdLibro() + " durante " + tiempoLectura + " ms.");
        try
        {
            Thread.sleep(tiempoLectura);
        } catch (InterruptedException e)
        {
            e.printStackTrace();
        }
        this.biblioteca.devolverLibro(libro);
        int tiempoEspera = (int) (Math.random() * 3000) + 1000;
        System.out.println("El socio " + nombre + " ha terminado de leer y esperará " + tiempoEspera + " ms antes retirar otro.");
        try{
            Thread.sleep(tiempoEspera);
        } catch (InterruptedException e)
        {
            e.printStackTrace();
        }
    }
}
