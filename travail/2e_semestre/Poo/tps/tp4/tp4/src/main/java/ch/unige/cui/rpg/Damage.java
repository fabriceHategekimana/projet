package ch.unige.cui.rpg;
/*est de type Entity car il est présent principalement
 * Pour représenter des valeurs du jeu mais qui vont 
 * changer en cours de route */

public class Damage{
	private int[] values= {0,0,0,0};
	private String[] types= { "physique", "magique", "feu", "électrique" };

	public Damage(){
	}	

	public void setDamage(String name, int value){ 
		int position= findIndexOf(name);
		this.values[position] = value;
	}

	//modifie le dégat en question selon la valeur. Dégat + valeur (la valeur peut être négative)
	public void modifyDamage(String name, int value){ 
		int position= findIndexOf(name);	
		this.values[position] += value;
	}

	public int total(){ 
		int somme= 0;
		for(int v : this.values){
			somme += v;
		}	
		return somme;
	}

	public void reduceDamage(Damage d){ 
		for(int i= 0; i < this.values.length; i++){
			this.values[i] -= d.getValue(i);
		}	
	}

	public int getValue(int i){ 
		return this.values[i];
	}
	
	//permet de trouver dans quelle position se trouve un type
	public int findIndexOf(String name){ 
		int position= -1;
		int i= 0;
		boolean notFound= true;
		while((notFound) && (i < this.types.length)){
			if(name.equals(this.types[i])){
				position= i;
				notFound = false;
			}
			i++;
		}
		if(position == -1){
			System.err.println("The type \'"+name+"\' was not found");
		}
		return position;
	}

	@Override
	public String toString() {
		return "Damage{" +
			"values = " + java.util.Arrays.toString(values) +
			", types = " + java.util.Arrays.toString(types) +
			"}";
	}

}
