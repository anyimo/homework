/**
  * Created by 安以陌 on 2018/7/20.
  */
object ZbjScala {
  def main(args: Array[String]) {
    var day = List("周一温度", "周二温度", "周三温度", "周四温度", "周五温度")
    var weather = List("20度", "30度", "35度", "36度", "40度")

    for (i <- Range(0, 5)) {

        println(day(i) + weather(i))

    }
  }
}










