package Ejercicio1.incisoB;

public  class Automovil extends Vehiculo
{
    private String modelo;
    private String marca;
    private String patente;
    private Motor motor;

    public Automovil(String n_Cashis,int anioFabricacion, String modelo, String marca, String patente, Motor motor)
    {
        super(n_Cashis, anioFabricacion);
        this.modelo = modelo;
        this.marca = marca;
        this.patente = patente;
        this.motor = motor;
    }

    public String getModelo()
    {
        return modelo;
    }

    public String getMarca()
    {
        return marca;
    }

    public String getPatente()
    {
        return patente;
    }

    public Motor getMotor()
    {
        return motor;
    }
}
