Compose Pattern
================

## Définition
Problème:
part-whole hierarchie?

![composite_design_pattern](../../images/composite_design_pattern.png)

Crée un arbre et fait exécuter des éléments dans les nodes.
C'est comm si on manipule une un groupe d'objet avec une seule instance seulement.

## Composition:
4 membres:
1. Component: L'interface qui défini le protocole de comunication
2. Leaf: définit le comportement des enfants (les plus bas)
3. Composite: Contient les enfants et fait des actions en rapport avec eux.
4. Client: manipule les objet de la composition par le biais de l'interface
## Exemple:

On peut donc définir une action sur le parent et l'action va être reproduite par les enfants.


## Définitions	
| classe           | rôle      | description                  |
|------------------|-----------|------------------------------|
| CompanyDirectory | Composite | répartie la companie en bloc |
| Manager          | Leaf      | type d'employé               |
| Developer        | Leaf      | type d'employé               |
| Employee         | Component | interface                    |
| Company          | Client    | interface                    |
 
## Pseudocode
main () 
    On crée deux Developpers
    on crée une CompanyDirectory
    on ajoute les deux Developpers dans la CompanyDirectory
    
    On crée deux Manager
    on crée une autre CompanyDirectory
    on ajoute les deux Manager dans la CompanyDirectory
    
    on crée une troisième CompanyDirectory
    on y ajoute les deux précédentes CompanyDirectory
    On fait un showEmployeeDetails (tout les CompanyDirectory vont appeller les Employee et tout les Employee vont se présenter)

## Code
```java
public class Company 
{ 
	public static void main (String[] args) 
	{ 
		Developer dev1 = new Developer(100, "Lokesh Sharma", "Pro Developer"); 
		Developer dev2 = new Developer(101, "Vinay Sharma", "Developer"); 
		CompanyDirectory engDirectory = new CompanyDirectory(); 
		engDirectory.addEmployee(dev1); 
		engDirectory.addEmployee(dev2); 
		
		Manager man1 = new Manager(200, "Kushagra Garg", "SEO Manager"); 
		Manager man2 = new Manager(201, "Vikram Sharma ", "Kushagra's Manager"); 
		
		CompanyDirectory accDirectory = new CompanyDirectory(); 
		accDirectory.addEmployee(man1); 
		accDirectory.addEmployee(man2); 
	
		CompanyDirectory directory = new CompanyDirectory(); 
		directory.addEmployee(engDirectory); 
		directory.addEmployee(accDirectory); 
		directory.showEmployeeDetails(); 
	} 
} 

public interface Employee 
{ 
	public void showEmployeeDetails(); 
} 
public class Developer implements Employee 
{ 
	private String name; 
	private long empId; 
	private String position; 

	public Developer(long empId, String name, String position) 
	{ 
		this.empId = empId; 
		this.name = name; 
				this.position = position; 
	} 
	
	@Override
	public void showEmployeeDetails() 
	{ 
		System.out.println(empId+" " +name+); 
	} 
} 

public class Manager implements Employee 
{ 
	private String name; 
	private long empId; 
		private String position; 

	public Manager(long empId, String name, String position) 
	{ 
		this.empId = empId; 
		this.name = name; 
				this.position = position; 
	} 
	
	@Override
	public void showEmployeeDetails() 
	{ 
		System.out.println(empId+" " +name); 
	} 
} 

import java.util.ArrayList; 
import java.util.List; 

public class CompanyDirectory implements Employee 
{ 
	private List<Employee> employeeList = new ArrayList<Employee>(); 
	
	@Override
	public void showEmployeeDetails() 
	{ 
		for(Employee emp:employeeList) 
		{ 
			emp.showEmployeeDetails(); 
		} 
	} 
	
	public void addEmployee(Employee emp) 
	{ 
		employeeList.add(emp); 
	} 
	
	public void removeEmployee(Employee emp) 
	{ 
		employeeList.remove(emp); 
	} 
} 

```
