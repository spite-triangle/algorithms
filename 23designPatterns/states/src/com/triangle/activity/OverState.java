package com.triangle.activity;

public class OverState extends State {
	public OverState(Activity activity){
		this.setActivity(activity);
	}

	@Override
	public void participant() {
		System.out.println("抽奖结束。。");	
	}
	
	@Override
	public void raffle() {
		System.out.println("抽奖结束。。");		
	}
	
	@Override
	public void receiveAward() {
		System.out.println("抽奖结束。。");	
	}
	
}
