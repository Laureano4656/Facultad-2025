package PiedraPapelTijera_con_double_dispatch;

public class Tijera implements PiedraPapelTijera
{
    public boolean versus(PiedraPapelTijera o)
    {
        return o.versusTijera();
    }

    public boolean versusPiedra()
    {
        return false;
    }

    public boolean versusPapel()
    {
        return true;
    }

    public boolean versusTijera()
    {
        return false;
    }

    @Override
    public String toString()
    {
        return "Tijera";
    }
}
