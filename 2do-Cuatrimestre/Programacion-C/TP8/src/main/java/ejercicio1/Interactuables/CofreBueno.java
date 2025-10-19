package ejercicio1.Interactuables;

import ejercicio1.Hechizable;
import ejercicio1.Posicion;

public class CofreBueno extends Cofre {
    public CofreBueno(Posicion posicion) {
        super(posicion);
    }

    @Override
    public void abrir(Hechizable h) {
        h.serBendecido();
    }
}
