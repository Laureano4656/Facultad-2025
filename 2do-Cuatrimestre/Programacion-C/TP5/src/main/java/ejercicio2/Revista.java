package ejercicio2;

public class Revista extends Producto{
    private int edicion;

    public Revista(int codigo, String titulo, int anioPublicacion, int edicion) {
        super(codigo, titulo, anioPublicacion);
        this.edicion = edicion;
    }
    public int getEdicion() {
        return edicion;
    }
    public void setEdicion(int edicion) {
        this.edicion = edicion;
    }

    @Override
    public String toString() {
        return "Revista{" +
                "edicion=" + edicion + super.toString() +
                '}';
    }
}
