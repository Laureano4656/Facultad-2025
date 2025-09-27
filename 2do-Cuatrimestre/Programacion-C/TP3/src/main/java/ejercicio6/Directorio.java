package ejercicio6;

import java.util.HashMap;

public class Directorio extends Entidad{
    private HashMap<String,Entidad> contenido;

    public Directorio(String nombre) {
        super(nombre,0);
        this.contenido = new HashMap<>();
    }
    public Directorio(String nombre, int tamanio,HashMap<String,Entidad> contenido) {
        super(nombre,tamanio);
        this.contenido = contenido;
    }
    public void addContenido(Entidad entidad) {
        this.contenido.put(entidad.getNombre(), entidad);
        super.setTamanio(this.calcTamanio());
    }
    public void removeContenido(String nombre) {
        this.contenido.remove(nombre);
        super.setTamanio(this.calcTamanio());
    }
    public HashMap<String, Entidad> getContenido() {
        return contenido;
    }
    public void ListContenido() {
        System.out.println("Contenido del directorio "+super.getNombre()+":");
        for (String key : contenido.keySet()) {
            System.out.println("- "+key+" (tamaño: "+contenido.get(key).calcTamanio()+")");
        }
    }
    @Override
    protected int calcTamanio() {
        int total = 0;
        for (Entidad entidad : contenido.values()) {
            total += entidad.calcTamanio();
        }
        return total;
    }

    @Override
    public String toString() {
        return "Directorio{" +
                "contenido=" + contenido +
                '}';
    }
}
