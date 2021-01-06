import configparser
from config.globalparameter import config_path


class ConfigData(object):

    def __init__(self):
        self.conf = self.get_config_obj()

    def get_config_obj(self):
        conf_obj = configparser.ConfigParser()
        conf_obj.read(config_path,encoding='utf-8')
        return conf_obj

    def get_values(self,sec_name,opt_name):
        try:
            return self.conf.get(sec_name,opt_name)
        except Exception as e:
            return e

    def get_email(self,optn):
        eml_name = self.conf.sections()[0]
        return self.get_values(eml_name,optn)

    def get_recipients(self,opname): #获取收件人
        rec = self.get_email(opname)
        if rec!=None:
            re = rec.split(';')
            return re
        else:
            return None


if __name__ == "__main__":
    c = ConfigData()
    # result = c.get_values('email','host')
    result = c.get_recipients('recipients')
    print(result)