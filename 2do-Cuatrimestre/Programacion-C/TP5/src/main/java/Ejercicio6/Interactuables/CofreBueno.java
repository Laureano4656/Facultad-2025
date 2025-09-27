package Ejercicio6.Interactuables;

import Ejercicio6.Hechizable;
import Ejercicio6.Posicion;

public class CofreBueno extends Cofre {
    public CofreBueno(Posicion posicion) {
        super(posicion);
    }

    @Override
    public void abrir(Hechizable h) {
        h.serBendecido();
    }
}
