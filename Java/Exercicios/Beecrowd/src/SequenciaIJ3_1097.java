
public class SequenciaIJ3_1097 {

	public static void main(String[] args) {
		int j = 7;
		for(int i = 1; i <= 9; i +=2) {
			for(int n = 0; n < 3; n ++) {
				System.out.printf("I=%d J=%d%n", i, j);
				j--;
			}
			j += 5;
			
		}

	}

}
