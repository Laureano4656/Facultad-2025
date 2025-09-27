package ejercicio3.exception;

public class CargaInvalidaException extends Exception {
    DatoCargaInvalido datoCargaInvalido;
    public CargaInvalidaException(DatoCargaInvalido datoCargaInvalido) {
        super("Carga inválida: " + datoCargaInvalido.getCombustible() + " litros. La cantidad debe ser positiva y no exceder la capacidad máxima.");
        this.datoCargaInvalido = datoCargaInvalido;
    }
    public DatoCargaInvalido getDatoCargaInvalido() {
        return this.datoCargaInvalido;
    }
}
