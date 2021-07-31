package com.triangle.waiter;

import java.util.HashMap;
import java.util.Map;

import com.triangle.commands.Breakfast;

/**
 * 命令管理者
 */
public class Waiter {
	private Map<String,Breakfast> orders = new HashMap<String,Breakfast>();

	public void addOrder(String order,Breakfast breakfast){
		this.orders.put(order,breakfast);	
		// 开始烹饪
		breakfast.cooking();
	}

	public void removeOrder(String order){
		if (orders.containsKey(order)) {
			// 撤销
			this.orders.get(order).undo();;
			// 移除
			this.orders.remove(order);
		}
	} 


}
