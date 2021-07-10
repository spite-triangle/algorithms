package com.triangle;

import com.triangle.school.Component;
import com.triangle.school.Department;
import com.triangle.school.School;
import com.triangle.school.University;

/**
 * App
 */
public class App {

	public static void main(String[] args) {
		// 根级
		Component university = new University("南京理工大学","国防");

		// 院级
		Component computerSchool = new School("计算机学院","计算机");
		Component engerySchool = new School("能源与动力学院","能源，动力");

		computerSchool.add(new Department("软件工程", "软件工程"));
		computerSchool.add(new Department("网络工程","网络工程"));

		engerySchool.add(new Department("动力工程","动力工程"));
		engerySchool.add(new Department("热物理","热物理"));
		
		// 添加两个院
		university.add(computerSchool);
		university.add(engerySchool);

		university.print();
	}
}