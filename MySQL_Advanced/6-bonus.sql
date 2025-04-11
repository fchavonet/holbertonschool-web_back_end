-- Adds a bonus correction, creating the project if needed.
DELIMITER $$

CREATE PROCEDURE AddBonus (
    IN user_id INTEGER,
    IN project_name VARCHAR(255),
    IN score INTEGER
)
BEGIN
    -- Insert the project if it does not already exist.
    INSERT INTO projects (name)
    SELECT project_name
    FROM DUAL
    WHERE NOT EXISTS (
        SELECT 1
        FROM projects
        WHERE name = project_name
    );

    -- Insert the correction with the associated user_id, project_id (looked up by project_name), and score.
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (
        user_id,
        (SELECT id FROM projects WHERE name = project_name),
        score
    );
END$$

DELIMITER ;
