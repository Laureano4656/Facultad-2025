package Ejercicio1.persistencia;

import java.sql.Date;
import java.util.GregorianCalendar;

public class MascotaDTO
{
    private int id;
    private String nombre;
    private Date fechaNacimiento;
    private String historiaClinica;
    private int idCliente;
    private String animal;

    public String getAnimal()
    {
        return animal;
    }

    public void setAnimal(String animal)
    {
        this.animal = animal;
    }

    public int getId()
    {
        return id;
    }

    public void setId(int id)
    {
        this.id = id;
    }

    public String getNombre()
    {
        return nombre;
    }

    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }

    public Date getFechaNacimiento()
    {
        return fechaNacimiento;
    }

    public void setFechaNacimiento(Date fechaNacimiento)
    {
        this.fechaNacimiento = fechaNacimiento;
    }

    public String getHistoriaClinica()
    {
        return historiaClinica;
    }

    public void setHistoriaClinica(String historiaClinica)
    {
        this.historiaClinica = historiaClinica;
    }

    public int getIdCliente()
    {
        return idCliente;
    }

    public void setIdCliente(int idCliente)
    {
        this.idCliente = idCliente;
    }
}
