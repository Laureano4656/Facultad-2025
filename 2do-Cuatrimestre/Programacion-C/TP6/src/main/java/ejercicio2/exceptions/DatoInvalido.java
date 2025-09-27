package ejercicio2.exceptions;

public class DatoInvalido {
    private double extraccion_solicitada;
    double saldo;

    public DatoInvalido(double extraccion_solicitada, double saldo) {
        this.extraccion_solicitada = extraccion_solicitada;
        this.saldo = saldo;
    }
    public double getExtraccion_solicitada() {
        return extraccion_solicitada;
    }
    public double getSaldo() {
        return saldo;
    }
}
