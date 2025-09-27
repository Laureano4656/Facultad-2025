package ejercicio8;

import java.time.LocalDate;
import java.util.ArrayList;

public class Partido {
    private LocalDate fecha;
    private Equipo equipo1;
    private Equipo equipo2;
    private Equipo ganador; // Puede ser null en caso de empate

    public Partido(LocalDate fecha, Equipo equipo1, Equipo equipo2) {
        this.fecha = fecha;
        this.equipo1 = equipo1;
        this.equipo2 = equipo2;
        this.ganador = null;
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public void setFecha(LocalDate fecha) {
        this.fecha = fecha;
    }

    public Equipo getEquipo1() {
        return equipo1;
    }

    public void setEquipo1(Equipo equipo1) {
        this.equipo1 = equipo1;
    }

    public Equipo getEquipo2() {
        return equipo2;
    }

    public void setEquipo2(Equipo equipo2) {
        this.equipo2 = equipo2;
    }

    public Equipo getGanador() {
        return ganador;
    }

    public void setGanador(Equipo ganador) {
        this.ganador = ganador;
    }

    @Override
    public String toString() {
        return "Partido{" +
                "fecha=" + fecha +
                ", equipo1=" + equipo1 +
                ", equipo2=" + equipo2 +
                ", ganador=" + ganador +
                '}';
    }
}
