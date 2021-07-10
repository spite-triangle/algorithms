package com.triangle.abstraction;

import com.triangle.implementor.Brand;

/**
 * 执行行为的抽象化 
 */
public abstract class AbstractPhone {
	protected Brand phoneBrand;

	public Brand getPhoneBrand() {
		return phoneBrand;
	}

	public void setPhoneBrand(Brand phoneBrand) {
		this.phoneBrand = phoneBrand;
	}

	/**
	 * 抽象的行为
	 */

	public abstract void open();

	public abstract void unlock();

	public abstract void close();
}
