package ejercicio1.exceptions;

public class ContrasenaInvalidaException extends Exception {
    private String contrasenia;

    public ContrasenaInvalidaException(String contrasenia) {
        super("La contrase��a no cumple con los requisitos de seguridad: " + contrasenia);
        this.contrasenia = contrasenia;
    }
    public String getContrasenia() {
        return contrasenia;
    }
}
