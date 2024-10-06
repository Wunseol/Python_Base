python_智能统计学技术

简单来说就是爬虫+数据分析

这个项目让我学会了什么？

互联网数据获取

熟悉网页构造
html
xml
css
json
菜鸟教程里面有，自学就行


requests库

numpy库

matplotlib库

pyplot库

pandas库

Numpy、Pandas、Matplotlib是Python数据科学领域的三个重要的常用库







利用python的各种库对数据进行处理

对数据进行可视化





主线
    互联网数据获取
        爬虫技术自学就行

    网页构造
        html
            xml
            css
            json
            菜鸟教程里面有这个自学就行


    树结构
                                        html html
                 head head                       body  body
        title title                            div div

    requests库
        学习它的各种方法

    numpy库
        学习它的各种方法

    matplotlib库
        学习它的各种方法

    pyplot
        流程图

    pandas
        series
        dataframe


Numpy、Pandas、Matplotlib是Python数据科学领域的三个重要的常用库，功能分别如下：
    Numpy
        Numpy: Numpy是Python数值计算最基础的库，它提供了一个高性能的多维数组对象，以及许多用于数组计算的函数。使用Numpy，我们可以方便地进行基础的数学、统计和线性代数计算，比如矩阵乘法、数组运算、傅里叶变换等等。
        Numpy 是python科学计算的基础包，本书大部分内容都基于numpy以及构建于其上的库。其功能有：
            快速高效的多维数组对象ndarray
            用于对数组执行元素级计算以及直接对数组执行数字运算的函数
            用于读写硬盘上基于数组的数据集的工具
            线性代数运算，傅里叶变换，以及随机数生成
            用于将C,C++,Fortran代码集成到python的工具
            除了为python提供快速的数组处理能力，numpy在数据分析方面还有一个主要作用，即作为在算法之间传递数据的容器。对于数值型数据，numpy 数组在储存和处理数据时要比内置的python数据结构高效得多。

        PPT
            NumPy 数值计算基础
                数据的维度
                    从一个数据到一组数据
                    维度：一组数据的组织形式
                    一维数据
                    列表和数组
                    二维数据
                    多维数据
                    高维数据
                    数据维度的Python表示

                掌握 NumPy数组对象 ndarray
                    NumPy是一个开源的Python科学计算基础库，包含：
                    一个强大的N维数组对象  ndarray
                    广播功能函数
                    整合C/C++/Fortran代码的工具
                    线性代数、傅里叶变换、随机数生成等功能
                    NumPy是SciPy、  Pandas等数据处理或科学计算库的基础

                NumPy的引用
                    import numpy as np
                    引入模块的别名
                    尽管别名可以省略或更改，建议使用上述约定的别名

                N维数组对象：ndarray
                    Python已有列表类型，为什么需要一个数组对象(类型)？
                    数组对象可以去掉元素间运算所需的循环，使一维向量更像单个数据
                    设置专门的数组对象，经过优化，可以提升这类应用的运算速度
                    观察：科学计算中，一个维度所有数据的类型往往相同
                    数组对象采用相同的数据类型，有助于节省运算和存储空间
                    ndarray是一个多维数组对象，由两部分构成：
                    实际的数据
                    描述这些数据的元数据（数据维度、数据类型等）
                    ndarray数组一般要求所有元素类型相同（同质），数组下标从0开始

                创建数组对象
                    1．数组属性：ndarray（数组）是存储单一数据类型的多维数组。
                           属性    	  说明   
                          ndim    	  返回 int。表示数组的维数
                          shape    	  返回 tuple。表示数组的尺寸，对于  n 行 m 列的矩阵，形状为(n,m)
                          size          返回 int。表示数组的元素总数，等于数组形状的乘积
                          dtype    	  返回 data-type。描述数组中元素的类型
                          itemsize    	  返回 int。表示数组的每个元素的大小（以字节为单位）。

                    2．数组创建
                        numpy.array(object, dtype=None, copy=True, order='K',subok=False, ndmin=0)
                          参数名称    	  说明   
                          object    	  接收array。表示想要创建的数组。无默认。   
                          dtype    	  接收data-type。表示数组所需的数据类型。如果未给定，则选择保存对象所需的最小类型。默认为None。   
                          ndmin    	  接收int。指定生成数组应该具有的最小维数。默认为None。   
                        创建数组并查看数组属性
                        重新设置数组的shape 属性
                        使用arange 函数创建数组
                        使用zeros函数创建数组，数据类型默认是float
                        使用eye函数创建数组，返回一个二维数组，其中对角线为1
                        使用diag函数创建数组
                        使用ones函数创建数组

                    3．数组数据类型
                        数组数据类型转换
                        查看数据类型，可以直接查看或者使用numpy.dtype函数查看。
                        数组的类型变换：astype()方法会创建新的数组（原始数据的一个拷贝），即使两个类型一致


                生成随机数
                    无约束条件下生成随机数
                    生成服从均匀分布的随机数
                    生成服从正态分布的随机数
                    生成给定上下范围的随机数，如创建一个最小值不低于2、最大值不高于10的2行5列数组
                    random模块常用随机数生成函数

                通过索引和切片访问数组
                    1．一维数组的索引和切片

                    2．多维数组的索引和切片


                变换数组的形态
                    改变数组形状
                        使用ravel函数展平数组
                        使用flatten函数展平数组

                    组合数组
                        使用hstack函数实现数组横向组合：np.hstack((arr1,arr2))
                        使用vstack函数实现数组纵向组合：np.vstack((arr1,arr2))
                        使用concatenate函数实现数组横向组合：np.concatenate((arr1,arr2),axis = 1))
                        使用concatenate函数实现数组纵向组合：np.concatenate((arr1,arr2),axis = 0))

                    切割数组
                        使用hsplit函数实现数组横向分割： np.hsplit(arr1,2)
                        使用vsplit函数实现数组纵向分割： np.vsplit(arr, 2)
                        使用split函数实现数组横向分割： np.split(arr, 2, axis=1)
                        使用split函数实现数组纵向分割：np.split(arr, 2, axis=0)
                        ls =a.tolist()


                掌握 NumPy矩阵与通用函数
                    矩阵是ndarray的子类
                    矩阵继承自Numpy数组对象的二维数组对象
                    使用mat函数与matrix函数创建矩阵
                    np.mat()函数用于将输入解释为矩阵；
                    data： mat可以从字符串或列表中生成。如果data是字符串，则将其解释为以逗号或空格分隔列的矩阵，以及分隔行的分号。
                    创建NumPy矩阵
                    使用bmat函数将小矩阵组合成大矩阵
                    NumPy矩阵计算针对整个矩阵中的每个元素进行，其运算速度比使用for循环更快。
                    NumPy矩阵计算针对整个矩阵中的每个元素进行，其运算速度比使用for循环更快。
                    矩阵的运算

                认识ufunc函数
                    全称通用函数（universalfunction），是一种能够对数组中所有元素进行操作的函数。
                    四则运算：加（+）、减（-）、乘（*）、除（/）、幂（**）。数组间的四则运算表示对每个数组中的元素分别进行四则运算，所以形状必须相同。
                    比较运算：>、<、==、>=、<=、!=。比较运算返回的结果是一个布尔数组，每个元素为每个数组对应元素的比较结果。
                    逻辑运算：np.any函数表示逻辑“or”，np.all函数表示逻辑“and”。运算结果返回布尔值。
                    比较运算：

                    逻辑运算：


                ufunc函数的广播机制
                    广播（broadcasting）是指不同形状的数组之间执行算术运算的方式。
                    当使用ufunc函数进行数组计算时，ufunc函数会对两个数组的对应元素进行计算。进行这种计算的前提是两个数组的shape一致。若两个数组的shape不一致，则NumPy会实行广播机制。为了更好地使用广播机制，需要遵循4个原则。
                    让所有输入数组都向其中shape最长的数组看齐，shape中不足的部分都通过在前面加1补齐。
                    输出数组的shape是输入数组shape的各个轴上的最大值。
                    如果输入数组的某个轴和输出数组的对应轴的长度相同或者其长度为1时，这个数组能够用来计算，否则出错。
                    当输入数组的某个轴的长度为1时，沿着此轴运算时都用此轴上的第一组值。

                利用 NumPy进行统计分析
                    读写文件
                        NumPy文件读写主要有二进制的文件读写和文件列表形式的数据读写两种形式
                        读取文本格式的数据
                        savetxt函数：将数组写到某种分隔符隔开的文本文件中。
                            np.savetxt("../tmp/arr.txt",arr,fmt="%d",delimiter=",")

                        loadtxt函数：把文件加载到一个二维数组中。
                            np.loadtxt("../tmp/arr.txt",delimiter=",")

                        读取文本格式的数据
                        genfromtxt函数面向的是结构化数组和缺失数据。
                            np.genfromtxt("../tmp/arr.txt",delimiter = ",")


                    使用数组进行简单统计分析
                        直接排序
                            sort函数是最常用的排序方法。 arr.sort()
                            sort函数也可以指定一个axis参数，使得sort函数可以沿着指定轴对数据集进行排序。
                            axis=1为沿横轴排序； axis=0为沿纵轴排序。

                        间接排序
                            argsort方法返回值为重新排序值的下标。 arr.argsort()
                            lexsort函数返回值是按照最后一个传入数据排序的。 np.lexsort((a,b,c))

                        去重与重复数据
                            通过unique函数可以找出数组中的唯一值并返回已排序的结果。
                            tile函数主要有两个参数，参数“A”指定重复的数组，参数“reps”指定重复的次数。
                            np.tile(A，reps)
                            repeat函数主要有三个参数，参数“a”是需要重复的数组元素，参数“repeats”是重复次数，参数“axis”指定沿着哪个轴进行重复，axis= 0表示按行进行元素重复；axis= 1表示按列进行元素重复。
                            numpy.repeat(a,repeats, axis=None)
                            这两个函数的主要区别在于，tile函数是对数组进行重复操作，repeat函数是对数组中的每个元素进行重复操作。


                    常用的统计函数
                        当axis=0时，表示沿着纵轴计算。当axis=1时，表示沿着横轴计算。默认时计算一个总值。
                          函数    	  说明   
                          sum    	  计算数组的和
                          mean    	  计算数组均值
                          std    	  计算数组标准差
                          var    	  计算数组方差
                          min    	  计算数组最小值
                          max    	  计算数组最大值
                          argmin    	  返回数组最小元素的索引
                          argmax    	  返回数组最小元素的索引
                          cumsum    	  计算所有元素的累计和
                          cumprod    	  计算所有元素的累计积
                        一元函数
                            对ndarray中的数据执行元素级运算的函数。
                              函数    	  说明   
                                np.abs(x) np.fabs(x)    	    计算数组各元素的绝对值
                                np.sqrt(x)    	    计算数组各元素的平方根
                                np.square(x)    	      计算数组各元素的平方
                                np.log(x) np.log10(x)    np.log2(x)    	    计算数组各元素的自然对数、  10底对数和2底对数
                                np.ceil(x) np.floor(x)            计算数组各元素的ceiling值  或 floor值
                                np.abs(x) np.fabs(x)    	    计算数组各元素的绝对值
                              函数    	  说明   
                                np.rint(x)            计算数组各元素的四舍五入值
                                np.modf(x)            将数组各元素的小数和整数部分以两个独立数组形式返回
                                np.cos(x) np.cosh(x) np.sin(x) np.sinh(x) np.tan(x) np.tanh(x)                计算数组各元素的普通型和双曲型三角函数
                                np.exp(x)    	    计算数组各元素的指数值
                                np.sign(x)    	    计算数组各元素的符号值，  1(+), 0,  ‐1( ‐ )
                                np.rint(x)    	    计算数组各元素的四舍五入值

                        任务实现
                            读取iris数据集中的花萼长度数据（已保存为csv格式），并对其进行排序、去重，并求出和、累积和、均值、标准差、方差、最小值、最大值






    Pandas
        Pandas: Pandas是基于Numpy的另一个Python数据科学库，主要用于数据的整理、处理和分析。Pandas提供数据结构，例如Series（一维标记数组）和DataFrame（二维标记数组），使得数据处理变得更高效和简洁。Pandas还提供了多种数据读取和输出工具，例如读写CSV文件、Excel文件、数据库等，方便我们进行数据的导入导出操作。
        Pandas提供了使我们能够快速便捷地处理结构化数据的大量数据结构和函数。它是使python成为强大而高效的数据分析环境的重要因素之一。本书用的最多的pandas对象是dataframe,它是一个面向列的二维表结构，且含有行标和列标。
        Pandas兼具numpy高性能的数组计算功能以及电子表格和关系型数据库（SQL）灵活的数据处理功能。它提供了复杂精细的索引功能，以便更为便捷地完成重塑，切片和切块聚合以及选取数据子集等操作。
        ppt
            pandas统计分析基础
                Pandas库与数据类型
                    Pandas库
                        Pandas是Python第三方库，提供高性能易用数据类型和分析工具
                        import pandas as pd
                        Pandas基于NumPy实现，常与NumPy和Matplotlib一同使用
                        两个数据类型： Series,DataFrame
                        基于上述数据类型的各类操作：基本操作、运算操作、特征类操作、关联类操作


                Pandas库的Series类型
                    Series类型由一组数据及与之相关的数据索引组成
                    Series类型可以由如下类型创建：
                        Python列表：index与列表元素个数一致
                        标量值：index表达Series类型的尺寸
                        Python字典：键值对中的“键”是索引， index从字典中进行选择操作
                        ndarray ：索引和数据都可以通过ndarray类型创建
                        其他函数： range()函数等

                    Series类型可以由如下类型创建：
                        标量值： index表达Series类型的尺寸

                    Series类型可以由如下类型创建：
                    Python字典：键值对中的“键”是索引，index从字典中进行选择操作
                    Series类型可以由如下类型创建：
                    ndarray：索引和数据都可以通过ndarray类型创建

                Pandas库中Series类型的基本操作
                    Series类型包括index和values两部分
                    Series类型的操作类似ndarray类型
                    Series类型的操作类似Python字典类型
                    Series类型的操作类似ndarray类型：
                        索引方法相同，采用[]
                        NumPy中运算和操作可用于Series类型
                        可以通过自定义索引的列表进行切片
                        可以通过自动索引进行切片，如果存在自定义索引，则一同被切片

                    Series类型包括index和values两部分
                    index:获得索引
                    values:获得数据
                    Series类型的操作类似ndarray类型
                    Series类型的操作类似Python字典类型：
                    通过自定义索引访问
                    保留字in操作
                    使用 .get()方法

                Pandas库中DataFrame类型
                    DataFrame是一个表格型的数据类型，每列值类型可以不同
                    DataFrame既有行索引、也有列索引
                    DataFrame常用于表达二维数据，但可以表达多维数据
                    DataFrame类型可以由如下类型创建：
                        二维ndarray对象
                        由一维ndarray、列表、字典、元组或Series构成的字典

                    DataFrame类型可以由如下类型创建：
                    二维ndarray对象
                    DataFrame类型可以由如下类型创建：
                    由一维ndarray、列表、字典、元组或Series构成的字典

                读写不同数据源的数据
                    读写文本文件
                        1.文本文件读取
                            使用read_table来读取文本文件。
                            pandas.read_table(filepath_or_buffer, sep=’\t’, header=’infer’, names=None, index_col=None, dtype=None, engine=None, nrows=None)
                            使用read_csv函数来读取csv文件。
                            pandas.read_csv(filepath_or_buffer, sep=’\t’, header=’infer’, names=None, index_col=None, dtype=None, engine=None, nrows=None)
                            read_table和read_csv常用参数及其说明。
                              参数名称    	  说明   
                              filepath    	  接收string。代表文件路径。无默认。   
                              sep    	  接收string。代表分隔符。read_csv默认为“,”，read_table默认为制表符“[Tab]”。   
                              header    	  接收int或sequence。表示将某行数据作为列名。默认为infer，表示自动识别。   
                              names    	  接收array。表示列名。默认为None。   
                              index_col    	  接收int、sequence或False。表示索引列的位置，取值为sequence则代表多重索引。默认为None。   
                              dtype    	  接收dict。代表写入的数据类型（列名为key，数据格式为values）。默认为None。   
                              engine    	  接收c或者python。代表数据解析引擎。默认为c。   
                              nrows    	  接收int。表示读取前n行。默认为None。   
                            read_table和read_csv函数中的sep参数是指定文本的分隔符的，如果分隔符指定错误，在读取数据的时候，每一行数据将连成一片。
                            header参数是用来指定列名的，如果是None则会添加一个默认的列名。
                            encoding代表文件的编码格式，常用的编码有utf-8、utf-16、gbk、gb2312、gb18030等。如果编码指定错误数据将无法读取，IPython解释器会报解析错误。

                        2.文本文件储存
                            文本文件的存储和读取类似，结构化数据可以通过pandas中的to_csv函数实现以csv文件格式存储文件。
                            DataFrame.to_csv(path_or_buf=None, sep=’,’, na_rep=”, columns=None, header=True, index=True,index_label=None,mode=’w’,encoding=None)
                              参数名称    	  说明    	  参数名称    	  说明   
                              path_or_buf    	  接收string。代表文件路径。无默认。    	  index    	  接收boolean，代表是否将行名（索引）写出。默认为True。   
                              sep    	  接收string。代表分隔符。默认为“,”。    	  index_labels    	  接收sequence。表示索引名。默认为None。   
                              na_rep    	  接收string。代表缺失值。默认为“”。    	  mode    	  接收特定string。代表数据写入模式。默认为w。   
                              columns    	  接收list。代表写出的列名。默认为None。    	  encoding    	  接收特定string。代表存储文件的编码格式。默认为None。   
                              header    	  接收boolean，代表是否将列名写出。默认为True。    	      	     


                    读写Excel文件
                        1.Excel文件读取
                            pandas提供了read_excel函数来读取“xls”“xlsx”两种Excel文件。
                            pandas.read_excel(io, sheetname=0, header=0, index_col=None, names=None, dtype=None)
                              参数名称    	  说明   
                              io    	  接收string。表示文件路径。无默认。   
                              sheetname    	  接收string、int。代表excel表内数据的分表位置。默认为0。   
                              header    	  接收int或sequence。表示将某行数据作为列名。默认为infer，表示自动识别。   
                              names    	  接收int、sequence或者False。表示索引列的位置，取值为sequence则代表多重索引。默认为None。   
                              index_col    	  接收int、sequence或者False。表示索引列的位置，取值为sequence则代表多重索引。默认为None。   
                              dtype    	  接收dict。代表写入的数据类型（列名为key，数据格式为values）。默认为None。   

                        2.Excel文件储存
                            将文件存储为Excel文件，可以使用to_excel方法。其语法格式如下。
                            DataFrame.to_excel(excel_writer=None, sheetname=None’, na_rep=”, header=True, index=True, index_label=None, mode=’w’, encoding=None)
                            to_csv方法的常用参数基本一致，区别之处在于指定存储文件的文件路径参数名称为excel_writer，并且没有sep参数，增加了一个sheetnames参数用来指定存储的Excelsheet的名称，默认为sheet1。



                DataFrame的常用操作
                    查看DataFrame的常用属性
                        基础属性
                          属性    	  返回值   
                          values    	  元素   
                          index    	  索引   
                          columns    	  列名   
                          dtypes    	  类型   
                          size    	  元素个数   
                          ndim    	  维度数   
                          shape    	  数据形状（行列数目）   

                    查改增删DataFrame数据
                        1.查看访问DataFrame中的数据——数据基本查看方式
                            对单列数据的访问：DataFrame的单列数据为一个Series。根据DataFrame的定义可以知晓DataFrame是一个带有标签的二维数组，每个标签相当每一列的列名。有以下两种方式来实现对单列数据的访问。
                            以字典访问某一个key的值的方式使用对应的列名，实现单列数据的访问。
                            以属性的方式访问，实现单列数据的访问。（不建议使用，易引起混淆）
                            对某一列的某几行访问：访问DataFrame中某一列的某几行时，单独一列的DataFrame可以视为一个Series（另一种pandas提供的类，可以看作是只有一列的DataFrame），而访问一个Series基本和访问一个一维的ndarray相同。
                            对多列数据访问：访问DataFrame多列数据可以将多个列索引名称视为一个列表，同时访问DataFrame多列数据中的多行数据和访问单列数据的多行数据方法基本相同。
                            对某几行访问：
                            如果只是需要访问DataFrame某几行数据的实现方式则和上述的访问多列多行相似，选择所有列，使用“:”代替即可。
                            head和tail也可以得到多行数据，但是用这两种方法得到的数据都是从开始或者末尾获取的连续数据。默认参数为访问5行，只要在方法后方的“()”中填入访问行数即可实现目标行数的查看。

                        1.查看访问DataFrame中的数据——loc，iloc访问方式
                            loc方法是针对DataFrame索引名称的切片方法，如果传入的不是索引名称，那么切片操作将无法执行。利用loc方法，能够实现所有单层索引切片操作。loc方法使用方法如下。
                            DataFrame.loc[行索引名称或条件, 列索引名称]
                            iloc和loc区别是iloc接收的必须是行索引和列索引的位置。iloc方法的使用方法如下。
                            DataFrame.iloc[行索引位置, 列索引位置]
                            使用loc方法和iloc实现多列切片，其原理的通俗解释就是将多列的列名或者位置作为一个列表或者数据传入。
                            使用loc，iloc方法可以取出DataFrame中的任意数据。
                            在loc使用的时候内部传入的行索引名称如果为一个区间，则前后均为闭区间；iloc方法使用时内部传入的行索引位置或列索引位置为区间时，则为前闭后开区间。
                            loc内部还可以传入表达式，结果会返回满足表达式的所有值。
                            若使用detail.iloc[detail['order_id']=='458',[1,5]]读取数据，则会报错，原因在于此处条件返回的为一个布尔值Series，而iloc可以接收的数据类型并不包括Series。根据Series的构成只要取出该Series的values就可以了。需改为detail.iloc[(detail['order_id']=='458').values,[1,5]])。
                            loc更加灵活多变，代码的可读性更高，iloc的代码简洁，但可读性不高。具体在数据分析工作中使用哪一种方法，根据情况而定，大多数时候建议使用loc方法。

                        1.查看访问DataFrame中的数据——切片方法之ix
                            ix方法更像是loc和iloc两种切片方法的融合。ix方法在使用时既可以接收索引名称也可以接收索引位置。其使用方法如下。
                            DataFrame.ix[行索引的名称或位置或者条件, 列索引名称或位置]
                            使用ix方法时有个注意事项：当索引名称和位置存在部分重叠时，ix默认优先识别名称。
                            控制ix方法需要注意以下几点。
                            使用ix参数时，尽量保持行索引名称和行索引位置重叠，使用时就无须考虑取值时区间的问题。一律为闭区间。
                            使用列索引名称，而非列索引位置。主要用来保证代码可读性。
                            使用列索引位置时，需要注解。同样保证代码可读性。
                            除此之外ix方法还有一个缺点，就是在面对数据量巨大的任务的时候，其效率会低于loc和iloc方法，所以在日常的数据分析工作中建议使用loc和iloc方法来执行切片操作。

                        2.更新修改DataFrame中的数据
                            更改DataFrame中的数据，原理是将这部分数据提取出来，重新赋值为新的数据。
                            需要注意的是，数据更改直接针对DataFrame原数据更改，操作无法撤销，如果做出更改，需要对更改条件做确认或对数据进行备份。

                        3.为DataFrame增添数据
                            DataFrame添加一列的方法非常简单，只需要新建一个列索引。并对该索引下的数据进行赋值操作即可。
                            新增的一列值是相同的则直接赋值一个常量即可。

                        4.删除某列或某行数据
                            删除某列或某行数据需要用到pandas提供的方法drop，drop方法的用法如下。
                            axis为0时表示删除行，axis为1时表示删除列。
                            drop(labels, axis=0, level=None, inplace=False, errors='raise')
                            常用参数如下所示。
                              参数名称    	  说明   
                              labels    	  接收string或array。代表删除的行或列的标签。无默认。
                              axis    	  接收0或1。代表操作的轴向。默认为0。
                              levels    	  接收int或者索引名。代表标签所在级别。默认为None。
                              inplace          接收boolean。代表操作是否对原数据生效。默认为False。



                描述分析DataFrame数据
                    1.数值型特征的描述性统计——NumPy中的描述性统计函数
                        数值型数据的描述性统计主要包括了计算数值型数据的完整情况、最小值、均值、中位数、最大值、四分位数、极差、标准差、方差、协方差和变异系数等。在NumPy库中一些常用的统计学函数如下表所示。
                        pandas库基于NumPy，自然也可以用这些函数对数据框进行描述性统计。
                          函数名称    	  说明    	  函数名称    	  说明
                          np.min    	  最小值    	  np.max    	  最大值
                          np.mean    	  均值    	  np.ptp    	  极差
                          np.median    	  中位数    	  np.std    	  标准差
                          np.var          方差          np.cov          协方差
                        pandas还提供了更加便利的方法来计算均值 ，如detail['amounts'].mean()。
                        pandas还提供了一个方法叫作describe，能够一次性得出数据框所有数值型特征的非空值数目、均值、四分位数、标准差。
                          方法名称    	  说明    	  方法名称    	  说明
                          min    	  最小值    	  max    	  最大值
                          mean    	  均值    	  ptp    	  极差
                          median    	  中位数    	  std    	  标准差
                          var    	  方差    	  cov    	  协方差
                          sem    	  标准误差    	  mode    	  众数
                          skew    	  样本偏度    	  kurt    	  样本峰度
                          quantile    	  四分位数    	  count    	  非空值数目
                          describe          描述统计          mad          平均绝对离差

                    2.类别型特征的描述性统计
                        描述类别型特征的分布状况，可以使用频数统计表。pandas库中实现频数统计的方法为value_counts。
                        pandas提供了categories类，可以使用astype方法将目标特征的数据类型转换为category类别。
                        describe方法除了支持传统数值型以外，还能够支持对category类型的数据进行描述性统计，四个统计量分别为列非空元素的数目，类别的数目，数目最多的类别，数目最多类别的数目。


                转换字符串时间为标准时间
                    pandas时间相关的类
                        在多数情况下，对时间类型数据进行分析的前提就是将原本为字符串的时间转换为标准时间类型。pandas继承了NumPy库和datetime库的时间相关模块，提供了6种时间相关的类。
                              类名称          说明
                              Timestamp          最基础的时间类。表示某个时间点。在绝大多数的场景中的时间数据都是Timestamp形式的时间。
                              Period    	  表示单个时间跨度，或者某个时间段，例如某一天，某一小时等。
                              Timedelta          表示不同单位的时间，例如1天，1.5小时，3分钟，4秒等，而非具体的某个时间段。
                              DatetimeIndex          一组Timestamp构成的Index，可以用来作为Series或者DataFrame的索引。
                              PeriodtimeIndex          一组Period构成的Index，可以用来作为Series或者DataFrame的索引。
                              TimedeltaIndex          一组Timedelta构成的Index，可以用来作为Series或者DataFrame的索引。

                        提取时间序列数据信息
                            Timestamp类型
                                其中Timestamp作为时间类中最基础的，也是最为常用的。在多数情况下，时间相关的字符串都会转换成为Timestamp。pandas提供了to_datetime函数，能够实现这一目标。
                                值得注意的是，Timestamp类型时间是有限制的。
                                在多数涉及时间相关的数据处理，统计分析的过程中，需要提取时间中的年份，月份等数据。使用对应的Timestamp类属性就能够实现这一目的。
                                结合Python列表推导式，可以实现对DataFrame某一列时间信息数据的提取。
                                  属性名称    	  说明    	  属性名称    	  说明   
                                  year    	  年    	  week    	  一年中第几周
                                  month    	  月    	  quarter    	  季节
                                  day    	  日    	  weekofyear    	  一年中第几周
                                  hour    	  小时    	  dayofyear    	  一年中的第几天
                                  minute    	  分钟    	  dayofweek    	  一周第几天
                                  second          秒          weekday          一周第几天
                                  date    	  日期    	  weekday_name    	  星期名称
                                  time          时间          is_leap_year          是否闰年

                            DatetimeIndex与PeriodIndex函数
                                除了将数据字原始DataFrame中直接转换为Timestamp格式外，还可以将数据单独提取出来将其转换为DatetimeIndex或者PeriodIndex。
                                转换为PeriodIndex的时候需要注意，需要通过freq参数指定时间间隔，常用的时间间隔有Y为年，M为月，D为日，H为小时，T为分钟，S为秒。两个函数可以用来转换数据还可以用来创建时间序列数据，其参数非常类似。

                            DatetimeIndex与PeriodIndex函数及其参数说明
                                DatetimeIndex和PeriodIndex两者区别在日常使用的过程中相对较小，其中DatetimeIndex是用来指代一系列时间点的一种数据结构，而PeriodIndex则是用来指代一系列时间段的数据结构。
                                  参数名称    	  说明   
                                  data    	  接收array。表示DatetimeIndex的值。无默认。
                                  freq    	  接收string。表示时间的间隔频率。无默认。
                                  start    	  接收string。表示生成规则时间数据的起始点。无默认。
                                  periods    	  表示需要生成的周期数目。无默认。
                                  end          接收string。表示生成规则时间数据的终结点。无默认。
                                  tz    	  接收timezone。表示数据的时区。默认为None。
                                  name          接收int，string。默认为空。指定DatetimeIndex的名字。
                                提取时间序列数据信息
                                在DatetimeIndex和PeriodIndex中提取信息
                                Ø在DatetimeIndex和PeriodIndex中提取对应信息可以以类属性方式实现。
                                Ø值得注意的是PeriodIndex相比于DatetimeIndex少了weekday_name属性，所以不能够用该属性提取星期名称数据。若想要提取信息名称可以通过提取weekday属性，而后将0-6四个标签分别赋值为Monday至Sunday。

                            加减时间数据
                            Timedelta类
                                Timedelta是时间相关的类中的一个异类，不仅能够使用正数，还能够使用负数表示单位时间，例如1秒，2分钟，3小时等。使用Timedelta类，配合常规的时间相关类能够轻松实现时间的算术运算。目前Timedelta函数中时间周期中没有年和月。所有周期名称，对应单位及其说明如下表所示。
                                  周期名称    	  单位    	  说明    	  周期名称    	  单位    	  说明
                                  weeks          无          星期          seconds          s          秒
                                  days    	  D    	  天    	  milliseconds    	  ms    	  毫秒
                                  hours    	  h    	  小时    	  microseconds    	  us    	  微妙
                                  minutes          m          分          nanoseconds          ns          纳秒
                                使用Timedelta ，可以很轻松地实现在某个时间上加减一段时间 。
                                除了使用Timedelta实现时间的平移外，还能够直接对两个时间序列进行相减，从而得出一个Timedelta。







    Matplotlib
        Matplotlib: Matplotlib是一个绘图库，用于绘制各种图形，包括线图、柱形图、饼图、散点图、等高线图等等。Matplotlib可以将数据可视化为图形进行分析和展示，有助于我们更好地理解和解释数据。Matplotlib还提供了很多的自定义选项，可以使得图形更加漂亮和易于阅读。
        Matplotlib是最流行的用于绘制数据图表的python库。它非常适合创建出版物上用的图表。它和ipython结合得很好，因而提供了一种非常好用的交互式数据绘图环境。绘制的图表也是交互式，可以利用绘制窗口中的工具栏放大图表中的某个区域对整个图表进行平移浏览。
        ppt
            Matplotlib数据可视化基础
                matplotlib库介绍

                Matplotlib库使用
                    Matplotlib库由各种可视化类构成，内部结构复杂
                    matplotlib.pyplot是绘制各类可视化图形的命令子库，相当于快捷方式
                    import matplotlib.pyplot as plt

                Matplotlib库小测
                    plt.plot()只有一个输入列表或数组时，参数被当作Y轴，X轴以索引自动生成
                    plt.savefig()将输出图形存储为文件，默认PNG格式，可以通过dpi修改输出质量
                    plt.plot(x,y)当有两个以上参数时，按照X轴和Y轴顺序绘制数据点

                pyplot绘图区域
                    在全局绘图区域中创建一个分区体系，并定位到一个子绘图区域
                        plt.subplot(nrows, ncols, plot_number)
                        plt.subplot(3,2,4)        
                        plt.subplot(324)
                        plt.subplot(211)
                        plt.subplot(212)


                pyplot的plot()函数
                    plt.plot(x, y, format_string, **kwargs)
                        x: X轴数据，列表或数组，可选
                        y: Y轴数据，列表或数组
                        format_string: 控制曲线的格式字符串，可选
                        **kwargs : 第二组或更多(x,y,format_string)
                        当绘制多条曲线时，各条曲线的x不能省略

                    format_string:控制曲线的格式字符串，可选由颜色字符、风格字符和标记字符组成
                    例子

                pyplot的文本显示
                    pyplot的中文显示（第一种方法）
                        pyplot并不默认支持中文显示，需要rcParams修改字体实现

                    pyplot的中文显示（第二种方法）
                        在有中文输出的地方，增加一个属性： fontproperties
                            函数    	    说明   
                            plt.xlabel()            对X轴增加文本标签
                            plt.ylabel()              对Y轴增加文本标签
                            plt.title()    	    对图形整体增加文本标签
                            plt.text()    	    在任意位置增加文本
                            plt.annotate()    	    在图形中增加带箭头的注解


                pyplot基础图表函数
                          函数          说明
                          plt・plot(x,y,fmt,..)          绘制一个坐标图
                          plt.boxplot(data,notch,position)    	  绘制一个箱形图
                          plt.bar(left,height,width,bottom)    	  绘制一个条形图
                          plt.barh(width,bottom^left,height)    	  绘制一个横向条形图
                          plt・polar(theta,  r)    	  绘制极坐标图
                          plt.pie(data,  explode)    	  绘制饼图

                          函数          说明
                          plt.psd(x,NFFT=256,pad_to,Fs)          绘制功率谱密度图
                          plt.specgram(x,NFFT=256,pad_to^  F)    	  绘制谱图
                          plt.cohere(x,y,NFFT=256,Fs)    	  绘制X-Y的相关性函数
                          plt.scatter(x,y)    	  绘制散点图，其中，x和y长度木晌
                          plt.step(x,y,where)    	  绘制步阶图
                          plt・hist(x,bins,normed)    	  绘制直方图

                          函数    	  说明   
                              plt.contour(X,Y,Z,N)    	  绘制等值图
                              plt.vlines()    	  绘制垂直图
                              plt.stem(x,y,linefmt.,marl<er-f:mt)    	  绘制柴火图
                              plt.plot_date()    	  绘制数据日期








