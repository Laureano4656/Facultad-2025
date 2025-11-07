package prueba;

import java.io.IOException;
import java.util.ArrayList;

import modelo.Escuela;
import modelo.Profesor;
import persistencia.EscuelaDTO;
import persistencia.IPersistencia;
import persistencia.PersistenciaXML;
import persistencia.UtilEscuela;

public class PruebaLectura
{
    public static void main(String[] args)
    {
        IPersistencia persistencia = new PersistenciaXML();
        //IPersistencia persistencia = new PersistenciaBIN();
        Escuela escuela = null;
        try
        {
            persistencia.abrirInput("Escuelita.xml");
            System.out.println("Archivo abierto");
            EscuelaDTO edto=(EscuelaDTO) persistencia.leer();
            escuela = UtilEscuela.escuelaFromEscuelaDTO(edto);
 
            System.out.println("Escuela recuperada");
            persistencia.cerrarInput();
            System.out.println("Archivo cerado");
        } catch (IOException e)
        {
            // TODO Auto-generated catch block
            System.out.println(e.getMessage());
        } catch (ClassNotFoundException e)
        {
            // TODO Auto-generated catch block
            System.out.println(e.getMessage());
        }

        System.out.println(escuela);
        ArrayList<Profesor> profesores = escuela.getProfesores();
        System.out.println("Verificando relaciones de agregacion: ");
        System.out.println(profesores.get(1).getAsignatura() == profesores.get(2).getAsignatura());
        System.out.println(profesores.get(1).getAsignatura() == profesores.get(3).getAsignatura());
        System.out.println(profesores.get(1).getAsignatura() == profesores.get(0).getAsignatura());

    }
}
