package ejercicio3.modelo;

import ejercicio3.ParametrosInvalidosExcpetion;


import java.util.Set;

public class MemoTest
{
    private Tablero tablero;
    private Set<String> jugadores;

    public MemoTest(Tablero tablero, Set<String> jugadores) throws ParametrosInvalidosExcpetion
    {
        if (tablero == null)
        {
            throw new ParametrosInvalidosExcpetion("El tablero no puede ser nulo");
        }
        if (jugadores == null || jugadores.isEmpty())
        {
            throw new ParametrosInvalidosExcpetion("Debe haber al menos un jugador");
        }
        this.tablero = tablero;
        this.jugadores = jugadores;
    }
}
