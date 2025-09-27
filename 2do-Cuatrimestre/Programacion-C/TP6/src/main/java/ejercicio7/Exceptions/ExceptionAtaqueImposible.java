package ejercicio7.Exceptions;

import ejercicio7.Personajes.Personaje;

public class ExceptionAtaqueImposible extends Exception {
    private Personaje atacante;
    private Personaje atacado;
    public ExceptionAtaqueImposible(String message, Personaje atacante, Personaje atacado) {
        super(message);
        this.atacante = atacante;
        this.atacado = atacado;
    }
    public Personaje getAtacante() {
        return atacante;
    }
    public Personaje getAtacado() {
        return atacado;
    }
}
