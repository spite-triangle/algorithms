package com.triangle.company;

import com.triangle.material.Cuprum;
import com.triangle.material.Paper;

public class Art implements Company {

	@Override
	public void create(Paper paper) {
		System.out.println("创建画纸。。");
	}

	@Override
	public void create(Cuprum cuprum) {
		System.out.println("创建铜像。。");	
	}
	
}
