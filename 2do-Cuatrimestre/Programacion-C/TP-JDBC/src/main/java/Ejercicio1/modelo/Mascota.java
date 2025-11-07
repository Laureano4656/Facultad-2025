package Ejercicio1.modelo;

import java.util.ArrayList;
import java.util.GregorianCalendar;

public class Mascota
{
    private int id;
    private String animal;
    private String nombre;
    private GregorianCalendar fechaNacimiento;
    private String historiaClinica;
    private ArrayList<PracticaVeterinaria> practicasVeterinarias;


    public Mascota(String animal, String nombre, GregorianCalendar fechaNacimiento, String historiaClinica)
    {
        this.animal = animal;
        this.nombre = nombre;
        this.fechaNacimiento = fechaNacimiento;
        this.historiaClinica = historiaClinica;
    }
    public String getNombre()
    {
        return nombre;
    }

    public ArrayList<PracticaVeterinaria> getPracticasVeterinarias()
    {
        return practicasVeterinarias;
    }

    public void setPracticasVeterinarias(ArrayList<PracticaVeterinaria> practicasVeterinarias)
    {
        this.practicasVeterinarias = practicasVeterinarias;
    }

    public String getHistoriaClinica()
    {
        return historiaClinica;
    }

    public void setHistoriaClinica(String historiaClinica)
    {
        this.historiaClinica = historiaClinica;
    }

    public GregorianCalendar getFechaNacimiento()
    {
        return fechaNacimiento;
    }

    public void setFechaNacimiento(GregorianCalendar fechaNacimiento)
    {
        this.fechaNacimiento = fechaNacimiento;
    }

    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }

    public int getId()
    {
        return id;
    }

    public void setId(int id)
    {
        this.id = id;
    }
}
