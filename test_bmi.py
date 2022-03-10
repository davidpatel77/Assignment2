
#import sys
#sys.path.append("..")

from bmi_cal import bmi_cal
import unittest

class test_bmi_val(unittest.TestCase):
    def test_bmi_input_height(person):
        bm=bmi_cal()
        person.assertEqual(bm.calculate_bmi(0,0,0),"Height can not be zero")
        person.assertEqual(bm.calculate_bmi(-1,0,0),"Height can not be negative")
        person.assertEqual(bm.calculate_bmi(-1,-1,0),"Height can not be negative")
        person.assertEqual(bm.calculate_bmi(0,0,1000),"Height can not be zero")
        person.assertEqual(bm.calculate_bmi(-1,0,1000),"Height can not be negative")
        person.assertEqual(bm.calculate_bmi(-1,-1,-1),"Height can not be negative")
        person.assertEqual(bm.calculate_bmi(5,-1,0),"Height can not be negative")
        person.assertEqual(bm.calculate_bmi(0,12,0),"Inches value should be in between 0 to 11")
        person.assertEqual(bm.calculate_bmi(11,0,0),"Height can not be 11 feet or more")
        person.assertEqual(bm.calculate_bmi(11,0,-1),"Height can not be 11 feet or more")
        person.assertEqual(bm.calculate_bmi(11,0,140),"Height can not be 11 feet or more")
        person.assertEqual(bm.calculate_bmi(11,0,1000),"Height can not be 11 feet or more")
        person.assertEqual(bm.calculate_bmi(11,0,1000),"Height can not be 11 feet or more")

    def test_bmi_input_weight(person):
        bm = bmi_cal()
        person.assertEqual(bm.calculate_bmi(5,11,0),"Weight can not be zero or negative")
        person.assertEqual(bm.calculate_bmi(5,11,-1),"Weight can not be zero or negative")
        person.assertEqual(bm.calculate_bmi(6,3,1000),"Your bmi is 192.0 and you are obese")

    def test_bmi_valid(person):
        bm=bmi_cal()
        person.assertEqual(bm.calculate_bmi(5,0,140),"Your bmi is 28.0 and you are over weight")