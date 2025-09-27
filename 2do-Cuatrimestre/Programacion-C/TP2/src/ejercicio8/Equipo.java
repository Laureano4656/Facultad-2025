package ejercicio8;

import java.util.ArrayList;

public class Equipo {
    private String nombre;
    private int cantidadPartidosGanados;
    private int cantidadPartidosPerdidos;
    private int cantidadPartidosEmpatados;
    private int cantidadGolesAFavor;
    private int cantidadGolesEnContra;
    private ArrayList<Jugador> jugadores;

    public Equipo(String nombre) {
        this.nombre = nombre;
        this.cantidadPartidosGanados = 0;
        this.cantidadPartidosPerdidos = 0;
        this.cantidadPartidosEmpatados = 0;
        this.cantidadGolesAFavor = 0;
        this.cantidadGolesEnContra = 0;
        this.jugadores = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getCantidadPartidosGanados() {
        return cantidadPartidosGanados;
    }

    public void setCantidadPartidosGanados(int cantidadPartidosGanados) {
        this.cantidadPartidosGanados = cantidadPartidosGanados;
    }

    public int getCantidadPartidosPerdidos() {
        return cantidadPartidosPerdidos;
    }

    public void setCantidadPartidosPerdidos(int cantidadPartidosPerdidos) {
        this.cantidadPartidosPerdidos = cantidadPartidosPerdidos;
    }

    public int getCantidadPartidosEmpatados() {
        return cantidadPartidosEmpatados;
    }

    public void setCantidadPartidosEmpatados(int cantidadPartidosEmpatados) {
        this.cantidadPartidosEmpatados = cantidadPartidosEmpatados;
    }

    public int getCantidadGolesAFavor() {
        return cantidadGolesAFavor;
    }

    public void setCantidadGolesAFavor(int cantidadGolesAFavor) {
        this.cantidadGolesAFavor = cantidadGolesAFavor;
    }

    public int getCantidadGolesEnContra() {
        return cantidadGolesEnContra;
    }

    public void setCantidadGolesEnContra(int cantidadGolesEnContra) {
        this.cantidadGolesEnContra = cantidadGolesEnContra;
    }

    public ArrayList<Jugador> getJugadores() {
        return jugadores;
    }

    public void setJugadores(ArrayList<Jugador> jugadores) {
        this.jugadores = jugadores;
    }

    public void agregarJugador(Jugador jugador) {
        this.jugadores.add(jugador);
    }

    @Override
    public String toString() {
        return "Equipo{" +
                "nombre='" + nombre + '\'' +
                ", cantidadPartidosGanados=" + cantidadPartidosGanados +
                ", cantidadPartidosPerdidos=" + cantidadPartidosPerdidos +
                ", cantidadPartidosEmpatados=" + cantidadPartidosEmpatados +
                ", cantidadGolesAFavor=" + cantidadGolesAFavor +
                ", cantidadGolesEnContra=" + cantidadGolesEnContra +
                ", jugadores=" + jugadores +
                '}';
    }
}
