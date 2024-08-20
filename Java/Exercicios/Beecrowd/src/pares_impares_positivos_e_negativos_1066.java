import java.util.Scanner;

/**
 * 1066_pares_impares_positivos_e_negativos
 */
public class pares_impares_positivos_e_negativos_1066 {
    
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int par = 0, impar = 0, positivo = 0, negativo = 0, valor;

        for(int i = 0; i < 5; i++){
            valor = sc.nextInt();
            if(valor % 2 == 0){
                par +=1;
            }
            else{
                impar += 1;
            }
            if(valor > 0 ){
                positivo += 1;
            }
            else if(valor < 0){
            negativo += 1;
            }
        }
        System.out.printf("%d valor(es) par(es)%n", par);
        System.out.printf("%d valor(es) impar(es)%n", impar);
        System.out.printf("%d valor(es) positivo(s)%n", positivo);
        System.out.printf("%d valor(es) negativo(s)%n", negativo);
        sc.close();

    }
    
}