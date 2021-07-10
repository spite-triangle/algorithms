package com.triangle.school;

public class Department extends Component{

	public Department(String name, String desc) {
		super(name, desc);
	}

	@Override
	public void print() {
		System.out.println(this.getName());	
	}	
}
