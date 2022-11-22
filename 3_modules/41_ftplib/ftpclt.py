#coding:utf-8
#ftp演示，首先要在本机或远程服务器开启ftp功能
import sys,os,ftplib,socket
print("=====================FTP客户端=====================");

# ftpHost = '145.192.1.'  #FTP主机
# ftpName = "pzftp"
# ftpPassword = "pz123456"
ftpHost = '145.192.1.15'  #FTP主机
ftpName = "kali"
ftpPassword = "kali"
__buffer_size = 8192

#连接登陆
def connect(host,username,password):
    try:
        ftp = ftplib.FTP(host)
        # ftp.login()#登录，参数user，password，acct均是可选参数，
        if (username != '') and (password != ''):
            ftp.login(username, password)
        return ftp
    except Exception as e:
        print("error:ftp connect :",e)
        print("error:FTP登陆失败，请检查主机号、用户名、密码是否正确")
        sys.exit(0)
    print('已连接到： "%s"' % HOST)

#中断并退出
def disconnect(ftp):
    ftp.quit()  #FTP.close()：单方面的关闭掉连接。FTP.quit():发送QUIT命令给服务器并关闭掉连接

#上传文件
def upload(ftp, filepath):
    f = open(filepath, "rb")
    file_name = os.path.split(filepath)[-1]
    try:
        ftp.storbinary('STOR %s'%file_name, f, __buffer_size)
        print('成功上传文件： "%s"' % file_name)
    except ftplib.error_perm:
        return False
    return True

#下载文件
def download(ftp, filename):
    f = open(filename,"wb").write
    try:
        ftp.retrbinary("RETR %s"%filename, f, __buffer_size)
        print('成功下载文件： "%s"' % filename)
    except ftplib.error_perm:
        return False
    return True

#获取目录下文件或文件夹想详细信息
def listinfo(ftp):
    ftp.dir()  

#查找是否存在指定文件    
def find(ftp,filename):
    ftp_f_list = ftp.nlst()  #获取目录下文件、文件夹列表
    if filename in ftp_f_list:
        return True
    else:
        return False
