import org.apache.spark.{SparkConf, SparkContext}

import scala.collection.mutable.ListBuffer

/**
  * Created by 安以陌 on 2018/7/23.
  */
/**
  * 1.读取文件textFile
  * 2.过滤"status":0}的数据 filter
  * 3.将 "data":Array[5]转变成多行  flatMap   抚平
  * 4.获取 "school":"华南师范大学",  "plan":"2",
  * 4.获取 "school":"华南师范大学",  "plan":"2",  reduce 缩减
  * 5.学校和招生人数 排序， 按照招生人数排序 。sort
  *
  */
object ZSpark{
  def main(args: Array[String]) {
    import org.json.JSONObject
    import scala.collection.mutable.ListBuffer
    val conf = new SparkConf().setMaster("local").setAppName("qunzi")
    val sc = new SparkContext(conf)
    val resultlist = sc.textFile("总.txt")
      .filter(line=>{
        val isJson = line.startsWith("{\"")&&line.endsWith("}")
        //我们获取itemlist里面的status 如何为hide ，则直接过滤
        var isShow = false
        if(isJson){
          val json = new JSONObject(line)
          val status=json.getJSONObject("mods").getJSONObject("itemlist").getString("status")
            isShow = status.equals("show")//是否是show的数据
            }
            isJson&isShow
            })
            .flatMap(line=>{
            val json = new JSONObject(line)
            val goods=json.getJSONObject("mods").getJSONObject("itemlist").
            getJSONObject("data").getJSONArray("auctions")
            var list = ListBuffer[JSONObject]()
            //将jsonarray转换为scala支持的列表
            for(i<-0 to goods.length()-1){
            list.append(goods.getJSONObject(i))
            }
            list
            })
            .map(line=>{
            val view_price = line.getString("view_price").toFloat
            var price_name = ""
              if(view_price>=2000) {
                price_name = "2000元以上"
              } else if(view_price>=1000) {
                price_name = "1000~2000元"
              } else if(view_price>=200){
            price_name = "200~1000元"
            }else if(view_price>=100){
            price_name = "100~200元"
            }else if(view_price>=50){
            price_name = "50~100元"
            }else if(view_price>=20){
            price_name = "20~50元"
            }else{
            price_name = "1~20元"
            }
            var view_sales = 0
            try{
            view_sales = line.getString("view_sales").replace("人付款","").toInt
            } catch {
            case e:Exception=>{println("付款为零")}
            }
            (price_name,view_sales)//价格区间， 购买人数
            })
            .reduceByKey(_+_)
            .take(7)
            for(i<-resultlist){
            println(i)
            }
            sc.stop()
            }
            }
            object YaSparkTaobaoTest{//统计多少正常数据
            def main(args: Array[String]) {
            // val conf = new SparkConf().setMaster("local").setAppName("qunzi")
            // val sc = new SparkContext(conf)
            // val count = sc.textFile("全班数据1.0.txt")
            // .filter(line=>line.startsWith("{\"")&&line.endsWith("}"))
            // .count()
            // println("总共有"+count)
            // sc.stop()
            println("1人付款".replace("人付款",""))
            }
            }
