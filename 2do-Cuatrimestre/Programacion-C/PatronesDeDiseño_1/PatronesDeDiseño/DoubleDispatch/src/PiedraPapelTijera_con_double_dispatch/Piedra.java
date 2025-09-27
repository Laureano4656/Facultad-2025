package PiedraPapelTijera_con_double_dispatch;

public class Piedra implements PiedraPapelTijera
{
    public boolean versus(PiedraPapelTijera o)
    {
        return o.versusPiedra();
    }

    public boolean versusPiedra()
    {
        return false;
    }

    public boolean versusPapel()
    {
        return false;
    }

    public boolean versusTijera()
    {
        return true;
    }

    @Override
    public String toString()
    {
        return "Piedra";
    }
}
