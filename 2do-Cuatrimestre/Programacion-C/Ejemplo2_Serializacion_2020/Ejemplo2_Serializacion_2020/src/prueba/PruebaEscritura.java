package prueba;

import java.io.IOException;

import java.util.ArrayList;
import java.util.GregorianCalendar;

import modelo.Asignatura;
import modelo.Escuela;
import modelo.Profesor;
import persistencia.EscuelaDTO;
import persistencia.IPersistencia;
import persistencia.PersistenciaBIN;
import persistencia.PersistenciaXML;
import persistencia.UtilEscuela;

public class PruebaEscritura
{


    public static void main(String[] args)
    {
       IPersistencia persistencia = new PersistenciaXML();
       // IPersistencia persistencia = new PersistenciaBIN();
        Escuela escuela = new Escuela("Escuela Media N 134");
        escuela.agregarAsignatura(new Asignatura("Lengua", 101));
        escuela.agregarAsignatura(new Asignatura("Matematica", 202));
        escuela.agregarAsignatura(new Asignatura("Geografia", 3000));
        ArrayList<Asignatura> materias = escuela.getAsignaturas();
        escuela.agregaProfesor(new Profesor("Carlos", new GregorianCalendar(1980, 0, 2), 0, materias.get(0)));
        escuela.agregaProfesor(new Profesor("Carolina", new GregorianCalendar(1969, 1, 11), 10, materias.get(1)));
        escuela.agregaProfesor(new Profesor("Guillermo", new GregorianCalendar(1976, 1, 5), 23, materias.get(1)));
        escuela.agregaProfesor(new Profesor("Valeria", new GregorianCalendar(1980, 0, 5), 10, materias.get(1)));
       
       
        try
        {
            persistencia.abrirOutput("Escuelita.xml");
            System.out.println("Crea archivo escritura");
            EscuelaDTO edto=UtilEscuela.escuelaDTOfromEscuela(escuela);
            
            persistencia.escribir(edto);
            
            
            System.out.println("Escuela grabada exitosamente");
            persistencia.cerrarOutput();
            System.out.println("Archivo cerrado");
        } catch (IOException e)
        {
            // TODO Auto-generated catch block
            System.out.println(e.getLocalizedMessage());
        }

    }
}
