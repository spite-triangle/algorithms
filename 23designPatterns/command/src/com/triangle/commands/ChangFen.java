package com.triangle.commands;

import com.triangle.chief.ChangFenChief;

/**
 * 具体命令实现
 */
public class ChangFen extends Breakfast {

	private ChangFenChief  chief;

	public ChangFen(ChangFenChief chief){
		this.chief = chief;
	}

	@Override
	public void cooking() {
		chief.cooking();
	}

	@Override
	public void undo() {
		chief.undo();	
	}
	
}
