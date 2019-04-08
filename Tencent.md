时间：120分钟
##不定项选择题
1.FIFO为先进先出的顺序完成页面的访问，而如果在采用先进先出页面淘汰算法的系统中，一进程在内存占3块（开始为空），页面访问序列为1、2、3、4、1、2、5、1、2、3、4、5、6，运行时会产生多少次页面中断？

2.Java接口是一系列方法的声明，是一些方法特征的集合，一个接口只有方法的特征没有方法的实现，下列关于Java接口说法正确的是？Java支持单重继承还是多重继承，一个类可以实现一个接口还是多个接口？

3.在计算机操作系统中，批处理任务是无须人工干预而执行系列程序的作业，现有多个批处理任务1,2,3,4,5同步抵达运算中心，多个批处理任务运行的时常分别是10分钟，6分钟，2分钟，4分钟和8分钟，它们的优先级是3,5,2,1,4，这里5的优先级最高，则在下列各种调度算法中，平均进程的周转时间为14分钟的是？

    A.先来先去服务调度算法
    B.优先级调度算法
    C.时间片轮转调度算法
    D.最短作业优先调度算法
4.{24,26,25,28,27,33,29,32,30,31}是以数组形式存储的最小值，删除堆顶元素24调整后的结果是什么？

5.实时处理框架Storm技术不适用于以下哪个场景？

    数据仓库基础工具
    连续计算
    处理无限的数据流
    分布式文件管理系统
6.假设腾讯大学选课表的表结构如下所示，现在小Q老师希望在课程成绩不小于60分的学生中，找出选修4门及4门以上的学生，并且按照总成绩的降序排列出来，那么正确的sql语句是

    CREATE TABLE 'test'{
    'id' int(11) NOT NULL AUTO_INCREMENT,
    'sid' int(11) DEFAULT NULL COMMENT'学号'
    'cid' int(11) DEFAULT NULL COMMENT'课程号码'
    'score' int(11) DEFAULT NULL COMMENT'课程成绩'
    PRIMARY KEY ('id')
    UNIQUE KEY 'sid'('sid','cid')
    }ENGINE=InnoDB
7.以下c++代码会输出什么？

    #include<iostream>
    using namesapce std;
    class A{
    public:
    	vultual void x()
    	{
    		cont << "A::x()" << endl;
    	}
    };
    class B{
    public:
    	vultual void x()
    	{
    		cont << "B::x()" << endl;
    	}	
    };
    int main()
    {
    A *a=new B;
    a->x();
    return 0;
    }

8.下面选项中对TCP和UDP论述正确的是？
TCP面向字节流，实际上是TCP把数据看成一连串无结构的字节流
TCP支持一对一，一对多，多对一和多对多的交互通信
TCP是面向连接的，如打电话要先拨号建立连接
UDP是无连接的，即发送数据之前不需要建立连接
9.有如下递归函数f(n)，其时间复杂度为多少？

    inf f(int n){
    	if (n<=1) return 1;
    	return (2 * f(n - 1) + 3 * f(n - 2));
    }

10.LRU(最近最少使用算法)是内存管理的一种页面置换算法，对于在内存中但又不用的数据块（内存块）叫做LRU，现假设系统为某进程分配了4个页框，该进程已访问的页面序号为2,0,2,9,3,4,2,8,2,4,8,4,5。若进程要访问的下一页的页号为7，根据LRU算法，应淘汰的页号是什么？

11.下面程序的正确执行结果为

    #include<iostream>
    using namaspace std;

    int g(int);
    void main(){
    	int a=1,i;
    	for(i=0;i<3;i++)
    		cout<<g(a)<<" ";
    	cout<<endl;
    }
    int g(int a){
    	int b=0;
    	static int c=3;
    	b++;
    	c++;
    	return (a+b+c);
    }

12.现假设有N个元素的进栈序列是C1,C2,C3...Cn，若C2=3，以下说法正确的是（）

    C3可能是1
    C1一定是4
    C3可能是2
    C3不可能是4
    C1可能是1

13.平衡二叉排序树要求每个节点的左右子树有着相同高度，或者要求任何节点的左右节点的左右子树高度差不超过1。按照10,30,65,50,90,40的顺序插入，并且插入的过程中不停的调整，那么最后形成的平衡二叉树高度是什么？

14.访问https网站用到了哪些技术

    对称加密技术
    非对称加密技术
    散列（哈希）算法
    数字证书
    安全套接层协议
15.关于以下C++代码哪些行可能会导致编译出错？

	#include <iostream>
	template <typename T>
	class vector
	{
	public:
		void push_back(T const&);//1
		void clear();//2
	private:
		T* elements;//3
	};
	void vector::clear()//4
	{
		//Function body
	}
	int main()
	{
		vector TestVector;//5
	return0;
	}

16.若一个公司的IP地址空间为192.168.33.0/24，要求划分一个子网给一个小组使用，小组最多会使用7台电脑上网，那么给这个小组最少划分的网络前缀长度为（27比特）
17.运用某算法对一数组进行升序排序，第二趟的排序结果为{8,9,10,4,5,6,20,1,2}，那么这个结果可能是以下哪些排序的结果？

    快速排序
    选择排序
    插入排序
    二路归并排序
    冒泡排序
18.在Linux系统中，小q需要在目录/web中查找包含"tencent"字符串的而且以log结尾的文件，以下哪个命令可以满足他的愿望？

    grep -R --include="*.log" "tencent" /web
    find /web | grep "tencent" *.log
    find / web -name "*.log" | grep "tencent"
    find /web "*.log" | xargs cat "tencent"
19.下列3层二叉树都是以数组结构顺序存储，不存在的结点用0表示，那么下列哪些二叉树的先序排列和中序排列相同？

    a b c 0 0 f g
    a b 0 d e 0 0
    a 0 c 0 0 f g
    a 0 c 0 0 0 g
    a b c d e f g
20.下列C++代码会输出什么？

	#include <iostream>
	class A{
	public:
		virtual void func()
		{
			std::cout << "A:func" << std::endl;
		}
	};
	class B{
	private:
		virtual bool func() const
		{
			std::cout << "B:func" << std::endl;
			return true;
		}
	};
	class C : public A, public B{

	};
	
	int main()
	{
		C c;
		c.func();
	}
##编程题
1.
小Q去商场购物，经常会遇到找零的问题。

小Q现在手上有n种不同面值的硬币，每种面值的硬币都有无限多个。

为了方便购物，小Q希望带尽量少的硬币，并且要能组合出1到m之间（包含1和m）的所有面值

输入

    20 4
    1 
    2 
    5 
    10

2.给定一个仅包含0或1的字符串，现在可以对其进行一种操作：

当有两个相邻的字符其中有一个是0另外一个是1的时候，可以消除掉这两个字符。

这样的操作可以一直进行下去直到找不到相邻的0和1为止，问这个字符串经历了操作以后的最短长度

输入 

    4 
    1100
输出

	0

3.小Q打算穿越怪兽谷。他不会打怪，但是他有钱。他知道，只要给怪兽一定的金币，怪兽就会一直护送着他出谷。

在谷中，他会依次遇到N只怪兽，每只怪兽都有自己的武力值和要‘贿赂’它所需的金币数。如果小Q没有‘贿赂’某只怪兽，而这只怪兽的武力值又大于护送他的怪兽武力值之和，这只怪兽就会攻击他。

小Q想知道，要想成功穿越怪兽谷而不被攻击，他最少要准备多少金币。

输入

    3
    6 5 8
    1 1 2

输出

	2