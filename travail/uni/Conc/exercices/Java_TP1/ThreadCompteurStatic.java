public class ThreadCompteurStatic {
	public static void main(String args[]){
		compteurStatic e1 = new compteurStatic();
		compteurStatic e2 = new compteurStatic();
		e1.start();
		e2.start();
	}
}
