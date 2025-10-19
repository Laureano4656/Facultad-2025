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
        return this.correcto;
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

    @Override
    public boolean equals(Object obj)
    {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Casillero casillero = (Casillero) obj;
        return tipoCarta.equals(casillero.tipoCarta);
    }
}
