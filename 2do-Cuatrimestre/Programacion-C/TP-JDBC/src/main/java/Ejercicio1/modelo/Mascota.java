package Ejercicio1.modelo;

import java.util.ArrayList;
import java.util.GregorianCalendar;

public class Mascota extends Animal
{
    private String nombre;
    private GregorianCalendar fechaNacimiento;
    private String historiaClinica;
    private ArrayList<PracticaVeterinaria> practicasVeterinarias;


    public Mascota(String raza, String especie, String nombre, GregorianCalendar fechaNacimiento, String historiaClinica)
    {
        super(raza, especie);
        this.nombre = nombre;
        this.fechaNacimiento = fechaNacimiento;
        this.historiaClinica = historiaClinica;
    }
    public String getNombre()
    {
        return nombre;
    }
}
