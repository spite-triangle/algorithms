package com.triangle;

import com.triangle.cumstor.Buyer;
import com.triangle.cumstor.Seller1;
import com.triangle.cumstor.Seller2;
import com.triangle.mediator.EstateMedium;
import com.triangle.mediator.Mediator;

/**
 * App
 */
public class App {

	public static void main(String[] args) {
		Mediator mediator = new EstateMedium();	
		Buyer buyer = new Buyer("buyer",mediator);
		Seller1 seller1 = new Seller1("Seller1",mediator);
		Seller2 seller2 = new Seller2("Seller2",mediator);

		System.out.println("===========ask===============");
		buyer.sendMessage("ask");

		System.out.println("============exchange=============");
		seller1.sendMessage("ask");

		System.out.println("================buy=================");
		buyer.sendMessage("buy");
	}	
}