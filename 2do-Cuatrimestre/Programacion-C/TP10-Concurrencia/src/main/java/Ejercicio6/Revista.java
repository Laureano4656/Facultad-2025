package Ejercicio6;

public class Revista
{
    private int idRevista;
    private String titulo;

    public Revista(int idrevista, String titulo)
    {
        this.idRevista = idrevista;
        this.titulo = titulo;
    }
    public int getIdrevista()
    {
        return this.idRevista;
    }

    public String getTitulo()
    {
        return titulo;
    }
}
