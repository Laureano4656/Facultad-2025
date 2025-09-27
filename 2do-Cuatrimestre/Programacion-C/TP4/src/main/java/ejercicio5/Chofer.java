package ejercicio5;

public class Chofer {
    private String nombre;
    private Categoria categoria;
    private Vehiculo vehiculoAsignado;

    public Chofer(String nombre, Categoria categoria) {
        this.nombre = nombre;
        this.categoria = categoria;
        this.vehiculoAsignado = null;
    }
    public boolean asignarVehiculo(Vehiculo vehiculo) {
        if (vehiculo.aceptoChofer(this)) {
            this.vehiculoAsignado = vehiculo;
            return true;
        }
        return false;
    }
    public Vehiculo getVehiculoAsignado() {
        return vehiculoAsignado;
    }
    public Categoria getCategoria() {
        return categoria;
    }
    public void desasignarVehiculo() {
        this.vehiculoAsignado = null;
    }
    @Override
    public String toString() {
        return "Chofer{" +
                "nombre='" + nombre + '\'' +
                ", categoria=" + categoria +
                ", vehiculoAsignado=" + (vehiculoAsignado != null ? vehiculoAsignado : "Ninguno") +
                '}';
    }
}
