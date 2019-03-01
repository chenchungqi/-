爬虫部分：
整个的过程大概分为三步：
S1：从抽奖公示页获取所有中奖者的微博ID
S2：由每个中奖者的微博ID进入其相应主页，获得需要的个人信息（性别、地区、生日）
S3：对收集到的信息进行相应的汇总保存

可视化部分：
1.首先通过手动转格式将csv格式转换为xlsx格式方便读取的处理
2.可视化分为三个文件，分别是city_analysis（分析中奖用户的城市分布）、sex_analysis(分析中奖用户的性别分布)、xingzuo_analysis（分析中奖用户的星座分布）
3.可视化主要使用到了pyecharts这个第三方库
4.在分析星座分布时对数据进行了二次处理
5.城市分布调用了中国地图更为直观的体现
![city_analysis](https://github.com/chenchungqi/weibo/blob/master/%E5%BE%AE%E5%8D%9A%E4%B8%AD%E5%A5%96%E7%94%A8%E6%88%B7%E7%9C%81%E4%BB%BD%E5%88%86%E5%B8%83%E5%9B%BE.png)
![sex_analysis](https://github.com/chenchungqi/weibo/blob/master/%E4%B8%AD%E5%A5%96%E7%94%A8%E6%88%B7%E7%94%B7%E5%A5%B3%E6%AF%94%E4%BE%8B%E7%A4%BA%E6%84%8F%E5%9B%BE.png)
![xingzuo_analysis](https://github.com/chenchungqi/weibo/blob/master/%E4%B8%AD%E5%A5%96%E7%94%A8%E6%88%B7%E6%98%9F%E5%BA%A7%E5%88%86%E5%B8%83%E5%9B%BE.png)
