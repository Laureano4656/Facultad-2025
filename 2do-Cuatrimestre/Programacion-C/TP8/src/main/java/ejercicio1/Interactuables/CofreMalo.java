package ejercicio1.Interactuables;

import ejercicio1.Hechizable;
import ejercicio1.Posicion;

public class CofreMalo extends Cofre {
    public CofreMalo(Posicion posicion) {
        super(posicion);
    }

    @Override
    public void abrir(Hechizable h) {
        h.serMaldito();
    }
}
