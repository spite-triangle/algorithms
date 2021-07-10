package com.triangle.derocator;

/**
 * 被修饰的对象
 */
public class Coffee extends Commodity{

	public Coffee(){
		this.price = 5.0f;
		this.desc = "coffee";
	}

	@Override
	public float cost() {
		return this.price;
	}

	@Override
	public String describe() {
		return this.desc;
	}
	
}
