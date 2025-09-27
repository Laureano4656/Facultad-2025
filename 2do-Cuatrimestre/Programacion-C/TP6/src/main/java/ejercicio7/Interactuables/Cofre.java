package ejercicio7.Interactuables;

import ejercicio7.Hechizable;
import ejercicio7.Posicion;
import ejercicio7.Posicionable;

public abstract class Cofre implements Posicionable {

    private Posicion posicion;
    public Cofre(Posicion posicion) {
        this.posicion = posicion;
    }

    public abstract void abrir(Hechizable h);

    @Override
    public Posicion getPosicion() {
        return posicion;
    }
    @Override
    public void setPosicion(Posicion p) {
        this.posicion = p;
    }
}
