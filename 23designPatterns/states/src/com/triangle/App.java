package com.triangle;

import com.triangle.activity.Activity;

/**
 * App
 */
public class App {

	public static void main(String[] args) {
		Activity activity = new Activity();
		for (int i = 0; i <50;i++){
			System.out.println("========== " + i  + " ===========");
			activity.getCurrentState().participant();
			activity.getCurrentState().raffle();
			activity.getCurrentState().receiveAward();
		}
	}
}