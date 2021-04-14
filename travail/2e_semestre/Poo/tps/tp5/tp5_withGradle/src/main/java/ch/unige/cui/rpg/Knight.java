package ch.unige.cui.rpg;

public class Knight{
  
  public Knight(String name, int maxHP, int gold, ProtectionStack protectionSt, Bag bag){
	  super(name, maxHP, gold, protectionSt, bag);
  }
  
  @Override
  public void wound(Damage dmg){
	super.wound(dmg);
  }
  
  @Override
  public void heal(int hp){
	super.heal(hp);
  }
  
  @Override
  public void startQuest(Quest q){
	  super.startQuest(q);
  }
  
  public String toString(){
	  return super.toString();
  }
  
}
