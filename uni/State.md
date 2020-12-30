State
======

Behavioral pattern.

## Définition
Donne un état interne à un objet pour modifier son comportement.

![state_design_pattern](../../images/state_design_pattern.png)

## Composition:
On transforme l'objet désiré en contexte, on crée une interface State qui va être implémenté par toutes les classes qui vont représenté un comportement différent de l'objet. Ça éviter de faire de faire beaucoup de is-else pour un objet.

## Exemple:
- Context: Defines an interface to client to interact. It maintains references to concrete state object which may be used to define current state of object.
- State: Defines interface for declaring what each concrete state should do.
- ConcreteState: Provides implementation for methods defined in State.

## Définitions	
Exemple avec un AlertStateContext. On peut imaginer un téléphone qui lance des alert, on peut le mettre en mode vibreur, silencieux ou avec du son. 
Ici, chacun de ces mode d'alert représente une implémentation d'une interface State qu'on crée. Comme ça si, on veut changer le comportement du télépohone on change juste sa classe interne avec Silence, Vibreur, etc.


| classe            | rôle          | description                      |
|-------------------|---------------|----------------------------------|
| Silent            | ConcreteState | met le télépnone en silencieux   |
| Vibration         | ConcreteState | met le téléphone en mode vibreur |
| AlertStateContext | Context       | définit le téléphone             |
| MobileAlertState  | State         | Définit le type d'état           |
| StatePattern      | Client        | utilise le téléphone             |

## Pseudocode
main() 
    création d'un AlertStateContext
    On lui fait lancer deux alerts
    On change son état interne grâce à un objet Silence
    On lui fait lancer trois alerts

## Code
```java
// Java program to demonstrate working of 
// State Design Pattern 

class StatePattern 
{ 
	public static void main(String[] args) 
	{ 
		AlertStateContext stateContext = new AlertStateContext(); 
		stateContext.alert(); 
		stateContext.alert(); 
		stateContext.setState(new Silent()); 
		stateContext.alert(); 
		stateContext.alert(); 
		stateContext.alert();		 
	} 
} 

interface MobileAlertState 
{ 
	public void alert(AlertStateContext ctx); 
} 

class AlertStateContext 
{ 
	private MobileAlertState currentState; 

	public AlertStateContext() 
	{ 
		currentState = new Vibration(); 
	} 

	public void setState(MobileAlertState state) 
	{ 
		currentState = state; 
	} 

	public void alert() 
	{ 
		currentState.alert(this); 
	} 
} 

class Vibration implements MobileAlertState 
{ 
	@Override
	public void alert(AlertStateContext ctx) 
	{ 
		System.out.println("vibration..."); 
	} 

} 

class Silent implements MobileAlertState 
{ 
	@Override
	public void alert(AlertStateContext ctx) 
	{ 
		System.out.println("silent..."); 
	} 

} 

```
