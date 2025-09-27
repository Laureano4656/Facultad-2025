package ejercicio6;

public class Archivo extends Entidad{

    public Archivo(String nombre, int tamanio) {
        super(nombre,tamanio);
    }
    @Override
    public int calcTamanio() {
        return super.getTamanio();
    }
    @Override
    public String toString() {
        return "Archivo{" +
                "nombre=" + super.getNombre() +
                ", tamanio=" + super.getTamanio() +
                '}';
    }
}
