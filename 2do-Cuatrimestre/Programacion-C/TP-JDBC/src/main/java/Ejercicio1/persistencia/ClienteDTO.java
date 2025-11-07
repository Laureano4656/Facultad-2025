package Ejercicio1.persistencia;

public class ClienteDTO
{
    private int id;
    private String nombre;
    private String telefono;
    private String direccion;
    private String email;

    public String getNombre()
    {
        return nombre;
    }

    public void setNombre(String nombre)
    {
        this.nombre = nombre;
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

    public int getId()
    {
        return id;
    }

    public void setId(int id)
    {
        this.id = id;
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
}
