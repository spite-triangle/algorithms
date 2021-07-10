package com.triangle.production;

public class Banana extends Fruits{

	public Banana(String name) {
		super(name + " banana");

	}

	@Override
	public void prepare() {
		System.out.println("准备水果：" + name);	
	}
	
}
