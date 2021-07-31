package com.triangle.cumstor;

import com.triangle.mediator.Mediator;

/**
 * 同事抽象类
 */
public abstract class Cumstor {
	// 关联中介对象
	protected Mediator mediator;

	public void setMediator(Mediator mediator) {
		this.mediator = mediator;
	}

	public Mediator getMediator() {
		return mediator;
	}

	// 发消息给中介
	public abstract void sendMessage(String info);

	// 从中介接收消息
	public abstract void receiveMessage(String info,Cumstor cumstor);

}
