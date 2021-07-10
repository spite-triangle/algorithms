package com.triangle.builders;

import com.triangle.production.Parlour;

/**
 * 构造器管理器
 */
public class ParlourManager {
	private AbstractParlourBuilder builder;

	public void setBuilder(AbstractParlourBuilder builder) {
		this.builder = builder;
	}	

	/**
	 * 组装产品控制
	 */
	public Parlour decorate(){
		this.builder.buildWall();	
		this.builder.buildSofa();
		this.builder.buildTV();
		return this.builder.getResult();
	}
}
