package Ejercicio2;

public class Proveedor
{
    private String email;
    private String nombre;
    private long serialVersionUID;
    private String telefono;

    public Proveedor(String email, String nombre, long serialVersionUID, String telefono)
    {
        this.email = email;
        this.nombre = nombre;
        this.serialVersionUID = serialVersionUID;
        this.telefono = telefono;
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

    public long getSerialVersionUID()
    {
        return serialVersionUID;
    }

    public void setSerialVersionUID(long serialVersionUID)
    {
        this.serialVersionUID = serialVersionUID;
    }

    public String getTelefono()
    {
        return telefono;
    }

    public void setTelefono(String telefono)
    {
        this.telefono = telefono;
    }
}
