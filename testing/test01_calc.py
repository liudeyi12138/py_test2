#!/user/bin /env pytnon
# -*- coding:utf-8 -*-
# Author:deyi liu
import allure
import pytest
import yaml
from test_calc.calc import Calc
'''
课后作业： 补全测试用例【 加减乘除】 使用 fixture 装置完成计算机器实例的初始化 
改造 pytest 的运行规则 ,测试用例命名以 calc_开始，【加， 减 ，乘，除】分别为 calc_add, calc_sub，… 
自动添加标签(add, sub, mul, div四种)，只运行标签为 add 和 div的测试用例。
封装 add, div 测试步骤到 yaml 文件中 
'''
test_datas = yaml.safe_load(open("C:/Users/alan/py_test2/datas/t_datas.yml"))

@allure.feature("测试calc")
class TestClac:

    @pytest.fixture()
    @allure.story("实例化")
    def setup(self):
        self.calc = Calc()

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,answer', test_datas["add"])
    @allure.story("测试加法")
    def calc_add(self, setup, a, b, answer):
        result = self.calc.add(a, b)
        # print("答案：{0}".format(result))
        assert result == answer

    @pytest.mark.div
    @pytest.mark.parametrize('a,b,answer', test_datas["div"])
    @allure.story("测试除法")
    def calc_div(self, setup, a, b, answer):
        try:
            result = self.calc.div(a, b)
            assert result == answer
        except ZeroDivisionError as e:
            print(e.message)

    @pytest.mark.sub
    @pytest.mark.parametrize('a,b,answer',  test_datas["sub"])
    @allure.story("测试减法")
    def calc_sub(self, setup, a, b, answer):
        result = self.calc.sub(a, b)
        assert result == answer

    @pytest.mark.mul
    @pytest.mark.parametrize('a,b,answer', test_datas["mul"])
    @allure.story("测试乘法")
    def calc_mul(self, setup, a, b, answer):
        result = self.calc.mul(a, b)
        assert result == answer


if __name__ == '__main__':
    pytest.main(['-vs','-m add or div', 'test01_calc.py'])
