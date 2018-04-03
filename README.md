# serialPortScanning
串口扫描，测试连接工具
scanning_port() 扫描当前都是那些串口是开放的
read_port() 读取串口的数据
ser = serial.Serial('/dev/cu.usbserial', 19200, timeout=1) 一定要看下设备的波率 要不然读取的数据是乱码
