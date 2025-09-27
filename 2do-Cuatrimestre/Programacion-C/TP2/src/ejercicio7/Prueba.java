package ejercicio7;

public class Prueba {
    public static void main(String[] args) {
        Agenda agenda = Agenda.getInstance();

        Contacto contacto1 = new Contacto("Juan", "123456789");
        contacto1.agregarTelefonoMovil("987654321");
        contacto1.agregarTelefonoMovil("876543219");

        Contacto contacto2 = new Contacto("Maria", "234567890");
        contacto2.agregarTelefonoMovil("765432198");

        agenda.agregarContacto(contacto1);
        agenda.agregarContacto(contacto2);

        System.out.println("Lista de contactos:");
        agenda.listarContactos();

        System.out.println("\nBuscando contacto 'Juan':");
        System.out.println(agenda.buscarContacto("Juan"));

        System.out.println("\nModificando contacto 'Maria':");
        Contacto contactoModificado = new Contacto("Maria", "345678901");
        contactoModificado.agregarTelefonoMovil("654321987");
        agenda.modificarContacto("Maria", contactoModificado);
        agenda.listarContactos();

        System.out.println("\nEliminando contacto 'Juan':");
        agenda.eliminarContacto("Juan");
        agenda.listarContactos();
    }
}
