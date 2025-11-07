package modelo;

import java.io.IOException;
import java.io.Serializable;

import java.util.GregorianCalendar;


public class Profesor extends Persona 
{
    private int antiguedad;
    private Asignatura asignatura;
    
   
  
   
    public Profesor(String string, GregorianCalendar gregorianCalendar,int antiguedad,Asignatura asignatura)
    {
        super(string, gregorianCalendar);
        this.antiguedad=antiguedad;
        this.asignatura=asignatura;
    }

    

    public int getAntiguedad()
    {
        return antiguedad;
    }

  

    public Asignatura getAsignatura()
    {
        return asignatura;
    }

     @Override
    public String toString()
    {
        // TODO Implement this method
        return super.toString()+ " Antiguedad: "+
            this.antiguedad+"  "+this.asignatura;
    }
     
     
}
