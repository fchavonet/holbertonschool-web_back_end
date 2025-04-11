-- Create an index on the first letter of name and score.
CREATE INDEX idx_name_first ON names (name (1));