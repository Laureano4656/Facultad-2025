package Ejercicio1.incisoB;

import java.io.Serializable;

public class MotorDTO implements Serializable
{
    private String n_Serie;
    private String comubstible;

    public String getN_Serie()
    {
        return n_Serie;
    }

    public void setN_Serie(String n_Serie)
    {
        this.n_Serie = n_Serie;
    }

    public String getComubstible()
    {
        return comubstible;
    }

    public void setComubstible(String comubstible)
    {
        this.comubstible = comubstible;
    }
}
