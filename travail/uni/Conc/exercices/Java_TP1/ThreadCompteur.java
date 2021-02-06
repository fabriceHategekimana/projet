
public class ThreadCompteur extends Thread{

	private Compteur compteur;
	
	ThreadCompteur(Compteur cpt){
		this.compteur=cpt;
	}

	public void run(){
		int inter;
		while(true){
			inter = compteur.getValue();
			compteur.increment();
			System.out.println("Thread "+Thread.currentThread().getName()+"  "+ inter);
		}
	}


  public static void main(String[] args) {
	Compteur cpt = new Compteur();
    	ThreadCompteur t1 = new ThreadCompteur(cpt);
	ThreadCompteur t2 = new ThreadCompteur(cpt);
	t1.start();
    	t2.start();
  }
}
