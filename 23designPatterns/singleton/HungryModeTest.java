/**
 * HungryMode
 */
public class HungryModeTest {

	public static void main(String[] args) {
		new Thread(()->{
			HungryMode a = HungryMode.getInstance();
			System.out.println(a);
		}).start();

		new Thread(()->{
			HungryMode a = HungryMode.getInstance();
			System.out.println(a);
		}).start();
	}
	
}

/**
 * HungryMode
 */
class HungryMode {

	// 直接靠类加载的初始化，生成实列
	private static HungryMode instance = new HungryMode();	

	private HungryMode(){}

	// 获取实列
	public static HungryMode getInstance() {
		return instance;	
	}
		
}