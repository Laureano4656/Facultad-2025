package ejercicio1;

public class Persona implements Comparable<Persona>
{
    private String apellido;
    private String nombre;
    private String direccion;

    public String getApellido()
    {
        return apellido;
    }

    public void setApellido(String apellido)
    {
        this.apellido = apellido;
    }

    public String getNombre()
    {
        return nombre;
    }

    public void setNombre(String nombre)
    {
        this.nombre = nombre;
    }

    public String getDireccion()
    {
        return direccion;
    }

    public void setDireccion(String direccion)
    {
        this.direccion = direccion;
    }

    @Override
    public int hashCode()
    {
        int hash;
        hash = (this.apellido != null ? this.apellido.hashCode() : 0);
        hash += (this.nombre != null ? this.nombre.hashCode() : 0);

        return hash;
    }

    @Override
    public boolean equals(Object obj)
    {
        if (this == obj)
        {
            return true;
        }
        if (!(obj instanceof Persona))
        {
            return false;
        }
        final Persona other = (Persona) obj;
        if (other.nombre.equals(this.nombre) && this.apellido.equals(other.apellido))
        {
            return true;
        }
        return other.nombre.equals(this.nombre) || this.direccion.equals(other.direccion);
    }

    @Override
    public int compareTo(Persona o)
    {
        if (this.apellido.equals(o.apellido))
        {
            return this.nombre.compareTo(o.nombre);
        }
        return this.apellido.compareTo(o.apellido);
    }

}
