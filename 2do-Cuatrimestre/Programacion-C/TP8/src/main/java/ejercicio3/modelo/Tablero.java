package ejercicio3.modelo;

import java.util.ArrayList;

import java.util.Collections;
import java.util.Random;

public class Tablero implements IMemoTest
{
    private static final Random r = new Random();
    private Casillero[][] casilleros;
    private ArrayList<Integer[]> posiciones;
    private int cantidadParejas;
    private int ancho;
    private int alto;

    public Tablero(int ancho, int alto) throws ParametrosInvalidosExcpetion
    {
        if (ancho <= 0 || alto <= 0)
        {
            throw new ParametrosInvalidosExcpetion("Los parametros deben ser mayores a 0");
        }
        if (ancho % 2 != 0 || alto % 2 != 0)
        {
            throw new ParametrosInvalidosExcpetion("Los parametros deben ser pares");
        }

        this.casilleros = new Casillero[alto][ancho];
        this.posiciones = new ArrayList<>();
        this.cantidadParejas = 0;
        this.ancho = ancho;
        this.alto = alto;
        ArrayList<String> tiposCartas = new ArrayList<>();
        int cantidad = (ancho * alto) / 2;
        for (int i = 1; i <= cantidad; i++) {
            tiposCartas.add("Tipo" + i);
            tiposCartas.add("Tipo" + i);
        }
        Collections.shuffle(tiposCartas);

        for (int i = 0; i < alto; i++)
        {
            for (int j = 0; j < ancho; j++)
            {
                this.casilleros[i][j] = new Casillero();
                this.posiciones.add(new Integer[]{i, j});
            }
        }
        Collections.shuffle(this.posiciones);
        for (int index = 0; index < this.posiciones.size(); index++) {
            Integer[] pos = this.posiciones.get(index);
            int i = pos[0];
            int j = pos[1];

            this.casilleros[i][j].setTipoCarta(tiposCartas.get(index));
        }
    }

    public Casillero getCasillero(int i, int j)
    {
        return this.casilleros[i][j];
    }
    public void compararCartas(int i1, int j1, int i2, int j2)
    {
        Casillero c1 = this.casilleros[i1][j1];
        Casillero c2 = this.casilleros[i2][j2];
        if (c1.equals(c2))
        {
            c1.setDadoVuelta(true);
            c2.setDadoVuelta(true);
            c1.setCorrecto(true);
            c2.setCorrecto(true);
            this.cantidadParejas = 0;
            return;
        }
        this.reiniciarCartasNoPareadas(i1, j1, i2, j2);
        this.cantidadParejas = 0;
    }
    public boolean gano()
    {
        for (Casillero[] casillero : this.casilleros)
        {
            for (int j = 0; j < this.casilleros[0].length; j++)
            {
                if (!casillero[j].isCorrecto())
                {
                    return false;
                }
            }
        }
        return true;
    }
    public void darVuelta(int i, int j)
    {
        if (this.cantidadParejas < 2)
        {
            this.casilleros[i][j].setDadoVuelta(true);
            this.cantidadParejas++;
        }else{
            // debo buscar la otra carta dada vuelta
            int iEncontrado = -1;
            int jEncontrado = -1;
            while (iEncontrado == -1)
            {
                for (int x = 0; x < this.casilleros.length; x++)
                {
                    for (int y = 0; y < this.casilleros[0].length; y++)
                    {
                        if (this.casilleros[x][y].isDadoVuelta() && !this.casilleros[x][y].isCorrecto())
                        {
                            iEncontrado = x;
                            jEncontrado = y;
                            break;
                        }
                    }
                    if (iEncontrado != -1)
                    {
                        break;
                    }
                }
            }
            this.compararCartas(iEncontrado, jEncontrado, i, j);
        }
    }
    public void reiniciarCartasNoPareadas(int i1, int j1, int i2, int j2)
    {
        this.casilleros[i1][j1].setDadoVuelta(false);
        this.casilleros[i2][j2].setDadoVuelta(false);
    }
    public boolean isDescubierta(int i, int j)
    {
        return this.casilleros[i][j].isDadoVuelta();
    }

    @Override
    public int getAlto()
    {
        return this.alto;
    }

    @Override
    public int getAncho()
    {
        return this.ancho;
    }

    @Override
    public boolean isDadoVuelta(int i, int j)
    {
        return this.casilleros[i][j].isDadoVuelta();
    }
}
