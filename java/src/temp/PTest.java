package temp;

public class PTest {
    public static void main(String[] args) {

        Parent parent = new Child();
        System.out.println();
        parent.helloWorld();
        System.out.println();

        Parent parent2 = new Child("chi");
        parent2.helloWorld();
        System.out.println();

        Child child = new Child();
        System.out.println();
        child.helloWorld();
        System.out.println();

        fun(parent);
        fun(child);



    }

    static void fun(Child child){
        System.out.println("child");
    }

    static void fun(Parent parent){
        System.out.println("parent");
    }
}
