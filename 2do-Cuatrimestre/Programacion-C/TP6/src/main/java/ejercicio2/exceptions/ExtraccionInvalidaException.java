package ejercicio2.exceptions;

public class ExtraccionInvalidaException extends Exception {
    DatoInvalido dato;
    public ExtraccionInvalidaException(DatoInvalido dato)
    {
        super("Extraccion invalida");
        this.dato = dato;
    }
}
