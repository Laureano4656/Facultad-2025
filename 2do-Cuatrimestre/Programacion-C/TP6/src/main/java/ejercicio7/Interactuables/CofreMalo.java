package ejercicio7.Interactuables;

import ejercicio7.Hechizable;
import ejercicio7.Posicion;

public class CofreMalo extends Cofre {
    public CofreMalo(Posicion posicion) {
        super(posicion);
    }

    @Override
    public void abrir(Hechizable h) {
        h.serMaldito();
    }
}
