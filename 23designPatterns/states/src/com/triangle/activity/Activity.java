package com.triangle.activity;

public class Activity {

	private State currentState = null;	
	private State participantState = null;
	private State raffleState = null;
	private State winnerState = null;
	private State overState = null;

	public int count = 0;

	public Activity(){
		this.participantState = new ParticipantState(this);
		this.raffleState = new RaffleState(this);
		this.winnerState = new WinnerState(this);
		this.overState = new OverState(this);

		this.currentState = this.participantState;

		count = 2;
	}

	public State getCurrentState() {
		return currentState;
	}
	public State getWinnerState() {
		return winnerState;
	}
	public State getOverState() {
		return overState;
	}
	public State getParticipantState() {
		return participantState;
	}
	public State getRaffleState() {
		return raffleState;
	}
	public void setCurrentState(State currentState) {
		this.currentState = currentState;
	}


}
