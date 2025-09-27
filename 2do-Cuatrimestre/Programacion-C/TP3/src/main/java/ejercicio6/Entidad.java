package ejercicio6;

import java.util.GregorianCalendar;

public abstract class Entidad {
    private String nombre;
    private GregorianCalendar fechaCreacion;
    private GregorianCalendar fechaActualizacion;
    private int tamanio;

    public Entidad(String nombre, int tamanio) {
        this.tamanio = tamanio;
        this.nombre = nombre;
        this.fechaCreacion = new GregorianCalendar();
        this.fechaActualizacion = new GregorianCalendar();
    }
    public Entidad(String nombre) {
        this(nombre,0);
    }
    protected abstract int calcTamanio();

    public String getNombre() {
        return nombre;
    }
    public int getTamanio() {
        return tamanio;
    }
    public void setTamanio(int tamanio) {
        this.tamanio = tamanio;
    }
}
