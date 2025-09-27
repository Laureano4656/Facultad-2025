package ejercicio4;

public class EmpleadoPermanente extends Empleado {
    private int antiguedad;
    private double sueldoBase;

    public EmpleadoPermanente(String nombre, Domicilio domicilio, int antiguedad, double sueldoBase) {
        super(nombre, domicilio);
        this.antiguedad = antiguedad;
        this.sueldoBase = sueldoBase;
    }
    public int getAntiguedad() {
        return antiguedad;
    }
    public double getSueldoBase() {
        return sueldoBase;
    }
    @Override
    public double calcularSueldo() {
        return sueldoBase - (sueldoBase * 0.11) - (sueldoBase * 0.06);
    }
}
