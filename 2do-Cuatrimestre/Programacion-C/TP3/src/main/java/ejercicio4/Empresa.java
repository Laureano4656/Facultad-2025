package ejercicio4;

import java.util.HashMap;

public class Empresa {
    private String nombre;
    private HashMap<String,Departamento> departamentos;

    public Empresa(String nombre, HashMap<String, Departamento> departamentos) {
        this.nombre = nombre;
        this.departamentos = departamentos;
    }
    public void agregarDepartamento(Departamento departamento) {
        departamentos.put(departamento.nombre, departamento);
    }
    public void eliminarDepartamento(Departamento departamento) {
        departamentos.remove(departamento.nombre);
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}
