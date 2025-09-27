package ejercicio7;

import java.util.HashMap;

public class Agenda {
    private static Agenda instance = null;
    private HashMap<String, Contacto> contactos;

    private Agenda() {
        contactos = new HashMap<String, Contacto>();
    }
    public void agregarContacto(Contacto contacto) {
        if (!contactos.containsKey(contacto.getNombre())) {
            contactos.put(contacto.getNombre(), contacto);
        }
    }
    public void eliminarContacto(String nombre) {
        contactos.remove(nombre);
    }
    public void modificarContacto(String nombre, Contacto contacto) {
        if (contactos.containsKey(nombre)) {
            contactos.put(nombre, contacto);
        }
    }
    public Contacto buscarContacto(String nombre) {
        return contactos.get(nombre);
    }
    public void listarContactos() {
        for (String nombre : contactos.keySet()) {
            System.out.println(contactos.get(nombre));
        }
    }
    public static Agenda getInstance() {
        if (instance == null) {
            instance = new Agenda();
        }
        return instance;
    }
}
