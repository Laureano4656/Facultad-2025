package Ejercicio4;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Baraja
{
    //La baraja contiene 4 cartas que valen del 1 al 9 puntos, (cuatro cartas valen 1 puntos, cuatro valen 2
    //puntos, etc.) y dieciséis cartas que valen 10 puntos
    private List<Integer> cartas;

    public Baraja() {
        this.cartas = new ArrayList<>();
        // 4 cartas de cada valor del 1 al 9
        for (int i = 1; i <= 9; i++) {
            for (int j = 0; j < 4; j++) {
                cartas.add(i);
            }
        }
        // 16 cartas que valen 10 puntos
        for (int i = 0; i < 16; i++) {
            cartas.add(10);
        }
        Collections.shuffle(this.cartas); // Barajamos las cartas
    }
    public  int tomarCarta() {
        if (cartas.isEmpty()) {
            return 0; // Si no hay cartas, devuelve 0
        }
        return cartas.remove(0);
    }

    public  int cantidadCartas() {
        return cartas.size();
    }


}
