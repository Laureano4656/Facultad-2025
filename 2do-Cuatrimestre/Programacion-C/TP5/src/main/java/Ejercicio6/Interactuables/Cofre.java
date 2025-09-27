package Ejercicio6.Interactuables;

import Ejercicio6.Hechizable;
import Ejercicio6.Posicion;
import Ejercicio6.Posicionable;

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
