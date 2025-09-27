package ejercicio8;

import java.util.ArrayList;
import java.util.HashMap;

public class Torneo {
    private static Torneo instance;
    private HashMap<String, Equipo> equipos;
    private ArrayList<Partido> partidos;

    private Torneo() {
        this.equipos = new HashMap<>();
        this.partidos = new ArrayList<>();
    }

    public int cantPartidosEquipo(Equipo equipo) {
        int contador = 0;
        for (Partido partido : this.partidos) {
            if (partido.getEquipo1().equals(equipo) || partido.getEquipo2().equals(equipo)) {
                contador++;
            }
        }
        return contador;
    }

    public int puntosEquipo(Equipo equipo) {
        int puntos = 0;
        for (Partido partido : this.partidos) {
            if (partido.getGanador() != null) {
                if (partido.getGanador().equals(equipo)) {
                    puntos += 3;
                }
            } else {
                if (partido.getEquipo1().equals(equipo) || partido.getEquipo2().equals(equipo)) {
                    puntos += 1;
                }
            }
        }
        return puntos;
    }

    public Equipo mayorPuntajeEquipo(Equipo equipo1, Equipo equipo2) {
        int puntosEquipo1 = puntosEquipo(equipo1);
        int puntosEquipo2 = puntosEquipo(equipo2);
        if (puntosEquipo1 > puntosEquipo2) {
            return equipo1;
        } else if (puntosEquipo2 > puntosEquipo1) {
            return equipo2;
        } else {
            int golesAFavorEquipo1 = equipo1.getCantidadGolesAFavor();
            int golesAFavorEquipo2 = equipo2.getCantidadGolesAFavor();
            if (golesAFavorEquipo1 > golesAFavorEquipo2) {
                return equipo1;
            } else if (golesAFavorEquipo2 > golesAFavorEquipo1) {
                return equipo2;
            } else {
                int golesEnContraEquipo1 = equipo1.getCantidadGolesEnContra();
                int golesEnContraEquipo2 = equipo2.getCantidadGolesEnContra();
                if (golesEnContraEquipo1 < golesEnContraEquipo2) {
                    return equipo1;
                } else if (golesEnContraEquipo2 < golesEnContraEquipo1) {
                    return equipo2;
                } else {
                    return equipo1; // Empate en todo
                }
            }
        }
    }

    public Jugador mayorGoleadorEquipo(Equipo equipo1, Equipo equipo2) {
        Jugador goleadorEquipo1 = null;
        Jugador goleadorEquipo2 = null;
        int maxGolesEquipo1 = -1;
        int maxGolesEquipo2 = -1;

        for (Jugador jugador : equipo1.getJugadores()) {
            if (jugador.getGolesAnotados() > maxGolesEquipo1) {
                maxGolesEquipo1 = jugador.getGolesAnotados();
                goleadorEquipo1 = jugador;
            }
        }

        for (Jugador jugador : equipo2.getJugadores()) {
            if (jugador.getGolesAnotados() > maxGolesEquipo2) {
                maxGolesEquipo2 = jugador.getGolesAnotados();
                goleadorEquipo2 = jugador;
            }
        }

        if (maxGolesEquipo1 > maxGolesEquipo2) {
            return goleadorEquipo1;
        } else if (maxGolesEquipo2 > maxGolesEquipo1) {
            return goleadorEquipo2;
        } else {
            return null; // Empate en goles anotados
        }
    }

    public Jugador mayorCantidadGoles(Jugador jugador1, Jugador jugador2) {
        if (jugador1.getGolesAnotados() > jugador2.getGolesAnotados()) {
            return jugador1;
        } else if (jugador2.getGolesAnotados() > jugador1.getGolesAnotados()) {
            return jugador2;
        } else {
            return null; // Empate en goles anotados
        }
    }

    public ArrayList<Partido> getPartidos() {
        return partidos;
    }

    public void setPartidos(ArrayList<Partido> partidos) {
        this.partidos = partidos;
    }

    public HashMap<String, Equipo> getEquipos() {
        return equipos;
    }

    public void setEquipos(HashMap<String, Equipo> equipos) {
        this.equipos = equipos;
    }

    public static Torneo getInstance() {
        if (instance == null) {
            instance = new Torneo();
        }
        return instance;
    }

    @Override
    public String toString() {
        return "Torneo{" +
                "equipos=" + equipos +
                ", partidos=" + partidos +
                '}';
    }
}
