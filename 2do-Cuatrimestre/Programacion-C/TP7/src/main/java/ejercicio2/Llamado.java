package ejercicio2;

import java.util.GregorianCalendar;

public class Llamado implements Comparable<Llamado>
{
    GregorianCalendar fechaHoraAtendido;
    GregorianCalendar fechaHoraSalida;
    int prioridad;
    Socio socio;

    public Llamado(int prioridad, Socio socio)
    {
        this.fechaHoraAtendido = new GregorianCalendar();
        this.fechaHoraSalida = null;
        this.prioridad = prioridad;
        this.socio = socio;
    }

    public GregorianCalendar getFechaHoraAtendido()
    {
        return fechaHoraAtendido;
    }

    public void setFechaHoraAtendido(GregorianCalendar fechaHoraAtendido)
    {
        this.fechaHoraAtendido = fechaHoraAtendido;
    }

    public GregorianCalendar getFechaHoraSalida()
    {
        return fechaHoraSalida;
    }

    public void setFechaHoraSalida(GregorianCalendar fechaHoraSalida)
    {
        this.fechaHoraSalida = fechaHoraSalida;
    }

    public int getPrioridad()
    {
        return prioridad;
    }

    public void setPrioridad(int prioridad)
    {
        this.prioridad = prioridad;
    }

    public Socio getSocio()
    {
        return socio;
    }

    public void setSocio(Socio socio)
    {
        this.socio = socio;
    }


    int compareTo(Object o){
        return Integer.compare(this.prioridad, l.prioridad);
    }
}
