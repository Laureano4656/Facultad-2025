package ejercicio6;

import java.util.HashMap;

public class ArchivoComprimido extends Entidad{
    private double factorCompresion;
    private HashMap<String,Entidad> contenido;

    public ArchivoComprimido(String nombre,  double factorCompresion, HashMap<String, Entidad> contenido) {
        super(nombre);
        this.factorCompresion = factorCompresion;
        this.contenido = contenido;
        super.setTamanio(this.calcTamanio());
    }

    @Override
    public int calcTamanio() {
        int total = 0;
        for (Entidad entidad : contenido.values()) {
            total += entidad.calcTamanio();
        }
        return (int)(total * factorCompresion);
    }
    @Override
    public String toString() {
        return "ArchivoComprimido{" +
                "factorCompresion=" + factorCompresion +
                ", contenido=" + contenido +
                '}';
    }
}
