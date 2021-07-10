package com.triangle;

import com.triangle.abstraction.AbstractPhone;
import com.triangle.abstraction.BarPhone;
import com.triangle.abstraction.PadPhone;
import com.triangle.implementor.Huawei;
import com.triangle.implementor.Nokia;

/**
 * app
 */
public class app {

	public static void main(String[] args) {

		AbstractPhone phone = new PadPhone(new Huawei());
		phone.open();
		phone.unlock();
		phone.close();

		System.out.println("===============================");
		AbstractPhone phone1 = new BarPhone(new Nokia());
		phone1.open();
		phone1.unlock();
		phone1.unlock();
	}
}