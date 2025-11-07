package persistencia;

import java.io.Serializable;
import java.util.GregorianCalendar;

import modelo.Asignatura;

public class ProfesorDTO extends PersonaDTO
{
    private int antiguedad;
    private Asignatura asignatura;
    
    
    
    public int getAntiguedad()
    {
        return antiguedad;
    }
    public void setAntiguedad(int antiguedad)
    {
        this.antiguedad = antiguedad;
    }
    public Asignatura getAsignatura()
    {
        return asignatura;
    }
    public void setAsignatura(Asignatura asignatura)
    {
        this.asignatura = asignatura;
    }
    
    
    
}
