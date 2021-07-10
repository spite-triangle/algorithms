package com.triangle.builders;

import com.triangle.production.Parlour;

/**
 * 抽象构造器
 */
public abstract class AbstractParlourBuilder {

	/**
	 * 设定产品
	 */
	protected Parlour mParlour = new Parlour();

	/**
	 * 产品的制作流程
	 */
	public abstract void buildWall();
	public abstract void buildTV();
	public abstract void buildSofa();

	/**
	 * 获取构建好的产品
	 */
	public Parlour getResult() {
		return mParlour;
	}
}
