package com.triangle.implementor;

public class Huawei implements Brand {

	public Huawei(){}

	@Override
	public void open() {
		System.out.println("Huawei 开机");
	}

	@Override
	public void unlock() {
		System.out.println("Huawei 解锁");	
	}

	@Override
	public void close() {
		System.out.println("Huawei 关机");
	}
	
}
