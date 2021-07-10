package com.triangle.school;

/**
 * 所有层级的父类
 */
public abstract class Component {
	private String name;
	private String desc;

	public Component(String name, String desc) {
		this.setName(name);
		this.setDesc(desc);
	}

	/**
	 * 通用的管理方法
	 */
	public void add(Component com){
		throw new UnsupportedOperationException();
	}

	public void remove(Component com){
		throw new UnsupportedOperationException();
	}

	/**
	 * 递归输出
	 */
	public abstract void print();

	public String getDesc() {
		return desc;
	}

	public void setDesc(String desc) {
		this.desc = desc;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}



}
