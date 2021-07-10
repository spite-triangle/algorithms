package com.triangle.builders;

public class CartoonParlour extends AbstractParlourBuilder{

	@Override
	public void buildWall() {
		System.out.println("创建墙壁。。。");
		this.mParlour.setWall("插画墙");
	}

	@Override
	public void buildTV() {
		System.out.println("购买电视。。。");	
		this.mParlour.setTV("bilibili");
	}

	@Override
	public void buildSofa() {
		System.out.println("购买沙发。。。");
		this.mParlour.setSofa("木头椅子");	
	}
}
