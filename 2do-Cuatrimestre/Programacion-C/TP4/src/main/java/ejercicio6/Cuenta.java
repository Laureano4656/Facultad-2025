package ejercicio6;

public abstract class Cuenta {
    protected String titular;
    protected double saldo;

    public Cuenta(String titular) {
        this.titular = titular;
        this.saldo = 0;
    }

    public String getTitular() {
        return titular;
    }

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double cantidad) {
        saldo += cantidad;
    }

    public abstract boolean validarExtraccion(double cantidad);

    public abstract void extraccionRealizada(double cantidad);

    public void extraer(double cantidad) {
        if (validarExtraccion(cantidad)) {
            this.saldo -= cantidad;
            extraccionRealizada(cantidad);
        }
    }
}
