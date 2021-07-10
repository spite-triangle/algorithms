package com.triangle.production;

public class Apple extends Fruits{

	public Apple(String name) {
		super(name + "apple");
	}

	@Override
	public void prepare() {
		System.out.println("准备水果：" + name);
	}
}

