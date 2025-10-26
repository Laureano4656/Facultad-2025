package Ejercicio1;

public class EstadoObservado
{
    private boolean jugando;
    private boolean tieneHambre;
    private boolean tieneSed;
    private String nombre;

    public EstadoObservado(String nombre)
    {
        this.nombre = nombre;
    }

    public String getNombre()
    {
        return nombre;
    }

    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }

    public EstadoObservado()
    {
        this.jugando = false;
        this.tieneHambre = false;
        this.tieneSed = false;
    }

    public boolean isJugando()
    {
        return jugando;
    }

    public void setJugando(boolean jugando)
    {
        this.jugando = jugando;
    }

    public boolean isTieneHambre()
    {
        return tieneHambre;
    }

    public void setTieneHambre(boolean tieneHambre)
    {
        this.tieneHambre = tieneHambre;
    }

    public boolean isTieneSed()
    {
        return tieneSed;
    }

    public void setTieneSed(boolean tieneSed)
    {
        this.tieneSed = tieneSed;
    }
}
