package com.triangle.derocator;

/**
 * 修饰和被修饰的父类 
 */
public abstract class Commodity {

	protected float price;
	protected String desc;

	
	/**
	 * 公共的功能方法
	 */
	public abstract float cost();
	public abstract String describe();
		
}
