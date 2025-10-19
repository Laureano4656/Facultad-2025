package ejercicio3.modelo;

public class Casillero
{
    private boolean dadoVuelta;
    private String tipoCarta;
    private boolean correcto;

    public Casillero()
    {
        this.dadoVuelta = false;
        this.tipoCarta = "";
        this.correcto = false;
    }

    public boolean isCorrecto()
    {
        return correcto;
    }

    public void setCorrecto(boolean correcto)
    {
        this.correcto = correcto;
    }

    public boolean isDadoVuelta()
    {
        return dadoVuelta;
    }
    public void setDadoVuelta(boolean dadoVuelta)
    {
        this.dadoVuelta = dadoVuelta;
    }
    public void darVuelta()
    {
        this.dadoVuelta = true;
    }
    public String getTipoCarta()
    {
        return tipoCarta;
    }
    public void setTipoCarta(String tipoCarta)
    {
        this.tipoCarta = tipoCarta;
    }
}
