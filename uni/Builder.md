Builder

Creationnal pattern

For complex object

![Builder_design_pattern](../../images/Builder_design_pattern.png)

- Product – define the type of the complex object.
- Builder – (abstract class or interface) defines all the creation steps. The GetProduct method is used to return the final product.
- ConcreteBuilder – Inherit from Builder. made to create particular complex products. 
- Director – The director class controls the algorithm that generates the final product object. Capture the specific concrete builder according to the parameters given at the construction. It calls methods of the concrete builder in the correct order to generate the product object. The GetProduct method of the builder object can be used to return the product.

Pour une interface donnée, il faudra aussi mettre en place son interface jumelle Builder
Pour un objet, on aura plusieur Builder différents.


## Use case:
On a un ingénieur qui doit construire une maison.
Nous utilison les buidler pour rendre invisible le détail de construction des maisons.

interface HousePlan -> Interface de l'objet complex 
class House implements HousePlan -> objet complex

interface HouseBuilder -> Builder
class IglooHouseBuilder implements HouseBuilder -> concrete builder
class TipiHouseBuilder implements HouseBuilder -> concrete builder

class CivilEngineer -> Director
	- private HouseBuilder houseBuilder; 
	 
class Builder
	- main

//MAIN
main() 
{ 
On construit un Builder igloo
On construit un ingénieur qui se charge de l'igloo

On demande à l'ingénieur de construire l'igloo
On demande à l'ingénieur de donner la maison
} 


```java
class Builder 
{ 
	public static void main(String[] args) 
	{ 
		HouseBuilder iglooBuilder = new IglooHouseBuilder(); 
		CivilEngineer engineer = new CivilEngineer(iglooBuilder); 

		engineer.constructHouse(); 

		House house = engineer.getHouse(); 

		System.out.println("Builder constructed: "+ house); 
	} 
} 
//Builder
interface HousePlan 
{ 
	public void setBasement(String basement); 

	public void setStructure(String structure); 

	public void setRoof(String roof); 

	public void setInterior(String interior); 
} 

// Product
class House implements HousePlan 
{ 

	private String basement; 
	private String structure; 
	private String roof; 
	private String interior; 

	public void setBasement(String basement) 
	{ 
		this.basement = basement; 
	} 

	public void setStructure(String structure) 
	{ 
		this.structure = structure; 
	} 

	public void setRoof(String roof) 
	{ 
		this.roof = roof; 
	} 

	public void setInterior(String interior) 
	{ 
		this.interior = interior; 
	} 

} 

//Buidler
interface HouseBuilder 
{ 

	public void buildBasement(); 

	public void buildStructure(); 

	public void bulidRoof(); 

	public void buildInterior(); 

	public House getHouse(); 
} 

//concreteBuilder
class IglooHouseBuilder implements HouseBuilder 
{ 
	private House house; 

	public IglooHouseBuilder() 
	{ 
		this.house = new House(); 
	} 

	public void buildBasement() 
	{ 
		house.setBasement("Ice Bars"); 
	} 

	public void buildStructure() 
	{ 
		house.setStructure("Ice Blocks"); 
	} 

	public void buildInterior() 
	{ 
		house.setInterior("Ice Carvings"); 
	} 

	public void bulidRoof() 
	{ 
		house.setRoof("Ice Dome"); 
	} 

	public House getHouse() 
	{ 
		return this.house; 
	} 
} 

//concreteBuilder
class TipiHouseBuilder implements HouseBuilder 
{ 
	private House house; 

	public TipiHouseBuilder() 
	{ 
		this.house = new House(); 
	} 

	public void buildBasement() 
	{ 
		house.setBasement("Wooden Poles"); 
	} 

	public void buildStructure() 
	{ 
		house.setStructure("Wood and Ice"); 
	} 

	public void buildInterior() 
	{ 
		house.setInterior("Fire Wood"); 
	} 

	public void bulidRoof() 
	{ 
		house.setRoof("Wood, caribou and seal skins"); 
	} 

	public House getHouse() 
	{ 
		return this.house; 
	} 

} 

//director
class CivilEngineer 
{ 

	private HouseBuilder houseBuilder; 

	public CivilEngineer(HouseBuilder houseBuilder) 
	{ 
		this.houseBuilder = houseBuilder; 
	} 

	public House getHouse() 
	{ 
		return this.houseBuilder.getHouse(); 
	} 

	public void constructHouse() 
	{ 
		this.houseBuilder.buildBasement(); 
		this.houseBuilder.buildStructure(); 
		this.houseBuilder.bulidRoof(); 
		this.houseBuilder.buildInterior(); 
	} 
} 

```
