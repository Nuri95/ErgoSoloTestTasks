# 1 вариант
"""
    SELECT
        count.count_course,
        users.name
    FROM
    (
        SELECT
            COUNT(user_id) AS count_course,
            user_id
        FROM
        (
            SELECT
                COUNT(course_id) count_courses,
                user_id,
                course_id
            FROM
            (
                SELECT
                    DISTINCT ON (user_id, course_id, lesson_no, exercise_no) user_id,
                    course_id,
                    lesson_no,
                    exercise_no,
                    id
                FROM saves
            ) AS sev
            GROUP BY course_id, user_id
        ) AS count_course
        WHERE count_course.count_courses >= 100
        GROUP BY user_id
    ) AS count
    LEFT JOIN users
        ON (count.user_id = users.id);
"""

# 2 вариант
"""
WITH saves_with_unique_records AS
(
    SELECT
    DISPATCH ON (user_id, course_id, lesson_no, exercise_no) user_id,
                course_id,
                lesson_no,
                exercise_no,
                id
    FROM saves
), number_of_execises AS (
    SELECT COUNT(course_id) AS count, user_id, course_id
    FROM saves_with_unique_records
    GROUP BY user_id, course_id
), count_courses AS (
    SELECT COUNT(user_id) AS count, user_id
    FROM number_of_execises
    WHERE number_of_execises.count >= 5
    GROUP BY user_id
)
SELECT
    count_courses.count,
    users.name
FROM count_courses
LEFT JOIN users ON (count_courses.user_id = users.id)
"""