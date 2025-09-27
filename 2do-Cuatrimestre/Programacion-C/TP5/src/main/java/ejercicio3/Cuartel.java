package ejercicio3;

public class Cuartel extends Edificio{
    private static final int COSTO = 500;
    private static final double ENERGIA_INICIAL = 3000;
    private static final int TIEMPO_CONSTRUCCION = 60;

    public Cuartel(int x, int y, String equipo) {
        super(equipo, COSTO, ENERGIA_INICIAL, x, y, TIEMPO_CONSTRUCCION);

    }
    @Override
    public void recibeDanio(int danio) {
        double energiaRestante = getEnergia() - danio*0.5;
        this.setEnergia(energiaRestante);
    }
}
