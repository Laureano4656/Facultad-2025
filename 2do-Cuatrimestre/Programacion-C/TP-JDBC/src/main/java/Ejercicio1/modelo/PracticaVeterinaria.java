package Ejercicio1.modelo;

import java.util.GregorianCalendar;

public class PracticaVeterinaria
{
    private String descripcion;
    private GregorianCalendar fecha;
    private GregorianCalendar fechaVencimiento;
    private String comentarios;

    public PracticaVeterinaria(String descripcion, GregorianCalendar fecha, GregorianCalendar fechaVencimiento, String comentarios)
    {
        this.descripcion = descripcion;
        this.fecha = fecha;
        this.fechaVencimiento = fechaVencimiento;
        this.comentarios = comentarios;
    }

    public String getDescripcion()
    {
        return descripcion;
    }

}
