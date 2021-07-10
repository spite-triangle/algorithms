package com.triangle.flyweight;

import java.util.HashMap;
import java.util.Map;

/**
 * 享元工厂，提供稳定的部分。
 */
public class WebsiteManager {
	private Map<String,Website> webs = new HashMap<String,Website>();

	public Website getWeb(String type){

		if (!webs.containsKey(type)) {
			if (type.equals("news")) {
				webs.put(type,new News());	
			}

			if (type.equals("move")) {
				webs.put(type,new Move());	
			}
		}
		return webs.get(type);
	}

}
