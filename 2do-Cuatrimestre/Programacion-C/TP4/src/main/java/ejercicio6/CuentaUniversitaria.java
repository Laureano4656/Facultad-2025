package ejercicio6;

public class CuentaUniversitaria extends Cuenta {
    private static final double limiteExtraccion = 1000.0;
    private double saldoExtraido;
    public CuentaUniversitaria(String titular) {
        super(titular);
        this.saldoExtraido = 0;
    }
    @Override
    public boolean validarExtraccion(double cantidad) {
        return saldo >= cantidad && (saldoExtraido + cantidad) <= limiteExtraccion;
    }
    @Override
    public void extraccionRealizada(double cantidad) {
        saldoExtraido += cantidad;
    }
}
