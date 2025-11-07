package Ejercicio1.incisoB;

import java.io.Serializable;

public class VehiculoDTO implements Serializable
{
    private String N_Cashis;
    private int anioFabricacion;

    public String getN_Cashis()
    {
        return N_Cashis;
    }

    public void setN_Cashis(String n_Cashis)
    {
        N_Cashis = n_Cashis;
    }

    public int getAnioFabricacion()
    {
        return anioFabricacion;
    }

    public void setAnioFabricacion(int anioFabricacion)
    {
        this.anioFabricacion = anioFabricacion;
    }
}
