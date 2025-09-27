package ejercicio8;

import java.util.ArrayList;
import java.util.HashMap;

public class Prueba {
    public static void main(String[] args) {
        Jugador jugador1 = new Jugador("Lionel Messi", "1987", 10, 1);
        Jugador jugador2 = new Jugador("Cristiano Ronaldo", "1985", 7, 1);
        Jugador jugador3 = new Jugador("Neymar Jr", "1992", 11, 1);
        Jugador jugador4 = new Jugador("Kylian Mbappe", "1998", 7, 1);
        Jugador jugador5 = new Jugador("Luka Modric", "1985", 10, 2);
        Jugador jugador6 = new Jugador("Sergio Ramos", "1986", 4, 3);
        Jugador jugador7 = new Jugador("Robert Lewandowski", "1988", 9, 1);
        Jugador jugador8 = new Jugador("Kevin De Bruyne", "1991", 17, 2);
        Jugador jugador9 = new Jugador("Virgil van Dijk", "1991", 4, 3);
        Jugador jugador10 = new Jugador("Mohamed Salah", "1992", 11, 1);
        Jugador jugador11 = new Jugador("Sadio Mane", "1992", 10, 1);
        Jugador jugador12 = new Jugador("Eden Hazard", "1991", 7, 2);

        jugador1.setGolesAnotados(30);
        jugador1.setPartidosJugados(25);
        jugador2.setGolesAnotados(25);
        jugador2.setPartidosJugados(20);
        jugador3.setGolesAnotados(20);
        jugador3.setPartidosJugados(15);
        jugador4.setGolesAnotados(15);
        jugador4.setPartidosJugados(10);
        jugador5.setGolesAnotados(10);
        jugador5.setPartidosJugados(30);
        jugador6.setGolesAnotados(5);
        jugador6.setPartidosJugados(35);
        jugador7.setGolesAnotados(28);
        jugador7.setPartidosJugados(22);
        jugador8.setGolesAnotados(12);
        jugador8.setPartidosJugados(28);
        jugador9.setGolesAnotados(3);
        jugador9.setPartidosJugados(40);
        jugador10.setGolesAnotados(22);
        jugador10.setPartidosJugados(18);
        jugador11.setGolesAnotados(18);
        jugador11.setPartidosJugados(16);
        jugador12.setGolesAnotados(14);
        jugador12.setPartidosJugados(26);


        Equipo equipoA = new Equipo("Equipo A");
        Equipo equipoB = new Equipo("Equipo B");
        Equipo equipoC = new Equipo("Equipo C");
        Equipo equipoD = new Equipo("Equipo D");

        HashMap<String, Equipo> equipos = new HashMap<>();
        equipos.put(equipoA.getNombre(), equipoA);
        equipos.put(equipoB.getNombre(), equipoB);
        equipos.put(equipoC.getNombre(), equipoC);
        equipos.put(equipoD.getNombre(), equipoD);

        ArrayList<Jugador> jugadoresA = new ArrayList<>();
        ArrayList<Jugador> jugadoresB = new ArrayList<>();
        ArrayList<Jugador> jugadoresC = new ArrayList<>();
        ArrayList<Jugador> jugadoresD = new ArrayList<>();

        jugadoresA.add(jugador1);
        jugadoresA.add(jugador2);
        jugadoresA.add(jugador3);


        jugadoresB.add(jugador4);
        jugadoresB.add(jugador5);
        jugadoresB.add(jugador6);


        jugadoresC.add(jugador7);
        jugadoresC.add(jugador8);
        jugadoresC.add(jugador9);


        jugadoresD.add(jugador10);
        jugadoresD.add(jugador11);
        jugadoresD.add(jugador12);


        equipoA.setJugadores(jugadoresA);
        equipoB.setJugadores(jugadoresB);
        equipoC.setJugadores(jugadoresC);
        equipoD.setJugadores(jugadoresD);


        Partido partido1 = new Partido(java.time.LocalDate.of(2023, 10, 1), equipoA, equipoB);
        Partido partido2 = new Partido(java.time.LocalDate.of(2023, 10, 2), equipoC, equipoD);
        Partido partido3 = new Partido(java.time.LocalDate.of(2023, 10, 3), equipoA, equipoC);
        Partido partido4 = new Partido(java.time.LocalDate.of(2023, 10, 4), equipoB, equipoD);
        Partido partido5 = new Partido(java.time.LocalDate.of(2023, 10, 5), equipoA, equipoD);
        Partido partido6 = new Partido(java.time.LocalDate.of(2023, 10, 6), equipoB, equipoC);

        partido1.setGanador(equipoA);
        partido2.setGanador(equipoA);
        partido3.setGanador(equipoC);
        partido4.setGanador(equipoD);
        partido5.setGanador(null); // Empate
        partido6.setGanador(equipoB);

        ArrayList<Partido> partidos = new ArrayList<>();
        partidos.add(partido1);
        partidos.add(partido2);
        partidos.add(partido3);
        partidos.add(partido4);
        partidos.add(partido5);
        partidos.add(partido6);

        Torneo torneo = Torneo.getInstance();
        torneo.setEquipos(equipos);
        torneo.setPartidos(partidos);

        // Ejemplo de uso de los métodos
        Jugador mayorGoleador = torneo.mayorCantidadGoles(jugador1, jugador2);
        if (mayorGoleador != null) {
            System.out.println("El mayor goleador es: " + mayorGoleador.getNombre());
        } else {
            System.out.println("Empate en goles anotados entre los jugadores.");
        }
        System.out.println("Cantidad de partidos equipo A: " + torneo.cantPartidosEquipo(equipoA));
        System.out.println("Cantidad de partidos equipo B: " + torneo.cantPartidosEquipo(equipoB));
        System.out.println("Cantidad de partidos equipo C: " + torneo.cantPartidosEquipo(equipoC));
        System.out.println("Cantidad de partidos equipo D: " + torneo.cantPartidosEquipo(equipoD));

        System.out.println("Puntos del equipo A: " + torneo.puntosEquipo(equipoA));
        System.out.println("Puntos del equipo B: " + torneo.puntosEquipo(equipoB));
        System.out.println("Puntos del equipo C: " + torneo.puntosEquipo(equipoC));
        System.out.println("Puntos del equipo D: " + torneo.puntosEquipo(equipoD));

        System.out.println("Mayor goleador entre equipo A y B: " + torneo.mayorGoleadorEquipo(equipoA, equipoB));
        System.out.println("Mayor goleador entre equipo C y D: " + torneo.mayorGoleadorEquipo(equipoC, equipoD));
        System.out.println("Mayor goleador entre equipo A y C: " + torneo.mayorGoleadorEquipo(equipoA, equipoC));
        System.out.println("Mayor goleador entre equipo B and D: " + torneo.mayorGoleadorEquipo(equipoB, equipoD));

        System.out.println("Mayor puntaje entre equipo A y B: " + torneo.mayorPuntajeEquipo(equipoA, equipoB));
        System.out.println("Mayor puntaje entre equipo C y D: " + torneo.mayorPuntajeEquipo(equipoC, equipoD));
        System.out.println("Mayor puntaje entre equipo A y C: " + torneo.mayorPuntajeEquipo(equipoA, equipoC));
        System.out.println("Mayor puntaje entre equipo B and D: " + torneo.mayorPuntajeEquipo(equipoB, equipoD));
    }
}
