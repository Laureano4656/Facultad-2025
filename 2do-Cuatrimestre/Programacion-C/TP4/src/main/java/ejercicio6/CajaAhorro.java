package ejercicio6;

public class CajaAhorro extends Cuenta {
    private int extraccionesMensuales;
    private static final int LIMITE_EXTRACCIONES = 5;

    public CajaAhorro(String titular) {
        super(titular);
        this.extraccionesMensuales = 0;
    }
    @Override
    public boolean validarExtraccion(double cantidad) {
        return saldo >= cantidad && extraccionesMensuales < LIMITE_EXTRACCIONES;
    }
    @Override
    public void extraccionRealizada(double cantidad) {
        extraccionesMensuales++;
    }
}
