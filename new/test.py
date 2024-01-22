import unittest
from triangle import *
class TestCalculator(unittest.TestCase):
    def test_positive_side(self):
        self.assertEqual(check_positive_side(-1, 2, 3), False);
        self.assertEqual(check_positive_side(1, 2, -3), False);
        self.assertEqual(check_positive_side(1, 2, 0), False);
        self.assertEqual(check_positive_side(1, 0, -3), False);
        self.assertEqual(check_positive_side(3,2,3), True);
        self.assertEqual(check_positive_side(2, 4, 5), True);
        self.assertEqual(check_positive_side(2, 3, 2), True);
    def test_two_side_sum(self):
        self.assertEqual(two_side_sum(1, 0, 2), False);
        self.assertEqual(two_side_sum(1, 2, 2), True);
        self.assertEqual(two_side_sum(1, 6, 2), False);
        self.assertEqual(two_side_sum(6, 2, 2), False);
        self.assertEqual(two_side_sum(3, 2, 3), True);
        self.assertEqual(two_side_sum(2, 4, 5), True);
        self.assertEqual(two_side_sum(2, 3, 2), True);
    def test_squaer(self):
        self.assertEqual(squaer(3, 3, 2), 2.83)
        self.assertEqual(squaer(2, 3, 2), 1.98)
        self.assertEqual(squaer(2, 4, 5), 3.8)

    def test_max_side(self):
        self.assertEqual(max_side(3, 3, 2), 3);
        self.assertEqual(max_side(2, 3, 2), 3);
        self.assertEqual(max_side(2, 4, 5), 5);

    def test_type_triangle(self):
        self.assertEqual(type_triangle(3, 3, 2), "Равнобедренный треугольник");
        self.assertEqual(type_triangle(2, 3, 2), "Равнобедренный треугольник");
        self.assertEqual(type_triangle(2, 4, 5), "Обычный треугольник");
        self.assertEqual(type_triangle(4, 4, 4), "Равносторонний треугольник");


    def test_type_triangle_v2(self):
        self.assertEqual(type_triangle_v2(3, 3, 2), "Остроугольный треугольник");
        self.assertEqual(type_triangle_v2(2, 3, 2), "Тупоугольный треугольник");
        self.assertEqual(type_triangle_v2(3, 4, 5), "Прямоугольный треугольник");
        self.assertEqual(type_triangle_v2(4, 4, 4), "Остроугольный треугольник");



        
if __name__ == "__main__":
  unittest.main()    



# #include "pch.h"
# #include <gtest/gtest.h>
# #include <Windows.h>
# #include "../../triangle/triangle/Header.h"

# using namespace std;

# TEST(TestCaseName, TestPositiveSide) {
# 	EXPECT_EQ(check_positive_side(-1, 2, 3), false);
# 	EXPECT_EQ(check_positive_side(1, 2, -3), false);
# 	EXPECT_EQ(check_positive_side(1, 2, 0), false);
# 	EXPECT_EQ(check_positive_side(1, 0, -3), false);
# 	EXPECT_EQ(check_positive_side(3,2,3), true);
# 	EXPECT_EQ(check_positive_side(2, 4, 5), true);
# 	EXPECT_EQ(check_positive_side(2, 3, 2), true);
# }

# TEST(TestCaseName, TestTwo_side_sum) {
# 	EXPECT_EQ(two_side_sum(1, 0, 2), false);
# 	EXPECT_EQ(two_side_sum(1, 2, 2), true);
# 	EXPECT_EQ(two_side_sum(1, 6, 2), false);
# 	EXPECT_EQ(two_side_sum(6, 2, 2), false);
# 	EXPECT_EQ(check_positive_side(3, 2, 3), true);
# 	EXPECT_EQ(check_positive_side(2, 4, 5), true);
# 	EXPECT_EQ(check_positive_side(2, 3, 2), true);
# }


# TEST(TestCaseName, TestSquaerTriangle) {
# 	EXPECT_EQ(squaer_triangle(3, 3, 2), float(2.83));
# 	EXPECT_EQ(squaer_triangle(2, 3, 2), float(1.98));
# 	EXPECT_EQ(squaer_triangle(2, 4, 5), float(3.8));
# 	//EXPECT_EQ(squaer_triangle(3.4E+39, 3.4E+39, 3.4E+39), 3.4E+39);
# }


# TEST(TestCaseName, TestMaxSide) {
# 	//EXPECT_EQ(max_side(float(3.4E+39), float(3.4E+39), float(3.4E+39)), float(3.4E+39), 3.4E+39);
# 	//cout << (3.4E+39 == float(3.4E+39)) << endl;
# 	EXPECT_EQ(max_side(2, 3, 2), 3);
# 	EXPECT_EQ(max_side(2, 4, 5), 5);
# }

# TEST(TestCaseName, TestTypeTriangle) {
# 	EXPECT_EQ(type_triangle(3, 3, 2), "Равнобедренный треугольник");
# 	EXPECT_EQ(type_triangle(2, 3, 2), "Равнобедренный треугольник");
# 	EXPECT_EQ(type_triangle(2, 4, 5), "Обычный треугольник");
# 	EXPECT_EQ(type_triangle(4, 4, 4), "Равносторонний треугольник");
# }

# TEST(TestCaseName, TestTypeTriangleV2) {
# 	EXPECT_EQ(type_triangle_v2(3, 3, 2), "Остроугольный треугольник");
# 	EXPECT_EQ(type_triangle_v2(2, 3, 2), "Тупоугольный треугольник");
# 	EXPECT_EQ(type_triangle_v2(3, 4, 5), "Прямоугольный треугольник");
# 	EXPECT_EQ(type_triangle_v2(4, 4, 4), "Остроугольный треугольник");
# }





# TEST(TestCaseName, TestPositiveSide) {
# 	EXPECT_EQ(check_positive_side(-1, 2, 3), false);
# 	EXPECT_EQ(check_positive_side(1, 2, -3), false);
# 	EXPECT_EQ(check_positive_side(1, 2, 0), false);
# 	EXPECT_EQ(check_positive_side(1, 0, -3), false);
# 	EXPECT_EQ(check_positive_side(3,2,3), true);
# 	EXPECT_EQ(check_positive_side(2, 4, 5), true);
# 	EXPECT_EQ(check_positive_side(2, 3, 2), true);
# }

# TEST(TestCaseName, TestTwo_side_sum) {
# 	EXPECT_EQ(two_side_sum(1, 0, 2), false);
# 	EXPECT_EQ(two_side_sum(1, 2, 2), true);
# 	EXPECT_EQ(two_side_sum(1, 6, 2), false);
# 	EXPECT_EQ(two_side_sum(6, 2, 2), false);
# 	EXPECT_EQ(check_positive_side(3, 2, 3), true);
# 	EXPECT_EQ(check_positive_side(2, 4, 5), true);
# 	EXPECT_EQ(check_positive_side(2, 3, 2), true);
# }


# TEST(TestCaseName, TestSquaerTriangle) {
# 	EXPECT_EQ(squaer_triangle(3, 3, 2), float(2.83));
# 	EXPECT_EQ(squaer_triangle(2, 3, 2), float(1.98));
# 	EXPECT_EQ(squaer_triangle(2, 4, 5), float(3.8));
# 	//EXPECT_EQ(squaer_triangle(3.4E+39, 3.4E+39, 3.4E+39), 3.4E+39);
# }


# TEST(TestCaseName, TestMaxSide) {
# 	//EXPECT_EQ(max_side(float(3.4E+39), float(3.4E+39), float(3.4E+39)), float(3.4E+39), 3.4E+39);
# 	//cout << (3.4E+39 == float(3.4E+39)) << endl;
# 	EXPECT_EQ(max_side(2, 3, 2), 3);
# 	EXPECT_EQ(max_side(2, 4, 5), 5);
# }

# TEST(TestCaseName, TestTypeTriangle) {
# 	EXPECT_EQ(type_triangle(3, 3, 2), "Равнобедренный треугольник");
# 	EXPECT_EQ(type_triangle(2, 3, 2), "Равнобедренный треугольник");
# 	EXPECT_EQ(type_triangle(2, 4, 5), "Обычный треугольник");
# 	EXPECT_EQ(type_triangle(4, 4, 4), "Равносторонний треугольник");
# }

# TEST(TestCaseName, TestTypeTriangleV2) {
# 	EXPECT_EQ(type_triangle_v2(3, 3, 2), "Остроугольный треугольник");
# 	EXPECT_EQ(type_triangle_v2(2, 3, 2), "Тупоугольный треугольник");
# 	EXPECT_EQ(type_triangle_v2(3, 4, 5), "Прямоугольный треугольник");
# 	EXPECT_EQ(type_triangle_v2(4, 4, 4), "Остроугольный треугольник");
# }


# int main(int argc, char** arvg) {

# 	SetConsoleCP(1251);
# 	SetConsoleOutputCP(1251);

# 	testing::InitGoogleTest(&argc, arvg);
# 	return RUN_ALL_TESTS();

# }



