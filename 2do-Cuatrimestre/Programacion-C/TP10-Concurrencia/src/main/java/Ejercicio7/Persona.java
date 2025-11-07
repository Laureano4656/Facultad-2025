package Ejercicio7;

public class Persona implements Runnable
{
    private String nombre;
    private Bote bote;
    private boolean destino;
    private boolean enDestino;

    public Persona(String nombre, Bote bote, boolean destino)
    {
        this.nombre = nombre;
        this.bote = bote;
        this.destino = destino; // true - Orilla derecha, false - Orilla izquierda
        this.enDestino = false;
    }

    @Override
    public void run()
    {
        System.out.println("La persona " + nombre + " quiere ir a la orilla " + (destino ? "derecha" : "izquierda") + ".");
        bote.subir(this);
        this.enDestino = true;


    }

    public String getNombre()
    {
        return nombre;
    }
    public boolean isEnDestino()
    {
        return enDestino;
    }
    public boolean getDestino()
    {
        return destino;
    }
}
