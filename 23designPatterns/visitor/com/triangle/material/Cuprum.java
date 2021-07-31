package com.triangle.material;

import com.triangle.company.Company;

public class Cuprum implements Material{

	@Override
	public void accept(Company visitor) {
		visitor.create(this);
	}
	
}
