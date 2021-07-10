

/**
 * 单例模式：懒汉方案测试
 */
public class LazymodeTest {

	public static void main(String[] args) {
		new Thread(()->{
			Lazymode a = Lazymode.getInstance();
			System.out.println(a);
		}).start();

		new Thread(()->{
			Lazymode a = Lazymode.getInstance();
			System.out.println(a);
		}).start();
	}
	
}

/**
 * Lazymode
 */
class Lazymode {

	// 静态变量：储存位移的实列
	// volatile: 1）保证在流水线执行时，防止指令重排序；2）保持内存可见性，变量的读写直接在内存上执行，不经过缓存。
	private static volatile Lazymode instance;

	// 私有的构造器
	private Lazymode(){}

	// 获取实例
	public static Lazymode getInstance() {
		// 不存在，就造一个
		if (instance == null) {
			// 加锁，防止多线程
			synchronized (Lazymode.class) {
				// 防止多个线程已经突破第一个null检测
				if (instance == null) {
					instance = new Lazymode();
				}
				
			}
		}
		return instance;	
	}		
}