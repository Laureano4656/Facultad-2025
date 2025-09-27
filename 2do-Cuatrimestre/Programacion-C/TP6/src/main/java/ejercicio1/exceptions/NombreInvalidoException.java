package ejercicio1.exceptions;

public class NombreInvalidoException extends Exception {
    private String nombre;

    public NombreInvalidoException(String nombre)
    {
        super("El nombre es invalido: " + nombre);
        this.nombre = nombre;
    }
    public String getNombre() {
        return nombre;
    }
}
