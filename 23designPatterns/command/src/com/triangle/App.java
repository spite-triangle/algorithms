
package com.triangle;

import com.triangle.chief.ChangFenChief;
import com.triangle.commands.ChangFen;
import com.triangle.waiter.Waiter;

/**
 * App
 */
public class App {

	public static void main(String[] args) {

		Waiter waiter = new Waiter();
		waiter.addOrder("chang1", new ChangFen( new ChangFenChief()));
		waiter.addOrder("chang2", new ChangFen( new ChangFenChief()));
		waiter.removeOrder("chang1");

	}


}