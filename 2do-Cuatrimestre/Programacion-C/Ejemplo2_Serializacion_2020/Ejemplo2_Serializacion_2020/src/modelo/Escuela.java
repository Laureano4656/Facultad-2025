package modelo;

import java.util.ArrayList;

public class Escuela 
{
    private ArrayList<Profesor> profesores = new ArrayList<Profesor>();
    private ArrayList<Asignatura> asignaturas = new ArrayList<Asignatura>();
    private String nombre;
    
    public Escuela(String nombre)
    {
	super();
	this.nombre = nombre;
    }

    public ArrayList<Asignatura> getAsignaturas()
    {
        return asignaturas;
    }

    public String getNombre()
    {
        return nombre;
    }

    public ArrayList<Profesor> getProfesores()
    {
        return profesores;
    }

    public void agregaProfesor(Profesor profesor)
    {
        this.profesores.add(profesor);
    }

    public void agregarAsignatura(Asignatura asignatura)
    {
        this.asignaturas.add(asignatura);

    }

    @Override
    public String toString()
    {
        return "Escuela: " +this.nombre+ "\nprofesores=" + profesores + "\nAsignaturas= " + asignaturas;
    }
    
}
