package com.triangle.production;


/**
 * 定义产品
 */
public class Parlour {

	private String TV;	
	private String sofa;
	private String wall;

	public void getConfiguration() {
		System.out.println("TV is " + TV);
		System.out.println("sofa is " + sofa);
		System.out.println("wall is " + wall);
	}

	public String getSofa() {
		return sofa;
	}
	public String getWall() {
		return wall;
	}
	public void setWall(String wall) {
		this.wall = wall;
	}
	public String getTV() {
		return TV;
	}
	public void setTV(String tV) {
		this.TV = tV;
	}
	public void setSofa(String sofa) {
		this.sofa = sofa;
	}
	
}
