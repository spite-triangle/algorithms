package com.triangle.activity;

public class ParticipantState extends State{

	public ParticipantState(Activity activity){
		this.setActivity(activity);
	}

	@Override
	public void participant() {
		if (this.getActivity().count <= 0) {
			System.out.println("活动结束");
			this.getActivity().setCurrentState(this.getActivity().getOverState());	
		}else{
			System.out.println("支付20硬币。");	
			// 切换到抽奖状态
			this.getActivity().setCurrentState(this.getActivity().getRaffleState());
		}
	}

	@Override
	public void raffle() {
		System.out.println("先交钱。");	
	}

	@Override
	public void receiveAward() {
		System.out.println("先抽奖。");
	}
	
}
