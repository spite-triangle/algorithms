package com.triangle;

import com.triangle.company.Art;
import com.triangle.company.Company;
import com.triangle.material.Cuprum;
import com.triangle.material.Paper;

/**
 * app
 */
public class app {

	public static void main(String[] args) {
		MaterialManage materials = new MaterialManage();

		materials.add(new Paper());
		materials.add(new Cuprum());

		Company art = new Art();

		materials.accept(art);

	}
	
}