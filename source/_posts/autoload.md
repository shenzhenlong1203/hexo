## PHP类的自动加载

### 类的加载

- require()和include()语句是语言结构，不是真正的函数。
- require()和include()语句也可以不加圆括号而直接加参数。
- require_once() 判断并加载文件。
- include_once() 判断并加载文件。 

		相同点：在脚本执行期间包括运行指定文件

    	不同点： 1.incluce在用到时加载，require在一开始就加载
           	    2.include_once()和require_once()文件中的代码已经被包括了，则不会再次包括，
                以避免函数重定义以及变量重新赋值等问题。
				3.include引入文件的时候，如果碰到错误，会给出提示，并继续运行下边的代码。
				4.require引入文件的时候，如果碰到错误，会给出提示，并停止运行下边的代码。
		问题：   1.多个文件中，类的命名重复问题。
				2. 一个文件中加载多个类文件。


###类的懒加载

- __autoload : 根据类名，找出类文件，然后require _once()
- spl _autoload : spl _autoload _register注册多个自定义的autoload函数

- __autoload : 定义路径法（path）和直接映射法（array）

- spl _autoload : autoload调用堆栈，注册多个自定义的autoload函数

		缺陷： __autoload的最大缺陷是无法有多个autoload方法 

###MVC加载原理

- ![http://123.56.234.128/szl/flow.png](http://123.56.234.128/szl/flow.png)

-		1.
		'include' => array( 'application/catalog/controllers',
	    'application/catalog/models', ),
	    $include => array('application/controllers', 'application/models', 'application/library'); 
	    set_include_path(get_include_path() . PATH_SEPARATOR .implode(PATH_SEPARATOR, $config['include']));
 
		2.public static function autoload($class) 
			{ 
				$path = ''; 
				$path = str_replace('_', '/', $class) . '.php'; 
				include_once($path); 
			} 
		} 
		/** 
		* sql自动加载 
		*/ 
		spl_autoload_register(array('Loader', 'autoload')); 

		3. 路由实例化并唤醒类方法
			public function route() 
			{ 
				if (class_exists($this->getController())) { 
				$rc = new ReflectionClass($this->getController()); 
				if ($rc->hasMethod($this->getAction())) { 
					$controller = $rc->newInstance(); 
					$method = $rc->getMethod($this->getAction()); 
					$method->invoke($controller); 
				} else 
					throw new Exception('no action'); 
				} else 
					throw new Exception('no controller'); 
			} 

###Composer加载原理

- __autoload 只能全局下加载，但在命名空间下无法实现

- composer（包管理器）的应用

-![http://123.56.234.128/szl/composer.png](http://123.56.234.128/szl/composer.png)
	
	1. psr-0
	
			{
	  			"autoload": {
	   			 "psr-0": {
	     		 "Foo\\": "src/",
	   			 }
	  			}
			}
	路径生成： "Foo\\Bar\\Baz.php" 
	2. psr-4
	
			{
	  			"autoload": {
	   			 "psr-4": {
	     		 "Foo\\": "src/",
	   			 }
	  			}
			}
	路径生成： "src/Foo/Bar/Baz.php"
	3. class-map
	
			{
			  "autoload": {
			    "classmap": ["src/", "lib/", "Something.php"]
			  }
			}
	路径生成： "src/Something.php"
	4. files
	 
			{
			  "autoload": {
			    "files": ["src/MyLibrary/functions.php"]
			  }
			}
	生成一个array


- 加载原理

![http://123.56.234.128/szl/autoload.png](http://123.56.234.128/szl/autoload.png)

###其他

composer加载第三方库的演示

###参考文档
1. [http://www.cnblogs.com/xia520pi/p/3697099.html]("http://www.cnblogs.com/xia520pi/p/3697099.html")
2. [http://www.jb51.net/article/31399.htm]("http://www.jb51.net/article/31399.htm")
3. [http://www.jb51.net/article/53876.htm]("http://www.jb51.net/article/53876.htm")