package modelo;

public interface IBuscaminas
{

    int getAncho();

    int getAlto();

    int getCantidad();

    boolean pisa(int i, int j);

    void marca(int i, int j);

    int getEntorno(int i, int j);

    boolean isPisado(int i, int j);

    boolean isMarcado(int i, int j);

    boolean isMina(int i, int j);

    int getPisadas();

}