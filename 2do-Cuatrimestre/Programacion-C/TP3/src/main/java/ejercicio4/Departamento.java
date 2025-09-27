package ejercicio4;

import java.util.HashMap;

public class Departamento {
    String nombre;
    HashMap<String, Empleado> empleados;

    public Departamento(String nombre, HashMap<String, Empleado> empleados) {
        this.nombre = nombre;
        this.empleados = empleados;
    }

    public void agregarEmpleado(Empleado empleado) {
        empleados.put(empleado.getNombre(), empleado);
    }
    public void eliminarEmpleado(Empleado empleado) {
        empleados.remove(empleado.getNombre());
    }

    public HashMap<String,Double> sueldoEmpleados() {
        HashMap<String,Double> sueldosEmpleados = new HashMap<>();
        for (Empleado empleado : empleados.values()) {
            sueldosEmpleados.put(empleado.getNombre(), empleado.calcularSueldo());
        }
        return sueldosEmpleados;
    }
}
