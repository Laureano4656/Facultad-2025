package ejercicio1;

import ejercicio1.exceptions.ContrasenaInvalidaException;
import ejercicio1.exceptions.NombreInvalidoException;

public class Usuario {
    String nombre;
    String contrasenia;

    public Usuario(String nombre, String contrasenia) {
        this.nombre = nombre;
        this.contrasenia = contrasenia;
    }
    public String getNombre() {
        return nombre;
    }
    public String getContrasenia() {
        return contrasenia;
    }
    public void setNombre(String nombre) throws NombreInvalidoException {
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new NombreInvalidoException(nombre);
        }
        this.nombre = nombre;
    }
    public void setContrasenia(String contrasenia) throws ContrasenaInvalidaException {
        if (contrasenia == null || contrasenia.length() < 6 || (contrasenia.trim().isEmpty()) || !(Character.isLetter(contrasenia.charAt(0)))) {
            throw new ContrasenaInvalidaException(contrasenia);
        }
        this.contrasenia = contrasenia;
    }
}
