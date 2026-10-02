-- Seed demo data (sensible demo records)
INSERT INTO users (id, username, email, role) VALUES
  (gen_random_uuid(), 'alice', 'alice@example.com', 'student'),
  (gen_random_uuid(), 'bob', 'bob@example.com', 'lecturer'),
  (gen_random_uuid(), 'carol', 'carol@example.com', 'alumni');

INSERT INTO profiles (id, user_id, full_name, bio)
SELECT gen_random_uuid(), id, username || ' Demo', 'This is a demo profile for ' || username
FROM users
WHERE username IN ('alice','bob','carol');

INSERT INTO projects (id, title, description, owner_id)
SELECT gen_random_uuid(), 'Demo Project: ' || username, 'A sample project by ' || username, id
FROM users
WHERE username = 'alice';

INSERT INTO events (id, title, description, starts_at, ends_at)
VALUES (gen_random_uuid(), 'Welcome Meetup', 'Introductory event', now() + interval '7 days', now() + interval '7 days' + interval '2 hours');

INSERT INTO resources (id, title, url)
VALUES (gen_random_uuid(), 'UWE AI Resources', 'https://uwe.ac.uk');

INSERT INTO discussions (id, title, body, author_id)
SELECT gen_random_uuid(), 'Introduce yourself', 'Welcome to the UWE MSc AI community — tell us about your research interests.', id
FROM users
WHERE username = 'alice';
