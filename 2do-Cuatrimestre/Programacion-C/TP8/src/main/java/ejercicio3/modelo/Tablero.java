package ejercicio3.modelo;

import ejercicio3.ParametrosInvalidosExcpetion;

import java.util.ArrayList;

import java.util.Collections;
import java.util.Random;

public class Tablero implements IMemoTest
{
    private static final Random r = new Random();
    private Casillero[][] casilleros;
    private ArrayList<Integer[]> posiciones;
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
    public boolean compararCartas(int i1, int j1, int i2, int j2)
    {
        Casillero c1 = this.casilleros[i1][j1];
        Casillero c2 = this.casilleros[i2][j2];
        if (c1.getTipoCarta().equals(c2.getTipoCarta()))
        {
            c1.setDadoVuelta(true);
            c2.setDadoVuelta(true);
            return true;
        }
        return false;
    }


    @Override
    public int getAlto()
    {
        return 0;
    }

    @Override
    public int getAncho()
    {
        return 0;
    }

    @Override
    public boolean isDadoVuelta(int i, int j)
    {
        return false;
    }
}
