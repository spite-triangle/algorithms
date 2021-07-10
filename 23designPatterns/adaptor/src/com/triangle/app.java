package com.triangle;

import com.triangle.interfaceadaptor.InterfaceAdaptor;
import com.triangle.objectadaptor.ObjectAdaptor;
import com.triangle.objectadaptor.Voltage;

/**
 * app
 */
public class app {

	public static void main(String[] args) {

		// 对象适配器
		Voltage v = new Voltage();
		System.out.println("电压：" + v.outputVoltage());
		ObjectAdaptor adaptor = new ObjectAdaptor();
		adaptor.setV(v);
		System.out.println("电压：" + adaptor.outputVoltage5v());

		// 接口适配器
		InterfaceAdaptor interAdaptor = new InterfaceAdaptor(){
			@Override
			public void interface1() {
				System.out.println("hello");
			}
		};
		
		interAdaptor.interface1();
	}	
}