package com.triangle;

import com.triangle.builders.AbstractParlourBuilder;
import com.triangle.builders.CartoonParlour;
import com.triangle.builders.ParlourManager;
import com.triangle.production.Parlour;

public class client {
	public static void main(String[] args) {
		// 管理器：组装产品
		ParlourManager manager = new ParlourManager();
		// 构建器：产品部件的创建
		AbstractParlourBuilder builder = new CartoonParlour();
		manager.setBuilder(builder);
		Parlour room = manager.decorate();
		room.getConfiguration();
	}	
}
