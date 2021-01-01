Builder
========

Creationnal pattern

## Définition
**Problème:** On a des objets qui héritent d'une super classe (ou interface), mais ils sont très compliqué à construire pour le client. On aimerait facilité la construction.
**Solution:** On crée une interface Builder (soeur jumelle de la super classe) qui définit comment construire les objets. Les Concretes Builders seront les soeurs des objets et on crée un director qui "constuira" les objets grâce aux ConcreteBuilders. 
Le client aura seulement à utiliser les Builders et le directors pour avoirs ses objets sans rentrer des paramètres super compliqués.

![Builder_design_pattern](images/Builder_design_pattern.png)

## Composition:
- Product: Définit le type de l'objet complexe
- Builder: (abstract class ou interface) définit toute les étape de création et la méthode pour retourner le produit.
- ConcreteBuilder: Hérite de Builder et est utilisé pour créer des porduits complexes.
- Director: Contrôle l'algorithme qui va généré le produit final. Choisi le concrète builder. Manipule le builder.

## Exemple:
Pour une interface donnée, il faudra aussi mettre en place son interface jumelle Builder
Pour un objet, on aura plusieur Builder différents.

## Use case:
On a un ingénieur qui doit construire une maison.
Nous utilison les buidler pour rendre invisible le détail de construction des maisons.

## Définitions	
| classe            | rôle             | description           |
|-------------------|------------------|-----------------------|
| HousePlan         | type             | interface             |
| House             | objet complexe   | définit les maisons   |
| HouseBuilder      | Builder          | interface             |
| IglooHouseBuilder | Concrete Builder | type de maison        |
| TipiHouseBuilder  | Concrete Builder | type de maison        |
| CivilEngineer     | Director         | Construit les maisons |
	 
## Pseudocode
main() 
On construit un Builder igloo
On construit un ingénieur qui se charge de l'igloo

On demande à l'ingénieur de construire l'igloo
On demande à l'ingénieur de donner la maison

## Code
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
