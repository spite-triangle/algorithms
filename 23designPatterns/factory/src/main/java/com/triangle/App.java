package com.triangle;

import com.triangle.factories.AbstractFactory;
import com.triangle.factories.ChineseFactory;
import com.triangle.production.Fruits;

public final class App {
    private App() {
    }

    /**
     * Says hello to the world.
     * @param args The arguments of the program.
     */
    public static void main(String[] args) {
        Store mStore = new Store();
        
        AbstractFactory factory = new ChineseFactory();
        Fruits fruit = mStore.getProduction("banana", factory);

        System.out.println(fruit.name);
    }
}
