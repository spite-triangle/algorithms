package com.triangle.company;

import com.triangle.material.Cuprum;
import com.triangle.material.Paper;

public class Min implements Company{

	@Override
	public void create(Paper paper) {
		System.out.println("创建纸币。。");
	}

	@Override
	public void create(Cuprum cuprum) {
		System.out.println("创建硬币。。");	
	}
	
}
