package com.triangle.material;

import com.triangle.company.Company;

/**
 * 元素的接口
 */
public interface Material {

	// 接待访问者
	public void accept(Company visitor);
	
}
