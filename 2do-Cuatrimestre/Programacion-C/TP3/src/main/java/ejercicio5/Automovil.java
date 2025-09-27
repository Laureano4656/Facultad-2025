package ejercicio5;

public abstract class Automovil {
    private String patente;
    private double velocidad;
    private double velocidadMaxima;
    private int marcha;

    public Automovil(String patente, double velocidadMaxima) {
        this.patente = patente;
        this.velocidadMaxima = velocidadMaxima;
        this.velocidad = 0;
        this.marcha = 0;
    }
    public Automovil(String patente) {
        this(patente, 160); // Velocidad maxima por defecto
    }

    public abstract void acelerar(double velocidad);

    public abstract void frenar(double velocidad);

    public String getPatente() {
        return patente;
    }
    public double getVelocidad() {
        return velocidad;
    }
    public void setVelocidad(double velocidad) {
        this.velocidad = velocidad;
    }
    public double getVelocidadMaxima() {
        return velocidadMaxima;
    }
    public void setMarcha(int marcha) {
        this.marcha = marcha;
    }
    public int getMarcha() {
        return marcha;
    }
}
