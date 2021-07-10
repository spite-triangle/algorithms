package com.triangle.objectadaptor;

public class ObjectAdaptor extends VoltageAdapted{
	private Voltage v;

	@Override
	public float outputVoltage5v() {
		System.out.println("开始转换电压。。");
		float outv = v.outputVoltage();
		return outv/44;
	}

	public Voltage getV() {
		return v;
	}

	public void setV(Voltage v) {
		this.v = v;
	}


}
