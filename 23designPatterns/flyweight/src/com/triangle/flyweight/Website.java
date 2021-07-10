package com.triangle.flyweight;

/**
 * 可共享部分的抽象类
 */
public abstract class Website {
	private String type;

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	/**
	 * 同样的操作
	 */
	public abstract void browse(String usename);

}
