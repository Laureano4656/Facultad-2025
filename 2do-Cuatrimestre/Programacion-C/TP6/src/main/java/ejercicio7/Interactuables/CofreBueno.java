package ejercicio7.Interactuables;

import ejercicio7.Hechizable;
import ejercicio7.Posicion;

public class CofreBueno extends Cofre {
    public CofreBueno(Posicion posicion) {
        super(posicion);
    }

    @Override
    public void abrir(Hechizable h) {
        h.serBendecido();
    }
}
