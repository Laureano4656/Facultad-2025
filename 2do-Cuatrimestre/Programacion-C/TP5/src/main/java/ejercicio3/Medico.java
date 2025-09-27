package ejercicio3;

public class Medico extends Personaje {
    private static final int COSTO = 40;
    private static final int ENERGIA_INICIAL = 100;

    public Medico(int x, int y, String equipo) {
        super(equipo, COSTO, ENERGIA_INICIAL, x, y);
    }

    @Override
    public void recibeDanio(int danio) {
        double energiaRestante = getEnergia() - danio * 1.5;
        this.setEnergia(energiaRestante);
    }
}
