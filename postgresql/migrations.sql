create table "table_name" (
    -- Field types
    "id" serial primary key,
    "foreign_key_id" integer not null references "other_table" on delete cascade,
    "text" text not null,
    "integer" integer not null,
    "bigint" bigint not null,
    "boolean" boolean not null,
    "float" double precision not null,
    "timestamp" timestamp not null,


    -- Default
    "default" double precision not null default 0,
    "current_timestamp" timestamp not null default current_timestamp,

    -- Unique
    "unique" text unique not null,
    unique ("one", "two"),
);

alter table "table_name"
    -- Add
    add column "text" text not null default '',

    -- Alter
    alter column "text" drop not null,
    alter column "text" set not null,

    -- Drop
    drop column "text",

    -- Constraint
    add constraint unique ("one_id", "two_id"),
    drop constraint "constraint_name",


