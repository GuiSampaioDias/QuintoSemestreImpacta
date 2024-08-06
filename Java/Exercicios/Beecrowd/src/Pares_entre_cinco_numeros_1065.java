import java.util.Scanner;

public class Pares_entre_cinco_numeros_1065 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int pares = 0, valor;

        for(int i = 0; i < 5; i++){
            valor = sc.nextInt();
            if(valor % 2 == 0){
                pares += 1;
            }
        }
            System.out.printf("%d valores pares%n", pares);
        sc.close();
    }
}
