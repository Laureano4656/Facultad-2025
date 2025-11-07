package persistencia;

import java.io.Serializable;
import java.util.ArrayList;

import modelo.Asignatura;
import modelo.Profesor;

public class EscuelaDTO implements Serializable
{
    private ArrayList<ProfesorDTO> profesoresDTO = new ArrayList<ProfesorDTO>();
    private ArrayList<Asignatura> asignaturas = new ArrayList<Asignatura>();
    private String nombre;
    
    
    
    
    public ArrayList<ProfesorDTO> getProfesoresDTO()
    {
        return profesoresDTO;
    }
    public void setProfesoresDTO(ArrayList<ProfesorDTO> profesores)
    {
        this.profesoresDTO = profesores;
    }
    public ArrayList<Asignatura> getAsignaturas()
    {
        return asignaturas;
    }
    public void setAsignaturas(ArrayList<Asignatura> asignaturas)
    {
        this.asignaturas = asignaturas;
    }
    public String getNombre()
    {
        return nombre;
    }
    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }
    

}
