package ejercicio3;

import ejercicio3.interfaces.IConstruible;
import ejercicio3.interfaces.IPosicionable;

public abstract class Edificio extends Unidad implements IPosicionable, IConstruible {
    private int x;
    private int y;
    private int tiempoConstruccion;

    public Edificio(String equipo, int costo, double energia, int x, int y, int tiempoConstruccion) {
        super(equipo, costo, energia);
        this.x = x;
        this.y = y;
        this.tiempoConstruccion = tiempoConstruccion;
    }

    @Override
    public int getX() {
        return x;
    }

    @Override
    public int getY() {
        return y;
    }

    @Override
    public void getTiempoConstruccion() {
        System.out.println("Tiempo de construccion: " + tiempoConstruccion );
    }
}
