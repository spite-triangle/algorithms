package com.triangle.mediator;

import java.util.HashMap;
import java.util.Map;

import com.triangle.cumstor.Cumstor;

/**
 * 中介抽象类
 */
public abstract class Mediator {
	protected Map<String,Cumstor> cumstors = new HashMap<String,Cumstor>();

	// 注册客户
	public abstract void register(String cumstorName, Cumstor cumstor);

	// 接待消息
	public abstract void relay(String info, Cumstor cumstor);

}
