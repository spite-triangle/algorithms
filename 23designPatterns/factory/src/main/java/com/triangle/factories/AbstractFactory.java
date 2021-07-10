package com.triangle.factories;
import com.triangle.production.Fruits;

public abstract class AbstractFactory {

	/**
	 * 抽象创建产品的方法
	 */
	public abstract Fruits createProduction(String name); 
}
