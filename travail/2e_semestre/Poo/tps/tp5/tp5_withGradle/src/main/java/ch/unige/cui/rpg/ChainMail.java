package ch.unige.cui.rpg;

public class ChainMail extends Protection {
    private int armorValue;
    private int weight;
    

    public ChainMail(int armorValue, int weight){
		super();
        this.armorValue=armorValue;
        this.weight=weight;
    }

	@Override
    public int getWeight() {
		super.getWeight();
        return weight;
    }
    
    @Override
    public Damage absorb(Damage dmg) {
        //chain mail only absorbs physical damage
		super.absorb(dmg);
        return new Damage(dmg.getPhysical()-armorValue, dmg.getMagical(), dmg.getElectrical(),dmg.getFire());
    }

    
}
