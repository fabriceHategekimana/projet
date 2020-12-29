Facade
=======

Structural Pattern

"On cache la complexité d'un système et son interaction"

Crée une interface de haut niveau pour rendre l'utilisation d'un système complexe plus facile. Ici on a plusieurs formes et on cherche un moyen de les créer simplement. C'est comme la face avant d'une construction. 

public interface Shape {
public class Rectangle implements Shape {
public class Square implements Shape {
public class Circle implements Shape {

public class ShapeMaker {

//MAIN
main()
  ShapeMaker shapeMaker = new ShapeMaker();

  shapeMaker.drawCircle();
  shapeMaker.drawRectangle();
  shapeMaker.drawSquare();		

![facade_design_pattern](../../images/facade_design_pattern.png)
```java

//Use the facade to draw various types of shapes.
//FacadePatternDemo.java
public class FacadePatternDemo {
   public static void main(String[] args) {
      ShapeMaker shapeMaker = new ShapeMaker();

      shapeMaker.drawCircle();
      shapeMaker.drawRectangle();
      shapeMaker.drawSquare();		
   }
}

//Create an interface.
//Shape.java
public interface Shape {
   void draw();
}

//Create concrete classes implementing the same interface.
//Rectangle.java
public class Rectangle implements Shape {

   @Override
   public void draw() {
      System.out.println("Rectangle::draw()");
   }
}

//Square.java
public class Square implements Shape {

   @Override
   public void draw() {
      System.out.println("Square::draw()");
   }
}

//Circle.java
public class Circle implements Shape {

   @Override
   public void draw() {
      System.out.println("Circle::draw()");
   }
}

//Create a facade class.
//ShapeMaker.java
public class ShapeMaker {
   private Shape circle;
   private Shape rectangle;
   private Shape square;

   public ShapeMaker() {
      circle = new Circle();
      rectangle = new Rectangle();
      square = new Square();
   }

   public void drawCircle(){
      circle.draw();
   }
   public void drawRectangle(){
      rectangle.draw();
   }
   public void drawSquare(){
      square.draw();
   }
}

```
