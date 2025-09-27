package ejercicio3.exception;

public class DatoCargaInvalido {
    private double cantidadDisponible;
    private double cantidadRequerida;
    private String combustible;

    public DatoCargaInvalido(double cantidadDisponible, double cantidadRequerida, String combustible) {
        this.cantidadDisponible = cantidadDisponible;
        this.cantidadRequerida = cantidadRequerida;
        this.combustible = combustible;
    }
    public double getCantidadDisponible() {
        return this.cantidadDisponible;
    }
    public double getCapacidadMaxima() {
        return this.cantidadRequerida;
    }
    public String getCombustible() {
        return this.combustible;
    }
}
