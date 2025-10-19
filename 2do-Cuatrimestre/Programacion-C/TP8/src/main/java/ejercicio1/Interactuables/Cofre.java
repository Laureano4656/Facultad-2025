package ejercicio1.Interactuables;

import ejercicio1.Hechizable;
import ejercicio1.Posicion;
import ejercicio1.Posicionable;

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
