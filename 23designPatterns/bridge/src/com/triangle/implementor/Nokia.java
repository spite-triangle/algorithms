package com.triangle.implementor;


public class Nokia implements Brand{

	public Nokia(){}

	@Override
	public void open() {
		System.out.println("Nokia 开机");
	}

	@Override
	public void unlock() {
		System.out.println("Nokia 解锁");
	}

	@Override
	public void close() {
		System.out.println("Nokia 关机");	
	}
	
}
