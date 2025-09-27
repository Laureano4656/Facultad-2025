package ejercicio4;

public class Camion extends Vehiculo {

    public Camion(String patente) {
        super(patente);
    }
    @Override
    public double calcularPrecio() {
        return (Vehiculo.getPrecioBase() + (Vehiculo.getPrecioBase()*0.4)) * this.getDiasAlquiler();
    }
}
