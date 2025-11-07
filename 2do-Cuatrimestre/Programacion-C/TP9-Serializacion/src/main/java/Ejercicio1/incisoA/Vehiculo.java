package Ejercicio1.incisoA;

import java.io.Serializable;

public class Vehiculo implements Serializable
{
    private String N_Cashis;
    private int anioFabricacion;

    public void setN_Cashis(String n_Cashis)
    {
        N_Cashis = n_Cashis;
    }

    public void setAnioFabricacion(int anioFabricacion)
    {
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
