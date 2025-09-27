package ejercicio4;

import java.util.HashMap;

public class Prueba {
    public static void main(String[] args) {
        // Crear domicilios
        Domicilio domicilio1 = new Domicilio("Matheu", 2343, "Ciudad X", "Provincia Y");
        Domicilio domicilio2 = new Domicilio("Colon", 5561, "Ciudad Z", "Provincia W");

        // Crear empleados departtamento mantenimiento
        Empleado empleado1 = new PermanenteIntermedio("Juan Perez", domicilio1, 7, 12000);
        Empleado empleado2 = new EmpleadoTemporal("Julio Garcia", domicilio2, 80, 160);
        Empleado empleado3 = new EmpleadoTemporal("Martin Rodriguuez", domicilio1, 70, 100);

        HashMap<String, Empleado> empleadosDeptoMant = new HashMap<String,Empleado>();
        empleadosDeptoMant.put(empleado1.getNombre(), empleado1);
        empleadosDeptoMant.put(empleado2.getNombre(), empleado2);
        empleadosDeptoMant.put(empleado3.getNombre(), empleado3);
        Departamento departamento = new Departamento("Mantenimiento", empleadosDeptoMant);

        // Crear empleados departamento de contabilidad

        Empleado empleado4 = new PermanenteExperto("Mara Anchorena", domicilio2, 18, 13000);
        Empleado empleado5 = new PermanentePrincipiante("Sandra Fernandez", domicilio1, 6, 11500);
        Empleado empleado6 = new PermanentePrincipiante("Luis Gomez", domicilio2, 2, 10500);
        Empleado empleado7 = new PermanenteIntermedio("Ana Lopez", domicilio1, 12, 12500);

        HashMap<String, Empleado> empleadosDeptoCont = new HashMap<String,Empleado>();
        empleadosDeptoCont.put(empleado4.getNombre(), empleado4);
        empleadosDeptoCont.put(empleado5.getNombre(), empleado5);
        empleadosDeptoCont.put(empleado6.getNombre(), empleado6);
        empleadosDeptoCont.put(empleado7.getNombre(), empleado7);
        Departamento departamento2 = new Departamento("Contabilidad", empleadosDeptoCont);

        // Crear empresa
        HashMap<String, Departamento> departamentosEmpresa = new HashMap<String,Departamento>();
        departamentosEmpresa.put(departamento.nombre, departamento);
        departamentosEmpresa.put(departamento2.nombre, departamento2);
        Empresa empresa = new Empresa("Mi Empresa", departamentosEmpresa);

//         Mostrar sueldos de los empleados en el departamento
        System.out.println("Sueldos en el departamento de " + departamento.nombre + ":");
        for (java.util.Map.Entry<String, Double> entry : departamento.sueldoEmpleados().entrySet()) {
            System.out.println(entry.getKey() + ": $" + entry.getValue());
        }
        System.out.println("Sueldos en el departamento de " + departamento2.nombre + ":");
        for (java.util.Map.Entry<String, Double> entry : departamento2.sueldoEmpleados().entrySet()) {
            System.out.println(entry.getKey() + ": $" + entry.getValue());
        }
    }
}
