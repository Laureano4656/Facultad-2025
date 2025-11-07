package Ejercicio1.incisoA;

import java.io.Serializable;

public class Motor implements Serializable
{
    private String n_Serie;
    private String comubstible;

    public void setN_Serie(String n_Serie)
    {
        this.n_Serie = n_Serie;
    }

    public void setComubstible(String comubstible)
    {
        this.comubstible = comubstible;
    }

    public String getN_Serie()
    {
        return n_Serie;
    }

    public String getComubstible()
    {
        return comubstible;
    }
}
