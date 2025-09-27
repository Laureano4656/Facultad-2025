package ejercicio7;

import ejercicio7.Exceptions.ExceptionAtaqueImposible;
import ejercicio7.Exceptions.ExceptionIncrementoImposible;
import ejercicio7.Personajes.Personaje;

import java.util.ArrayList;

public class Mapa {
    private ArrayList<Personaje> personajes;

    public Mapa() {
        this.personajes = new ArrayList<>();
    }

    public void agregarPersonaje(Personaje p) {
        this.personajes.add(p);
    }

    public void eliminarPersonaje(Personaje p) {
        this.personajes.remove(p);
    }

    public void muevePersonaje(Personaje p, double dx, double dy){
        try {
            p.incrementaPosicion(dx, dy);
        }catch(ExceptionIncrementoImposible e){
            // mover al maximo posible
            double maxDistancia = Math.sqrt(Math.pow(dx, 2) + Math.pow(dy, 2));
            double factor = e.getMaxDistanciaSoportada() / maxDistancia;
            double nuevoDx = dx * factor;
            double nuevoDy = dy * factor;
            try {
                p.incrementaPosicion(nuevoDx,nuevoDy);
            } catch (ExceptionIncrementoImposible ex) {
                // no deberia llegar aqui
                ex.printStackTrace();
            }
        }
    }
    public void ataca(Personaje atacante, Personaje defensor) throws ExceptionAtaqueImposible {
        atacante.atacar(defensor);
    }
}
