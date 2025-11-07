package Ejercicio1.incisoB;

import java.io.Serializable;

public abstract class Vehiculo
{
    private String N_Cashis;
    private int anioFabricacion;

    public Vehiculo(String n_Cashis, int anioFabricacion)
    {
        N_Cashis = n_Cashis;
        this.anioFabricacion = anioFabricacion;
    }

    public String getN_Cashis()
    {
        return N_Cashis;
    }

    public int getAnioFabricacion()
    {
        return anioFabricacion;
    }
}
