package com.triangle.company;

import com.triangle.material.Cuprum;
import com.triangle.material.Paper;

/**
 * 访问者
 */
public interface Company {
	
	// 创建
	public void create(Paper paper);

	// 创建
	public void create(Cuprum cuprum);

}
