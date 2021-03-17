/*est de type object Value car représente une combinaison
*d'équipement du jeu qui ne variera pas avec le temps*/
public class ProtectionStack implements Protection{ 
	private final Protection[] layers;

	public ProtectionStack(Protection[] p){
		this.layers= p;
	}	

	public Damage absorb(Damage dmg){ 
		for(Protection p : layers){
			dmg= p.absorb(dmg);
		}
		return dmg;
	}

	public int weight(){ 
		int somme= 0;
		for(Protection p : layers){
			somme += p.Weight();
		}
		return somme;	
	}

	@Override
	public int hashCode() {
		int result = 17;
		result = 31 * result + java.util.Arrays.hashCode(layers);
		return result;
	}

	@Override
	public boolean equals(Object o) {
		if (this == o) return true;
		if (o == null || getClass() != o.getClass()) return false;

		ProtectionStack object = (ProtectionStack) o;

		return !(!java.util.Arrays.equals(layers, object.layers));
	}

}
