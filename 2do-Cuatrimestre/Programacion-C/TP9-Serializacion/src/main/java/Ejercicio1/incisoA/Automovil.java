package Ejercicio1.incisoA;

import java.io.Serializable;

public class Automovil extends Vehiculo implements Serializable
{
    private String modelo;
    private String marca;
    private String patente;
    private Motor motor;

    public void setModelo(String modelo)
    {
        this.modelo = modelo;
    }

    public void setMarca(String marca)
    {
        this.marca = marca;
    }

    public void setPatente(String patente)
    {
        this.patente = patente;
    }

    public void setMotor(Motor motor)
    {
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
