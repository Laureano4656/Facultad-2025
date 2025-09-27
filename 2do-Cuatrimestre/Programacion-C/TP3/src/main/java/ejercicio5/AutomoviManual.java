package ejercicio5;

public class AutomoviManual extends  Automovil{
    public AutomoviManual(String patente, double velocidadMaxima) {
        super(patente, velocidadMaxima);
    }

    public AutomoviManual(String patente) {
        super(patente);
    }

    @Override
    public void acelerar(double velocidad) {
        if (super.getVelocidad() + velocidad <= super.getVelocidadMaxima()) {
            super.setVelocidad(super.getVelocidad() + velocidad);
        } else {
            System.out.println("No se puede acelerar más allá de la velocidad máxima.");
        }
    }

    @Override
    public void frenar(double velocidad) {
        if (getVelocidad() - velocidad >= 0) {
            setVelocidad(getVelocidad() - velocidad);
        } else {
            setVelocidad(0);
        }
    }
}
