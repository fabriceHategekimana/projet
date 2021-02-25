import java.lang.Math; 

class TP1Utils{

	////////////////// code fourni aux etudiants ///////////////////////////
	
	//caster les elemnts de arr en double et stocker dans 
	//une array d double
	static double[] str2double(String[] arrIn, int n)	{
		//on utilise ici la fonction parsedouble qui prend 
		//en argument un String et renvoie un double
		double[] arrOut = new double[n];
		for(int i=0;i<n;i++){
			arrOut[i] = Double.parseDouble(arrIn[i]);
		}
		return arrOut;
	}
	
	//affichage d un tableai d double
	static void dispArr(double[] arr, int n){
		for(int i=0;i<n;i++){
			System.out.println(arr[i]);
		}
	}
	
	////////////////////////////////////////////////////////////////////////
	
	//A vous d ajouter les fonctions statiques demandees dans le TP et de les
	//appeler dans le main
	
	static double moyenne(double[] x, int n){ 
		double somme= 0;
		int i= 0;
		while(i<n){ 
		    somme= somme + x[i];
		    i++;	
		}	
		return somme;
	}
	
	static double ecartType(double[] x, int n){ 
		double m = moyenne(x, n);	
		double numerateur= 0;

		int i= 0;
		while(i<n){
		    numerateur= numerateur+Math.pow((x[i]-m), 2);
		    i++;
		}

		double sigma= Math.sqrt(numerateur/n);

		return sigma;
	}

	static double[] triBulle(double[] x, int n){ 
	    double intermediaire= 0;
	    boolean estTrie= false;
//
	    while(!(estTrie)){
	    estTrie= true;
		for(int i= 0; i<n-1; i++){
		    if(x[i]>x[i+1]){
			estTrie= false;
			intermediaire = x[i+1];
			x[i+1]= x[i];
			x[i]= intermediaire;
		    }
		}
	    }

	    return x; //on est pas obliger de retourner x mais je trouve le protocole plus propre comme ça
	}
	
	static double mediane(double[] x, int n){ 
		double[] sortedX= triBulle(x, n);
		double med= 0.0;
		if(n%2 == 0){ //si n est pair
		    	int val= (int) Math.ceil(n/2.0);
			med =  sortedX[val];
		}
		else{ 
		    	double[] tab= {(n/2.0)-1.0, n/2.0};
		    	int val= (int) Math.ceil(TP1Utils.moyenne(tab, 2));
			med = sortedX[val];
		}
		return med;
	}
}
