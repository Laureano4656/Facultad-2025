package ejercicio4;

public abstract class Vehiculo {
    private String patente;
    private static double precioBase = 500;
    private int diasAlquiler;

    public Vehiculo(String patente) {
        this.patente = patente;
        this.diasAlquiler = 0;
    }
    public Vehiculo(String patente, int diasAlquiler) {
        this.patente = patente;
        this.diasAlquiler = diasAlquiler;
    }
    public int getDiasAlquiler() {
        return diasAlquiler;
    }
    public void setDiasAlquiler(int diasAlquiler) {
        this.diasAlquiler = diasAlquiler;
    }
    public String getPatente() {
        return patente;
    }
    public static double getPrecioBase() {
        return precioBase;
    }
    public static void setPrecioBase(double precioBase) {
        Vehiculo.precioBase = precioBase;
    }
    public void setPatente(String patente) {
        this.patente = patente;
    }
    public abstract double calcularPrecio() throws Exception;
}
