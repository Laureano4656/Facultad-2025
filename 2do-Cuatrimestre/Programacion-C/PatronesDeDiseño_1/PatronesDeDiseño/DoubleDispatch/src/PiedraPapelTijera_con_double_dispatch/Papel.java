package PiedraPapelTijera_con_double_dispatch;

public class Papel implements PiedraPapelTijera
{
    public boolean versus(PiedraPapelTijera o)
    {
        return o.versusPapel();
    }

    public boolean versusPiedra()
    {
        return true;
    }

    public boolean versusPapel()
    {
        return false;
    }

    public boolean versusTijera()
    {
        return false;
    }

    @Override
    public String toString()
    {
        return "Papel";
    }
}

