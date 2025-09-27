package ejercicio3.exception;

public class TipoCombustibleInvalidoException extends CargaInvalidaException {

    public TipoCombustibleInvalidoException(double cantidadDisponible, double capacidadMaxima, String combustible) {
        super(new DatoCargaInvalido(cantidadDisponible, capacidadMaxima, combustible));
    }

}
