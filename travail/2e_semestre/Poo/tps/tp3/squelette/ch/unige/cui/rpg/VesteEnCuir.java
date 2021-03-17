package ch.unige.cui.rpg;

public class VesteEnCuir implements Protection{
	private int cWeight;
	private Damage protection;

	public VesteEnCuir(int wheight, Damage dmg){
		this.cWeight= wheight;
		this.protection = dmg;
	}	

	public int weight(){ 
		return cWeight;
	}

	public Damage absorb(Damage dmg){ 
		dmg.reduceDamage(protection);
		return dmg;
	}
}
