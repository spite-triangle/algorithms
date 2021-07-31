package com.triangle.mediator;

import com.triangle.cumstor.Buyer;
import com.triangle.cumstor.Cumstor;
import com.triangle.cumstor.Seller1;
import com.triangle.cumstor.Seller2;

/**
 * EstateMedium
 */
public class EstateMedium extends Mediator{

	@Override
	public void register(String cumstorName, Cumstor cumstor) {
		this.cumstors.put(cumstorName,cumstor);
	}

	@Override
	public void relay(String info, Cumstor cumstor) {

		if(cumstor instanceof Buyer) {
			cumstors.get("Seller1").receiveMessage(info, cumstor);
			cumstors.get("Seller2").receiveMessage(info, cumstor);
		}
		
		if(cumstor instanceof Seller1){
			cumstors.get("Seller2").receiveMessage(info, cumstor);
		}

		if(cumstor instanceof Seller2){
			cumstors.get("Seller2").receiveMessage(info, cumstor);
		}
	}

	
}