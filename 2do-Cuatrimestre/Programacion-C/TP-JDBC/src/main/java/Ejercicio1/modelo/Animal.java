package Ejercicio1.modelo;

public abstract class Animal
{
    private String raza;
    private String especie;

    public Animal(String raza, String especie)
    {
        this.raza = raza;
        this.especie = especie;
    }

    public String getRaza()
    {
        return raza;
    }

    public void setRaza(String raza)
    {
        this.raza = raza;
    }

    public String getEspecie()
    {
        return especie;
    }

    public void setEspecie(String especie)
    {
        this.especie = especie;
    }
}
