package com.triangle;

import com.triangle.flyweight.Website;
import com.triangle.flyweight.WebsiteManager;

/**
 * App
 */
public class App {

	public static void main(String[] args) {
		WebsiteManager manager = new WebsiteManager();

		Website web = manager.getWeb("news");
		web.browse("young");

		web = manager.getWeb("move");
		web.browse("triangle");

		web = manager.getWeb("news");
		web.browse("li");

	}
}