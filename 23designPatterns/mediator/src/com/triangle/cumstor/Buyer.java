package com.triangle.cumstor;

import com.triangle.mediator.Mediator;

public class Buyer extends Cumstor{
	public Buyer(String name,Mediator mediator){
		// 持有中介
		this.mediator = mediator;
		// 注册自己
		mediator.register(name,this);
	}

	@Override
	public void sendMessage(String info) {
		mediator.relay(info, this);
	}

	@Override
	public void receiveMessage(String info, Cumstor cumstor) {

		if(cumstor instanceof Seller1){
			System.out.println("buyer rec: " + info);
		}
		
		if (cumstor instanceof Seller2) {
			System.out.println("buyer rec: " + info);
		}
	}
	
}
