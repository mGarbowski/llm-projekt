-- Enable pgvector extensions
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create full-text search configuration for Polish language
BEGIN;
      CREATE TEXT SEARCH CONFIGURATION public.polish ( COPY = pg_catalog.english );

      CREATE TEXT SEARCH DICTIONARY polish_ispell (
        TEMPLATE = ispell,
        DictFile = polish,
        AffFile = polish,
        StopWords = polish
      );

      ALTER TEXT SEARCH CONFIGURATION polish
        ALTER MAPPING FOR asciiword, asciihword, hword_asciipart, word, hword, hword_part
        WITH polish_ispell;
COMMIT;