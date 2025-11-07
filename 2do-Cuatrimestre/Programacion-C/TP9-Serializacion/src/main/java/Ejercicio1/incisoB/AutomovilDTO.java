package Ejercicio1.incisoB;

import java.io.Serializable;

public class AutomovilDTO extends VehiculoDTO implements Serializable
{
    private String modelo;
    private String marca;
    private String patente;
    private MotorDTO motor;

    public String getModelo()
    {
        return modelo;
    }

    public void setModelo(String modelo)
    {
        this.modelo = modelo;
    }

    public String getMarca()
    {
        return marca;
    }

    public void setMarca(String marca)
    {
        this.marca = marca;
    }

    public String getPatente()
    {
        return patente;
    }

    public void setPatente(String patente)
    {
        this.patente = patente;
    }

    public MotorDTO getMotor()
    {
        return motor;
    }

    public void setMotor(MotorDTO motor)
    {
        this.motor = motor;
    }
}
