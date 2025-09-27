package ejercicio3.exception;

public class FaltaCombustibleException extends CargaInvalidaException {

    public FaltaCombustibleException(double cantidadDisponible, double capacidadMaxima, String combustible)
    {
        super(new DatoCargaInvalido(cantidadDisponible, capacidadMaxima, combustible));

    }

}
