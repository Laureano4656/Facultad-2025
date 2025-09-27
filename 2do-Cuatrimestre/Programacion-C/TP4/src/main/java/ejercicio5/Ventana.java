package ejercicio5;

import javax.swing.*;

public class Ventana {
    private JPanel panel1;
    private JLabel choferesLabel;
    private JList<Chofer> chofersList;
    private JList<Vehiculo> vehiculosList;
    private DefaultListModel<Vehiculo> vehiculosListModel;
    private DefaultListModel<Chofer> choferesListModel;

    public Ventana() {
//        JFrame frame = new JFrame("Asignación de Choferes a Vehículos");
//        frame.setContentPane(panel1);
//        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        frame.setSize(600, 400);
//        frame.setVisible(true);
//
//        // Inicializar modelos de lista
//        vehiculosListModel = new DefaultListModel<>();
//        choferesListModel = new DefaultListModel<>();
//        vehiculosList.setModel(vehiculosListModel);
//        chofersList.setModel(choferesListModel);
//
//        // Agregar datos de ejemplo
//        Categoria catA = new Categoria(true, true);
//        Categoria catB = new Categoria(false, true);
//        Categoria catC = new Categoria(false, false);
//
//        Chofer chofer1 = new Chofer("Juan", catA);
//        Chofer chofer2 = new Chofer("Pedro", catB);
//        Chofer chofer3 = new Chofer("Luis", catC);
//
//        choferesListModel.addElement(chofer1);
//        choferesListModel.addElement(chofer2);
//        choferesListModel.addElement(chofer3);
//
//        Vehiculo vehiculo1 = new Colectivo("Mercedes", 25);
//        Vehiculo vehiculo2 = new ColectivoLargaDistancia("Volvo", 40, true);
//
//        vehiculosListModel.addElement(vehiculo1);
//        vehiculosListModel.addElement(vehiculo2);
//
//        // Manejar selección de chofer y vehículo
//        chofersList.addListSelectionListener(e -> {
//            if (!e.getValueIsAdjusting()) {
//                asignarVehiculoAChofer();
//            }
//        });
//
//        vehiculosList.addListSelectionListener(e -> {
//            if (!e.getValueIsAdjusting()) {
//                asignarVehiculoAChofer();
//            }
//        });
    }
    public static void main(String[] args) {
        new Ventana();
    }
}
