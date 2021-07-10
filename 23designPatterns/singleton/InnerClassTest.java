public class InnerClassTest {
	public static void main(String[] args) {
		InnerClass a = InnerClass.getInstance();
		InnerClass b = InnerClass.getInstance();
		System.out.println(a);
		System.out.println(b);
	}
}

class InnerClass{

	// 静态内部类
	private static class InnerInstance{
		private static InnerClass instance = new InnerClass();
	}

	private InnerClass(){}

	public static InnerClass getInstance() {
		return InnerInstance.instance;	
	}
}
