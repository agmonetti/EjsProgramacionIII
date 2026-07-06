import java.util.PriorityQueue;

class Evento implements Comparable<Evento> {
    int tiempo;
    int tipo;

    public Evento(int tiempo, int tipo) {
        this.tiempo = tiempo;
        this.tipo = tipo;
    }

    @Override
    public int compareTo(Evento otro) {
        if (this.tiempo == otro.tiempo) {
            // EMPATE: Primero procesamos la salida (-1) antes que la entrada (+1)
            return Integer.compare(this.tipo, otro.tipo);
        }
        return Integer.compare(this.tiempo, otro.tiempo);
    }
}

public class intervaloColores {
    public static void main(String[] args) {
        // El ejemplo exacto de Wehbe en el PDF
        int[][] intervalos = {{1, 5}, {2, 4}, {3, 6}, {7, 8}};
        
        PriorityQueue<Evento> cola = new PriorityQueue<>();

        // 1. Partimos los intervalos
        for (int i = 0; i < intervalos.length; i++) {
            cola.add(new Evento(intervalos[i][0], +1)); 
            cola.add(new Evento(intervalos[i][1], -1)); 
        }

        int cantColores = 0;
        int maxColores = 0;

        System.out.println("--- INICIANDO LÍNEA DE BARRIDO ---\n");

        // 2. El ciclo que procesa el tiempo
        while (!cola.isEmpty()) {
            Evento actual = cola.poll();
            
            // Sumamos o restamos
            cantColores += actual.tipo;
            
            // Actualizamos el récord histórico
            if (cantColores > maxColores) {
                maxColores = cantColores;
            }
            
            // Imprimimos el estado exacto de las variables en esta vuelta
            String accion = (actual.tipo == 1) ? "ENTRA (+1)" : "SALE (-1) ";
            System.out.println("Reloj: " + actual.tiempo 
                             + " | Acción: " + accion 
                             + " | Colores Activos: " + cantColores 
                             + " | Récord (Max): " + maxColores);
        }

        System.out.println("\n--- FIN DEL BARRIDO ---");
        System.out.println("Resultado: Se necesitan " + maxColores + " colores en total.");
    }
	
}
