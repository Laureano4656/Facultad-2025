package ejercicio5;

public class Chofer {
    private Categoria categoria;
    private Domicilio domicilio;
    private Colectivo colectivo;
    private String nombre;

    public Chofer(Categoria categoria, Domicilio domicilio,Colectivo colectivo, String nombre) {
        this.categoria = categoria;
        this.domicilio = domicilio;
        this.colectivo = colectivo;
        this.nombre = nombre;
    }

    public void desvincularColectivo() {
        this.colectivo = null;
    }

    public Colectivo getColectivo() {
        return colectivo;
    }
    public void setColectivo(Colectivo colectivo) {
        this.colectivo = colectivo;
    }
    public Domicilio getDomicilio() {
        return domicilio;
    }

    public void setDomicilio(Domicilio domicilio) {
        this.domicilio = domicilio;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Categoria getCategoria() {
        return categoria;
    }

    public void setCategoria(Categoria categoria) {
        this.categoria = categoria;
    }
    @Override
    public String toString() {
        return "Chofer{" +
                "categoria=" + categoria +
                ", domicilio=" + domicilio +
                ", colectivo=" + colectivo +
                ", nombre='" + nombre + '\'' +
                '}';
    }
}
