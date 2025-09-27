package ejercicio3;

import ejercicio3.interfaces.IHostil;

public class Soldado extends Personaje implements IHostil {
    private static final int COSTO = 100;
    private static final int ENERGIA_INICIAL = 500;
    private static final int DANIO = 50;

    public Soldado(int x, int y, String equipo) {
        super(equipo, COSTO, ENERGIA_INICIAL, x, y);
    }
    @Override
    public void recibeDanio(int danio) {
        double energiaRestante = getEnergia() - danio;
        this.setEnergia(energiaRestante);
    }
    @Override
    public void atacar(Unidad objetivo) {
        objetivo.recibeDanio(DANIO);
    }
}
