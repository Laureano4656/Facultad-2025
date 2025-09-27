package ejercicio6;

public class CuentaCorriente extends Cuenta {
    private double limiteDescubierto;

    public CuentaCorriente(String titular, double limiteDescubierto) {
        super(titular);
        this.limiteDescubierto = limiteDescubierto;
    }

    @Override
    public boolean validarExtraccion(double cantidad) {
        return saldo + limiteDescubierto >= cantidad;
    }
    @Override
    public void extraccionRealizada(double cantidad) {
        // No additional actions needed for CuentaCorriente
    }
}
