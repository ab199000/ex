from ugol import proverka
import unittest
class TestTriangleCheck(unittest.TestCase):

    def gran1_triangle(self):
        self.assertEqual(proverka(
            -2147483646, -2147483647, -2147483648),
            "Это невозможный треугольник. Стороны треугольника не могут быть меньше или равны нулю")

    def gran_triangle(self):
        self.assertEqual(proverka(
            2147483646, 2147483647, 2147483648), "Это прямоугольный треугольник. Площадь = 1.9969186231178143e+18")

    def equilateral_triangle(self):
        self.assertEqual(proverka(
            1, 1, 1), "Это равносторонний треугольник. Площадь: 0.4330127018922193")

    def equilateral_triangle1(self):
        self.assertEqual(proverka(
            1312, 1312, 123), "Это равносторонний треугольник. Площадь: 0.4330127018922193")

    # ошибка неправильный вид тр

    def scalene_triangle(self):
        self.assertEqual(proverka(
            2, 3, 4), "Это разносторонний треугольник. Площадь: 2.9047375096555625")

    def scalene_triangle1(self):
        self.assertEqual(proverka(
            900, 815, 758), "Это разносторонний треугольник. Площадь: 289687.2327484204")

    def scalene_triangle2(self):
        self.assertEqual(proverka(
            189912, 139272, 189912), "Это разносторонний треугольник. Площадь: 12303598434.334677")

    # ошибка неправильный вид тр

    def isosceles_triangle(self):
        self.assertEqual(proverka(
            3, 4, 3), "Это равнобедренный треугольник. Площадь: 6")

    def test_is_error1(self):
        self.assertEqual(proverka(
            1, 2, 3), "Это невозможный треугольник. Сумма двух любых сторон треугольника не может быть меньше третьей")

    def test_check_error2(self):
        self.assertEqual(proverka(
            1, 2, 0), "Это невозможный треугольник. Стороны треугольника не могут быть меньше или равны нулю")

    def test_check_error3(self):
        self.assertEqual(proverka(
            848, 901, 2), "Это невозможный треугольник. Стороны треугольника не могут быть меньше или равны нулю")

    def test_check_error4(self):
        self.assertEqual(proverka(
            0, 0, 0), "Это невозможный треугольник. Стороны треугольника не могут быть меньше или равны нулю")

    def test_check_error5(self):
        self.assertEqual(proverka(
            -1, 2, 4), "Это невозможный треугольник. Стороны треугольника не могут быть меньше или равны нулю")


if __name__ == "__main__":
    unittest.main()
