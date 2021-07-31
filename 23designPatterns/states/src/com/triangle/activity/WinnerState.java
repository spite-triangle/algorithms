package com.triangle.activity;

public class WinnerState extends State {

	public WinnerState(Activity activity){
		this.setActivity(activity);
	}

	@Override
	public void participant() {
		System.out.println("正在颁奖。");	
	}

	@Override
	public void raffle() {
		System.out.println("正在颁奖。");	
	}

	@Override
	public void receiveAward() {
		System.out.println("颁奖。");
		this.getActivity().count -= 1;
		this.getActivity().setCurrentState(this.getActivity().getParticipantState());
	}
}