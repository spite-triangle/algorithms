package com.triangle.activity;

/**
 * 状态的抽象类
 */
public abstract class State {

	// 拥有状态的对象
	private Activity activity;

	
	public Activity getActivity() {
		return activity;
	}
	
	public void setActivity(Activity activity) {
		this.activity = activity;
	}
	
	// 状态的行为
	abstract public void participant();

	abstract public void raffle();

	abstract public void receiveAward();

}
