package persistencia;

import java.io.Serializable;
import java.util.GregorianCalendar;

public class PersonaDTO implements Serializable
{
	private String nombre;
    private GregorianCalendar fechaNacimiento;
	
    
    public String getNombre()
	{
		return nombre;
	}
	public void setNombre(String nombre)
	{
		this.nombre = nombre;
	}
	public GregorianCalendar getFechaNacimiento()
	{
		return fechaNacimiento;
	}
	public void setFechaNacimiento(GregorianCalendar fechaNacimiento)
	{
		this.fechaNacimiento = fechaNacimiento;
	}
    
    
    
}
