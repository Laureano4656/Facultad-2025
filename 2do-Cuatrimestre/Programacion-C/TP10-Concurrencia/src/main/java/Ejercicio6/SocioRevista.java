package Ejercicio6;

public class SocioRevista implements Runnable
{
    private String nombre;
    private Biblioteca biblioteca;


    public SocioRevista(String nombre, Biblioteca biblioteca)
    {
        this.nombre = nombre;
        this.biblioteca = biblioteca;
    }

    @Override
    public void run()
    {
        int idRevista = (int) (Math.random() * biblioteca.tamanioRevistas()) + 1;
        System.out.println("El socio " + nombre + " quiere leer la revista de id  '" + idRevista + "'.");
        Revista revista = biblioteca.obtenerRevista(idRevista);
        int tiempoLectura = (int) (Math.random() * 5000) + 1000;
        System.out.println("El socio " + nombre + " está leyendo el revista con ID " + revista.getIdrevista() + " durante " + tiempoLectura + " ms.");
        try
        {
            Thread.sleep(tiempoLectura);
        } catch (InterruptedException e)
        {
            e.printStackTrace();
        }
        this.biblioteca.devolverRevista(revista);
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
