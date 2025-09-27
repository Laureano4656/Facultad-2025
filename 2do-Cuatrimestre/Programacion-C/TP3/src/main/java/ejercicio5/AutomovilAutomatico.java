package ejercicio5;

public class AutomovilAutomatico extends Automovil {
    public AutomovilAutomatico(String patente, double velocidadMaxima) {
        super(patente, velocidadMaxima);
    }

    public AutomovilAutomatico(String patente) {
        super(patente);
    }

    @Override
    public void acelerar(double velocidad) {
        if (super.getVelocidad() + velocidad <= super.getVelocidadMaxima()) {
            super.setVelocidad(super.getVelocidad() + velocidad);
            actualizarMarcha();
        } else {
            System.out.println("No se puede acelerar más allá de la velocidad máxima.");
        }
    }

    @Override
    public void frenar(double velocidad) {
        if (getVelocidad() - velocidad >= 0) {
            setVelocidad(getVelocidad() - velocidad);
            actualizarMarcha();
        } else {
            setVelocidad(0);
            actualizarMarcha();
        }
    }

    private void actualizarMarcha() {
        double velocidad = getVelocidad();
        if (velocidad == 0) {
            setMarcha(0); // Punto muerto
        } else if (velocidad > 0 && velocidad <= 10) {
            setMarcha(1);
        } else if (velocidad > 10 && velocidad <= 35) {
            setMarcha(2);
        } else if (velocidad > 35 && velocidad <= 50) {
            setMarcha(3);
        } else if (velocidad > 50 && velocidad <= 90) {
            setMarcha(4);
        } else {
            setMarcha(5);
        }
    }
}
