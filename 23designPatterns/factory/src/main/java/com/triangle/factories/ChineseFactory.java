package com.triangle.factories;


import com.triangle.production.Apple;
import com.triangle.production.Banana;
import com.triangle.production.Fruits;

public class ChineseFactory extends AbstractFactory{

	@Override
	public Fruits createProduction(String name) {
		Fruits production  = null;
		if (name.equals("apple")) {
			production = new Apple("chinese");
			production.prepare();
		}

		if (name.equals("banana")) {
			production = new Banana("chinese");
			production.prepare();
		}

		return production;
	}

}
