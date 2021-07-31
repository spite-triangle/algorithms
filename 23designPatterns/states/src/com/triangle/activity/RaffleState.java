package com.triangle.activity;

public class RaffleState extends State {

	public RaffleState(Activity activity){
		this.setActivity(activity);
	}

	@Override
	public void participant() {
		System.out.println("正在抽奖。");	
	}

	@Override
	public void raffle() {
		double rand = Math.random();
		if (rand > 0.5) {
			System.out.println("抽到了。。");
			this.getActivity().setCurrentState(this.getActivity().getWinnerState());	
		}else{
			System.out.println("没中。。");
			this.getActivity().setCurrentState(this.getActivity().getParticipantState());
		}
	}

	@Override
	public void receiveAward() {
		System.out.println("还未中奖。");	
	}
	
}
