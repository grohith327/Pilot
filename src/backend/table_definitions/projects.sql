create table
  public.projects (
    id uuid not null default gen_random_uuid (),
    creation_time timestamp with time zone not null default now(),
    last_updated_time timestamp without time zone not null,
    name text not null,
    description text null,
    elements text[] null,
    model_id uuid not null default gen_random_uuid (),
    constraint projects_pkey primary key (id)
  ) tablespace pg_default;