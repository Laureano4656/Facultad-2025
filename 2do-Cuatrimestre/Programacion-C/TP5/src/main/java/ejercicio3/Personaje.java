package ejercicio3;

import ejercicio3.interfaces.IMovible;
import ejercicio3.interfaces.IPosicionable;

public abstract class Personaje extends Unidad implements IPosicionable, IMovible {
    private int x;
    private int y;

    public Personaje(String equipo, int costo, int energia, int x, int y) {
        super(equipo, costo, energia);
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    @Override
    public void mover(int x, int y) {
        this.x = x;
        this.y = y;
        System.out.println("El personaje se ha movido a la posición (" + x + ", " + y + ")");
    }
}
