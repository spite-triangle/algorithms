package com.triangle.flyweight;

public class Move extends Website{

	public Move(){
		this.setType("move");
	}	

	@Override
	public void browse(String usename) {
		System.out.println(usename + "浏览" + this.getType());
	}
	
}
