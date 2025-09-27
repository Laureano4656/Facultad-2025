package ejercicio9;

import java.util.ArrayList;
import java.util.GregorianCalendar;
import java.util.HashMap;

public class Partido {
    private HashMap<String, Jugador> jugadoresEquipo1;
    private HashMap<String, Jugador> jugadoresEquipo2;
    private GregorianCalendar fecha;
    private int golesEquipo1;
    private int golesEquipo2;
    private String ganador;

    public Partido(HashMap<String, Jugador> jugadoresEquipo1, HashMap<String, Jugador> jugadoresEquipo2, GregorianCalendar fecha) {
        this.jugadoresEquipo1 = jugadoresEquipo1;
        this.jugadoresEquipo2 = jugadoresEquipo2;
        this.fecha = fecha;
        this.golesEquipo1 = 0;
        this.golesEquipo2 = 0;
        this.ganador = null;
    }

    public void registrarResultado(HashMap<String, Integer> jugadores, int golesEquipo1, int golesEquipo2) {
        this.golesEquipo1 = golesEquipo1;
        this.golesEquipo2 = golesEquipo2;

        for (String nombre : jugadores.keySet()) {
            int puntos = jugadores.get(nombre);
            Jugador jugador1 = jugadoresEquipo1.get(nombre);
            if (jugador1 != null) {
                jugador1.sumarPuntos(puntos);
            } else {
                Jugador jugador2 = jugadoresEquipo2.get(nombre);
                if (jugador2 != null) {
                    jugador2.sumarPuntos(puntos);
                }
            }
        }

        if (golesEquipo1 > golesEquipo2) {
            this.ganador = "Equipo A";
        } else if (golesEquipo2 > golesEquipo1) {
            this.ganador = "Equipo B";
        } else {
            this.ganador = null; // Empate
        }

    }
}
