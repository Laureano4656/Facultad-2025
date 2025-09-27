package ejercicio6;

public class Prueba {
    public static void main(String[] args) {
        Directorio directorioC = new Directorio("C:");
        Entidad archivo1 = new Archivo("Recordatorio.txt", 5);
        directorioC.addContenido(archivo1);
        //directorio de fotos entero
        Directorio directorioFotos = new Directorio("Fotos");
        Entidad foto2 = new Archivo("CAM00053.jpg", 150);
        directorioFotos.addContenido(foto2);
        Entidad foto3 = new Archivo("CAM00054.jpg", 200);
        directorioFotos.addContenido(foto3);
        Entidad foto4 = new Archivo("CAM00055.jpg", 170);
        directorioFotos.addContenido(foto4);
        Entidad foto5 = new Archivo("CAM00056.jpg", 150);
        directorioFotos.addContenido(foto5);
        Entidad foto6 = new Archivo("CAM00057.jpg", 250);
        directorioFotos.addContenido(foto6);

        Directorio directorioViaje = new Directorio("Viaje");
        Entidad foto7 = new Archivo("DSC08904.jpg", 1500);
        directorioViaje.addContenido(foto7);
        Entidad foto8 = new Archivo("DSC08909.jpg", 1000);
        directorioViaje.addContenido(foto8);
        Entidad foto9 = new Archivo("DSC08910.jpg", 2000); // debo crear un link a este archivo
        directorioViaje.addContenido(foto9);
        Entidad foto10 = new Archivo("DSC08911.jpg", 2500);
        directorioViaje.addContenido(foto10);
        Link linkRaiz = new Link(directorioC);
        directorioViaje.addContenido(linkRaiz);
        directorioFotos.addContenido(directorioViaje);

        directorioC.addContenido(directorioFotos);

        //creo link
        Link linkFoto = new Link(foto9);
        directorioC.addContenido(linkFoto);

        //direcotrio de documentos entero
        Directorio directorioDocumentos = new Directorio("Documentos");
        Entidad doc1 = new Archivo("carta.doc", 30);
        directorioDocumentos.addContenido(doc1);
        Entidad doc2 = new Archivo("curriculum.doc", 60);
        directorioDocumentos.addContenido(doc2);
        Entidad doc3 = new Archivo("receta de cocina.doc", 80);
        directorioDocumentos.addContenido(doc3);

        directorioC.addContenido(directorioDocumentos);

        // directorio mp3 entero
        Directorio directorioMp3 = new Directorio("MP3");
        Entidad mp3_1 = new Archivo("El choclo.mp3", 3500);
        directorioMp3.addContenido(mp3_1);
        Entidad mp3_2 = new Archivo("El dia que me quieras.mp3", 4500);
        directorioMp3.addContenido(mp3_2);
        Entidad mp3_3 = new Archivo("Naranjo en flor.mp3", 5000);
        directorioMp3.addContenido(mp3_3);

        Directorio directorioQueen = new Directorio("Queen");
        Entidad mp3_4 = new Archivo("Bohemian rhapsody.mp3", 5300);
        directorioQueen.addContenido(mp3_4);
        Entidad mp3_5 = new Archivo("Made in heaven.mp3", 6500);
        directorioQueen.addContenido(mp3_5);
        Entidad mp3_6 = new Archivo("Save me.mp3", 2500); // debo crear un link a este archivo
        directorioQueen.addContenido(mp3_6);
        directorioMp3.addContenido(directorioQueen);

        Link linkMp3 = new Link(mp3_6);
        directorioC.addContenido(linkMp3);

        Directorio directorioTheBeatles = new Directorio("The Beatles");
        Entidad mp3_7 = new Archivo("Let it be.mp3", 3530);
        directorioTheBeatles.addContenido(mp3_7);
        Entidad mp3_8 = new Archivo("Yesterday.mp3", 3000);
        directorioTheBeatles.addContenido(mp3_8);
        directorioMp3.addContenido(directorioTheBeatles);

        directorioC.addContenido(directorioMp3);

        ArchivoComprimido queenZip = new ArchivoComprimido("Queen.zip", 0.8, directorioQueen.getContenido());
        ArchivoComprimido documentosZip = new ArchivoComprimido("Documentos.zip", 0.3, directorioDocumentos.getContenido());

        directorioC.addContenido(queenZip);
        directorioC.addContenido(documentosZip);

        directorioC.ListContenido();
        System.out.println("El tamaño del directorio C: es "+directorioC.calcTamanio()+" kb");
    }
}
