package ejercicio4;

public class EmpleadoTemporal extends Empleado {
    private double valorHora;
    private int horasTrabajadas;

    public EmpleadoTemporal(String nombre, Domicilio domicilio, double valorHora, int horasTrabajadas) {
        super(nombre, domicilio);
        this.valorHora = valorHora;
        this.horasTrabajadas = horasTrabajadas;
    }

    @Override
    public double calcularSueldo() {
        return valorHora * horasTrabajadas;
    }
}
