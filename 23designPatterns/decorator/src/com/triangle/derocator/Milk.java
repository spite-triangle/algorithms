package com.triangle.derocator;

public class Milk extends Commodity{
	// 被修饰的对象
	private Commodity decoratedObj;

	public Milk(Commodity decoratedObj) {
		this.decoratedObj = decoratedObj;
		this.price = 1.0f;
		this.desc = "milk";
	}



	@Override
	public float cost() {
		return this.price + this.decoratedObj.cost();
	}

	@Override
	public String describe() {
		return this.desc + " + " + this.decoratedObj.describe();	
	}
	
}
