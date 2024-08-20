
//import java.util.Locale;
import java.util.Scanner;

public class Experiencias_1094 {
	public static void main(String[] args) {
		// Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		int quantidade = sc.nextInt();
		int total = 0, coelhos = 0, ratos = 0, sapos = 0;
		double per_rato, per_coelho, per_sapos;
		for (int i = 0; i < quantidade; i++) {
			double valor = sc.nextDouble();
			String animal = sc.nextLine();
			total += valor;
			switch (animal) {
				case "C":
					coelhos += valor;
					break;
				case "R":
					ratos += valor;
					break;
				case "S":
					sapos += valor;
					break;
				default:
					break;

			}
			
			per_rato = 100 * (double)ratos;


		}

		sc.close();
	}

}
