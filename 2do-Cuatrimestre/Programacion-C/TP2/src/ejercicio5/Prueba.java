package ejercicio5;

import java.util.ArrayList;

public class Prueba {

    public static void main(String[] args) {

        Categoria categoria1 = new Categoria("Principiante", 50000);
        Categoria categoria2 = new Categoria("Intermedio", 60000);
        Categoria categoria3 = new Categoria("Experto", 80000);

        Domicilio domicilio1 = new Domicilio("Calle Falsa", 123);
        Domicilio domicilio2 = new Domicilio("Avenida Siempre Viva", 742);
        Domicilio domicilio3 = new Domicilio("Boulevard de los Sueños Rotos", 456);

        Colectivo colectivo1 = new Colectivo("Mercedes Benz");
        Colectivo colectivo2 = new Colectivo("Volvo");
        Colectivo colectivo3 = new Colectivo("Scania");

        Chofer chofer1 = new Chofer(categoria1, domicilio1, colectivo1, "Juan Perez");
        Chofer chofer2 = new Chofer(categoria2, domicilio2, colectivo2, "Maria Gomez");
        Chofer chofer3 = new Chofer(categoria3, domicilio3, colectivo3, "Carlos Sanchez");

        System.out.println(chofer1);
        System.out.println(chofer2);
        System.out.println(chofer3);

        Empresa empresa = Empresa.getInstance("Transporte XYZ");

        ArrayList<Chofer> chofers = new ArrayList<Chofer>();
        chofers.add(chofer1);
        chofers.add(chofer2);
        chofers.add(chofer3);
        empresa.setChoferes(chofers);

        ArrayList<Colectivo> colectivos = new ArrayList<Colectivo>();
        colectivos.add(colectivo1);
        colectivos.add(colectivo2);
        colectivos.add(colectivo3);
        empresa.setColectivos(colectivos);

        System.out.println("Empresa: " + empresa.getNombre());
        System.out.println("Cantidad de choferes: " + empresa.cantidadChoferes());
        System.out.println("Cantidad de choferes sin colectivo: " + empresa.cantidadSinColectivo());
        System.out.println("Cantidad de choferes en categoria 'Intermedio': " + empresa.cantCategoria(categoria2));
        System.out.println("Categorias con sueldo mayor a 55000:");
        empresa.categoriaMayorA(55000);
        System.out.println("Choferes con sueldo mayor a 55000:");
        empresa.sueldoMayorA(55000);

        chofer3.setColectivo(null);
        System.out.println("Cantidad de choferes sin colectivo: " + empresa.cantidadSinColectivo());
    }
}
