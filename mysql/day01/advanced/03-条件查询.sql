-- SELECT 字段列表 FROM 表名 WHERE 条件列表;
-- 运算符
-- stu_id < 5 并且 class = 1的学生
SELECT * FROM student WHERE stu_id < 5 AND class_id = 1;

-- 模糊查询
-- 姓名是关开始的学生信息
SELECT * FROM student WHERE stu_name LIKE '关%';
SELECT * FROM student WHERE stu_name LIKE '关_';

-- 范围查询
-- between .. and ..表示在一个连续的范围内查询
-- stu_id 在3-5之间的学生
SELECT * FROM student WHERE stu_id BETWEEN	3 AND 5;
-- stu_id 不在3-5之间的学生
SELECT * FROM student WHERE stu_id NOT BETWEEN	3 AND 5;

-- in表示在一个非连续的范围内查询 字段 in (value1, value2, ...)
-- stu_id 在1, 3, 5, 6的学生信息
SELECT * FROM student WHERE stu_id in (6, 3, 5, 1);
-- stu_id 不在1, 3, 5, 6的学生信息
SELECT * FROM student WHERE stu_id NOT in (6, 3, 5, 1);

-- 是否为null
-- IS NULL
-- 查询class_id为null的数据
SELECT * FROM student WHERE class_id IS NULL;
-- IS NOT NULL
-- 查询class_id不为null的数据
SELECT * FROM student WHERE class_id IS NOT NULL;






