package com.triangle.abstraction;

import com.triangle.implementor.Brand;

public class PadPhone extends AbstractPhone{

	public PadPhone(Brand brand){
		this.phoneBrand = brand;
	}

	@Override
	public void open() {
		System.out.println("按开机键。。。");
		this.phoneBrand.open();		
	}

	@Override
	public void unlock() {
		System.out.println("上滑屏幕。。。");	
		this.phoneBrand.unlock();
	}

	@Override
	public void close() {
		System.out.println("按开机键。。。");	
		this.phoneBrand.close();
	}
	
}
