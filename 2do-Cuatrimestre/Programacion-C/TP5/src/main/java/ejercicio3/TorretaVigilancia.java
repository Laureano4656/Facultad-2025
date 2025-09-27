package ejercicio3;

import ejercicio3.interfaces.IHostil;

public class TorretaVigilancia extends Edificio implements IHostil {
    private static final int COSTO = 200;
    private static final double ENERGIA_INICIAL = 2000;
    private static final int TIEMPO_CONSTRUCCION = 40;
    private static final int DANIO = 10;

    public TorretaVigilancia(int x, int y, String equipo) {
        super(equipo, COSTO, ENERGIA_INICIAL, x, y, TIEMPO_CONSTRUCCION);
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
