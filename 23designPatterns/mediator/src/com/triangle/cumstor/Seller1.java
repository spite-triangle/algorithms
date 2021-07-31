package com.triangle.cumstor;

import com.triangle.mediator.Mediator;

public class Seller1 extends Cumstor{

	public Seller1(String name,Mediator mediator){
		// 持有中介
		this.mediator = mediator;
		// 注册自己
		mediator.register(name,this);
	}

	@Override
	public void sendMessage(String info) {
		// 将信息发给中介处理
		mediator.relay(info, this);
	}

	@Override
	public void receiveMessage(String info,Cumstor cumstor) {
		if (info.equals("ask") && cumstor instanceof Buyer) {
			System.out.println("Seller1:12");
		}

		if(info.equals("buy") && cumstor instanceof Buyer){
			System.out.println("Seller1: 买我的。");
		}

		if (info.equals("ask") && cumstor instanceof Seller2) {
			System.out.println("Seller1:12");
		}
	}
	
}
