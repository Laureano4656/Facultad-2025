package ejercicio4;

public abstract class Empleado {
    private String nombre;
    private static int actLegajo = 0;
    private int legajo;
    private Domicilio domicilio;

    public Empleado(String nombre, Domicilio domicilio) {
        this.nombre = nombre;
        this.domicilio = domicilio;
        this.legajo = actLegajo;
        actLegajo++;
    }
    public abstract double calcularSueldo();

    public String getNombre() {
        return nombre;
    }
    public int getLegajo() {
        return legajo;
    }

    public Domicilio getDomicilio() {
        return domicilio;
    }
}
