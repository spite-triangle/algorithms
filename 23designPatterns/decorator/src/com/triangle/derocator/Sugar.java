package com.triangle.derocator;

public class Sugar extends Commodity{
	// 被修饰的对象
	private Commodity decoratedObj;

	public Sugar(Commodity decoratedObj) {
		this.decoratedObj = decoratedObj;
		this.price = 0.5f;
		this.desc = "Sugar";
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
