package modelo;

import java.text.SimpleDateFormat;
import java.util.GregorianCalendar;

public class Persona
{
    private static SimpleDateFormat formato = new SimpleDateFormat("dd MMMMMMMMM yyyy");
    private String nombre;
    private GregorianCalendar fechaNacimiento;

    public Persona(String nombre, GregorianCalendar fechaNacimiento)
    {
	this.nombre = nombre;
	this.fechaNacimiento = fechaNacimiento;
    }

    

    public String getNombre()
    {
	return nombre;
    }

    
    public GregorianCalendar getFechaNacimiento()
    {
	return fechaNacimiento;
    }

    @Override
    public String toString()
    {
	// TODO Implement this method
	return "Nombre: " + this.nombre + " fecha de nacimiento: "
		+ Persona.formato.format(this.fechaNacimiento.getTime());
    }

}
