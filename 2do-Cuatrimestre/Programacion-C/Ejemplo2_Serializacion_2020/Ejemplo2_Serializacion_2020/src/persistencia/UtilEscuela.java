package persistencia;

import java.util.ArrayList;

import modelo.Escuela;
import modelo.Profesor;

public class UtilEscuela
{
    public static EscuelaDTO escuelaDTOfromEscuela(Escuela escuela)
    {
	EscuelaDTO respuesta = new EscuelaDTO();
	respuesta.setNombre(escuela.getNombre());
	respuesta.setAsignaturas(escuela.getAsignaturas());
	ArrayList<ProfesorDTO> profesoresDTO = new ArrayList<ProfesorDTO>();
	for (int i = 0; i < escuela.getProfesores().size(); i++)
	    profesoresDTO.add(UtilEscuela.ProfesorDTOFromProfesor(escuela.getProfesores().get(i)));
	respuesta.setProfesoresDTO(profesoresDTO);
	return respuesta;
    }

    public static Escuela escuelaFromEscuelaDTO(EscuelaDTO eDTO)
    {

	Escuela escuela = new Escuela(eDTO.getNombre());
	for (int i = 0; i < eDTO.getAsignaturas().size(); i++)
	    escuela.agregarAsignatura(eDTO.getAsignaturas().get(i));

	for (int i = 0; i < eDTO.getProfesoresDTO().size(); i++)
	    escuela.agregaProfesor(UtilEscuela.profesorFromProfesorDTO(eDTO.getProfesoresDTO().get(i)));

	return escuela;

    }

    public static Profesor profesorFromProfesorDTO(ProfesorDTO pDTO)
    {
	Profesor respuesta = new Profesor(pDTO.getNombre(), pDTO.getFechaNacimiento(), pDTO.getAntiguedad(),
		pDTO.getAsignatura());
	return respuesta;
    }

    public static ProfesorDTO ProfesorDTOFromProfesor(Profesor profesor)
    {
	ProfesorDTO respuesta = new ProfesorDTO();
	respuesta.setNombre(profesor.getNombre());
	respuesta.setFechaNacimiento(profesor.getFechaNacimiento());
	respuesta.setAntiguedad(profesor.getAntiguedad());
	respuesta.setAsignatura(profesor.getAsignatura());

	return respuesta;
    }
}
