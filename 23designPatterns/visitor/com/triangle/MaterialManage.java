package com.triangle;

import java.util.ArrayList;
import java.util.List;

import com.triangle.company.Company;
import com.triangle.material.Material;

/**
 * 对元素进行管理
 */
public class MaterialManage {
	// 储存元素
	List<Material> materials = new ArrayList<Material>();	

	// 访问者，访问元素
	public void accept(Company visitor){
		for (Material material : materials) {
			material.accept(visitor);
		}
	}

	// 添加元素
	public void add(Material material){
		materials.add(material);
	}

	// 移除元素
	public void remove(Material material){
		materials.remove(material);
	}
	
}
