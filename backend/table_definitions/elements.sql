create table
  public.elements (
    id uuid not null default gen_random_uuid (),
    creation_time timestamp with time zone not null default now(),
    last_updated_time timestamp without time zone not null,
    name text not null,
    description text null,
    success_rate real null,
    success_count bigint null,
    impression bigint null,
    project_id uuid not null,
    status text not null,
    constraint elements_pkey primary key (id)
  ) tablespace pg_default;