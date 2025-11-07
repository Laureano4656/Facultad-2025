package Ejercicio1.incisoB;

import java.io.Serializable;
import java.util.ArrayList;

public class Flota implements Serializable
{
    private String nombre;
    private ArrayList<Automovil> automoviles ;


    public Flota(String nombre, ArrayList<Automovil> automoviles)
    {
        this.nombre = nombre;
        this.automoviles = automoviles;
    }

    public String getNombre()
    {
        return nombre;
    }

    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }

    public ArrayList<Automovil> getAutomoviles()
    {
        return automoviles;
    }

    public void setAutomoviles(ArrayList<Automovil> automoviles)
    {
        this.automoviles = automoviles;
    }
}
