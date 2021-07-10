package com.triangle.abstraction;

import com.triangle.implementor.Brand;

public class BarPhone extends AbstractPhone{

	public BarPhone(Brand brand){
		this.phoneBrand = brand;
	}

	@Override
	public void open() {
		System.out.println("按任意键。。。");
		this.phoneBrand.open();		
	}

	@Override
	public void unlock() {
		System.out.println("长按#。。。");	
		this.phoneBrand.unlock();
	}

	@Override
	public void close() {
		System.out.println("按开机键。。。");	
		this.phoneBrand.close();
	}
	

}
