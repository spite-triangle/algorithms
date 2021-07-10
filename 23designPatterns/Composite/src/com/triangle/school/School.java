package com.triangle.school;

import java.util.ArrayList;
import java.util.List;

public class School extends Component{

	private List<Component> departments = new ArrayList<Component>();

	public School(String name, String desc) {
		super(name, desc);
	}

	@Override
	public void add(Component com) {
		departments.add(com);
	}

	@Override
	public void remove(Component com) {
		departments.remove(com);
	}

	@Override
	public void print() {
		System.out.println(this.getName());

		for (Component component : departments) {
			component.print();
		}
	}
	

}
