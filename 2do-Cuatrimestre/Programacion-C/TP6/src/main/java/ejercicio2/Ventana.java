package ejercicio2;

import ejercicio2.exceptions.DepositoInvalidoException;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Ventana {
    private JPanel panel1;
    private JButton depositar;
    private JButton extraer;
    private JTextField monto;

    public Ventana() {
        depositar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    double cantidad = Double.parseDouble(monto.getText());
                    CuentaBancaria cuenta = new CuentaBancaria("Juan Perez");
                    cuenta.depositar(cantidad);
                    JOptionPane.showMessageDialog(null, "Deposito exitoso. Saldo actual: " + cuenta.getSaldo());
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(null, "Por favor ingrese un numero valido.");
                } catch (DepositoInvalidoException ex) {
                    JOptionPane.showMessageDialog(null, "Error: Deposito invalido de " + ex.getCantidadInvalida());
                }
            }
        });
        extraer.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try{
                    double cantidad = Double.parseDouble(monto.getText());
                    CuentaBancaria cuenta = new CuentaBancaria("Juan Perez");
                    cuenta.extraer(cantidad);
                    JOptionPane.showMessageDialog(null, "Extraccion exitosa. Saldo actual: " + cuenta.getSaldo());
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(null, "Por favor ingrese un numero valido.");
                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(null, "Error: " + ex.getMessage());
                }
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Ventana");
        frame.setContentPane(new Ventana().panel1);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);


    }
}
