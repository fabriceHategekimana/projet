package ch.unige.cui.rpg;

public class FireProofLeatherVest extends Protection{
    private final int fireProtection;
    private final int physicalProtection;
    private final int weight;

    public FireProofLeatherVest(int fireProtection, int physicalProtection, int weight){
		super();
        this.fireProtection=fireProtection;
        this.physicalProtection=physicalProtection;
        this.weight=weight;
    }

    @Override
    public int getWeight() {
		super.getWeight();
        return weight;
    }
    
    @Override
    public Damage absorb(Damage dmg) {
        //fireproof leather vest protects a little bit from physical
        //and a lot from fire
		super.absorb(dmg);
        return new Damage(dmg.getPhysical()-physicalProtection,dmg.getMagical(),dmg.getElectrical(),dmg.getFire()-fireProtection);
    }


}
