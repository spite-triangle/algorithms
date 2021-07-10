package com.triangle.flyweight;

public class News extends Website{

	public News() {
		this.setType("news");
	}

	@Override
	public void browse(String usename) {
		System.out.println(usename + "浏览" + this.getType());
	}
	
}
