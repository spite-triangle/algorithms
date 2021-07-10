package com.triangle.production;

/**
 * Fruits
 */
public abstract class Fruits {

	public String name;

	public Fruits(String name) {
		this.name = name;
	}

	/**
	 * 产品初始
	 */
	public abstract void prepare();
	
}