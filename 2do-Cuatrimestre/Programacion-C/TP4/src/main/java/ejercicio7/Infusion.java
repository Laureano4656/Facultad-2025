package ejercicio7;

public abstract class Infusion {
    private String nombre;
    private double precio;

    public Infusion(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }
    public void calentarAgua() {
        System.out.println("Calentando agua...");
    }
    public void agregarTipoInfusion() {
        System.out.println("Agregando " + nombre + "...");
    }
    public void tomarBebida() {
        System.out.println("Tomando bebida");
    }
    public abstract void endulzar();
    public void preparar() {
        calentarAgua();
        agregarTipoInfusion();
        endulzar();
    }
}
