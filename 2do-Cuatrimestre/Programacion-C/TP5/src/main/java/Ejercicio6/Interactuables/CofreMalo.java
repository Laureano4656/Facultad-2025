package Ejercicio6.Interactuables;

import Ejercicio6.Hechizable;
import Ejercicio6.Posicion;

public class CofreMalo extends Cofre {
    public CofreMalo(Posicion posicion) {
        super(posicion);
    }

    @Override
    public void abrir(Hechizable h) {
        h.serMaldito();
    }
}
