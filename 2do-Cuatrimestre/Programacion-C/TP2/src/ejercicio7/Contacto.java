package ejercicio7;

import java.util.ArrayList;

public class Contacto {
    private String nombre;
    private String telefonoFijo;
    private ArrayList<String> telefonosMoviles;

    public Contacto(String nombre) {
        this.nombre = nombre;
        this.telefonoFijo = "";
        this.telefonosMoviles = new ArrayList<String>();
    }
    public Contacto(String nombre, String telefonoFijo) {
        this.nombre = nombre;
        this.telefonoFijo = telefonoFijo;
        this.telefonosMoviles = new ArrayList<String>();
    }
    public Contacto(String nombre, String telefonoFijo, ArrayList<String> telefonosMoviles) {
        this.nombre = nombre;
        this.telefonoFijo = telefonoFijo;
        this.telefonosMoviles = telefonosMoviles;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTelefonoFijo() {
        return telefonoFijo;
    }

    public void setTelefonoFijo(String telefonoFijo) {
        this.telefonoFijo = telefonoFijo;
    }

    public ArrayList<String> getTelefonosMoviles() {
        return telefonosMoviles;
    }

    public void setTelefonosMoviles(ArrayList<String> telefonosMoviles) {
        this.telefonosMoviles = telefonosMoviles;
    }
    public void agregarTelefonoMovil(String telefonoMovil) {
        this.telefonosMoviles.add(telefonoMovil);
    }
    @Override
    public String toString() {
        return "Contacto [nombre=" + nombre + ", telefonoFijo=" + telefonoFijo + ", telefonosMoviles=" + telefonosMoviles + "]";
    }
}
