package com.triangle;

import com.triangle.factories.AbstractFactory;
import com.triangle.production.Fruits;

public class Store {
	Fruits getProduction(String name,AbstractFactory factory){
		return factory.createProduction(name);
	}
}
