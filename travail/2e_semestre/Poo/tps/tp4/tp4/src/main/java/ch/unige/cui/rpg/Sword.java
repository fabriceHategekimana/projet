package ch.unige.cui.rpg;

public class Sword implements Equipement{
	private Damage d;
	private int weight;

	public Sword(Damage d, int weight) {
		this.d = d;
		this.weight = weight;
	}

	public Damage getDamage() {
		return d;
	}

	public int weight() {
		return weight;
	}


}
