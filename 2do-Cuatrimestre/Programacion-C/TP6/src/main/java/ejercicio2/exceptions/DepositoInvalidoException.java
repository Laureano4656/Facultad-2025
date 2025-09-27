package ejercicio2.exceptions;

public class DepositoInvalidoException extends Exception {
    private double cantidadInvalida;

    public DepositoInvalidoException(double cantidadInvalida) {
        super("Deposito invalido");
        this.cantidadInvalida = cantidadInvalida;
    }
    public double getCantidadInvalida() {
        return cantidadInvalida;
    }
}
