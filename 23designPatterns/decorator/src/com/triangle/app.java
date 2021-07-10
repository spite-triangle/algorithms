package com.triangle;

import com.triangle.derocator.Coffee;
import com.triangle.derocator.Commodity;
import com.triangle.derocator.Milk;
import com.triangle.derocator.Sugar;

/**
 * app
 */
public class app {

	public static void main(String[] args) {
		Commodity coffee = new Coffee();

		coffee = new Sugar(coffee);
		coffee = new Milk(coffee);
		coffee = new Sugar(coffee);

		// cost() 与 describe() 方法被递归调用，从修饰一路调用到主体
		System.out.println("cost:" + coffee.cost());
		System.out.println("desc:" + coffee.describe());
	}
}