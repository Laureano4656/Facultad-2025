package Ejercicio1.persistencia;

import java.util.GregorianCalendar;

public class PracticaVeterinariaDTO
{
    private String descripcion;
    private GregorianCalendar fecha;
    private GregorianCalendar fechaVencimiento;
    private String comentarios;
    private int idMascota;

    public String getDescripcion()
    {
        return descripcion;
    }

    public void setDescripcion(String descripcion)
    {
        this.descripcion = descripcion;
    }

    public GregorianCalendar getFecha()
    {
        return fecha;
    }

    public void setFecha(GregorianCalendar fecha)
    {
        this.fecha = fecha;
    }

    public GregorianCalendar getFechaVencimiento()
    {
        return fechaVencimiento;
    }

    public void setFechaVencimiento(GregorianCalendar fechaVencimiento)
    {
        this.fechaVencimiento = fechaVencimiento;
    }

    public String getComentarios()
    {
        return comentarios;
    }

    public void setComentarios(String comentarios)
    {
        this.comentarios = comentarios;
    }

    public int getIdMascota()
    {
        return idMascota;
    }

    public void setIdMascota(int idMascota)
    {
        this.idMascota = idMascota;
    }
}
