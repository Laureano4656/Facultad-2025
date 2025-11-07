package Ejercicio1.modelo;

import java.util.ArrayList;

public class Cliente
{
    private int id;
    private String nombre;
    private String telefono;
    private String direccion;
    private String email;
    private ArrayList<Mascota> mascotas;

    public Cliente(String nombre, String telefono, String direccion, String email)
    {
        this.nombre = nombre;
        this.telefono = telefono;
        this.direccion = direccion;
        this.email = email;
        this.mascotas = new ArrayList<>();
    }

    public int getId()
    {
        return id;
    }

    public void setId(int id)
    {
        this.id = id;
    }

    public void agregarMascota(Mascota mascota)
    {
        this.mascotas.add(mascota);
    }

    public String getTelefono()
    {
        return telefono;
    }

    public void setTelefono(String telefono)
    {
        this.telefono = telefono;
    }

    public String getDireccion()
    {
        return direccion;
    }

    public void setDireccion(String direccion)
    {
        this.direccion = direccion;
    }

    public String getEmail()
    {
        return email;
    }

    public void setEmail(String email)
    {
        this.email = email;
    }

    public String getNombre()
    {
        return nombre;
    }

    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }

    public ArrayList<Mascota> getMascotas()
    {
        return mascotas;
    }

    public void setMascotas(ArrayList<Mascota> mascotas)
    {
        this.mascotas = mascotas;
    }
}
