package ch.unige.cui.rpg;

import java.util.Stack;

public class Bag{
	private int capacity;
	private int goldPocket;
	private Stack<Equipement> mainPocket;

	public Bag(int capacity){
		this.capacity= capacity;
		mainPocket= new Stack<Equipement>();
	}	

	public int takeMoney(int value){ 
		if(this.goldPocket > value){
			this.goldPocket -= value;
			return value;
		}		
		else{ 
			return 0;
		}
	}

	public void putMoney(int value){ 
		if(value > -1){
			this.goldPocket += value;	
			return 0;
		}
		else{
			return 1;	
		}
	}

	public int putEquipment(Equipement e){ 
		if(this.capacity >= e.weight()){
			this.mainPocket.push(e);
			this.capacity -= e.weight();
			return 0;
		}
		else{ 
			System.out.println("Il n'y a plus assez de place dans le sac...");	
			return 1;
		}
	}

	public Equipement getEquipement(){ 
		Equipement e= this.mainPocket.pop();
		this.capacity += e.weight();
		return e;
	}

}
