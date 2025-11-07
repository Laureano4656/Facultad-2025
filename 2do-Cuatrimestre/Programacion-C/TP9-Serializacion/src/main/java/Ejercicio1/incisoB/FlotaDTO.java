package Ejercicio1.incisoB;

import java.util.ArrayList;

public class FlotaDTO
{
    private String nombre;
    private ArrayList<AutomovilDTO> automoviles ;

    public String getNombre()
    {
        return nombre;
    }

    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }

    public ArrayList<AutomovilDTO> getAutomoviles()
    {
        return automoviles;
    }

    public void setAutomoviles(ArrayList<AutomovilDTO> automoviles)
    {
        this.automoviles = automoviles;
    }
}
