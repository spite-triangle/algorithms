package com.triangle.school;

import java.util.ArrayList;
import java.util.List;

public class University extends Component{

	private List<Component> schools = new ArrayList<Component>();

	public University(String name, String desc) {
		super(name, desc);
	}

	@Override
	public void add(Component com) {
		schools.add(com);
	}

	@Override
	public void remove(Component com) {
		schools.remove(com);
	}

	@Override
	public void print() {
		System.out.println(this.getName());

		for (Component component : schools) {
			component.print();
		}
	}
	
}
